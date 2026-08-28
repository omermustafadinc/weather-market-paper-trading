"""Fiyat temsilinin testi.

Kalshi hava piyasaları `tapered_deci_cent`: uçlarda adım 0.1 sent. Sent'e
yuvarlamak, ucuz kontratlarda (edge iddialarının en çok çıktığı yerde)
yarım sente kadar hayali edge üretir. Bu yüzden her şey tamsayı desi-sent.
"""

from __future__ import annotations

import pytest

from wxbot.kalshi import (
    KalshiDataError,
    event_target_date,
    parse_orderbook,
    tick_size_dcents,
    to_dcents,
)

# Hava piyasalarının gerçek yapısı (demo API'den okundu)
WEATHER_RANGES = [
    {"start": "0.0000", "end": "0.1000", "step": "0.0010"},
    {"start": "0.1000", "end": "0.9000", "step": "0.0100"},
    {"start": "0.9000", "end": "1.0000", "step": "0.0010"},
]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("0.4300", 430),
        ("0.0350", 35),     # yarım sent — sente yuvarlansa bilgi kaybolurdu
        ("0.9650", 965),
        ("0.0010", 1),      # en ince adım
        ("1.0000", 1000),
        ("0.0000", 0),
        (43, 430),          # eski şema: tamsayı sent
        (None, None),
        ("", None),
    ],
)
def test_desi_sente_cevirme(raw, expected) -> None:
    assert to_dcents(raw) == expected


def test_izgaraya_oturmayan_fiyat_reddedilir() -> None:
    """Desi-sentten ince bir fiyat gelirse sessizce yuvarlamak yerine patla."""
    with pytest.raises(KalshiDataError, match="ızgara"):
        to_dcents("0.43005")


def test_yarim_sent_bilgisi_korunur() -> None:
    """Asıl mesele: 3.5 sent ile 3 sent aynı şey değil."""
    assert to_dcents("0.0350") != to_dcents("0.0300")
    assert to_dcents("0.0350") - to_dcents("0.0300") == 5   # 0.5 sent


@pytest.mark.parametrize(
    ("price_dcents", "expected_step"),
    [
        (5, 1),       # 0.005 -> uçta, desi-sent adım
        (35, 1),      # 0.035 -> uçta
        (100, 1),     # sınır: iki aralık da içeriyor, ilki kazanır
        (430, 10),    # 0.43  -> ortada, tam sent adım
        (890, 10),
        (965, 1),     # 0.965 -> üst uçta, desi-sent adım
    ],
)
def test_adim_buyuklugu(price_dcents, expected_step) -> None:
    assert tick_size_dcents(price_dcents, WEATHER_RANGES) == expected_step


def test_adim_bilinmiyorsa_tutucu_varsayim() -> None:
    """price_ranges yoksa tam sent varsay — ince ızgara uydurmaktansa kaba kal."""
    assert tick_size_dcents(430, None) == 10
    assert tick_size_dcents(430, []) == 10


def test_orderbook_tum_seviyeler_ve_siralama() -> None:
    """Mid değil, TÜM seviyeler; en iyi (en yüksek) fiyat rank 0."""
    ob = {"orderbook_fp": {
        "yes_dollars": [["0.0300", "450"], ["0.4300", "52"], ["0.0350", "10"]],
        "no_dollars": [["0.5600", "16"], ["0.5100", "53"]],
    }}
    levels = parse_orderbook(ob)
    yes = [l for l in levels if l.side == "yes"]
    no = [l for l in levels if l.side == "no"]

    assert [l.price_dcents for l in yes] == [430, 35, 30]   # azalan
    assert [l.rank for l in yes] == [0, 1, 2]
    assert [l.price_dcents for l in no] == [560, 510]
    assert sum(l.quantity for l in yes) == 512.0            # hiçbir seviye düşmedi
    assert len(levels) == 5


def test_bos_orderbook_hata_vermez() -> None:
    assert parse_orderbook({"orderbook_fp": {"yes_dollars": [], "no_dollars": []}}) == []
    assert parse_orderbook({}) == []


def test_bozuk_seviye_sekli_patlar() -> None:
    with pytest.raises(KalshiDataError):
        parse_orderbook({"orderbook_fp": {"yes_dollars": [["0.4300"]]}})


@pytest.mark.parametrize(
    ("ticker", "y", "m", "d"),
    [
        ("KXHIGHNY-26AUG28", 2026, 8, 28),
        ("KXHIGHCHI-26DEC01", 2026, 12, 1),
        ("KXHIGHLAX-27JAN15", 2027, 1, 15),
    ],
)
def test_event_tarihi(ticker, y, m, d) -> None:
    dt = event_target_date(ticker)
    assert (dt.year, dt.month, dt.day) == (y, m, d)


@pytest.mark.parametrize("bad", ["KXHIGHNY", "KXHIGHNY-26XYZ28", "KXHIGHNY-2AUG28"])
def test_bozuk_event_tickeri_patlar(bad) -> None:
    with pytest.raises(KalshiDataError):
        event_target_date(bad)
