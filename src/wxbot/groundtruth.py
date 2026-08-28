"""Gerçekleşen değer: gözlenen günlük maksimum sıcaklık.

İki kaynak, iki farklı iş:

* **NWS CLI raporu** — kontratın çözümlendiği resmi ürün. Yalnızca ~1 hafta
  geriye gidiyor, dolayısıyla canlı çözümleme için kullanılıyor.
* **NCEI GHCN-Daily** — aynı istasyonların uzun geçmişi (aylar/yıllar), ama
  ~4 gün yayın gecikmesi var. Geçmiş çalışmalar için.

İkisinin aynı şeyi ölçtüğünü doğruladım: 2026-08-24'te beş şehirde (NYC, MDW,
MIA, LAX, PHL) değerler birebir aynı çıktı. İstasyon kimlikleri ayrıca resmi
`ghcnd-stations.txt` dosyasından isim ve koordinatla teyit edildi.

Not: Kalshi günlük sıcaklık piyasaları Ağustos 2025'ten beri The Weather
Company üzerinden çözümleniyor; TWC alttan NWS kullanıyor ama arada bir katman
var (bkz. DECISIONS.md §4). Yani buradaki değerler çözümlemeye çok yakın ama
tanım gereği aynı olduğu garanti değil — bu fark ayrı bir metrik olarak
izlenecek.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date

from . import config as cfg
from .http import Fetcher

_MONTHS = {m: i for i, m in enumerate(
    ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
     "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"], start=1)}

_CLI_DATE = re.compile(r"CLIMATE SUMMARY FOR\s+([A-Z]+)\s+(\d{1,2})\s+(\d{4})")
_CLI_MAX = re.compile(r"^\s*MAXIMUM\s+(-?\d+)", re.M)


class GroundTruthError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class Observation:
    location_key: str
    target_date: str
    tmax_f: int
    source: str            # 'nws_cli' | 'ncei_ghcn'
    source_url: str
    #: Değerin yayınlandığı an (biliniyorsa). Lookahead denetimi buna bakar.
    observed_at_iso: str = ""


# ---------------------------------------------------------------------------
# NWS CLI — resmi çözümleme ürünü
# ---------------------------------------------------------------------------


def parse_cli(text: str) -> tuple[str, int] | None:
    """CLI ürün metninden (hedef gün, maksimum °F).

    Rapor sabah yayınlanır ve BİR ÖNCEKİ günü özetler; hedef günü metnin
    kendisinden okuyoruz, yayın tarihinden çıkarmıyoruz.
    """
    md = _CLI_DATE.search(text)
    if not md:
        return None
    mon, day, yr = md.group(1), int(md.group(2)), int(md.group(3))
    if mon not in _MONTHS:
        return None
    mx = _CLI_MAX.search(text)
    if not mx:
        return None
    return f"{yr:04d}-{_MONTHS[mon]:02d}-{day:02d}", int(mx.group(1))


def fetch_cli(f: Fetcher, city: cfg.City, *, limit: int = 15) -> list[Observation]:
    """Bir şehrin son CLI raporlarını çek ve çözümle."""
    idx = f.get(f"{cfg.NWS_BASE}/products/types/CLI/locations/{city.cli_code}").json()
    out: list[Observation] = []
    for g in (idx.get("@graph") or [])[:limit]:
        prod = f.get(g["@id"]).json()
        parsed = parse_cli(prod.get("productText") or "")
        if parsed:
            out.append(Observation(city.key, parsed[0], parsed[1], "nws_cli",
                                   g["@id"], g.get("issuanceTime", "")))
    return out


# ---------------------------------------------------------------------------
# NCEI GHCN-Daily — uzun geçmiş
# ---------------------------------------------------------------------------


def fetch_ncei_tmax(f: Fetcher, city: cfg.City, start: date, end: date) -> dict[str, int]:
    """GHCN-Daily'den günlük maksimum (°F). Gecikme ~4 gün."""
    r = f.get(cfg.NCEI_DATA, params={
        "dataset": "daily-summaries", "stations": city.ghcn,
        "startDate": start.isoformat(), "endDate": end.isoformat(),
        "dataTypes": "TMAX", "format": "json", "units": "standard",
    })
    rows = r.json()
    if not isinstance(rows, list):
        raise GroundTruthError(f"{city.key}: beklenmedik NCEI yanıtı: {str(rows)[:200]}")
    out: dict[str, int] = {}
    for row in rows:
        v = row.get("TMAX")
        if v in (None, ""):
            continue
        try:
            out[row["DATE"]] = int(round(float(v)))
        except (TypeError, ValueError):
            continue
    return out
