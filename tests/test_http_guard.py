"""HTTP kısıtlarının testi.

Kullanıcının katı kısıtları: hiçbir koşulda emir gönderen endpoint çağrılmayacak,
sadece read-only. Bu dosya bunun kodla zorlandığını doğruluyor — niyet beyanıyla
değil.
"""

from __future__ import annotations

import inspect
import re
from pathlib import Path

import pytest

from wxbot import http as wxhttp
from wxbot.http import ALLOWED_HOSTS, Fetcher, HttpGuardError, check_url

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"


# ---------------------------------------------------------------------------
# Host whitelist
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "url",
    [
        f"{KALSHI}/markets?series_ticker=KXHIGHNY",
        f"{KALSHI}/markets/KXHIGHNY-26AUG28-B80.5/orderbook?depth=30",
        f"{KALSHI}/events?series_ticker=KXHIGHNY",
        "https://ensemble-api.open-meteo.com/v1/ensemble?latitude=40.78",
        "https://api.weather.gov/products/types/CLI/locations/NYC",
    ],
)
def test_izinli_urller_gecer(url: str) -> None:
    assert check_url(url) in ALLOWED_HOSTS


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com/anything",
        "https://api.openai.com/v1/chat",
        "https://gamma-api.polymarket.com/markets",   # araştırıldı ama kullanılmıyor
        "https://r.jina.ai/https://api.elections.kalshi.com/x",  # teşhis aracı, üretimde yok
        "https://evil.api.elections.kalshi.com.attacker.net/x",
    ],
)
def test_whitelist_disi_host_reddedilir(url: str) -> None:
    with pytest.raises(HttpGuardError, match="whitelist"):
        check_url(url)


@pytest.mark.parametrize("scheme", ["http", "ftp", "file"])
def test_https_disi_reddedilir(scheme: str) -> None:
    with pytest.raises(HttpGuardError, match="https"):
        check_url(f"{scheme}://api.elections.kalshi.com/trade-api/v2/markets")


# ---------------------------------------------------------------------------
# Path denylist — savunma derinliği
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "path",
    [
        "/trade-api/v2/portfolio/orders",
        "/trade-api/v2/portfolio/orders/abc-123",
        "/trade-api/v2/portfolio/positions",
        "/trade-api/v2/portfolio/balance",
        "/trade-api/v2/portfolio/fills",
        "/trade-api/v2/login",
    ],
)
def test_emir_ve_hesap_yollari_reddedilir(path: str) -> None:
    """Whitelist'teki host üzerinde bile hesap/emir alt ağacına gidilemez."""
    with pytest.raises(HttpGuardError, match="yasak path"):
        check_url(f"https://api.elections.kalshi.com{path}")


# ---------------------------------------------------------------------------
# Fetcher yüzeyi: GET dışında fiil YOK
# ---------------------------------------------------------------------------


def test_fetcher_sadece_get_sunar() -> None:
    public = {n for n in dir(Fetcher) if not n.startswith("_")}
    assert public == {"get", "close"}, f"beklenmeyen public metot: {public}"


@pytest.mark.parametrize("verb", ["post", "put", "delete", "patch", "head", "options"])
def test_fetcher_yazma_fiili_barindirmaz(verb: str) -> None:
    assert not hasattr(Fetcher, verb)


def test_paket_kodunda_yazma_fiili_yok() -> None:
    """Kaynak taraması: pakette hiçbir yerde POST/PUT/DELETE çağrısı olmamalı.

    Guard'ı aşan bir kod yolu ileride yanlışlıkla eklenirse burası patlasın.
    """
    pkg = Path(wxhttp.__file__).parent
    pattern = re.compile(
        r"\b(requests|session|self\._session)\s*\.\s*(post|put|delete|patch)\s*\(",
        re.I,
    )
    offenders = []
    for py in pkg.rglob("*.py"):
        for i, line in enumerate(py.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                offenders.append(f"{py.name}:{i}: {line.strip()}")
    assert not offenders, "yazma fiili bulundu:\n" + "\n".join(offenders)


def test_get_govdesinde_tek_fiil_get() -> None:
    src = inspect.getsource(Fetcher.get)
    assert "_session.get(" in src
    for verb in ("post", "put", "delete", "patch"):
        assert f"_session.{verb}(" not in src


# ---------------------------------------------------------------------------
# User-Agent
# ---------------------------------------------------------------------------


def test_user_agent_aciklayici() -> None:
    ua = wxhttp.USER_AGENT
    assert "research" in ua.lower()
    assert "read-only" in ua.lower()
    assert "github.com/" in ua, "iletişim bilgisi (repo adresi) olmalı"


def test_user_agent_kisisel_eposta_sizdirmaz() -> None:
    """Repo public; User-Agent her isteğe gidiyor. Kişisel e-posta olmamalı."""
    assert "@" not in wxhttp.USER_AGENT, (
        "User-Agent'ta e-posta var — public repoda ve her HTTP isteğinde görünür"
    )


def test_her_izinli_host_icin_rate_limit_tanimli() -> None:
    missing = ALLOWED_HOSTS - set(wxhttp.RATE_LIMITS)
    assert not missing, f"rate limit tanımsız host: {missing}"
