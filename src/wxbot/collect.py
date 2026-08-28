"""Collector: piyasa ve tahmin snapshot'larını append-only olarak toplar.

İki garanti:

* **Idempotent.** Aynı slot içinde tekrar koşmak yeni satır yazmaz (UNIQUE +
  INSERT OR IGNORE). GitHub Actions cron'u aynı slotta iki kez tetiklese de,
  çöküp yeniden başlasak da veri çiftlenmez.
* **Kaldığı yerden devam.** Yarıda kalan bir koşu 'running' kalır; sonraki koşu
  aynı slotta eksik kalanları tamamlar, tamamlananları atlar.

Ham yanıt her zaman olduğu gibi saklanır. Normalize seviyeler kolaylık içindir;
anlaşmazlıkta `raw_book_json` kazanır.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import uuid
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from . import config as cfg
from . import db
from .clock import now_us, us_to_iso
from .http import Fetcher, HttpFetchError
from .kalshi import KalshiClient, event_target_date, field, parse_orderbook, to_dcents


# ---------------------------------------------------------------------------
# Koşu defteri
# ---------------------------------------------------------------------------


def open_run(conn: sqlite3.Connection, slot_seconds: int) -> tuple[int, int, str]:
    """Koşuyu aç, (run_id, slot_id, run_uid) döndür."""
    started = now_us()
    slot_id = db.slot_id_for(started, slot_seconds)
    run_uid = os.environ.get("GITHUB_RUN_ID") or f"local-{uuid.uuid4().hex[:12]}"
    conn.execute(
        "INSERT OR IGNORE INTO runs (run_uid, slot_id, slot_seconds, started_at_us)"
        " VALUES (?,?,?,?)",
        (run_uid, slot_id, slot_seconds, started),
    )
    row = conn.execute("SELECT id FROM runs WHERE run_uid = ?", (run_uid,)).fetchone()
    return int(row["id"]), slot_id, run_uid


def close_run(conn: sqlite3.Connection, run_id: int, *, error: str | None = None) -> None:
    conn.execute(
        "UPDATE runs SET finished_at_us = ?, status = ?, error = ? WHERE id = ?",
        (now_us(), "failed" if error else "ok", error, run_id),
    )


# ---------------------------------------------------------------------------
# Piyasa toplama
# ---------------------------------------------------------------------------


def collect_markets(
    conn: sqlite3.Connection,
    client: KalshiClient,
    run_id: int,
    slot_id: int,
    *,
    purpose: str = "decision",
    horizon_days: int = cfg.HORIZON_DAYS,
    verbose: bool = True,
) -> dict[str, int]:
    """Her şehir için ufuk içindeki olayların TÜM kovalarını ve orderbook'larını al."""
    venue = cfg.venue_name()
    stats = {"markets": 0, "levels": 0, "skipped": 0, "errors": 0}

    for city in cfg.CITIES:
        today_local = datetime.now(ZoneInfo(city.tz)).date()
        horizon = {today_local + timedelta(days=d) for d in range(horizon_days + 1)}

        try:
            events = client.events(city.series)
        except HttpFetchError as exc:
            stats["errors"] += 1
            if verbose:
                print(f"  {city.key}: olaylar alınamadı: {exc}", file=sys.stderr)
            continue

        for ev in events:
            ev_ticker = ev.get("event_ticker", "")
            try:
                target = event_target_date(ev_ticker)
            except Exception:
                continue
            if target not in horizon:
                continue

            for m in ev.get("markets") or []:
                ticker = m.get("ticker")
                if not ticker or m.get("status") not in ("active", "open"):
                    continue

                # Aynı slot+amaç için zaten var mı? (idempotanlık / devam)
                exists = conn.execute(
                    "SELECT 1 FROM market_snapshots"
                    " WHERE venue=? AND market_ticker=? AND slot_id=? AND purpose=?",
                    (venue, ticker, slot_id, purpose),
                ).fetchone()
                if exists:
                    stats["skipped"] += 1
                    continue

                try:
                    book, fetched_us, url = client.orderbook(ticker, cfg.ORDERBOOK_DEPTH)
                except HttpFetchError as exc:
                    stats["errors"] += 1
                    if verbose:
                        print(f"  {ticker}: orderbook alınamadı: {exc}", file=sys.stderr)
                    continue

                cur = conn.execute(
                    """INSERT OR IGNORE INTO market_snapshots
                       (run_id, slot_id, purpose, venue, series_ticker, event_ticker,
                        market_ticker, fetched_at_us, fetched_at_iso, source_url,
                        raw_market_json, raw_book_json, yes_bid_dcents, yes_ask_dcents,
                        volume, open_interest)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (run_id, slot_id, purpose, venue, city.series, ev_ticker, ticker,
                     fetched_us, us_to_iso(fetched_us), url,
                     db.json_dumps(m), db.json_dumps(book),
                     to_dcents(field(m, "yes_bid_dollars", "yes_bid")),
                     to_dcents(field(m, "yes_ask_dollars", "yes_ask")),
                     _num(field(m, "volume_fp", "volume")),
                     _num(field(m, "open_interest_fp", "open_interest"))),
                )
                if not cur.lastrowid:
                    stats["skipped"] += 1
                    continue
                snap_id = int(cur.lastrowid)
                stats["markets"] += 1

                for lv in parse_orderbook(book):
                    conn.execute(
                        "INSERT OR IGNORE INTO orderbook_levels"
                        " (snapshot_id, side, price_dcents, quantity, level_rank)"
                        " VALUES (?,?,?,?,?)",
                        (snap_id, lv.side, lv.price_dcents, lv.quantity, lv.rank),
                    )
                    stats["levels"] += 1

    return stats


def _num(v: object) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(v)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# Tahmin toplama
# ---------------------------------------------------------------------------


def collect_forecasts(
    conn: sqlite3.Connection,
    fetcher: Fetcher,
    run_id: int,
    *,
    horizon_days: int = cfg.HORIZON_DAYS,
    verbose: bool = True,
) -> dict[str, int]:
    """Her şehir × model için ensemble tahminini al.

    Tahminin kendi (daha uzun) slotu var: ensemble modelleri 3-12 saatte bir
    koşuyor, 15 dakikada bir çekmek aynı veriyi tekrar indirmek olurdu.
    """
    stats = {"forecasts": 0, "skipped": 0, "errors": 0, "thin": 0}
    fslot = db.slot_id_for(now_us(), cfg.FORECAST_SLOT_SECONDS)

    for city in cfg.CITIES:
        today_local = datetime.now(ZoneInfo(city.tz)).date()
        targets = [today_local + timedelta(days=d) for d in range(horizon_days + 1)]

        for model in cfg.ENSEMBLE_MODELS:
            done = conn.execute(
                "SELECT 1 FROM forecast_snapshots"
                " WHERE provider='open-meteo' AND model=? AND location_key=?"
                "   AND variable=? AND target_date=? AND slot_id=?",
                (model.name, city.key, cfg.DAILY_VARIABLE, targets[0].isoformat(), fslot),
            ).fetchone()
            if done:
                stats["skipped"] += 1
                continue

            try:
                r = fetcher.get(cfg.OPEN_METEO_ENSEMBLE, params={
                    "latitude": city.lat, "longitude": city.lon,
                    "models": model.name, "daily": cfg.DAILY_VARIABLE,
                    "forecast_days": horizon_days + 1,
                    "temperature_unit": cfg.TEMP_UNIT, "timezone": city.tz,
                })
            except HttpFetchError as exc:
                stats["errors"] += 1
                if verbose:
                    print(f"  {city.key}/{model.name}: {exc}", file=sys.stderr)
                continue

            payload = r.json()
            daily = payload.get("daily") or {}
            times = daily.get("time") or []
            members = [k for k in daily
                       if k.startswith(cfg.DAILY_VARIABLE) and k != "time"]
            if len(members) < model.expected_members:
                stats["thin"] += 1
                if verbose:
                    print(f"  uyarı {city.key}/{model.name}: "
                          f"{len(members)}/{model.expected_members} üye",
                          file=sys.stderr)

            for target in targets:
                iso_t = target.isoformat()
                if iso_t not in times:
                    continue
                conn.execute(
                    """INSERT OR IGNORE INTO forecast_snapshots
                       (run_id, slot_id, provider, model, location_key, latitude,
                        longitude, variable, target_date, fetched_at_us,
                        fetched_at_iso, source_url, raw_json, member_count)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (run_id, fslot, "open-meteo", model.name, city.key, city.lat,
                     city.lon, cfg.DAILY_VARIABLE, iso_t, r.fetched_at_us,
                     us_to_iso(r.fetched_at_us), r.url,
                     db.json_dumps(payload), len(members)),
                )
                stats["forecasts"] += 1

    return stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Piyasa ve tahmin snapshot'ı topla")
    ap.add_argument("--db", default=str(db.DEFAULT_DB_PATH))
    ap.add_argument("--purpose", choices=("decision", "fill"), default="decision")
    ap.add_argument("--markets-only", action="store_true")
    ap.add_argument("--forecasts-only", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    verbose = not args.quiet
    conn = db.init_db(args.db)
    run_id, slot_id, run_uid = open_run(conn, cfg.MARKET_SLOT_SECONDS)
    if verbose:
        print(f"koşu {run_uid} | slot {slot_id} | venue {cfg.venue_name()} "
              f"| {us_to_iso(now_us())}")

    error: str | None = None
    try:
        with Fetcher() as f:
            if not args.forecasts_only:
                s = collect_markets(conn, KalshiClient(f, cfg.kalshi_base()),
                                    run_id, slot_id, purpose=args.purpose,
                                    verbose=verbose)
                if verbose:
                    print(f"piyasa : {s['markets']} snapshot, {s['levels']} seviye, "
                          f"{s['skipped']} atlandı, {s['errors']} hata")
            if not args.markets_only:
                s = collect_forecasts(conn, f, run_id, verbose=verbose)
                if verbose:
                    print(f"tahmin : {s['forecasts']} snapshot, {s['skipped']} atlandı, "
                          f"{s['errors']} hata, {s['thin']} eksik üye")
    except Exception as exc:  # noqa: BLE001 — koşuyu 'failed' işaretleyip yükselt
        error = f"{type(exc).__name__}: {exc}"
        close_run(conn, run_id, error=error)
        raise
    else:
        close_run(conn, run_id)

    # Toplama sonrası lookahead denetimi: bozuk veri birikmesin.
    db.assert_no_lookahead(conn)
    if verbose:
        print("lookahead denetimi: temiz")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
