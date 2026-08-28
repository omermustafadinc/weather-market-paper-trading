"""Lookahead yasağının testi.

Kullanıcının şartı: `data_asof > decision_at` olan tek bir satır bile varsa
sistem hata fırlatmalı. Bu dosya iki savunma katmanını ayrı ayrı sınıyor:

  A) DB CHECK kısıtı — bozuk satır zaten INSERT edilemiyor mu?
  B) Tarayıcı        — kısıt devre dışı bırakılıp satır zorla yazılsa bile
                       `assert_no_lookahead` yakalıyor mu?

B katmanı gereksiz görünebilir ama değil: CHECK kısıtları tablolar arası
ilişkileri göremez (karar hangi snapshot'a dayanıyordu, çözümleme ne zaman
yayınlandı gibi). Asıl sinsi lookahead orada olur.
"""

from __future__ import annotations

import sqlite3

import pytest

from conftest import T1, T2, T3, T4, TARGET_DATE, Fixture
from wxbot import db
from wxbot.clock import iso_to_us, us_to_iso


# ===========================================================================
# A) DB CHECK kısıtı: bozuk satır hiç girmemeli
# ===========================================================================


def test_temiz_fixture_ihlalsiz(fx: Fixture) -> None:
    """Temel veri seti geçerli olmalı, yoksa diğer testler anlamsız."""
    assert db.scan_lookahead_violations(fx.conn) == []
    db.assert_no_lookahead(fx.conn)


def test_check_kisiti_gelecekten_veriyi_reddeder(conn: sqlite3.Connection) -> None:
    """data_asof > decision_at olan bir karar INSERT edilememeli."""
    fx = Fixture(conn)
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            """INSERT INTO decisions
               (run_id, slot_id, venue, market_ticker, event_ticker, target_date,
                data_asof_us, data_asof_iso, decision_at_us, decision_at_iso,
                market_snapshot_id, forecast_basis, action, reason, model_prob,
                target_contracts)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (fx.run_id, 999, "kalshi", "X-1", "X", TARGET_DATE,
             T2, us_to_iso(T2),           # data_asof = T2
             T1, us_to_iso(T1),           # decision_at = T1  -> T2 > T1, ihlal
             fx.snap_decision, "[]", "no_trade", "test", 0.5, 0.0),
        )


def test_check_kisiti_bos_gerekce_reddeder(conn: sqlite3.Connection) -> None:
    """'İşlem yapmama kararı da gerekçesiyle loglanır' — gerekçe boş olamaz."""
    fx = Fixture(conn)
    for bad_reason in ("", "   ", "\n\t "):
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """INSERT INTO decisions
                   (run_id, slot_id, venue, market_ticker, event_ticker, target_date,
                    data_asof_us, data_asof_iso, decision_at_us, decision_at_iso,
                    market_snapshot_id, forecast_basis, action, reason, model_prob,
                    target_contracts)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (fx.run_id, 998, "kalshi", "X-2", "X", TARGET_DATE,
                 T1, us_to_iso(T1), T2, us_to_iso(T2),
                 fx.snap_decision, "[]", "no_trade", bad_reason, 0.5, 0.0),
            )


def test_check_kisiti_30sn_alti_fill_reddeder(conn: sqlite3.Connection) -> None:
    """Karar ile fill arasında en az 30 sn olmalı."""
    fx = Fixture(conn)
    conn.execute("DELETE FROM sim_fills")
    too_soon = T2 + 29_000_000  # 29 saniye
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            """INSERT INTO sim_fills
               (decision_id, fill_snapshot_id, decision_at_us, book_asof_us,
                filled_at_us, filled_at_iso, side, requested_contracts,
                filled_contracts, avg_price_cents, fee_cents, fill_status)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (fx.decision_id, fx.snap_fill, T2, T3, too_soon, us_to_iso(too_soon),
             "yes", 5.0, 5.0, 44.0, 1.0, "full"),
        )


def test_check_kisiti_istenenden_fazla_fill_reddeder(conn: sqlite3.Connection) -> None:
    fx = Fixture(conn)
    conn.execute("DELETE FROM sim_fills")
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            """INSERT INTO sim_fills
               (decision_id, fill_snapshot_id, decision_at_us, book_asof_us,
                filled_at_us, filled_at_iso, side, requested_contracts,
                filled_contracts, avg_price_cents, fee_cents, fill_status)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (fx.decision_id, fx.snap_fill, T2, T3, T4, us_to_iso(T4),
             "yes", 5.0, 9.0, 44.0, 1.0, "full"),   # 5 istendi, 9 doldu
        )


