"""JSONL ham veriyi SQLite'a aktarır — ve doğrulama kapısı burasıdır.

Ham veri (JSONL) tek doğru kaynak; SQLite ondan türetilir ve her an sıfırdan
yeniden kurulabilir. Bu ayrımın asıl kazancı doğrulama: lookahead kuralları
şemada CHECK kısıtı olarak duruyor, dolayısıyla **kirli bir kayıt SQLite'a
giremez**. Girmeye çalışırsa ingest gürültülü biçimde başarısız olur; sessizce
atlamaz.

Idempotent: aynı JSONL'i tekrar aktarmak yeni satır üretmez (UNIQUE kısıtları).
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

from zoneinfo import ZoneInfo

from . import config as cfg
from . import db, rawstore
from .clock import us_to_dt, us_to_iso
from .kalshi import field, parse_orderbook, to_dcents


class IngestError(RuntimeError):
    """Ham kayıt SQLite'a alınamadı. Sessizce atlamak yerine patlıyoruz."""


# ---------------------------------------------------------------------------


def _ensure_run(conn: sqlite3.Connection, run_uid: str, slot_id: int,
                slot_seconds: int, started_at_us: int) -> int:
    conn.execute(
        "INSERT OR IGNORE INTO runs (run_uid, slot_id, slot_seconds, started_at_us,"
        " finished_at_us, status) VALUES (?,?,?,?,?,'ok')",
        (run_uid, slot_id, slot_seconds, started_at_us, started_at_us),
    )
    row = conn.execute("SELECT id FROM runs WHERE run_uid = ?", (run_uid,)).fetchone()
    return int(row["id"])


def ingest_market(conn: sqlite3.Connection, rec: dict,
                  meta_index: dict[str, dict] | None = None) -> bool:
    """Bir piyasa kaydını aktar. True = yeni satır yazıldı.

    Kayıt tam metadata değil, o günün `market_meta` kaydından fark taşır;
    burada birleştirip DB'ye tam hâlini yazıyoruz.
    """
    from . import config as cfg

    run_id = _ensure_run(conn, rec.get("run_uid", "unknown"), rec["slot_id"],
                         cfg.MARKET_SLOT_SECONDS, rec["fetched_at_us"])

    if "market" in rec:                       # v1 öncesi düz kayıt
        m = rec["market"]
    else:
        meta = (meta_index or {}).get(rec["market_ticker"])
        if meta is None:
            raise IngestError(
                f"{rec['market_ticker']} için market_meta kaydı bulunamadı "
                f"({rec['fetched_at_iso']}). Ham veri eksik."
            )
        m = rawstore.apply_delta(meta, rec["market_delta"])
    try:
        cur = conn.execute(
            """INSERT OR IGNORE INTO market_snapshots
               (run_id, slot_id, purpose, venue, series_ticker, event_ticker,
                market_ticker, fetched_at_us, fetched_at_iso, source_url,
                raw_market_json, raw_book_json, yes_bid_dcents, yes_ask_dcents,
                volume, open_interest)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (run_id, rec["slot_id"], rec["purpose"], rec["venue"],
             rec["series_ticker"], rec["event_ticker"], rec["market_ticker"],
             rec["fetched_at_us"], rec["fetched_at_iso"], rec["source_url"],
             db.json_dumps(m), db.json_dumps(rec["book"]),
             to_dcents(field(m, "yes_bid_dollars", "yes_bid")),
             to_dcents(field(m, "yes_ask_dollars", "yes_ask")),
             _num(field(m, "volume_fp", "volume")),
             _num(field(m, "open_interest_fp", "open_interest"))),
        )
    except sqlite3.IntegrityError as exc:
        raise IngestError(
            f"piyasa kaydı reddedildi ({rec['market_ticker']} @ "
            f"{rec['fetched_at_iso']}): {exc}"
        ) from exc

    # `lastrowid` bağlantı seviyesinde; INSERT OR IGNORE atlandığında önceki
    # bir eklemenin rowid'ini döndürüp "yeni satır yazdım" yalanı söyler.
    # `rowcount` gerçekten değişen satır sayısını verir.
    if cur.rowcount != 1:
        return False
    snap_id = int(cur.lastrowid)
    for lv in parse_orderbook(rec["book"]):
        conn.execute(
            "INSERT OR IGNORE INTO orderbook_levels"
            " (snapshot_id, side, price_dcents, quantity, level_rank)"
            " VALUES (?,?,?,?,?)",
            (snap_id, lv.side, lv.price_dcents, lv.quantity, lv.rank),
        )
    return True


def ingest_forecast(conn: sqlite3.Connection, rec: dict) -> int:
    """Bir tahmin kaydını hedef günlere açarak aktar. Yazılan satır sayısını döndürür."""
    from . import config as cfg

    run_id = _ensure_run(conn, rec.get("run_uid", "unknown"), rec["slot_id"],
                         cfg.FORECAST_SLOT_SECONDS, rec["fetched_at_us"])
    written = 0
    for target in rec.get("target_dates") or []:
        try:
            cur = conn.execute(
                """INSERT OR IGNORE INTO forecast_snapshots
                   (run_id, slot_id, provider, model, location_key, latitude,
                    longitude, variable, target_date, fetched_at_us, fetched_at_iso,
                    source_url, raw_json, member_count)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (run_id, rec["slot_id"], rec["provider"], rec["model"],
                 rec["location_key"], rec["latitude"], rec["longitude"],
                 rec["variable"], target, rec["fetched_at_us"], rec["fetched_at_iso"],
                 rec["source_url"], db.json_dumps(rec["payload"]), rec["member_count"]),
            )
        except sqlite3.IntegrityError as exc:
            raise IngestError(
                f"tahmin kaydı reddedildi ({rec['location_key']}/{rec['model']} "
                f"-> {target}): {exc}"
            ) from exc
        written += 1 if cur.rowcount == 1 else 0
    return written


