"""Ham veri deposu: append-only JSONL.

Neden SQLite değil de JSONL:

* **Ham veri append-only olmalı.** JSONL'de yazma tek işlem: dosyanın sonuna
  satır eklemek. Var olan bir satırı değiştirmek için kod yolu yok.
* **Git ile çalışıyor.** Toplayıcı GitHub Actions'ta koşuyor ve veriyi repoya
  commit'liyor. SQLite ikili dosyası her koşuda baştan sona değişir — günde
  ~12 MB'lık binary diff, ay sonunda kullanılamaz bir repo demek. JSONL'de
  diff yalnızca eklenen satırlar kadar.
* **SQLite türetilmiş oluyor.** `wxbot.ingest` JSONL'den kurar. Bu bir kayıp
  değil kazanç: veritabanı her an sıfırdan yeniden üretilebilir, ve lookahead
  denetimi ingest kapısında çalışır.

Dosya düzeni: `data/raw/{kind}/{YYYY-MM-DD}.jsonl` — tarih, verinin ÇEKİLDİĞİ
UTC günü (hedef gün değil).
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Iterator

from .clock import us_to_dt

RAW_ROOT = Path(__file__).resolve().parents[2] / "data" / "raw"

#: Kayıt biçimi sürümü. Şekil değişirse artar; ingest eski sürümleri de okur.
RECORD_VERSION = 1

KINDS = ("market", "market_meta", "forecast")


def path_for(kind: str, fetched_at_us: int, root: Path | None = None) -> Path:
    if kind not in KINDS:
        raise ValueError(f"bilinmeyen kayıt türü: {kind!r}")
    day = us_to_dt(fetched_at_us).date().isoformat()
    return (root or RAW_ROOT) / kind / f"{day}.jsonl"


def append(kind: str, record: dict[str, Any], root: Path | None = None) -> Path:
    """Kaydı günün dosyasının sonuna ekle.

    `os.O_APPEND` ile açıyoruz: yazma atomik olarak dosya sonuna gider, var olan
    hiçbir bayta dokunulmaz. Çökme hâlinde en kötü ihtimalle yarım bir son satır
    kalır; okuyucu onu atlar (bkz. `read_day`).
    """
    fetched_at_us = int(record["fetched_at_us"])
    p = path_for(kind, fetched_at_us, root)
    p.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, separators=(",", ":"), sort_keys=True,
                      ensure_ascii=False) + "\n"
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(fd, line.encode("utf-8"))
    finally:
        os.close(fd)
    return p


def read_day(kind: str, day: str, root: Path | None = None) -> Iterator[dict[str, Any]]:
    """Bir günün kayıtlarını oku. Bozuk son satır sessizce atlanır.

    Yarım satır, koşu ortasında öldürülen bir işlemin izidir. Onu atlamak veri
    kaybı değil — o kayıt zaten hiç tamamlanmadı, ve slot idempotanlığı sayesinde
    bir sonraki koşu aynı veriyi tekrar toplar.
    """
    p = (root or RAW_ROOT) / kind / f"{day}.jsonl"
    if not p.exists():
        return
    with p.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue  # yarım satır: yok say


def days(kind: str, root: Path | None = None) -> list[str]:
    d = (root or RAW_ROOT) / kind
    if not d.exists():
        return []
    return sorted(p.stem for p in d.glob("*.jsonl"))


def read_all(kind: str, root: Path | None = None) -> Iterator[dict[str, Any]]:
    for day in days(kind, root):
        yield from read_day(kind, day, root)


# ---------------------------------------------------------------------------
# Idempotanlık
# ---------------------------------------------------------------------------


def collected_market_keys(
    day: str, slot_id: int, purpose: str, root: Path | None = None
) -> set[str]:
    """Bu slotta bu amaçla zaten toplanmış piyasa ticker'ları.

    Collector bunu SQLite'a değil doğrudan JSONL'e sorar: runner'da veritabanı
    kurmaya gerek kalmıyor, ve idempotanlık ham verinin kendisine dayanıyor.
    """
    return {
        r["market_ticker"]
        for r in read_day("market", day, root)
        if r.get("slot_id") == slot_id and r.get("purpose") == purpose
    }


def collected_forecast_keys(
    day: str, slot_id: int, root: Path | None = None
) -> set[tuple[str, str]]:
    """Bu tahmin slotunda zaten toplanmış (şehir, model) çiftleri."""
    return {
        (r["location_key"], r["model"])
        for r in read_day("forecast", day, root)
        if r.get("slot_id") == slot_id
    }


# ---------------------------------------------------------------------------
# Kayıt kurucular — şekli tek yerde tutuyoruz
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Metadata tekrarını önleme
# ---------------------------------------------------------------------------
#
# Piyasa metadata'sı bir snapshot kaydının ~%82'sini kaplıyor ve büyük kısmı
# gün boyu hiç değişmeyen kural metni (rules_secondary, early_close_condition,
# price_ranges...). Aynı 1 KB'ı günde 96 kez yazmak repoyu boşuna şişirir.
#
# Çözüm KAYIPSIZ: metadata'yı `market_meta` olarak günde bir kez yaz, snapshot
# kaydında yalnızca ondan FARKLI olan alanları tut. Geri kurma tam:
#     market = {**meta, **delta}
#
# Alan listesi elle sayılmıyor — hangi alanın değişken olduğunu veri söylüyor.
# Kalshi şemasına yeni alan eklerse kod değişmeden doğru çalışmaya devam eder.


def market_delta(meta: dict, market: dict) -> dict:
    """`market`i `meta`dan ayıran alanlar. Silinen alanlar None ile işaretlenir."""
    delta = {k: v for k, v in market.items() if meta.get(k) != v}
    for k in meta:
        if k not in market:
            delta[k] = None
    return delta


def apply_delta(meta: dict, delta: dict) -> dict:
    """`market_delta`nın tersi: tam metadata'yı geri kur."""
    out = dict(meta)
    for k, v in delta.items():
        if v is None and k in meta and k not in ("__deleted__",):
            out.pop(k, None)
        else:
            out[k] = v
    return out


