"""Grid-istasyon bias çalışması.

Sorduğu soru: Open-Meteo'nun bir grid noktası için verdiği tahmin, kontratın
çözümlendiği İSTASYONDA gözlenen değerden sistematik olarak sapıyor mu?

Bu önemli çünkü Kalshi kovaları 2°F genişliğinde. 1°F'lik sabit bir sapma bile
kova olasılıklarını on puanlarca kaydırır ve kalibre edilmemiş bir modelde
"edge" gibi görünür.

Yöntem
------
* **Tahmin:** `previous-runs-api`, `temperature_2m_previous_dayN`. Bu, N gün
  önce yapılmış tahmini verir — lead time kontrollü ve tanımı gereği
  lookahead'e kapalı. (Ensemble API'nin `past_days` verisi bunun tersine
  bugünkü koşunun geriye dönük analizidir ve kullanılamaz; saçılımın lead time
  ile DARALMASINDAN anlaşılıyor. Bkz. DECISIONS.md.)
* **Gerçekleşen:** NCEI GHCN-Daily TMAX, istasyonun kendisi.
* Günlük maksimum, YEREL takvim gününe göre hesaplanıyor — kontrat da öyle.

Kısıtları (sonuç okunurken akılda tutulmalı)
--------------------------------------------
* previous-runs *deterministik* tahmin verir, ensemble ortalaması değil. Yani
  ölçtüğümüz sapma, kullandığım ensemble'ın ortalamasının sapmasıyla birebir
  aynı olmayabilir. Konumdan gelen bileşen (grid hücresi vs nokta istasyon)
  ikisinde de ortak; modelden gelen bileşen farklı olabilir.
* GFS previous-runs'ta veri döndürmüyor, o yüzden listede yok.
* NCEI ~4 gün gecikmeli yayınlıyor; en yeni günler dışarıda kalır.
"""

from __future__ import annotations

import argparse
import collections
import math
import statistics
from datetime import date, timedelta

from . import config as cfg
from .groundtruth import fetch_ncei_tmax
from .http import Fetcher

#: previous-runs'ta veri döndüren modeller (test edildi).
BIAS_MODELS = ("ecmwf_ifs025", "icon_seamless", "best_match")

#: Kaç gün önceden yapılmış tahmine bakılacak. Kalshi günlük piyasalarında
#: asıl ilgi alanı 1-2 gün.
LEADS = (1, 2, 3)


def daily_max_from_hourly(times: list[str], values: list[float | None]) -> dict[str, float]:
    """Saatlik seriden yerel takvim gününe göre günlük maksimum."""
    by_day: dict[str, float] = {}
    for t, v in zip(times, values):
        if v is None:
            continue
        day = t[:10]
        if day not in by_day or v > by_day[day]:
            by_day[day] = v
    return by_day


def fetch_forecast_daily_max(
    f: Fetcher, city: cfg.City, model: str, leads: tuple[int, ...], past_days: int,
) -> dict[int, dict[str, float]]:
    """{lead: {gün: tahmin edilen günlük maks}}"""
    variables = [f"temperature_2m_previous_day{n}" for n in leads]
    r = f.get(cfg.OPEN_METEO_PREVIOUS_RUNS, params={
        "latitude": city.lat, "longitude": city.lon, "models": model,
        "hourly": ",".join(variables), "past_days": past_days, "forecast_days": 1,
        "temperature_unit": cfg.TEMP_UNIT, "timezone": city.tz,
    })
    h = r.json().get("hourly") or {}
    times = h.get("time") or []
    return {n: daily_max_from_hourly(times, h.get(f"temperature_2m_previous_day{n}") or [])
            for n in leads}


def _stats(errors: list[float]) -> dict[str, float]:
    n = len(errors)
    mean = statistics.fmean(errors)
    return {
        "n": n,
        "bias": mean,
        "mae": statistics.fmean(abs(e) for e in errors),
        "rmse": math.sqrt(statistics.fmean(e * e for e in errors)),
        "sd": statistics.pstdev(errors) if n > 1 else 0.0,
    }


def run_study(past_days: int = 120, models=BIAS_MODELS, leads=LEADS) -> dict:
    """Şehir × model × lead için hata istatistikleri."""
    today = date.today()
    start = today - timedelta(days=past_days + 2)
    results: dict = {}

    with Fetcher() as f:
        for city in cfg.CITIES:
            obs = fetch_ncei_tmax(f, city, start, today)
            results[city.key] = {"n_obs": len(obs), "models": {}}
            for model in models:
                fc = fetch_forecast_daily_max(f, city, model, leads, past_days)
                per_lead = {}
                for lead, series in fc.items():
                    errs = [series[d] - obs[d] for d in series if d in obs]
                    if errs:
                        per_lead[lead] = _stats(errs)
                results[city.key]["models"][model] = per_lead
    return results


def print_report(results: dict, leads=LEADS) -> None:
    print("GRID-İSTASYON BIAS ÇALIŞMASI")
    print("bias = tahmin - gözlem  (pozitif = model sıcak tahmin ediyor)\n")

    for model in sorted({m for c in results.values() for m in c["models"]}):
        print(f"=== {model} ===")
        print(f"  {'şehir':<6}{'n':>5}" +
              "".join(f"{'lead'+str(l)+' bias':>13}{'mae':>7}" for l in leads))
        for key, city_res in results.items():
            per_lead = city_res["models"].get(model, {})
            if not per_lead:
                print(f"  {key:<6}{'veri yok':>5}")
                continue
            row = f"  {key:<6}{per_lead.get(leads[0],{}).get('n',0):>5}"
            for l in leads:
                st = per_lead.get(l)
                row += f"{st['bias']:>+13.2f}{st['mae']:>7.2f}" if st else f"{'-':>13}{'-':>7}"
            print(row)
        print()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Grid-istasyon bias çalışması")
    ap.add_argument("--past-days", type=int, default=120)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    res = run_study(args.past_days)
    if args.json:
        import json
        print(json.dumps(res, indent=1))
    else:
        print_report(res)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
