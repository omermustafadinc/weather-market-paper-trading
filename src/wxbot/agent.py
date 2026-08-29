"""Ajan: karar ver, sonra gecikmeli kitaba karşı doldur.

İki ayrı komut, kasıtlı olarak ayrı:

    decide  ->  karar anındaki kitap + tahminle KARAR ver, hepsini logla
    fill    ->  45 sn sonra çekilmiş kitaba karşı fill'i hesapla

Aralarındaki gecikme simüle edilmiyor, gerçekten yaşanıyor: workflow karar
verdikten sonra bekliyor ve orderbook'u yeniden çekiyor. Ölçtüğümüz kadarıyla
piyasaların ~%26'sı o sürede hareket ediyor, yani bu fark önemsiz değil.

Her karar loglanır — işlem yapmama kararı da, gerekçesiyle. Bu bir rapor
kolaylığı değil, dürüstlük şartı: yalnızca yapılan işlemleri loglayan bir
sistem, kaç fırsatı elediğini ve neden elediğini gizler.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from . import config as cfg
from . import db, model, rawstore
from .clock import now_us, us_to_dt, us_to_iso
from .collect import _run_uid
from .fills import Level, simulate_fill
from .kalshi import event_target_date
from .strategy import StrategyConfig, best_candidate


# ---------------------------------------------------------------------------
# Karar
# ---------------------------------------------------------------------------


def decide(
    conn: sqlite3.Connection, *, scfg: StrategyConfig | None = None,
    root: Path | None = None, horizon_days: int = cfg.HORIZON_DAYS,
    slot: int | None = None, replay: bool = False, verbose: bool = True,
) -> dict[str, int]:
    """Kararları üret.

    İki kip:

    * **canlı** (varsayılan): `decision_at = şu an`. Toplama bittikten hemen
      sonra koşar; fill 45 sn sonraki kitaba karşı hesaplanır.
    * **replay** (`replay=True`): geçmişte toplanmış bir slot üzerinde çalışır
      ve `decision_at = data_asof + 1 sn` alır. Zaman damgası sentetiktir ve
      kayda öyle geçer. Lookahead değişmez kuralı burada DAHA sıkı sağlanır:
      karar, veriden yalnızca 1 saniye sonra verilmiş sayılır, fill kitabı ise
      ~87 sn sonrasından gelir.
    """
    scfg = scfg or StrategyConfig()
    run_uid = _run_uid()
    venue = cfg.venue_name()
    slot_id = slot if slot is not None else db.slot_id_for(now_us(), cfg.MARKET_SLOT_SECONDS)
    today_utc = us_to_dt(now_us()).date().isoformat()
    already = rawstore.collected_decision_keys(today_utc, slot_id, root)

    stats = {"decisions": 0, "trades": 0, "no_trade": 0, "skipped": 0,
             "no_model": 0, "past_or_today": 0}
    exposure = 0.0

    for city in cfg.CITIES:
        today_local = datetime.now(ZoneInfo(city.tz)).date()
        # SADECE GELECEK GÜNLER.
        #
        # Bugünü ve geçmişi bilerek dışarıda bırakıyoruz. Sebebi ölçüldü:
        # 02:47Z koşusu dünün piyasalarında karar verdi ve lookahead tarayıcısı
        # yakaladı — Philadelphia'nın CLI raporu 5 saat önce yayınlanmıştı,
        # yani sonuç zaten biliniyordu. Dahası, geçmiş bir gün için Open-Meteo
        # "tahmin" değil analiz döndürür; model o kovalarda dâhi görünürdü.
        #
        # Bugünün piyasaları da güvenli değil: öğleden sonra maksimum çoktan
        # gerçekleşmiş olabilir ve "tahmin" fiilen gözleme dönüşür. Sabit ~1
        # günlük lead time'da kalmak, ölçtüğümüz şeyin gerçekten tahmin becerisi
        # olmasını garantiliyor.
        horizon = {(today_local + timedelta(days=d)).isoformat()
                   for d in range(1, horizon_days + 1)}

        events = [r["event_ticker"] for r in conn.execute(
            "SELECT DISTINCT event_ticker FROM market_snapshots"
            " WHERE series_ticker = ? AND slot_id = ? AND purpose = 'decision'",
            (city.series, slot_id))]

        for ev in events:
            try:
                target = event_target_date(ev).isoformat()
            except Exception:
                continue
            if target not in horizon:
                stats["past_or_today"] = stats.get("past_or_today", 0) + 1
                continue

            snaps = list(conn.execute(
                """SELECT id, market_ticker, fetched_at_us, raw_market_json, raw_book_json
                   FROM market_snapshots
                   WHERE event_ticker = ? AND slot_id = ? AND purpose = 'decision'""",
                (ev, slot_id)))
            if not snaps:
                continue

            # data_asof: karara giren TÜM girdilerin en yenisi.
            market_asof = max(int(s["fetched_at_us"]) for s in snaps)
            sample = model.load_ensemble_sample(conn, city.key, target,
                                                as_of_us=market_asof)
            if sample.member_count == 0:
                stats["no_model"] += 1
                continue

            buckets = model.load_buckets(conn, ev, as_of_us=market_asof)
            try:
                model.check_ladder(buckets)
                dist = model.build_distribution(sample)
                probs = model.bucket_probabilities(dist, buckets)
            except model.ModelError as exc:
                if verbose:
                    print(f"  {ev}: model kurulamadı: {exc}", file=sys.stderr)
                continue

            data_asof = max(market_asof, sample.data_asof_us)

            for s in snaps:
                ticker = s["market_ticker"]
                if ticker in already:
                    stats["skipped"] += 1
                    continue
                q = probs.get(ticker)
                if q is None:
                    continue

                yes_ask, no_ask = _asks(s["raw_book_json"])
                cand = best_candidate(ticker, q, yes_ask, no_ask, scfg,
                                      current_exposure_dcents=exposure)

                # KARAR ANI: veriyi topladık, modeli kurduk, şimdi karar veriyoruz.
                # Replay'de "şu an" yerine verinin hemen sonrası alınır; aksi
                # hâlde fill kitabı karardan önce kalır ve kural ihlal olurdu.
                decision_at = (data_asof + 1_000_000) if replay else now_us()
                if decision_at < data_asof:      # olmamalı; olursa sessiz geçme
                    raise db.LookaheadError(
                        f"{ticker}: decision_at ({us_to_iso(decision_at)}) < "
                        f"data_asof ({us_to_iso(data_asof)})")

                action = f"buy_{cand.side}" if cand.tradeable else "no_trade"
                market_prob = (cand.price_dcents / 1000.0) if cand.price_dcents else None

                rawstore.append("decision", rawstore.decision_record(
                    run_uid=run_uid, venue=venue, slot_id=slot_id,
                    market_ticker=ticker, event_ticker=ev, target_date=target,
                    data_asof_us=data_asof, data_asof_iso=us_to_iso(data_asof),
                    decision_at_us=decision_at, decision_at_iso=us_to_iso(decision_at),
                    market_snapshot_key=f"{ticker}|{slot_id}|decision",
                    forecast_basis=list(sample.snapshot_ids),
                    action=action, reason=cand.reason,
                    model_prob=q if cand.side == "yes" else q,
                    market_prob=market_prob, edge=cand.edge,
                    kelly_fraction=cand.kelly,
                    target_contracts=cand.contracts,
                    limits={"binding": cand.binding, "net_edge": cand.net_edge,
                            "fee_per_contract_dcents": cand.fee_per_contract * 1000,
                            "side": cand.side,
                            "dist": dist.describe(),
                            "models": sample.model_count,
                            "members": sample.member_count,
                            "mode": "replay" if replay else "live",
                            "cfg": {"edge_margin": scfg.edge_margin,
                                    "kelly_fraction": scfg.kelly_fraction,
                                    "max_position_fraction": scfg.max_position_fraction,
                                    "bankroll_dcents": scfg.bankroll_dcents}},
                ), root)

                already.add(ticker)
                stats["decisions"] += 1
                if cand.tradeable:
                    stats["trades"] += 1
                    exposure += cand.contracts * cand.price_dcents
                else:
                    stats["no_trade"] += 1

    if verbose:
        print(f"karar  : {stats['decisions']} karar "
              f"({stats['trades']} işlem, {stats['no_trade']} işlem yok), "
              f"{stats['skipped']} atlandı, {stats['no_model']} model yok, "
              f"{stats['past_or_today']} olay bugün/geçmiş (atlandı) "
              f"(slot {slot_id})")
    return stats


def _asks(raw_book_json: str) -> tuple[int | None, int | None]:
    """Kitaptan yes_ask ve no_ask türet.

    Kalshi'de ayrı satış tarafı yok: YES almak NO bid'lerini yer.
    Doğrulandı (üretim verisiyle 16/16): yes_ask = 1000 − en iyi no bid.
    """
    import json
    from .kalshi import parse_orderbook
    levels = parse_orderbook(json.loads(raw_book_json))
    best_yes = max((l.price_dcents for l in levels if l.side == "yes"), default=None)
    best_no = max((l.price_dcents for l in levels if l.side == "no"), default=None)
    yes_ask = None if best_no is None else 1000 - best_no
    no_ask = None if best_yes is None else 1000 - best_yes
    return yes_ask, no_ask


# ---------------------------------------------------------------------------
# Fill
# ---------------------------------------------------------------------------


def fill(
    conn: sqlite3.Connection, *, root: Path | None = None, slot: int | None = None,
    replay: bool = False, verbose: bool = True,
) -> dict[str, int]:
    """Karar verilmiş işlemleri, gecikme sonrası kitaba karşı doldur."""
    import json

    run_uid = _run_uid()
    venue = cfg.venue_name()
    slot_id = slot if slot is not None else db.slot_id_for(now_us(), cfg.MARKET_SLOT_SECONDS)
    today_utc = us_to_dt(now_us()).date().isoformat()
    already = rawstore.collected_fill_keys(today_utc, slot_id, root)

    stats = {"full": 0, "partial": 0, "none": 0, "skipped": 0, "no_book": 0}

    rows = list(conn.execute(
        """SELECT market_ticker, decision_at_us, action, target_contracts, limits_json
           FROM decisions
           WHERE slot_id = ? AND action <> 'no_trade' AND target_contracts > 0""",
        (slot_id,)))

    for d in rows:
        ticker = d["market_ticker"]
        if ticker in already:
            stats["skipped"] += 1
            continue

        book_row = conn.execute(
            """SELECT fetched_at_us, raw_book_json FROM market_snapshots
               WHERE market_ticker = ? AND slot_id = ? AND purpose = 'fill'""",
            (ticker, slot_id)).fetchone()
        if book_row is None:
            stats["no_book"] += 1
            continue

        side = "yes" if d["action"] == "buy_yes" else "no"
        # YES almak NO seviyelerini yer, NO almak YES seviyelerini.
        book_side = "no" if side == "yes" else "yes"
        from .kalshi import parse_orderbook
        levels = [Level(l.price_dcents, l.quantity)
                  for l in parse_orderbook(json.loads(book_row["raw_book_json"]))
                  if l.side == book_side]

        f = simulate_fill(levels, side, float(d["target_contracts"]))
        # Fill anı: canlıda şimdi, replay'de kitabın çekildiği an (o kitaba
        # karşı dolduruyoruz, dolayısıyla dürüst zaman odur).
        filled_at = int(book_row["fetched_at_us"]) if replay else now_us()

        rawstore.append("fill", rawstore.fill_record(
            run_uid=run_uid, venue=venue, slot_id=slot_id, market_ticker=ticker,
            decision_at_us=int(d["decision_at_us"]),
            book_asof_us=int(book_row["fetched_at_us"]),
            filled_at_us=filled_at, filled_at_iso=us_to_iso(filled_at),
            side=side, requested=f.requested, filled=f.filled,
            avg_price_dcents=f.avg_price_dcents, fee_dcents=f.fee_dcents,
            levels=[list(x) for x in f.levels], status=f.status, notes=f.note,
        ), root)

        already.add(ticker)
        stats[f.status] += 1

    if verbose:
        print(f"fill   : {stats['full']} tam, {stats['partial']} kısmi, "
              f"{stats['none']} fill yok, {stats['skipped']} atlandı, "
              f"{stats['no_book']} kitap yok (slot {slot_id})")
    return stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Karar ver veya fill hesapla")
    ap.add_argument("command", choices=("decide", "fill"))
    ap.add_argument("--db", default=str(db.DEFAULT_DB_PATH))
    ap.add_argument("--root", default=None)
    ap.add_argument("--edge-margin", type=float, default=None)
    ap.add_argument("--slot", type=int, default=None,
                    help="belirli bir slot üzerinde çalış (replay için)")
    ap.add_argument("--replay", action="store_true",
                    help="geçmiş slot: decision_at = data_asof + 1sn (sentetik, kayda geçer)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.root) if args.root else None
    conn = db.connect(args.db)
    try:
        if args.command == "decide":
            scfg = StrategyConfig(edge_margin=args.edge_margin) if args.edge_margin \
                is not None else StrategyConfig()
            decide(conn, scfg=scfg, root=root, slot=args.slot,
                   replay=args.replay, verbose=not args.quiet)
        else:
            fill(conn, root=root, slot=args.slot, replay=args.replay,
                 verbose=not args.quiet)
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