def ingest_decision(conn: sqlite3.Connection, rec: dict) -> bool:
    """Karar kaydını aktar. Lookahead kuralları CHECK kısıtı olarak devrede;
    ihlal eden kayıt buradan geçemez."""
    from . import config as cfg

    run_id = _ensure_run(conn, rec.get("run_uid", "unknown"), rec["slot_id"],
                         cfg.MARKET_SLOT_SECONDS, rec["decision_at_us"])

    # Kararın yerel günü: piyasanın kendi zaman diliminde. Ham kayıt formatını
    # değiştirmeden burada türetiyoruz, böylece geçmiş kayıtlar da düzeliyor.
    city = cfg.CITY_BY_SERIES.get(rec["market_ticker"].split("-")[0])
    if city is None:
        raise IngestError(f"bilinmeyen seri: {rec['market_ticker']}")
    local_date = (us_to_dt(rec["decision_at_us"])
                  .astimezone(ZoneInfo(city.tz)).date().isoformat())

    ticker, slot, purpose = rec["market_snapshot_key"].split("|")
    snap = conn.execute(
        "SELECT id FROM market_snapshots WHERE market_ticker=? AND slot_id=? AND purpose=?",
        (ticker, int(slot), purpose)).fetchone()
    if snap is None:
        raise IngestError(
            f"{rec['market_ticker']} kararı için piyasa snapshot'ı bulunamadı "
            f"({rec['market_snapshot_key']})")

    try:
        cur = conn.execute(
            """INSERT OR IGNORE INTO decisions
               (run_id, slot_id, venue, market_ticker, event_ticker, target_date,
                data_asof_us, data_asof_iso, decision_at_us, decision_at_iso,
                decision_local_date, market_snapshot_id, forecast_basis, action,
                reason, model_prob, market_prob, edge, kelly_fraction,
                target_contracts, limits_json)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (run_id, rec["slot_id"], rec["venue"], rec["market_ticker"],
             rec["event_ticker"], rec["target_date"], rec["data_asof_us"],
             rec["data_asof_iso"], rec["decision_at_us"], rec["decision_at_iso"],
             local_date,
             int(snap["id"]), db.json_dumps(rec["forecast_basis"]), rec["action"],
             rec["reason"], rec["model_prob"], rec["market_prob"], rec["edge"],
             rec["kelly_fraction"], rec["target_contracts"],
             db.json_dumps(rec["limits"])))
    except sqlite3.IntegrityError as exc:
        raise IngestError(
            f"karar reddedildi ({rec['market_ticker']} @ {rec['decision_at_iso']}): "
            f"{exc}") from exc
    return cur.rowcount == 1


def ingest_fill(conn: sqlite3.Connection, rec: dict) -> bool:
    dec = conn.execute(
        "SELECT id FROM decisions WHERE market_ticker=? AND slot_id=? AND venue=?",
        (rec["market_ticker"], rec["slot_id"], rec["venue"])).fetchone()
    if dec is None:
        raise IngestError(f"{rec['market_ticker']} fill'i için karar bulunamadı")

    snap = conn.execute(
        "SELECT id FROM market_snapshots WHERE market_ticker=? AND slot_id=? "
        "AND purpose='fill'", (rec["market_ticker"], rec["slot_id"])).fetchone()
    if snap is None:
        raise IngestError(f"{rec['market_ticker']} fill'i için gecikmeli kitap yok")

    try:
        cur = conn.execute(
            """INSERT OR IGNORE INTO sim_fills
               (decision_id, fill_snapshot_id, decision_at_us, book_asof_us,
                filled_at_us, filled_at_iso, side, requested_contracts,
                filled_contracts, avg_price_dcents, fee_dcents, levels_consumed,
                fill_status, notes)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (int(dec["id"]), int(snap["id"]), rec["decision_at_us"],
             rec["book_asof_us"], rec["filled_at_us"], rec["filled_at_iso"],
             rec["side"], rec["requested_contracts"], rec["filled_contracts"],
             rec["avg_price_dcents"], rec["fee_dcents"],
             db.json_dumps(rec["levels_consumed"]), rec["fill_status"],
             rec["notes"]))
    except sqlite3.IntegrityError as exc:
        raise IngestError(
            f"fill reddedildi ({rec['market_ticker']}): {exc}") from exc
    return cur.rowcount == 1


