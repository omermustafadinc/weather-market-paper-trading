"""Strateji testleri: edge, eşik, Kelly ve limitler."""

from __future__ import annotations

import pytest

from wxbot.strategy import StrategyConfig, best_candidate, evaluate


def cfg(**kw) -> StrategyConfig:
    return StrategyConfig(**kw)


# ---------------------------------------------------------------------------
# Edge ve eşik
# ---------------------------------------------------------------------------


def test_edge_model_eksi_fiyat() -> None:
    c = evaluate("X", "yes", 400, 0.55, cfg())
    assert c.edge == pytest.approx(0.15)


def test_negatif_edge_islem_yok() -> None:
    c = evaluate("X", "yes", 600, 0.40, cfg())
    assert not c.tradeable
    assert "<= 0" in c.reason


def test_fee_edgei_yer() -> None:
    """Fee'ye eşit brüt edge sıfır beklenen getiri demektir."""
    c = evaluate("X", "yes", 500, 0.5175, cfg(edge_margin=0.0))
    assert c.fee_per_contract == pytest.approx(0.02)   # 50c'te 2 sent (yukarı yuvarlı)
    assert c.net_edge < c.edge


def test_esigin_altinda_islem_yok() -> None:
    c = evaluate("X", "yes", 400, 0.44, cfg(edge_margin=0.05))
    assert not c.tradeable
    assert "eşik" in c.reason


def test_esigin_ustunde_islem_var() -> None:
    c = evaluate("X", "yes", 400, 0.55, cfg(edge_margin=0.03))
    assert c.tradeable
    assert c.contracts > 0


# ---------------------------------------------------------------------------
# Kelly
# ---------------------------------------------------------------------------


def test_kelly_formulu() -> None:
    """f* = (q − p) / (1 − p), sonra kesirli çarpan."""
    c = evaluate("X", "yes", 400, 0.60, cfg(kelly_fraction=0.25))
    assert c.kelly == pytest.approx((0.60 - 0.40) / (1 - 0.40) * 0.25)


def test_kelly_carpani_dortte_biri_asamaz() -> None:
    """Kullanıcı şartı: kesirli Kelly, en fazla 1/4."""
    with pytest.raises(ValueError, match="kelly_fraction"):
        StrategyConfig(kelly_fraction=0.5)
    with pytest.raises(ValueError, match="kelly_fraction"):
        StrategyConfig(kelly_fraction=0.0)


def test_buyuk_edge_daha_buyuk_kelly() -> None:
    kucuk = evaluate("X", "yes", 400, 0.50, cfg())
    buyuk = evaluate("X", "yes", 400, 0.70, cfg())
    assert buyuk.kelly > kucuk.kelly


# ---------------------------------------------------------------------------
# Limitler
# ---------------------------------------------------------------------------


def test_pozisyon_tavani_kellyi_ezer() -> None:
    """Kalibre edilmemiş modelde 1/4 Kelly tek kontrata sermayenin %13'ünü
    koyardı; tavan tam da bunu engellemek için var."""
    c = evaluate("X", "yes", 400, 0.70, cfg(max_position_fraction=0.02,
                                            bankroll_dcents=1_000_000))
    assert c.binding == "pozisyon_tavanı"
    assert c.contracts * c.price_dcents == pytest.approx(20_000)


def test_kelly_kucukse_kelly_baglar() -> None:
    c = evaluate("X", "yes", 400, 0.70, cfg(max_position_fraction=0.90))
    assert c.binding == "kelly"


def test_toplam_limit_baglar() -> None:
    c = evaluate("X", "yes", 400, 0.70, cfg(bankroll_dcents=1_000_000,
                                            max_total_exposure_fraction=0.20),
                 current_exposure_dcents=195_000)
    assert c.binding == "toplam_limit"
    assert c.contracts * c.price_dcents == pytest.approx(5_000)


def test_toplam_limit_dolunca_islem_yok() -> None:
    c = evaluate("X", "yes", 400, 0.70, cfg(max_total_exposure_fraction=0.20),
                 current_exposure_dcents=200_000)
    assert not c.tradeable
    assert "toplam pozisyon limiti" in c.reason


def test_bir_kontrattan_az_ise_islem_yok() -> None:
    c = evaluate("X", "yes", 900, 0.99, cfg(bankroll_dcents=100.0))
    assert not c.tradeable
    assert "< 1 kontrat" in c.reason


# ---------------------------------------------------------------------------
# Uç fiyat koruması
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("price", [1, 10, 29])
def test_cok_ucuz_kontrat_reddedilir(price) -> None:
    """Modelin en güvenilmez olduğu bölge; olasılık tabanı zaten yapay."""
    c = evaluate("X", "yes", price, 0.90, cfg())
    assert not c.tradeable
    assert "uç sınırı" in c.reason


@pytest.mark.parametrize("price", [971, 990, 999])
def test_cok_pahali_kontrat_reddedilir(price) -> None:
    c = evaluate("X", "yes", price, 0.999, cfg())
    assert not c.tradeable
    assert "uç sınırı" in c.reason


def test_fiyat_yoksa_islem_yok() -> None:
    """Tek taraflı kitap: o yönde alış yok."""
    c = evaluate("X", "yes", None, 0.90, cfg())
    assert not c.tradeable
    assert "tek taraflı" in c.reason


# ---------------------------------------------------------------------------
# İki yön
# ---------------------------------------------------------------------------


def test_no_tarafi_secilebilir() -> None:
    """Model kovaya düşük olasılık veriyorsa NO almak doğru yön."""
    c = best_candidate("X", 0.10, yes_ask=400, no_ask=500, cfg=cfg())
    assert c.side == "no"
    assert c.tradeable


def test_iki_yon_de_uygunsa_yuksek_net_edge_secilir() -> None:
    c = best_candidate("X", 0.80, yes_ask=300, no_ask=100, cfg=cfg())
    assert c.side == "yes"


def test_hicbir_yon_uygun_degilse_gerekce_doner() -> None:
    c = best_candidate("X", 0.50, yes_ask=500, no_ask=500, cfg=cfg())
    assert not c.tradeable
    assert c.reason


def test_her_karar_gerekceli() -> None:
    """İşlem yapmama kararı da gerekçesiyle loglanır — şart bu."""
    for q in (0.01, 0.25, 0.5, 0.75, 0.99):
        for ya, na in ((400, 600), (None, 500), (10, 990)):
            c = best_candidate("X", q, ya, na, cfg())
            assert c.reason.strip(), f"gerekçesiz karar: q={q} ya={ya} na={na}"
            assert c.binding, "bağlayan kısıt kaydedilmemiş"
