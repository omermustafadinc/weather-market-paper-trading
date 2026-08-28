"""Yapılandırma: şehirler, modeller, uçlar.

Buradaki her koordinat ve her CLI kodu uydurulmadı — Kalshi'nin kontrat
kurallarından okundu ve `api.weather.gov/stations` ile doğrulandı
(bkz. DECISIONS.md §5).

Dikkat edilecek bir tuzak: Chicago piyasası **Midway**'e (CLIMDW) göre
çözümleniyor, O'Hare'e değil. "Chicago" deyip O'Hare kullanmak sistematik
olarak yanlış model üretirdi.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Uçlar
# ---------------------------------------------------------------------------

KALSHI_PROD = "https://api.elections.kalshi.com/trade-api/v2"
KALSHI_DEMO = "https://demo-api.kalshi.co/trade-api/v2"

OPEN_METEO_ENSEMBLE = "https://ensemble-api.open-meteo.com/v1/ensemble"
NWS_BASE = "https://api.weather.gov"
NCEI_DATA = "https://www.ncei.noaa.gov/access/services/data/v1"
OPEN_METEO_PREVIOUS_RUNS = "https://previous-runs-api.open-meteo.com/v1/forecast"


def kalshi_base() -> str:
    """Üretim mi demo mu.

    Varsayılan üretim. Demo yalnızca `WXBOT_KALSHI_ENV=demo` ile açılır ve
    o veriler DB'ye `kalshi-demo` olarak yazılır — demo verisi asla gerçek
    piyasa verisiyle karışmasın (demo orderbook'ları boş, bkz. DECISIONS.md §2).
    """
    return KALSHI_DEMO if os.environ.get("WXBOT_KALSHI_ENV") == "demo" else KALSHI_PROD


def venue_name() -> str:
    return "kalshi-demo" if os.environ.get("WXBOT_KALSHI_ENV") == "demo" else "kalshi"


# ---------------------------------------------------------------------------
# Şehirler
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class City:
    key: str            # kısa anahtar (DB'de location_key)
    series: str         # Kalshi seri ticker'ı
    cli_code: str       # NWS CLI lokasyon kodu (kontrat kuralından)
    station: str        # NWS istasyon kimliği
    ghcn: str           # NCEI GHCN-Daily kimliği (geçmiş ground truth)
    lat: float
    lon: float
    tz: str             # yerel gün sınırı için IANA zaman dilimi
    name: str


CITIES: tuple[City, ...] = (
    City("NY",  "KXHIGHNY",   "NYC", "KNYC", "USW00094728", 40.7833,  -73.9667, "America/New_York",
         "New York City, Central Park"),
    City("CHI", "KXHIGHCHI",  "MDW", "KMDW", "USW00014819", 41.7842,  -87.7553, "America/Chicago",
         "Chicago Midway Airport"),
    City("MIA", "KXHIGHMIA",  "MIA", "KMIA", "USW00012839", 25.7906,  -80.3164, "America/New_York",
         "Miami International Airport"),
    City("AUS", "KXHIGHAUS",  "AUS", "KAUS", "USW00013904", 30.1830,  -97.6799, "America/Chicago",
         "Austin-Bergstrom International Airport"),
    City("DEN", "KXHIGHDEN",  "DEN", "KDEN", "USW00003017", 39.8466, -104.6562, "America/Denver",
         "Denver International Airport"),
    City("LAX", "KXHIGHLAX",  "LAX", "KLAX", "USW00023174", 33.9381, -118.3889, "America/Los_Angeles",
         "Los Angeles International Airport"),
    City("PHL", "KXHIGHPHIL", "PHL", "KPHL", "USW00013739", 39.8733,  -75.2268, "America/New_York",
         "Philadelphia International Airport"),
)

CITY_BY_KEY = {c.key: c for c in CITIES}
CITY_BY_SERIES = {c.series: c for c in CITIES}


# ---------------------------------------------------------------------------
# Ensemble modelleri
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class EnsembleModel:
    name: str
    expected_members: int
    note: str


#: Üye sayıları canlı doğrulandı (2026-08-27, NYC). Beklenenden az üye gelirse
#: collector uyarır — sessizce eksik veriyle model kurmayalım.
ENSEMBLE_MODELS: tuple[EnsembleModel, ...] = (
    EnsembleModel("ecmwf_ifs025",               51, "ECMWF IFS 0.25°, 6 saatte bir"),
    EnsembleModel("icon_seamless",              40, "DWD ICON, 3-6 saatte bir"),
    EnsembleModel("gfs025",                     31, "NOAA GEFS 0.25°, 6 saatte bir"),
    EnsembleModel("gem_global",                 21, "CMC GEM, 12 saatte bir"),
    EnsembleModel("bom_access_global_ensemble", 18, "BOM ACCESS-GE, 6 saatte bir"),
    EnsembleModel("ukmo_global_ensemble_20km",  18, "UKMO MOGREPS-G"),
)

TOTAL_EXPECTED_MEMBERS = sum(m.expected_members for m in ENSEMBLE_MODELS)

#: Kalshi sıcaklık piyasaları Fahrenheit; modeli de Fahrenheit tutuyoruz ki
#: birim dönüşümü karar yolunda hiç olmasın.
TEMP_UNIT = "fahrenheit"
DAILY_VARIABLE = "temperature_2m_max"


# ---------------------------------------------------------------------------
# Zamanlama
# ---------------------------------------------------------------------------

#: Piyasa snapshot slotu. GitHub Actions cron'u ±birkaç dk kayabildiği için
#: slot, kaymayı yutacak kadar geniş; idempotanlık buna dayanıyor.
#:
#: 30 dakika: günlük çözümlenen piyasalar için 48 karar noktası fazlasıyla
#: yeterli, ve depolamayı makul tutuyor (repoya commit'leniyor). 15 dakika
#: veriyi ikiye katlardı, karşılığında kayda değer bir şey kazandırmadan.
MARKET_SLOT_SECONDS = int(os.environ.get("WXBOT_MARKET_SLOT_SECONDS", 1800))

#: Tahmin slotu daha uzun: ensemble modelleri 3-12 saatte bir koşuyor, her 15
#: dakikada bir çekmek aynı veriyi tekrar indirmek olurdu (Open-Meteo kotasını
#: da boşuna yer).
FORECAST_SLOT_SECONDS = int(os.environ.get("WXBOT_FORECAST_SLOT_SECONDS", 3600))

#: Karar ile fill arasındaki gecikme. Şemadaki 30 sn asgarisinin üstünde.
FILL_DELAY_SECONDS = int(os.environ.get("WXBOT_FILL_DELAY_SECONDS", 45))

#: Kaç gün ilerisi toplansın (bugün = 0).
HORIZON_DAYS = int(os.environ.get("WXBOT_HORIZON_DAYS", 2))

#: Orderbook derinliği. Tüm seviyeleri istiyoruz.
ORDERBOOK_DEPTH = 100