def ingest_settlement(conn: sqlite3.Connection, rec: dict) -> bool:
    try:
        cur = conn.execute(
            """INSERT OR IGNORE INTO settlements
               (venue, market_ticker, event_ticker, target_date, observed_at_us,
                observed_at_iso, source, source_url, raw_json, outcome, observed_value)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (rec["venue"], rec["market_ticker"], rec["event_ticker"],
             rec["target_date"], rec["observed_at_us"], rec["observed_at_iso"],
             rec["source"], rec["source_url"], db.json_dumps(rec["raw"]),
             rec["outcome"], rec["observed_value"]))
    except sqlite3.IntegrityError as exc:
        raise IngestError(
            f"çözümleme reddedildi ({rec['market_ticker']}): {exc}") from exc
    return cur.rowcount == 1


def _num(v: object) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(v)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------


def ingest_all(conn: sqlite3.Connection, root: Path | None = None,
               *, verbose: bool = True) -> dict[str, int]:
    stats = {"market_new": 0, "market_seen": 0, "forecast_new": 0, "forecast_seen": 0,
             "decision_new": 0, "decision_seen": 0, "fill_new": 0, "fill_seen": 0,
             "settlement_new": 0, "settlement_seen": 0,
             "decision_invalid": 0, "fill_invalid": 0}

    conn.execute("BEGIN")
    try:
        # Metadata gün bazlı; kayıtları da gün gün okuyup doğru indeksle eşliyoruz.
        for day in rawstore.days("market", root):
            meta_index = rawstore.load_meta_index(day, root)
            for rec in rawstore.read_day("market", day, root):
                stats["market_seen"] += 1
                stats["market_new"] += 1 if ingest_market(conn, rec, meta_index) else 0
        for rec in rawstore.read_all("forecast", root):
            stats["forecast_seen"] += 1
            stats["forecast_new"] += ingest_forecast(conn, rec)
        # İptal edilmiş kayıtlar atlanır — silinmezler, yalnızca aktarılmazlar.
        invalid = rawstore.invalidated_keys(root)
        # Sıra önemli: fill kaydı kendi kararına referans veriyor.
        for rec in rawstore.read_all("decision", root):
            stats["decision_seen"] += 1
            if (rec["venue"], rec["market_ticker"], rec["slot_id"]) in invalid["decision"]:
                stats["decision_invalid"] += 1
                continue
            stats["decision_new"] += 1 if ingest_decision(conn, rec) else 0
        for rec in rawstore.read_all("fill", root):
            stats["fill_seen"] += 1
            if (rec["venue"], rec["market_ticker"], rec["slot_id"]) in invalid["fill"]:
                stats["fill_invalid"] += 1
                continue
            stats["fill_new"] += 1 if ingest_fill(conn, rec) else 0
        for rec in rawstore.read_all("settlement", root):
            stats["settlement_seen"] += 1
            stats["settlement_new"] += 1 if ingest_settlement(conn, rec) else 0
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise

    if verbose:
        print(f"piyasa : {stats['market_seen']} kayıt okundu, "
              f"{stats['market_new']} yeni satır")
        print(f"tahmin : {stats['forecast_seen']} kayıt okundu, "
              f"{stats['forecast_new']} yeni satır")
        if stats["decision_seen"] or stats["fill_seen"]:
            print(f"karar  : {stats['decision_seen']} kayıt okundu, "
                  f"{stats['decision_new']} yeni satır")
            print(f"fill   : {stats['fill_seen']} kayıt okundu, "
                  f"{stats['fill_new']} yeni satır")
            if stats["decision_invalid"] or stats["fill_invalid"]:
                print(f"iptal  : {stats['decision_invalid']} karar, "
                      f"{stats['fill_invalid']} fill (karantina kaydı gereği atlandı)")
        if stats["settlement_seen"]:
            print(f"çözüm  : {stats['settlement_seen']} kayıt okundu, "
                  f"{stats['settlement_new']} yeni satır")
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Ham JSONL'den SQLite kur")
    ap.add_argument("--db", default=str(db.DEFAULT_DB_PATH))
    ap.add_argument("--root", default=None, help="ham veri kökü (test için)")
    ap.add_argument("--rebuild", action="store_true",
                    help="var olan DB'yi silip sıfırdan kur")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    dbp = Path(args.db)
    if args.rebuild and dbp.exists():
        for suffix in ("", "-wal", "-shm"):
            p = Path(str(dbp) + suffix)
            p.unlink(missing_ok=True)
        if not args.quiet:
            print(f"silindi: {dbp}")

    conn = db.init_db(dbp)
    try:
        ingest_all(conn, Path(args.root) if args.root else None,
                   verbose=not args.quiet)
        # Doğrulama kapısı: tek ihlal varsa buradan geçilmez.
        db.assert_no_lookahead(conn)
        if not args.quiet:
            print("lookahead denetimi: temiz")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
