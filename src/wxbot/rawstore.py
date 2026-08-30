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

#: Ham veri kökü. `WXBOT_RAW_ROOT` ile değiştirilebilir — lokal denemelerin
#: gerçek veriye karışmaması için (alt süreçler de bu değişkeni görür).
RAW_ROOT = Path(os.environ.get("WXBOT_RAW_ROOT")
                or Path(__file__).resolve().parents[2] / "data" / "raw")

#: Kayıt biçimi sürümü. Şekil değişirse artar; ingest eski sürümleri de okur.
RECORD_VERSION = 1

KINDS = ("market", "market_meta", "forecast", "decision", "fill",
         "settlement", "invalidation")


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


# ---------------------------------------------------------------------------
# Karar ve fill kayıtları
# ---------------------------------------------------------------------------


def decision_record(
    *, run_uid: str, venue: str, slot_id: int, market_ticker: str, event_ticker: str,
    target_date: str, data_asof_us: int, data_asof_iso: str, decision_at_us: int,
    decision_at_iso: str, market_snapshot_key: str, forecast_basis: list,
    action: str, reason: str, model_prob: float, market_prob: float | None,
    edge: float | None, kelly_fraction: float | None, target_contracts: float,
    limits: dict,
) -> dict[str, Any]:
    """HER karar loglanır — işlem yapmama kararı da, gerekçesiyle."""
    return {
        "v": RECORD_VERSION, "kind": "decision", "run_uid": run_uid, "venue": venue,
        "slot_id": slot_id, "market_ticker": market_ticker,
        "event_ticker": event_ticker, "target_date": target_date,
        "data_asof_us": data_asof_us, "data_asof_iso": data_asof_iso,
        "decision_at_us": decision_at_us, "decision_at_iso": decision_at_iso,
        "market_snapshot_key": market_snapshot_key, "forecast_basis": forecast_basis,
        "action": action, "reason": reason, "model_prob": model_prob,
        "market_prob": market_prob, "edge": edge, "kelly_fraction": kelly_fraction,
        "target_contracts": target_contracts, "limits": limits,
        # rawstore.append gün dosyasını buradan seçiyor
        "fetched_at_us": decision_at_us,
    }


def fill_record(
    *, run_uid: str, venue: str, slot_id: int, market_ticker: str,
    decision_at_us: int, book_asof_us: int, filled_at_us: int, filled_at_iso: str,
    side: str, requested: float, filled: float, avg_price_dcents: float | None,
    fee_dcents: float, levels: list, status: str, notes: str,
) -> dict[str, Any]:
    return {
        "v": RECORD_VERSION, "kind": "fill", "run_uid": run_uid, "venue": venue,
        "slot_id": slot_id, "market_ticker": market_ticker,
        "decision_at_us": decision_at_us, "book_asof_us": book_asof_us,
        "filled_at_us": filled_at_us, "filled_at_iso": filled_at_iso,
        "side": side, "requested_contracts": requested, "filled_contracts": filled,
        "avg_price_dcents": avg_price_dcents, "fee_dcents": fee_dcents,
        "levels_consumed": levels, "fill_status": status, "notes": notes,
        "fetched_at_us": filled_at_us,
    }


def collected_decision_keys(day: str, slot_id: int, root: Path | None = None) -> set[str]:
    return {r["market_ticker"] for r in read_day("decision", day, root)
            if r.get("slot_id") == slot_id}


def collected_fill_keys(day: str, slot_id: int, root: Path | None = None) -> set[str]:
    return {r["market_ticker"] for r in read_day("fill", day, root)
            if r.get("slot_id") == slot_id}


def settlement_record(
    *, run_uid: str, venue: str, market_ticker: str, event_ticker: str,
    target_date: str, observed_at_us: int, observed_at_iso: str, source: str,
    source_url: str, observed_value: float, outcome: int, raw: dict,
) -> dict[str, Any]:
    """Gerçekleşen sonuç.

    `observed_at_us` gözlemin YAYINLANDIĞI andır — kararlardan sonra olmak
    zorunda. Lookahead tarayıcısındaki `decision_after_settlement` kontrolü
    tam olarak buna bakıyor.
    """
    return {
        "v": RECORD_VERSION, "kind": "settlement", "run_uid": run_uid,
        "venue": venue, "market_ticker": market_ticker,
        "event_ticker": event_ticker, "target_date": target_date,
        "observed_at_us": observed_at_us, "observed_at_iso": observed_at_iso,
        "source": source, "source_url": source_url,
        "observed_value": observed_value, "outcome": outcome, "raw": raw,
        "fetched_at_us": observed_at_us,
    }


def collected_settlement_keys(day: str, root: Path | None = None) -> set[str]:
    return {r["market_ticker"] for r in read_day("settlement", day, root)}


# ---------------------------------------------------------------------------
# İptal (karantina) — satır silmeden
# ---------------------------------------------------------------------------
#
# Hatalı bir kuralla üretilmiş türetilmiş kayıtları (karar/fill) devre dışı
# bırakmak gerekebiliyor. İlk denemede satırları dosyadan sildim ve iki sorun
# çıktı: (a) "ham veri append-only, asla üzerine yazma" şartını çiğniyor,
# (b) eşzamanlı bir CI koşusu aynı dosyaya eklerken git çakışması doğuyor.
#
# Doğrusu: hiçbir şey silme, bir İPTAL KAYDI ekle. Ingest bu kayıtları okuyup
# eşleşenleri atlar. Kayıt duruyor, neden iptal edildiği de duruyor.


def invalidation_record(
    *, run_uid: str, target_kind: str, keys: list[list], reason: str,
    at_us: int, revoke: bool = False,
) -> dict[str, Any]:
    """`keys`: [venue, market_ticker, slot_id] üçlüleri.

    `revoke=True` bir ÖNCEKİ iptali geri alır. Gerekli oldu: iptal kuralım
    yerel hedef günü UTC karar gününe karşı karşılaştırıyordu ve ABD
    şehirlerinde 00:00-04:00Z arası verilen MEŞRU ertesi-gün kararlarını
    yanlışlıkla iptal etti. Silmek yerine geri alma kaydı yazıyoruz;
    tarihçe bozulmadan kalıyor.
    """
    if target_kind not in ("decision", "fill"):
        raise ValueError(f"yalnızca türetilmiş kayıtlar iptal edilebilir: {target_kind!r}")
    return {
        "v": RECORD_VERSION, "kind": "invalidation", "run_uid": run_uid,
        "target_kind": target_kind, "keys": [list(k) for k in keys],
        "reason": reason, "revoke": bool(revoke), "fetched_at_us": at_us,
    }


def invalidated_keys(root: Path | None = None) -> dict[str, set[tuple]]:
    """{target_kind: {(venue, market_ticker, slot_id), ...}}

    Kayıtlar YAZILMA SIRASINA göre işlenir: iptal ekler, geri alma çıkarır.
    """
    out: dict[str, set[tuple]] = {"decision": set(), "fill": set()}
    for rec in sorted(read_all("invalidation", root),
                      key=lambda r: r.get("fetched_at_us", 0)):
        tk = rec.get("target_kind")
        if tk not in out:
            continue
        keys = {(k[0], k[1], int(k[2])) for k in rec.get("keys", [])}
        if rec.get("revoke"):
            out[tk] -= keys
        else:
            out[tk] |= keys
    return out
