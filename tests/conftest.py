"""Test yardımcıları: tutarlı, geçerli bir temel veri seti kurar.

Testler bu temelin üstünde tek bir alanı bozarak her kontrolü ayrı ayrı sınar.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from wxbot import db  # noqa: E402
from wxbot.clock import iso_to_us, us_to_iso  # noqa: E402

# Sabit zaman çizelgesi (hepsi UTC):
#   T0  tahmin çekildi
#   T1  piyasa kitabı çekildi        (data_asof)
#   T2  karar verildi                (decision_at)   T2 > T1
#   T3  45 sn sonra ikinci kitap     (book_asof)
#   T4  fill hesaplandı              T4 - T2 >= 30 sn
#   T5  ertesi sabah çözümleme yayınlandı
T0 = iso_to_us("2026-08-27T13:58:00Z")
T1 = iso_to_us("2026-08-27T14:00:00Z")
T2 = iso_to_us("2026-08-27T14:00:05Z")
T3 = iso_to_us("2026-08-27T14:00:50Z")
T4 = iso_to_us("2026-08-27T14:00:52Z")
T5 = iso_to_us("2026-08-29T11:05:00Z")

TARGET_DATE = "2026-08-28"
TICKER = "KXHIGHNY-26AUG28-B80.5"
EVENT = "KXHIGHNY-26AUG28"
SERIES = "KXHIGHNY"
VENUE = "kalshi"
SLOT = 100


class Fixture:
    """Geçerli bir temel veri seti + tek alan bozma yardımcısı."""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self.run_id = self._run()
        self.snap_decision = self._snapshot(T1, "decision")
        self.snap_fill = self._snapshot(T3, "fill")
        self.fc_id = self._forecast(T0)
        self.decision_id = self._decision()
        self.fill_id = self._fill()

    # -- ekleyiciler ------------------------------------------------------
    def _run(self) -> int:
        cur = self.conn.execute(
            "INSERT INTO runs (run_uid, slot_id, slot_seconds, started_at_us, status)"
            " VALUES (?,?,?,?,'ok')",
            ("test-run-1", SLOT, 900, T0),
        )
        return int(cur.lastrowid)

    def _snapshot(self, at_us: int, purpose: str) -> int:
        cur = self.conn.execute(
            """INSERT INTO market_snapshots
               (run_id, slot_id, purpose, venue, series_ticker, event_ticker,
                market_ticker, fetched_at_us, fetched_at_iso, source_url,
                raw_market_json, raw_book_json, yes_bid_cents, yes_ask_cents)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (self.run_id, SLOT, purpose, VENUE, SERIES, EVENT, TICKER, at_us,
             us_to_iso(at_us), "https://api.elections.kalshi.com/x", "{}",
             '{"yes_dollars":[["0.4300","52.00"]],"no_dollars":[]}', 43, 44),
        )
        return int(cur.lastrowid)

    def _forecast(self, at_us: int) -> int:
        cur = self.conn.execute(
            """INSERT INTO forecast_snapshots
               (run_id, slot_id, provider, model, location_key, latitude, longitude,
                variable, target_date, fetched_at_us, fetched_at_iso, source_url,
                raw_json, member_count)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (self.run_id, SLOT, "open-meteo", "ecmwf_ifs025", "NY", 40.78, -73.97,
             "temperature_2m_max", TARGET_DATE, at_us, us_to_iso(at_us),
             "https://ensemble-api.open-meteo.com/x", "{}", 51),
        )
        return int(cur.lastrowid)

    def _decision(self) -> int:
        cur = self.conn.execute(
            """INSERT INTO decisions
               (run_id, slot_id, venue, market_ticker, event_ticker, target_date,
                data_asof_us, data_asof_iso, decision_at_us, decision_at_iso,
                market_snapshot_id, forecast_basis, action, reason,
                model_prob, market_prob, edge, kelly_fraction, target_contracts)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (self.run_id, SLOT, VENUE, TICKER, EVENT, TARGET_DATE,
             T1, us_to_iso(T1), T2, us_to_iso(T2),
             self.snap_decision, f"[{self.fc_id}]", "buy_yes",
             "model %52 diyor, ask 44c, edge 8 puan > 4 puan eşiği",
             0.52, 0.44, 0.08, 0.25, 5.0),
        )
        return int(cur.lastrowid)

    def _fill(self) -> int:
        cur = self.conn.execute(
            """INSERT INTO sim_fills
               (decision_id, fill_snapshot_id, decision_at_us, book_asof_us,
                filled_at_us, filled_at_iso, side, requested_contracts,
                filled_contracts, avg_price_cents, fee_cents, fill_status)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (self.decision_id, self.snap_fill, T2, T3, T4, us_to_iso(T4),
             "yes", 5.0, 5.0, 44.0, 1.0, "full"),
        )
        return int(cur.lastrowid)

    def add_settlement(self, observed_at_us: int = T5) -> int:
        cur = self.conn.execute(
            """INSERT INTO settlements
               (venue, market_ticker, event_ticker, target_date, observed_at_us,
                observed_at_iso, source, source_url, raw_json, outcome, observed_value)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (VENUE, TICKER, EVENT, TARGET_DATE, observed_at_us,
             us_to_iso(observed_at_us), "nws_cli",
             "https://api.weather.gov/products/x", "{}", 1, 81.0),
        )
        return int(cur.lastrowid)

    def corrupt(self, sql: str, params: tuple = ()) -> None:
        """CHECK kısıtlarını geçici olarak kapatıp bozuk satır yaz.

        Tarayıcıyı CHECK kısıtlarından BAĞIMSIZ sınamak için gerekli: iki
        savunma katmanının ikisini de ayrı ayrı test etmek istiyoruz.
        """
        self.conn.execute("PRAGMA ignore_check_constraints = ON")
        try:
            self.conn.execute(sql, params)
        finally:
            self.conn.execute("PRAGMA ignore_check_constraints = OFF")


@pytest.fixture()
def conn() -> sqlite3.Connection:
    c = db.init_db(":memory:")
    yield c
    c.close()


@pytest.fixture()
def fx(conn: sqlite3.Connection) -> Fixture:
    return Fixture(conn)
