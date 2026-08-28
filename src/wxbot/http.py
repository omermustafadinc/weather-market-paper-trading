"""Tek HTTP kapısı. Bu modülün dışında hiçbir yerde ağ isteği yapılmaz.

Üç katmanlı kısıt (hepsi burada, tek yerde, denetlenebilir):

  1. YALNIZCA GET.  Bu modül `requests.get` dışında bir fiil kullanmaz; POST/PUT/
     DELETE gönderecek bir kod yolu *yoktur*. Emir göndermek mümkün değil.
  2. HOST WHITELIST. Listede olmayan hosta istek atılamaz.
  3. PATH DENYLIST.  Savunma derinliği: whitelist'teki bir host üzerinde bile
     hesap/emir alt ağaçlarına (Kalshi /portfolio/*) dokunulmaz.

Ayrıca her yanıt, alındığı andaki UTC zaman damgasıyla birlikte döner. Bu damga
sistemdeki `data_asof`'un tek kaynağıdır — çağıran taraf kendi zamanını uyduramaz.
"""

from __future__ import annotations

import re
import threading
import time
from dataclasses import dataclass
from typing import Any, Mapping
from urllib.parse import urlparse

import certifi
import requests

from . import __version__
from .clock import now_us

# --------------------------------------------------------------------------
# Kısıtlar
# --------------------------------------------------------------------------

#: Yalnızca bu hostlara istek atılabilir.
ALLOWED_HOSTS: frozenset[str] = frozenset(
    {
        # Piyasa verisi (read-only public endpoint'ler)
        "api.elections.kalshi.com",
        "demo-api.kalshi.co",
        "kalshi-public-docs.s3.amazonaws.com",
        # Tahmin
        "api.open-meteo.com",
        "ensemble-api.open-meteo.com",
        "historical-forecast-api.open-meteo.com",
        "previous-runs-api.open-meteo.com",
        "archive-api.open-meteo.com",
        # Ground truth / gözlem
        "api.weather.gov",
    }
)

#: Whitelist'teki hostlarda bile yasak alt ağaçlar. Kalshi'nin hesap ve emir
#: uçlarının tamamı burada; kâğıt üzerinde işlem için hiçbirine ihtiyaç yok.
DENIED_PATH_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"/portfolio(/|$)", re.I),
    re.compile(r"/orders?(/|$)", re.I),
    re.compile(r"/positions?(/|$)", re.I),
    re.compile(r"/fills?(/|$)", re.I),
    re.compile(r"/balance(/|$)", re.I),
    re.compile(r"/log[io]n(/|$)", re.I),
)

USER_AGENT = (
    f"weather-paper-trading-research/{__version__} "
    "(non-commercial research; read-only; paper trading only; "
    "contact: mustafadinc.02.02@gmail.com)"
)

#: Host başına istek/saniye tavanı. Yayınlanmış limitlerin belirgin altında
#: tutuldu; Kalshi'nin resmi limitine erişemediğimiz için orada temkinliyiz
#: (bkz. DECISIONS.md §7.5).
RATE_LIMITS: Mapping[str, float] = {
    "api.elections.kalshi.com": 4.0,
    "demo-api.kalshi.co": 4.0,
    "kalshi-public-docs.s3.amazonaws.com": 2.0,
    "api.open-meteo.com": 2.0,
    "ensemble-api.open-meteo.com": 2.0,
    "historical-forecast-api.open-meteo.com": 2.0,
    "previous-runs-api.open-meteo.com": 2.0,
    "archive-api.open-meteo.com": 2.0,
    "api.weather.gov": 2.0,
}
_DEFAULT_RATE = 1.0


class HttpGuardError(RuntimeError):
    """İstek kısıtlara takıldı. Bu hata yutulmamalı — bir kısıt ihlali işaretidir."""


class HttpFetchError(RuntimeError):
    """İstek kısıtlara uydu ama ağ/sunucu tarafında başarısız oldu."""


# --------------------------------------------------------------------------
# Rate limit
# --------------------------------------------------------------------------


class _TokenBucket:
    """Host başına basit token bucket. Süreç içi; thread-safe."""

    def __init__(self, rate_per_sec: float, burst: float | None = None) -> None:
        self.rate = rate_per_sec
        self.capacity = burst if burst is not None else max(1.0, rate_per_sec)
        self._tokens = self.capacity
        self._last = time.monotonic()
        self._lock = threading.Lock()

    def take(self) -> None:
        with self._lock:
            while True:
                now = time.monotonic()
                self._tokens = min(
                    self.capacity, self._tokens + (now - self._last) * self.rate
                )
                self._last = now
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return
                time.sleep((1.0 - self._tokens) / self.rate)


