"""Kalshi read-only istemcisi ve fiyat normalizasyonu.

Fiyatlar API'den string dolar olarak geliyor ("0.4300"). Para hesabında float
kullanmıyoruz: Decimal ile okuyup **tamsayı desi-sent**e (1/1000 dolar)
çeviriyoruz.

Neden sent değil desi-sent: hava piyasaları `tapered_deci_cent` yapısında.
Fiyat adımı 0.10-0.90 arasında 1 sent, ama uçlarda (0-0.10 ve 0.90-1.00)
**0.1 sent**. Ucuz kontratlar tam o uçlarda yaşıyor; sente yuvarlamak
3.5 sentlik bir kontratta yarım sentlik hayali edge üretirdi.

Orderbook semantiği (simülatör için kritik, burada sadece sadakatle saklıyoruz):
Kalshi iki tarafta da *bekleyen alış* verir — `yes` tarafı YES almak için,
`no` tarafı NO almak için konmuş emirler. Ayrı bir "satış" tarafı yoktur;
p fiyatından bir YES satışı, (100-p) fiyatından bir NO alışıyla aynı şeydir.
Bu dönüşümü collector yapmaz, simülatör yapar — ham veri ham kalsın.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Any

from .http import Fetcher

_MONTHS = {m: i for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"], start=1)}

_EVENT_DATE_RE = re.compile(r"-(\d{2})([A-Z]{3})(\d{2})$")


class KalshiDataError(ValueError):
    """Beklenmedik API şekli. Sessizce tahmin etmek yerine patlıyoruz."""


def event_target_date(event_ticker: str) -> date:
    """'KXHIGHNY-26AUG28' -> date(2026, 8, 28).

    Tarihi ticker'dan okuyoruz çünkü hedef gün *yerel* gün ve API'nin UTC
    close_time'ı gece yarısını aşabiliyor.
    """
    m = _EVENT_DATE_RE.search(event_ticker)
    if not m:
        raise KalshiDataError(f"event ticker'dan tarih çıkarılamadı: {event_ticker!r}")
    yy, mon, dd = m.group(1), m.group(2), m.group(3)
    if mon not in _MONTHS:
        raise KalshiDataError(f"bilinmeyen ay: {mon!r} ({event_ticker})")
    return date(2000 + int(yy), _MONTHS[mon], int(dd))


DCENTS_PER_DOLLAR = Decimal(1000)


def to_dcents(value: Any) -> int | None:
    """API fiyatını tamsayı desi-sente (1/1000 dolar) çevir. Float kullanmaz.

    Hem yeni ('0.4300' dolar) hem eski (43 tamsayı sent) şekli kabul eder.
    '0.4300' -> 430,  '0.0350' -> 35,  43 (eski, sent) -> 430.
    """
    if value is None or value == "":
        return None
    if isinstance(value, int) and not isinstance(value, bool):
        return value * 10                 # eski şema: tamsayı sent
    try:
        d = Decimal(str(value))
    except InvalidOperation as exc:
        raise KalshiDataError(f"fiyat çözümlenemedi: {value!r}") from exc
    dcents = d * DCENTS_PER_DOLLAR
    if dcents != dcents.to_integral_value():
        raise KalshiDataError(
            f"desi-sent ızgarasına oturmayan fiyat: {value!r} "
            "(Kalshi'nin en ince adımı 0.0010)"
        )
    return int(dcents)


def tick_size_dcents(price_dcents: int, price_ranges: list[dict] | None) -> int:
    """Verilen fiyatta geçerli adım büyüklüğü (desi-sent).

    `price_ranges` piyasa metadata'sından gelir, örn. hava piyasaları için:
      0.000-0.100 adım 0.001 | 0.100-0.900 adım 0.010 | 0.900-1.000 adım 0.001
    Simülatör, kitabı yürürken geçerli olmayan fiyat seviyesi uydurmasın diye.
    """
    if not price_ranges:
        return 10  # bilinmiyorsa tam sent varsay (tutucu)
    for rng in price_ranges:
        start = to_dcents(rng.get("start"))
        end = to_dcents(rng.get("end"))
        step = to_dcents(rng.get("step"))
        if start is None or end is None or step is None:
            continue
        if start <= price_dcents <= end:
            return step
    return 10


def to_qty(value: Any) -> float:
    if value is None or value == "":
        return 0.0
    return float(Decimal(str(value)))


@dataclass(frozen=True, slots=True)
class Level:
    side: str            # 'yes' | 'no'
    price_dcents: int    # 1/1000 dolar
    quantity: float
    rank: int            # 0 = en iyi (en yüksek) fiyat


def parse_orderbook(payload: dict) -> list[Level]:
    """Ham orderbook yanıtını seviyelere çevir. TÜM seviyeler korunur."""
    book = payload.get("orderbook_fp") or payload.get("orderbook") or {}
    levels: list[Level] = []
    for side, keys in (("yes", ("yes_dollars", "yes")), ("no", ("no_dollars", "no"))):
        raw = None
        for k in keys:
            if k in book:
                raw = book[k]
                break
        if not raw:
            continue
        parsed = []
        for entry in raw:
            if not isinstance(entry, (list, tuple)) or len(entry) < 2:
                raise KalshiDataError(f"beklenmedik seviye şekli: {entry!r}")
            c = to_dcents(entry[0])
            if c is None:
                continue
            parsed.append((c, to_qty(entry[1])))
        # En iyi bekleyen alış = en yüksek fiyat -> rank 0
        parsed.sort(key=lambda x: -x[0])
        for rank, (c, q) in enumerate(parsed):
            levels.append(Level(side, c, q, rank))
    return levels


def field(market: dict, *names: str) -> Any:
    """Şema sürümleri arası ilk dolu alanı getir."""
    for n in names:
        if n in market and market[n] not in (None, ""):
            return market[n]
    return None


class KalshiClient:
    """Yalnızca okuma. Emir uçları `wxbot.http` tarafından zaten engelli."""

    def __init__(self, fetcher: Fetcher, base: str) -> None:
        self.f = fetcher
        self.base = base.rstrip("/")

    def events(self, series_ticker: str, *, limit: int = 200) -> list[dict]:
        r = self.f.get(
            f"{self.base}/events",
            params={"series_ticker": series_ticker, "limit": limit,
                    "with_nested_markets": "true"},
        )
        return r.json().get("events") or []

    def orderbook(self, market_ticker: str, depth: int) -> tuple[dict, int, str]:
        """(ham yanıt, fetched_at_us, url) döndürür."""
        r = self.f.get(
            f"{self.base}/markets/{market_ticker}/orderbook", params={"depth": depth}
        )
        return r.json(), r.fetched_at_us, r.url

    def series(self, series_ticker: str) -> dict:
        r = self.f.get(f"{self.base}/series/{series_ticker}")
        return r.json().get("series") or {}
