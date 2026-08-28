"""Collector: piyasa ve tahmin snapshot'larını append-only JSONL'e yazar.

Veritabanına hiç dokunmaz — SQLite türetilmiş bir görünüm (bkz. `wxbot.ingest`).
Bu ayrım kasıtlı: toplayıcı GitHub Actions'ta koşuyor ve tek işi ham veriyi
sadakatle biriktirmek. Yorumlama, normalize etme, doğrulama hepsi ingest'te.

İki garanti:

* **Idempotent.** Aynı slot içinde tekrar koşmak yeni satır yazmaz; hangi
  ticker'ın bu slotta zaten toplandığı doğrudan JSONL'den okunuyor.
* **Kaldığı yerden devam.** Yarıda kalan bir koşunun eksikleri sonraki koşuda
  tamamlanır, tamamlananlar atlanır. Yarım kalmış son satır okunurken atlanır.
"""

from __future__ import annotations

import argparse
import os
import sys
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from . import config as cfg
from . import rawstore
from .clock import now_us, us_to_dt, us_to_iso
from .db import slot_id_for
from .http import Fetcher, HttpFetchError
from .kalshi import KalshiClient, event_target_date


def _run_uid() -> str:
    gh = os.environ.get("GITHUB_RUN_ID")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    return f"gh-{gh}-{attempt}" if gh else f"local-{uuid.uuid4().hex[:12]}"


# ---------------------------------------------------------------------------
# Piyasa
# ---------------------------------------------------------------------------


def collect_markets(
    client: KalshiClient, run_uid: str, *, purpose: str = "decision",
    horizon_days: int = cfg.HORIZON_DAYS, root=None, verbose: bool = True,
) -> dict[str, int]:
    venue = cfg.venue_name()
    slot_id = slot_id_for(now_us(), cfg.MARKET_SLOT_SECONDS)
    today_utc = us_to_dt(now_us()).date().isoformat()
    already = rawstore.collected_market_keys(today_utc, slot_id, purpose, root)
    # Metadata günde bir kez yazılır; snapshot'lar ondan farkı taşır (kayıpsız).
    meta_index = rawstore.load_meta_index(today_utc, root)

    stats = {"written": 0, "skipped": 0, "errors": 0, "meta": 0}

    for city in cfg.CITIES:
        today_local = datetime.now(ZoneInfo(city.tz)).date()
        horizon = {today_local + timedelta(days=d) for d in range(horizon_days + 1)}

        try:
            events = client.events(city.series)
        except HttpFetchError as exc:
            stats["errors"] += 1
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
                if ticker in already:
                    stats["skipped"] += 1
                    continue

                try:
                    book, fetched_us, url = client.orderbook(ticker, cfg.ORDERBOOK_DEPTH)
                except HttpFetchError as exc:
                    stats["errors"] += 1
                    print(f"  {ticker}: orderbook alınamadı: {exc}", file=sys.stderr)
                    continue

                if ticker not in meta_index:
                    rawstore.append("market_meta", rawstore.market_meta_record(
                        run_uid=run_uid, venue=venue, market_ticker=ticker,
                        fetched_at_us=fetched_us,
                        fetched_at_iso=us_to_iso(fetched_us), market=m,
                    ), root)
                    meta_index[ticker] = m
                    stats["meta"] += 1

                rawstore.append("market", rawstore.market_record(
                    run_uid=run_uid, venue=venue, slot_id=slot_id, purpose=purpose,
                    series_ticker=city.series, event_ticker=ev_ticker,
                    market_ticker=ticker, target_date=target.isoformat(),
                    fetched_at_us=fetched_us, fetched_at_iso=us_to_iso(fetched_us),
                    source_url=url,
                    market_delta=rawstore.market_delta(meta_index[ticker], m),
                    book=book,
                ), root)
                already.add(ticker)
                stats["written"] += 1

    if verbose:
        print(f"piyasa : {stats['written']} yazıldı ({stats['meta']} yeni metadata), "
              f"{stats['skipped']} atlandı, {stats['errors']} hata  (slot {slot_id})")
    return stats