_buckets: dict[str, _TokenBucket] = {}
_buckets_lock = threading.Lock()


def _bucket_for(host: str) -> _TokenBucket:
    with _buckets_lock:
        if host not in _buckets:
            _buckets[host] = _TokenBucket(RATE_LIMITS.get(host, _DEFAULT_RATE))
        return _buckets[host]


# --------------------------------------------------------------------------
# Doğrulama
# --------------------------------------------------------------------------


def check_url(url: str) -> str:
    """URL'i kısıtlara karşı doğrula, host'u döndür. İhlalde HttpGuardError.

    Bu fonksiyon ayrı ve saf tutuldu ki test edilebilsin.
    """
    parsed = urlparse(url)

    if parsed.scheme != "https":
        raise HttpGuardError(f"yalnızca https: {url!r} (scheme={parsed.scheme!r})")

    host = parsed.hostname or ""
    if host not in ALLOWED_HOSTS:
        raise HttpGuardError(
            f"host whitelist'te değil: {host!r}. "
            f"İzinliler: {sorted(ALLOWED_HOSTS)}"
        )

    for pat in DENIED_PATH_PATTERNS:
        if pat.search(parsed.path):
            raise HttpGuardError(
                f"yasak path: {parsed.path!r} (kural: {pat.pattern!r}). "
                "Bu ajan hesap/emir uçlarına dokunmaz."
            )

    return host


# --------------------------------------------------------------------------
# Yanıt
# --------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Response:
    """Bir GET'in sonucu.

    `fetched_at_us`: yanıtın *alındığı* an (UTC, mikrosaniye). Veri bundan daha
    yeni olamaz, dolayısıyla `data_asof` için tutucu ve doğru seçim budur.
    """

    url: str
    status: int
    body: bytes
    fetched_at_us: int
    elapsed_ms: int

    def json(self) -> Any:
        import json

        return json.loads(self.body)

    @property
    def text(self) -> str:
        return self.body.decode("utf-8", errors="replace")


# --------------------------------------------------------------------------
# Tek giriş noktası
# --------------------------------------------------------------------------


class Fetcher:
    """Kısıtlı GET istemcisi.

    Bilerek `get` dışında metot yok. Bir yerde emir göndermek istesek bile
    bu sınıfla yapamayız.
    """

    def __init__(self, *, timeout: float = 30.0, max_retries: int = 3) -> None:
        self.timeout = timeout
        self.max_retries = max_retries
        self._session = requests.Session()
        self._session.headers.update(
            {"User-Agent": USER_AGENT, "Accept": "application/json"}
        )
        # macOS'ta python.org kurulumunun sistem CA'sı yok; certifi'yi zorluyoruz.
        self._session.verify = certifi.where()

    def get(self, url: str, params: Mapping[str, Any] | None = None) -> Response:
        host = check_url(url)
        last_err: Exception | None = None

        for attempt in range(self.max_retries):
            _bucket_for(host).take()
            t0 = time.monotonic()
            try:
                resp = self._session.get(url, params=params, timeout=self.timeout)
            except requests.RequestException as exc:
                last_err = exc
                time.sleep(min(2**attempt, 8))
                continue

            fetched_at_us = now_us()
            elapsed_ms = int((time.monotonic() - t0) * 1000)

            if resp.status_code == 429 or resp.status_code >= 500:
                last_err = HttpFetchError(
                    f"HTTP {resp.status_code} {url} :: {resp.text[:200]}"
                )
                retry_after = resp.headers.get("Retry-After")
                delay = (
                    float(retry_after)
                    if retry_after and retry_after.isdigit()
                    else min(2**attempt, 8)
                )
                time.sleep(delay)
                continue

            if resp.status_code >= 400:
                raise HttpFetchError(
                    f"HTTP {resp.status_code} {resp.url} :: {resp.text[:300]}"
                )

            return Response(
                url=resp.url,
                status=resp.status_code,
                body=resp.content,
                fetched_at_us=fetched_at_us,
                elapsed_ms=elapsed_ms,
            )

        raise HttpFetchError(f"{self.max_retries} denemede başarısız: {url}") from last_err

    def close(self) -> None:
        self._session.close()

    def __enter__(self) -> "Fetcher":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