def load_meta_index(day: str, root: Path | None = None) -> dict[str, dict]:
    """O güne yazılmış metadata'ları ticker -> market sözlüğü olarak getir."""
    idx: dict[str, dict] = {}
    for rec in read_day("market_meta", day, root):
        idx[rec["market_ticker"]] = rec["market"]
    return idx


def market_meta_record(
    *, run_uid: str, venue: str, market_ticker: str, fetched_at_us: int,
    fetched_at_iso: str, market: dict,
) -> dict[str, Any]:
    return {
        "v": RECORD_VERSION, "kind": "market_meta", "run_uid": run_uid, "venue": venue,
        "market_ticker": market_ticker, "fetched_at_us": fetched_at_us,
        "fetched_at_iso": fetched_at_iso, "market": market,
    }


def market_record(
    *, run_uid: str, venue: str, slot_id: int, purpose: str, series_ticker: str,
    event_ticker: str,
    market_ticker: str, target_date: str, fetched_at_us: int, fetched_at_iso: str,
    source_url: str, market_delta: dict, book: dict,
) -> dict[str, Any]:
    return {
        "v": RECORD_VERSION, "kind": "market", "run_uid": run_uid, "venue": venue,
        "slot_id": slot_id,
        "purpose": purpose, "series_ticker": series_ticker,
        "event_ticker": event_ticker, "market_ticker": market_ticker,
        "target_date": target_date, "fetched_at_us": fetched_at_us,
        "fetched_at_iso": fetched_at_iso, "source_url": source_url,
        # Tam metadata değil, o günün `market_meta` kaydından FARK.
        # Geri kurma: rawstore.apply_delta(meta, market_delta)
        "market_delta": market_delta, "book": book,
    }


def forecast_record(
    *, run_uid: str, provider: str, model: str, location_key: str, latitude: float,
    longitude: float,
    variable: str, target_dates: list[str], slot_id: int, fetched_at_us: int,
    fetched_at_iso: str, source_url: str, member_count: int, payload: dict,
) -> dict[str, Any]:
    """Tek istek birden çok hedef günü kapsıyor; payload bir kez saklanır.

    Günlere ayırmayı ingest yapar — aynı JSON'u gün sayısı kadar tekrarlamak
    dosyayı gereksiz şişirirdi.
    """
    return {
        "v": RECORD_VERSION, "kind": "forecast", "run_uid": run_uid,
        "provider": provider, "model": model,
        "location_key": location_key, "latitude": latitude, "longitude": longitude,
        "variable": variable, "target_dates": target_dates, "slot_id": slot_id,
        "fetched_at_us": fetched_at_us, "fetched_at_iso": fetched_at_iso,
        "source_url": source_url, "member_count": member_count, "payload": payload,
    }
