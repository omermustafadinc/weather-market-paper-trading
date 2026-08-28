"""Fill simülasyonunun testi.

En kritik dosya bu. Mid'den doldurmak, sonsuz derinlik varsaymak veya fee'yi
unutmak — üçü de sonucu güzelleştirir ve üçü de yalandır. Testler bunları
tek tek engelliyor.
"""

from __future__ import annotations

import pytest

from wxbot.fills import (
    DOLLAR_DCENTS,
    Level,
    ask_ladder,
    simulate_fill,
    taker_fee_dcents,
)

# Gerçek üretim verisinden alınmış bir NO tarafı (KXHIGHNY-26AUG29-B79.5)
NO_BOOK = [Level(630, 50.0), Level(620, 30.0), Level(610, 100.0), Level(600, 200.0)]


# ---------------------------------------------------------------------------
# Merdiven
# ---------------------------------------------------------------------------


def test_yes_almak_no_tarafini_yer() -> None:
    """Üretim verisiyle 16/16 doğrulanan ilişki: yes_ask = 1000 − no_bid."""
    ladder = ask_ladder(NO_BOOK, "yes")
    assert [lv.price_dcents for lv in ladder] == [370, 380, 390, 400]
    assert [lv.quantity for lv in ladder] == [50.0, 30.0, 100.0, 200.0]


def test_merdiven_en_ucuzdan_siralanir() -> None:
    ladder = ask_ladder(NO_BOOK, "yes")
    assert ladder == sorted(ladder, key=lambda lv: lv.price_dcents)


def test_sifir_adetli_seviyeler_atlanir() -> None:
    assert len(ask_ladder([Level(600, 0.0), Level(610, 5.0)], "yes")) == 1


def test_gecersiz_taraf_patlar() -> None:
    with pytest.raises(ValueError, match="side"):
        ask_ladder(NO_BOOK, "maybe")


# ---------------------------------------------------------------------------
# Fill — mid'den doldurma yok
# ---------------------------------------------------------------------------


def test_kucuk_emir_en_iyi_seviyede_dolar() -> None:
    f = simulate_fill(NO_BOOK, "yes", 10.0)
    assert f.status == "full"
    assert f.filled == 10.0
    assert f.avg_price_dcents == 370.0
    assert f.levels == ((370, 10.0),)


def test_buyuk_emir_kitabi_yurur_ve_ortalama_kotulesir() -> None:
    """Asıl mesele: en iyi fiyattan değil, tükettiğin ortalamadan dolarsın."""
    f = simulate_fill(NO_BOOK, "yes", 38.0)   # %10 tavanı tam 38
    assert f.status == "full"
    assert f.levels == ((370, 38.0),)

    # Tavanı gevşetip gerçekten yürüsün
    f = simulate_fill(NO_BOOK, "yes", 100.0, max_liquidity_fraction=1.0)
    assert f.filled == 100.0
    assert f.levels == ((370, 50.0), (380, 30.0), (390, 20.0))
    expected = (370 * 50 + 380 * 30 + 390 * 20) / 100
    assert f.avg_price_dcents == pytest.approx(expected)
    assert f.avg_price_dcents > 370, "ortalama en iyi fiyattan kötü olmalı"


def test_mid_fiyattan_doldurmaz() -> None:
    """Mid ~ (yes_bid + yes_ask)/2 olurdu; fill her zaman ask tarafında."""
    f = simulate_fill(NO_BOOK, "yes", 20.0)
    assert f.avg_price_dcents == 370.0      # ask, mid değil


# ---------------------------------------------------------------------------
# Derinlik yetmezliği
# ---------------------------------------------------------------------------


def test_derinlik_yetmezse_kismi_fill() -> None:
    thin = [Level(600, 5.0)]
    f = simulate_fill(thin, "yes", 100.0, max_liquidity_fraction=1.0)
    assert f.status == "partial"
    assert f.filled == 5.0
    assert "derinlik yetmedi" in f.note


def test_bos_kitapta_fill_yok() -> None:
    f = simulate_fill([], "yes", 10.0)
    assert f.status == "none"
    assert f.filled == 0.0
    assert f.avg_price_dcents is None
    assert f.fee_dcents == 0.0


def test_sifir_talep_fill_yok() -> None:
    assert simulate_fill(NO_BOOK, "yes", 0.0).status == "none"


# ---------------------------------------------------------------------------
# Likidite tavanı — görünürün %10'undan fazlasını alma
# ---------------------------------------------------------------------------


def test_likidite_tavani_uygulanir() -> None:
    f = simulate_fill(NO_BOOK, "yes", 10_000.0)
    visible = sum(lv.quantity for lv in NO_BOOK)      # 380
    assert f.filled == pytest.approx(visible * 0.10)  # 38
    assert f.capped_by_liquidity
    assert f.status == "partial"
    assert "likidite tavanı" in f.note


def test_tavan_altinda_kalan_emir_etkilenmez() -> None:
    f = simulate_fill(NO_BOOK, "yes", 20.0)
    assert not f.capped_by_liquidity
    assert f.status == "full"


# ---------------------------------------------------------------------------
# Limit fiyat
# ---------------------------------------------------------------------------


def test_limit_fiyat_pahali_seviyeleri_yemez() -> None:
    f = simulate_fill(NO_BOOK, "yes", 100.0, max_liquidity_fraction=1.0,
                      max_price_dcents=380)
    assert f.filled == 80.0                     # 370'te 50 + 380'de 30
    assert all(p <= 380 for p, _ in f.levels)
    assert f.status == "partial"


def test_limit_hicbir_seviyeye_ulasmazsa_fill_yok() -> None:
    f = simulate_fill(NO_BOOK, "yes", 10.0, max_price_dcents=300)
    assert f.status == "none"
    assert "limit" in f.note


# ---------------------------------------------------------------------------
# Fee
# ---------------------------------------------------------------------------


def test_fee_50_sentte_tavan_yapar() -> None:
    """Kalshi formülü 0.07·C·P·(1−P): 50 sentte kontrat başına 1.75 sent."""
    assert taker_fee_dcents(100, 500) == pytest.approx(1750.0)   # $1.75


def test_fee_uclarda_kuculur() -> None:
    orta = taker_fee_dcents(100, 500)
    uc = taker_fee_dcents(100, 100)
    assert uc < orta
    assert taker_fee_dcents(100, 100) == taker_fee_dcents(100, 900)  # simetrik


def test_fee_sente_yukari_yuvarlanir() -> None:
    """Yuvarlama aşağı olsaydı maliyeti olduğundan az gösterirdik."""
    fee = taker_fee_dcents(1, 500)          # 0.07·0.25 = 0.0175 $ -> 2 sent
    assert fee == 20.0


def test_fee_carpani_uygulanir() -> None:
    assert taker_fee_dcents(100, 500, multiplier=2.0) > taker_fee_dcents(100, 500)


def test_fill_fee_iceriyor_ve_maliyeti_artiriyor() -> None:
    f = simulate_fill(NO_BOOK, "yes", 20.0)
    assert f.fee_dcents > 0
    assert f.total_cost_dcents > f.cost_dcents


def test_sifir_kontratta_fee_yok() -> None:
    assert taker_fee_dcents(0, 500) == 0.0
