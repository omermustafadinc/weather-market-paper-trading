"""SQLite katmanı ve lookahead denetimi.

Lookahead'e karşı iki savunma var:

  1. DB CHECK kısıtları (schema.sql) — ihlal eden satır zaten INSERT edilemez.
  2. Buradaki tarayıcı — tüm tabloyu baştan sona okur ve tek bir ihlal bulursa
     `LookaheadError` fırlatır. İkinci katman gereksiz değil: CHECK kısıtları
     yalnızca satır-içi ilişkileri görebilir, tablolar arası ilişkileri
     (karar hangi snapshot'a dayanıyordu, çözümleme ne zaman yayınlandı)
     göremez.

`assert_no_lookahead()` çağrılmadan hiçbir sonuç raporlanmaz.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from .clock import us_to_iso

SCHEMA_PATH = Path(__file__).with_name("schema.sql")
DEFAULT_DB_PATH = Path(__file__).resolve().parents[2] / "data" / "wxbot.db"

#: Karar ile fill arasındaki asgari gecikme (mikrosaniye).
MIN_FILL_DELAY_US = 30_000_000


class LookaheadError(AssertionError):
    """Geleceğe bakma tespit edildi. Bu hata asla yutulmaz."""


@dataclass(frozen=True, slots=True)
class Violation:
    check: str
    table: str
    row_id: int
    detail: str

    def __str__(self) -> str:
        return f"[{self.check}] {self.table}#{self.row_id}: {self.detail}"


# ---------------------------------------------------------------------------
# Bağlantı
# ---------------------------------------------------------------------------


def connect(path: str | Path = DEFAULT_DB_PATH, *, read_only: bool = False) -> sqlite3.Connection:
    path = Path(path)
    if not read_only:
        path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA synchronous = FULL")  # çökmede veri kaybetme
    return conn


def init_db(path: str | Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = connect(path)
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.execute(
        "INSERT OR IGNORE INTO meta (key, value) VALUES ('schema_version', '1')"
    )
    return conn


# ---------------------------------------------------------------------------
# Lookahead taraması
# ---------------------------------------------------------------------------

#: (isim, açıklama, sorgu). Her sorgu ihlal eden satırları döndürür.
#: Sorgular `id` ve `detail` sütunlarını döndürmeli.
_CHECKS: tuple[tuple[str, str, str], ...] = (
    (
        "decision_data_asof",
        "Kararın verisi karardan sonra gelmiş",
        """
        SELECT id,
               'data_asof=' || data_asof_iso || ' > decision_at=' || decision_at_iso
                   || ' (' || market_ticker || ')' AS detail
        FROM decisions
        WHERE data_asof_us > decision_at_us
        """,
    ),
    (
        "decision_uses_future_market_snapshot",
        "Karar, karardan sonra çekilmiş bir piyasa snapshot'ına dayanıyor",
        """
        SELECT d.id,
               'market_snapshot#' || m.id || ' fetched=' || m.fetched_at_iso
                   || ' > decision_at=' || d.decision_at_iso AS detail
        FROM decisions d
        JOIN market_snapshots m ON m.id = d.market_snapshot_id
        WHERE m.fetched_at_us > d.decision_at_us
        """,
    ),
    (
        "decision_uses_future_forecast",
        "Karar, karardan sonra çekilmiş bir tahmine dayanıyor",
        """
        SELECT d.id,
               'forecast_snapshot#' || f.id || ' fetched=' || f.fetched_at_iso
                   || ' > decision_at=' || d.decision_at_iso AS detail
        FROM decisions d
        JOIN json_each(d.forecast_basis) je
        JOIN forecast_snapshots f ON f.id = je.value
        WHERE f.fetched_at_us > d.decision_at_us
        """,
    ),
    (
        "decision_after_settlement",
        "Karar, sonucun yayınlanmasından sonra verilmiş (cevabı bilerek işlem)",
        """
        SELECT d.id,
               'settlement observed=' || s.observed_at_iso
                   || ' <= decision_at=' || d.decision_at_iso
                   || ' (' || d.market_ticker || ')' AS detail
        FROM decisions d
        JOIN settlements s
          ON s.market_ticker = d.market_ticker AND s.venue = d.venue
        WHERE d.decision_at_us >= s.observed_at_us
        """,
    ),
    (
        "decision_on_past_or_today",
        "Karar, hedef günü geçmiş veya içinde bulunulan bir olayda verilmiş",
        """
        SELECT id,
               'hedef ' || target_date || ' <= karar günü (yerel) '
                   || decision_local_date
                   || ' (' || market_ticker || ')' AS detail
        FROM decisions
        WHERE target_date <= decision_local_date
        """,
    ),
    (
        "fill_before_min_delay",
        "Fill, karardan sonra 30 saniye beklemeden gerçekleşmiş",
        """
        SELECT id,
               'gecikme=' || ((filled_at_us - decision_at_us) / 1000000.0)
                   || 's < 30s' AS detail
        FROM sim_fills
        WHERE filled_at_us - decision_at_us < 30000000
        """,
    ),
    (
        "fill_uses_stale_book",
        "Fill, karardan ÖNCEKİ bir orderbook'a karşı hesaplanmış",
        """
        SELECT id,
               'book_asof_us=' || book_asof_us || ' < decision_at_us=' || decision_at_us
                   AS detail
        FROM sim_fills
        WHERE book_asof_us < decision_at_us
        """,
    ),
    (
        "fill_book_snapshot_mismatch",
        "Fill'in referans verdiği snapshot ile kaydettiği kitap zamanı uyuşmuyor",
        """
        SELECT f.id,
               'sim_fills.book_asof_us=' || f.book_asof_us
                   || ' != market_snapshots.fetched_at_us=' || m.fetched_at_us AS detail
        FROM sim_fills f
        JOIN market_snapshots m ON m.id = f.fill_snapshot_id
        WHERE f.book_asof_us <> m.fetched_at_us
        """,
    ),
    (
        "settlement_before_target_end",
        "Çözümleme, hedef günün bitmesinden önce kaydedilmiş",
        """
        SELECT id,
               'observed=' || observed_at_iso || ' target_date=' || target_date AS detail
        FROM settlements
        WHERE observed_at_us < CAST(strftime('%s', target_date || ' 00:00:00') AS INTEGER)
                               * 1000000
        """,
    ),
)


def scan_lookahead_violations(conn: sqlite3.Connection) -> list[Violation]:
    """Tüm kontrolleri çalıştır, ihlalleri döndür. Boş liste = temiz."""
    violations: list[Violation] = []
    table_of = {
        "decision_data_asof": "decisions",
        "decision_uses_future_market_snapshot": "decisions",
        "decision_uses_future_forecast": "decisions",
        "decision_after_settlement": "decisions",
        "decision_on_past_or_today": "decisions",
        "fill_before_min_delay": "sim_fills",
        "fill_uses_stale_book": "sim_fills",
        "fill_book_snapshot_mismatch": "sim_fills",
        "settlement_before_target_end": "settlements",
    }
    for name, _desc, sql in _CHECKS:
        for row in conn.execute(sql):
            violations.append(
                Violation(
                    check=name,
                    table=table_of[name],
                    row_id=int(row["id"]),
                    detail=str(row["detail"]),
                )
            )
    return violations


def assert_no_lookahead(conn: sqlite3.Connection) -> None:
    """İhlal varsa LookaheadError fırlat.

    Rapor üreten her kod yolu bunu ÖNCE çağırmak zorunda.
    """
    violations = scan_lookahead_violations(conn)
    if violations:
        lines = "\n".join(f"  {v}" for v in violations[:50])
        more = "" if len(violations) <= 50 else f"\n  ... ve {len(violations) - 50} tane daha"
        raise LookaheadError(
            f"{len(violations)} lookahead ihlali bulundu — sonuç raporlanmayacak:\n"
            f"{lines}{more}"
        )


def check_names() -> list[str]:
    return [name for name, _d, _s in _CHECKS]


# ---------------------------------------------------------------------------
# Küçük yardımcılar
# ---------------------------------------------------------------------------


def slot_id_for(us: int, slot_seconds: int) -> int:
    """Zamanı sabit aralıklı bir slota indir. Idempotanlığın anahtarı."""
    return (us // 1_000_000) // slot_seconds


def json_dumps(obj: object) -> str:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True, ensure_ascii=False)


def iso(us: int) -> str:
    return us_to_iso(us)
