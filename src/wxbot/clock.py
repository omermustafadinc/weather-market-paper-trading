"""Zaman. Tek kural: her şey UTC ve mikrosaniye çözünürlüklü tamsayı.

Yerel saat yalnızca görüntüde kullanılır, asla saklanmaz. Lookahead kontrolleri
tamsayı karşılaştırmasına dayandığı için burada float yok.
"""

from __future__ import annotations

from datetime import datetime, timezone


def now_us() -> int:
    """Şu an, epoch'tan beri mikrosaniye (UTC)."""
    return dt_to_us(datetime.now(timezone.utc))


def dt_to_us(dt: datetime) -> int:
    if dt.tzinfo is None:
        raise ValueError(f"naive datetime kabul edilmiyor: {dt!r}")
    return int(dt.astimezone(timezone.utc).timestamp() * 1_000_000)


def us_to_dt(us: int) -> datetime:
    return datetime.fromtimestamp(us / 1_000_000, tz=timezone.utc)


def us_to_iso(us: int) -> str:
    """Okunabilir ISO-8601 UTC. Sıralama için değil, insan için."""
    return us_to_dt(us).isoformat(timespec="microseconds").replace("+00:00", "Z")


def iso_to_us(s: str) -> int:
    return dt_to_us(datetime.fromisoformat(s.replace("Z", "+00:00")))
