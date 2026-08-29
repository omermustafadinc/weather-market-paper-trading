"""Çözümleme: gerçekleşen sıcaklığı bul, her kovayı 0/1'e bağla.

Kaynak NWS CLI raporu — kontratın çözümlendiği resmi ürün. Rapor ertesi sabah
yayınlanıyor, dolayısıyla `observed_at` her zaman kararlardan sonra.

Bir uyarı, DECISIONS.md §4'ten: Kalshi günlük sıcaklık piyasaları Ağustos
2025'ten beri The Weather Company üzerinden çözümleniyor. TWC alttan NWS
kullanıyor ama arada bir katman var. Yani buradaki sonuç çözümlemeye çok
yakın; tanımı gereği aynı olduğu garanti değil. Bu farkın kaç günde ortaya
çıktığı ayrı bir metrik olarak izlenmeli — şu an izlenmiyor, çünkü TWC'nin
dokümante public API'si bulunamadı.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from . import config as cfg
from . import db, model, rawstore
from .clock import iso_to_us, us_to_dt, us_to_iso
from .collect import _run_uid
from .groundtruth import fetch_cli
from .http import Fetcher


def settle(
    conn: sqlite3.Connection, *, root: Path | None = None, verbose: bool = True,
) -> dict[str, int]:
    """Çözümlenmemiş piyasaları, yayınlanmış CLI raporlarıyla kapat."""
    run_uid = _run_uid()
    venue = cfg.venue_name()
    stats = {"settled": 0, "already": 0, "no_report": 0, "no_bucket": 0}

    with Fetcher() as f:
        for city in cfg.CITIES:
            # Bu şehir için çözümlenmemiş (event, hedef gün) çiftleri
            pending = list(conn.execute(
                """SELECT DISTINCT m.event_ticker, m.market_ticker
                   FROM market_snapshots m
                   LEFT JOIN settlements s
                     ON s.market_ticker = m.market_ticker AND s.venue = m.venue
                   WHERE m.series_ticker = ? AND s.id IS NULL""",
                (city.series,)))
            if not pending:
                continue

            try:
                observations = {o.target_date: o for o in fetch_cli(f, city)}
            except Exception as exc:
                if verbose:
                    print(f"  {city.key}: CLI alınamadı: {exc}")
                continue

            for row in pending:
                ticker = row["market_ticker"]
                ev = row["event_ticker"]
                try:
                    target = model.event_target_date_str(ev)
                except Exception:
                    continue

                obs = observations.get(target)
                if obs is None:
                    stats["no_report"] += 1
                    continue

                snap = conn.execute(
                    "SELECT raw_market_json FROM market_snapshots"
                    " WHERE market_ticker = ? ORDER BY fetched_at_us DESC LIMIT 1",
                    (ticker,)).fetchone()
                if snap is None:
                    continue
                try:
                    bucket = model.Bucket.from_market(json.loads(snap["raw_market_json"]))
                    outcome = 1 if bucket.contains_int(obs.tmax_f) else 0
                except model.ModelError:
                    stats["no_bucket"] += 1
                    continue

                observed_at = (iso_to_us(obs.observed_at_iso)
                               if obs.observed_at_iso else None)
                if observed_at is None:
                    stats["no_report"] += 1
                    continue

                rawstore.append("settlement", rawstore.settlement_record(
                    run_uid=run_uid, venue=venue, market_ticker=ticker,
                    event_ticker=ev, target_date=target,
                    observed_at_us=observed_at, observed_at_iso=us_to_iso(observed_at),
                    source="nws_cli", source_url=obs.source_url,
                    observed_value=float(obs.tmax_f), outcome=outcome,
                    raw={"tmax_f": obs.tmax_f, "bucket": bucket.subtitle},
                ), root)
                stats["settled"] += 1

    if verbose:
        print(f"çözümleme: {stats['settled']} kapandı, "
              f"{stats['no_report']} rapor yok, {stats['no_bucket']} kova hatası")
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Piyasaları NWS CLI ile çözümle")
    ap.add_argument("--db", default=str(db.DEFAULT_DB_PATH))
    ap.add_argument("--root", default=None)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    conn = db.connect(args.db)
    try:
        settle(conn, root=Path(args.root) if args.root else None,
               verbose=not args.quiet)
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