# ---------------------------------------------------------------------------
# Tahmin
# ---------------------------------------------------------------------------


def collect_forecasts(
    fetcher: Fetcher, run_uid: str, *, horizon_days: int = cfg.HORIZON_DAYS,
    root=None, verbose: bool = True,
) -> dict[str, int]:
    """Tahminin kendi (daha uzun) slotu var: ensemble modelleri 3-12 saatte bir
    koşuyor, 15 dakikada bir çekmek aynı veriyi tekrar indirmek olurdu."""
    slot_id = slot_id_for(now_us(), cfg.FORECAST_SLOT_SECONDS)
    today_utc = us_to_dt(now_us()).date().isoformat()
    already = rawstore.collected_forecast_keys(today_utc, slot_id, root)

    stats = {"written": 0, "skipped": 0, "errors": 0, "thin": 0}

    for city in cfg.CITIES:
        today_local = datetime.now(ZoneInfo(city.tz)).date()
        targets = [(today_local + timedelta(days=d)).isoformat()
                   for d in range(horizon_days + 1)]

        for model in cfg.ENSEMBLE_MODELS:
            if (city.key, model.name) in already:
                stats["skipped"] += 1
                continue

            try:
                r = fetcher.get(cfg.OPEN_METEO_ENSEMBLE, params={
                    "latitude": city.lat, "longitude": city.lon, "models": model.name,
                    "daily": cfg.DAILY_VARIABLE, "forecast_days": horizon_days + 1,
                    "temperature_unit": cfg.TEMP_UNIT, "timezone": city.tz,
                })
            except HttpFetchError as exc:
                stats["errors"] += 1
                print(f"  {city.key}/{model.name}: {exc}", file=sys.stderr)
                continue

            payload = r.json()
            daily = payload.get("daily") or {}
            members = [k for k in daily
                       if k.startswith(cfg.DAILY_VARIABLE) and k != "time"]
            if len(members) < model.expected_members:
                stats["thin"] += 1
                print(f"  uyarı {city.key}/{model.name}: {len(members)}/"
                      f"{model.expected_members} üye", file=sys.stderr)

            covered = [t for t in targets if t in (daily.get("time") or [])]
            rawstore.append("forecast", rawstore.forecast_record(
                run_uid=run_uid, provider="open-meteo", model=model.name,
                location_key=city.key, latitude=city.lat, longitude=city.lon,
                variable=cfg.DAILY_VARIABLE, target_dates=covered, slot_id=slot_id,
                fetched_at_us=r.fetched_at_us, fetched_at_iso=us_to_iso(r.fetched_at_us),
                source_url=r.url, member_count=len(members), payload=payload,
            ), root)
            already.add((city.key, model.name))
            stats["written"] += 1

    if verbose:
        print(f"tahmin : {stats['written']} yazıldı, {stats['skipped']} atlandı, "
              f"{stats['errors']} hata, {stats['thin']} eksik üye  (slot {slot_id})")
    return stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Ham piyasa ve tahmin verisi topla")
    ap.add_argument("--purpose", choices=("decision", "fill"), default="decision")
    ap.add_argument("--markets-only", action="store_true")
    ap.add_argument("--forecasts-only", action="store_true")
    ap.add_argument("--root", default=None, help="ham veri kökü (test için)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    from pathlib import Path
    root = Path(args.root) if args.root else None
    verbose = not args.quiet
    run_uid = _run_uid()
    if verbose:
        print(f"koşu {run_uid} | venue {cfg.venue_name()} | {us_to_iso(now_us())}")

    errors = 0
    with Fetcher() as f:
        if not args.forecasts_only:
            errors += collect_markets(KalshiClient(f, cfg.kalshi_base()), run_uid,
                                      purpose=args.purpose, root=root,
                                      verbose=verbose)["errors"]
        if not args.markets_only:
            errors += collect_forecasts(f, run_uid, root=root, verbose=verbose)["errors"]

    # Hata olsa bile toplanan veri geçerli; çıkış kodu durumu bildirir.
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
