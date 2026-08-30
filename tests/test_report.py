"""Rapor metriklerinin testi."""

from __future__ import annotations

import pytest

from wxbot.report import (
    TradeResult,
    brier,
    calibration,
    climatology_prob,
    Case,
)


# ---------------------------------------------------------------------------
# Brier
# ---------------------------------------------------------------------------


def test_brier_mukemmel_tahmin_sifir() -> None:
    assert brier([(1.0, 1), (0.0, 0)]) == pytest.approx(0.0)


def test_brier_tam_yanlis_bir() -> None:
    assert brier([(0.0, 1), (1.0, 0)]) == pytest.approx(1.0)


def test_brier_yarim_ceyrek() -> None:
    assert brier([(0.5, 1), (0.5, 0)]) == pytest.approx(0.25)


def test_brier_bos_none() -> None:
    assert brier([]) is None


def test_brier_dusuk_olan_iyi() -> None:
    iyi = brier([(0.9, 1), (0.1, 0)])
    kotu = brier([(0.6, 1), (0.4, 0)])
    assert iyi < kotu


# ---------------------------------------------------------------------------
# Kalibrasyon
# ---------------------------------------------------------------------------


def test_kalibrasyon_mukemmel_kose_koseye() -> None:
    """%70 diyen tahminlerin %70'i gerçekleşiyorsa fark sıfır olmalı."""
    pairs = [(0.7, 1)] * 7 + [(0.7, 0)] * 3
    rows = [r for r in calibration(pairs) if r["n"]]
    assert len(rows) == 1
    assert rows[0]["mean_pred"] == pytest.approx(0.7)
    assert rows[0]["observed"] == pytest.approx(0.7)


def test_kalibrasyon_asiri_guven_yakalanir() -> None:
    """Model %90 diyor ama %50 gerçekleşiyor -> aşırı güvenli."""
    pairs = [(0.9, 1)] * 5 + [(0.9, 0)] * 5
    row = [r for r in calibration(pairs) if r["n"]][0]
    assert row["observed"] < row["mean_pred"]


def test_kalibrasyon_bos_kovalar_gosterilir() -> None:
    rows = calibration([(0.05, 1)], bins=10)
    assert len(rows) == 10
    assert sum(r["n"] for r in rows) == 1
    assert rows[0]["n"] == 1


def test_kalibrasyon_bir_olasiligi_son_kovaya_koyar() -> None:
    rows = calibration([(1.0, 1)], bins=10)
    assert rows[-1]["n"] == 1


# ---------------------------------------------------------------------------
# İşlem sonucu
# ---------------------------------------------------------------------------


def _t(side="yes", price=400.0, outcome=1, contracts=10.0, fee=50.0):
    return TradeResult("X", side, contracts, price, fee, outcome, 0.1).compute()


def test_kazanan_yes_pozisyonu() -> None:
    """10 kontrat, 40c'den, kazandı: 10×(100c − 40c) = 600c, eksi fee."""
    t = _t(side="yes", price=400.0, outcome=1)
    assert t.payoff_dcents == pytest.approx(10_000.0)
    assert t.pnl_before_fee_dcents == pytest.approx(6_000.0)
    assert t.pnl_after_fee_dcents == pytest.approx(5_950.0)


def test_kaybeden_yes_pozisyonu() -> None:
    t = _t(side="yes", price=400.0, outcome=0)
    assert t.payoff_dcents == 0.0
    assert t.pnl_before_fee_dcents == pytest.approx(-4_000.0)
    assert t.pnl_after_fee_dcents == pytest.approx(-4_050.0)


def test_no_pozisyonu_ters_sonucla_kazanir() -> None:
    """NO alan, kova GERÇEKLEŞMEYİNCE kazanır."""
    assert _t(side="no", price=600.0, outcome=0).pnl_before_fee_dcents == pytest.approx(4_000.0)
    assert _t(side="no", price=600.0, outcome=1).pnl_before_fee_dcents == pytest.approx(-6_000.0)


def test_fee_her_zaman_pnli_azaltir() -> None:
    for outcome in (0, 1):
        t = _t(outcome=outcome, fee=123.0)
        assert t.pnl_after_fee_dcents == pytest.approx(t.pnl_before_fee_dcents - 123.0)
        assert t.pnl_after_fee_dcents < t.pnl_before_fee_dcents


def test_fee_oncesi_ve_sonrasi_ayri_raporlanir() -> None:
    """Kullanıcı şartı: fee'den ÖNCE ve SONRA PnL, ayrı ayrı."""
    t = _t()
    assert t.pnl_before_fee_dcents != t.pnl_after_fee_dcents


# ---------------------------------------------------------------------------
# Klimatoloji referansı
# ---------------------------------------------------------------------------


def test_klimatoloji_kova_sayisinin_tersi() -> None:
    cases = [Case("NY", "2026-08-29", "E1", f"M{i}", 0.5, 0.5, 0, "", 24.0)
             for i in range(6)]
    assert climatology_prob(cases) == pytest.approx(1 / 6)


def test_klimatoloji_bos_sifir() -> None:
    assert climatology_prob([]) == 0.0


# ---------------------------------------------------------------------------
# Baseline karşılaştırması adil mi
# ---------------------------------------------------------------------------


def test_rastgele_baseline_ayni_buyuklukte_islem_yapar(conn) -> None:
    """Baseline bizimle AYNI kontrat adetlerini kullanmalı.

    İlk sürümde baseline tek kontratla işlem yapıyordu ve bizim ~200
    kontratlık pozisyonlarımızla karşılaştırılıyordu: rastgele +0.05 $,
    bizim +364 $. 200 katlık ölçek farkı beceri gibi görünüyordu.
    """
    import sqlite3

    from wxbot.report import random_baseline

    conn.execute(
        """INSERT INTO runs (run_uid, slot_id, slot_seconds, started_at_us)
           VALUES ('r',1,1800,1)""")
    conn.execute(
        """INSERT INTO market_snapshots
           (run_id, slot_id, purpose, venue, series_ticker, event_ticker,
            market_ticker, fetched_at_us, fetched_at_iso, source_url,
            raw_market_json, raw_book_json, yes_bid_dcents, yes_ask_dcents)
           VALUES (1,1,'decision','kalshi','KXHIGHNY','E','M',1,'i','u','{}','{}',
                   400,410)""")
    conn.execute(
        """INSERT INTO settlements
           (venue, market_ticker, event_ticker, target_date, observed_at_us,
            observed_at_iso, source, source_url, raw_json, outcome, observed_value)
           VALUES ('kalshi','M','E','2026-08-29',9999999999999999,'i','nws_cli',
                   'u','{}',1,80.0)""")

    kucuk = random_baseline(conn, [1.0] * 5, trials=50)
    buyuk = random_baseline(conn, [200.0] * 5, trials=50)
    assert kucuk and buyuk
    # 200 kat büyük pozisyonlar, kabaca 200 kat büyük saçılım üretmeli
    yayilim_k = kucuk["p95"] - kucuk["p05"]
    yayilim_b = buyuk["p95"] - buyuk["p05"]
    assert yayilim_b > yayilim_k * 50, "baseline pozisyon büyüklüğünü yok sayıyor"


def test_rastgele_baseline_bos_girdide_none(conn) -> None:
    from wxbot.report import random_baseline
    assert random_baseline(conn, []) is None