# ===========================================================================
# B) Tarayıcı: kısıt zorla atlansa bile yakalamalı
# ===========================================================================


@pytest.mark.parametrize(
    ("check_name", "sql", "params_from"),
    [
        (
            "decision_data_asof",
            "UPDATE decisions SET data_asof_us = ?, data_asof_iso = ? WHERE id = ?",
            lambda fx: (T4, us_to_iso(T4), fx.decision_id),
        ),
        (
            "decision_uses_future_market_snapshot",
            "UPDATE market_snapshots SET fetched_at_us = ?, fetched_at_iso = ? WHERE id = ?",
            lambda fx: (T4, us_to_iso(T4), fx.snap_decision),
        ),
        (
            "fill_before_min_delay",
            "UPDATE sim_fills SET filled_at_us = ? WHERE id = ?",
            lambda fx: (T2 + 1_000_000, fx.fill_id),
        ),
        (
            "fill_uses_stale_book",
            "UPDATE sim_fills SET book_asof_us = ? WHERE id = ?",
            lambda fx: (T1, fx.fill_id),
        ),
        (
            "fill_book_snapshot_mismatch",
            "UPDATE sim_fills SET book_asof_us = ? WHERE id = ?",
            lambda fx: (T3 + 7, fx.fill_id),
        ),
    ],
)
def test_tarayici_her_ihlali_yakalar(fx: Fixture, check_name, sql, params_from) -> None:
    """CHECK kısıtı devre dışı bırakılıp satır bozulsa bile tarayıcı görmeli."""
    fx.corrupt(sql, params_from(fx))

    violations = db.scan_lookahead_violations(fx.conn)
    names = {v.check for v in violations}
    assert check_name in names, f"{check_name} yakalanmadı; bulunanlar: {names}"

    with pytest.raises(db.LookaheadError) as exc:
        db.assert_no_lookahead(fx.conn)
    assert check_name in str(exc.value)


def test_tarayici_gelecekteki_tahmini_yakalar(fx: Fixture) -> None:
    """Karar, karardan sonra çekilmiş bir tahmine dayanamaz."""
    fx.corrupt(
        "UPDATE forecast_snapshots SET fetched_at_us = ?, fetched_at_iso = ? WHERE id = ?",
        (T4, us_to_iso(T4), fx.fc_id),
    )
    with pytest.raises(db.LookaheadError, match="decision_uses_future_forecast"):
        db.assert_no_lookahead(fx.conn)


def test_tarayici_sonuc_bilinerek_verilen_karari_yakalar(fx: Fixture) -> None:
    """En sinsi hâli: çözümleme yayınlandıktan SONRA verilen karar.

    Zaman damgaları tek tek tutarlı olduğu için hiçbir CHECK kısıtı bunu
    göremez — yalnızca tablolar arası bakan tarayıcı görebilir.
    """
    # Çözümleme karardan ÖNCE yayınlanmış olsun.
    early = iso_to_us("2026-08-27T13:00:00Z")
    fx.add_settlement(observed_at_us=early)

    violations = db.scan_lookahead_violations(fx.conn)
    assert "decision_after_settlement" in {v.check for v in violations}

    with pytest.raises(db.LookaheadError, match="decision_after_settlement"):
        db.assert_no_lookahead(fx.conn)


def test_normal_cozumleme_ihlal_saymaz(fx: Fixture) -> None:
    """Ertesi sabah yayınlanan çözümleme ihlal değildir."""
    fx.add_settlement()  # T5 = ertesi gün sabah
    db.assert_no_lookahead(fx.conn)


# ===========================================================================
# Bütünlük
# ===========================================================================


def test_her_kontrolun_testi_var() -> None:
    """Yeni bir kontrol eklenip testi unutulursa burası uyarsın."""
    tested = {
        "decision_data_asof",
        "decision_uses_future_market_snapshot",
        "decision_uses_future_forecast",
        "decision_after_settlement",
        "fill_before_min_delay",
        "fill_uses_stale_book",
        "fill_book_snapshot_mismatch",
        "settlement_before_target_end",
    }
    assert set(db.check_names()) == tested, (
        "db._CHECKS ile test kapsamı ayrıştı — yeni kontrole test yaz."
    )


def test_gercek_veritabani_temiz() -> None:
    """Diskteki gerçek DB varsa o da temiz olmalı.

    Bu test, raporlanan her sonucun arkasındaki asıl garanti.
    """
    if not db.DEFAULT_DB_PATH.exists():
        pytest.skip("henüz veri toplanmadı")
    conn = db.connect(db.DEFAULT_DB_PATH, read_only=True)
    try:
        db.assert_no_lookahead(conn)
    finally:
        conn.close()
