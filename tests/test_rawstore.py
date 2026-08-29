"""Ham veri deposunun testi: append-only gerçekten append-only mi?"""

from __future__ import annotations

import json

import pytest

from wxbot import ingest, rawstore
from wxbot.clock import iso_to_us, us_to_iso
from wxbot.db import LookaheadError

T = iso_to_us("2026-08-28T14:00:00Z")


def _market(ticker, bid="0.4300"):
    return {"ticker": ticker, "yes_bid_dollars": bid, "yes_ask_dollars": "0.4400",
            "volume_fp": "2071.61", "rules_primary": "uzun statik kural metni " * 8}


def _meta_rec(ticker="KXHIGHNY-26AUG29-B79.5", at=T):
    return rawstore.market_meta_record(
        run_uid="test-1", venue="kalshi", market_ticker=ticker, fetched_at_us=at,
        fetched_at_iso=us_to_iso(at), market=_market(ticker))


def _market_rec(ticker="KXHIGHNY-26AUG29-B79.5", slot=1, at=T, purpose="decision",
                bid="0.4300"):
    meta = _market(ticker)
    return rawstore.market_record(
        run_uid="test-1", venue="kalshi", slot_id=slot, purpose=purpose,
        series_ticker="KXHIGHNY", event_ticker="KXHIGHNY-26AUG29",
        market_ticker=ticker, target_date="2026-08-29", fetched_at_us=at,
        fetched_at_iso=us_to_iso(at), source_url="https://api.elections.kalshi.com/x",
        market_delta=rawstore.market_delta(meta, _market(ticker, bid)),
        book={"orderbook_fp": {"yes_dollars": [["0.4300", "52"], ["0.0350", "10"]],
                               "no_dollars": [["0.5600", "16"]]}},
    )


def _forecast_rec(model="ecmwf_ifs025", slot=1, at=T, city="NY"):
    return rawstore.forecast_record(
        run_uid="test-1", provider="open-meteo", model=model, location_key=city,
        latitude=40.7833, longitude=-73.9667, variable="temperature_2m_max",
        target_dates=["2026-08-28", "2026-08-29"], slot_id=slot, fetched_at_us=at,
        fetched_at_iso=us_to_iso(at), source_url="https://ensemble-api.open-meteo.com/x",
        member_count=51, payload={"daily": {"time": ["2026-08-28", "2026-08-29"]}},
    )


# ---------------------------------------------------------------------------


def test_yaz_oku_dongusu(tmp_path) -> None:
    rawstore.append("market", _market_rec(), tmp_path)
    got = list(rawstore.read_day("market", "2026-08-28", tmp_path))
    assert len(got) == 1
    assert got[0]["market_ticker"] == "KXHIGHNY-26AUG29-B79.5"
    assert got[0]["book"]["orderbook_fp"]["yes_dollars"][0] == ["0.4300", "52"]


def test_dosya_gune_gore_ayrilir(tmp_path) -> None:
    rawstore.append("market", _market_rec(at=iso_to_us("2026-08-28T23:59:00Z")), tmp_path)
    rawstore.append("market", _market_rec(at=iso_to_us("2026-08-29T00:01:00Z")), tmp_path)
    assert rawstore.days("market", tmp_path) == ["2026-08-28", "2026-08-29"]


def test_ekleme_var_olan_satirlari_bozmaz(tmp_path) -> None:
    """Append-only'nin özü: eski baytlar aynı kalmalı."""
    p = rawstore.append("market", _market_rec(ticker="A"), tmp_path)
    before = p.read_bytes()
    rawstore.append("market", _market_rec(ticker="B"), tmp_path)
    rawstore.append("market", _market_rec(ticker="C"), tmp_path)
    after = p.read_bytes()
    assert after.startswith(before), "var olan içerik değişmiş"
    assert len(list(rawstore.read_day("market", "2026-08-28", tmp_path))) == 3


def test_yarim_son_satir_atlanir(tmp_path) -> None:
    """Koşu ortasında öldürülen işlem yarım satır bırakabilir; okuyucu atlamalı."""
    p = rawstore.append("market", _market_rec(ticker="A"), tmp_path)
    with p.open("a") as fh:
        fh.write('{"kind":"market","market_ticker":"YARIM"')   # kapanmamış JSON
    recs = list(rawstore.read_day("market", "2026-08-28", tmp_path))
    assert len(recs) == 1 and recs[0]["market_ticker"] == "A"


def test_idempotanlik_anahtarlari(tmp_path) -> None:
    rawstore.append("market", _market_rec(ticker="A", slot=7), tmp_path)
    rawstore.append("market", _market_rec(ticker="B", slot=7), tmp_path)
    rawstore.append("market", _market_rec(ticker="C", slot=8), tmp_path)

    assert rawstore.collected_market_keys("2026-08-28", 7, "decision", tmp_path) == {"A", "B"}
    assert rawstore.collected_market_keys("2026-08-28", 8, "decision", tmp_path) == {"C"}
    assert rawstore.collected_market_keys("2026-08-28", 9, "decision", tmp_path) == set()


def test_amac_ayrimi_slot_icinde_korunur(tmp_path) -> None:
    """Karar kitabı ile fill kitabı aynı slotta ayrı ayrı toplanabilmeli."""
    rawstore.append("market", _market_rec(ticker="A", slot=7, purpose="decision"), tmp_path)
    assert rawstore.collected_market_keys("2026-08-28", 7, "fill", tmp_path) == set()
    rawstore.append("market", _market_rec(ticker="A", slot=7, purpose="fill"), tmp_path)
    assert rawstore.collected_market_keys("2026-08-28", 7, "fill", tmp_path) == {"A"}


def test_tahmin_anahtarlari(tmp_path) -> None:
    rawstore.append("forecast", _forecast_rec(model="gfs025", city="NY"), tmp_path)
    rawstore.append("forecast", _forecast_rec(model="gfs025", city="CHI"), tmp_path)
    keys = rawstore.collected_forecast_keys("2026-08-28", 1, tmp_path)
    assert keys == {("NY", "gfs025"), ("CHI", "gfs025")}


def test_bilinmeyen_tur_reddedilir() -> None:
    with pytest.raises(ValueError, match="bilinmeyen kayıt türü"):
        rawstore.path_for("saçma", T)


# ---------------------------------------------------------------------------
# Ingest
# ---------------------------------------------------------------------------


def test_ingest_ve_idempotanlik(tmp_path, conn) -> None:
    for t in ("A", "B"):
        rawstore.append("market_meta", _meta_rec(ticker=t), tmp_path)
        rawstore.append("market", _market_rec(ticker=t), tmp_path)
    rawstore.append("forecast", _forecast_rec(), tmp_path)

    s1 = ingest.ingest_all(conn, tmp_path, verbose=False)
    assert s1["market_new"] == 2
    assert s1["forecast_new"] == 2          # bir kayıt, iki hedef gün

    s2 = ingest.ingest_all(conn, tmp_path, verbose=False)
    assert s2["market_new"] == 0 and s2["forecast_new"] == 0, "ingest idempotent değil"

    n = conn.execute("SELECT count(*) FROM orderbook_levels").fetchone()[0]
    assert n == 6                            # 2 piyasa × 3 seviye
    # Yarım sent bilgisi aktarımda korunmuş olmalı
    prices = {r[0] for r in conn.execute("SELECT price_dcents FROM orderbook_levels")}
    assert 35 in prices, "0.0350 fiyatı kayboldu"


def test_ingest_lookahead_kapisi(tmp_path, conn) -> None:
    """Ham veri kirliyse SQLite'a giremez — ingest gürültülü başarısız olur."""
    rawstore.append("market_meta", _meta_rec(), tmp_path)
    rawstore.append("market", _market_rec(), tmp_path)
    ingest.ingest_all(conn, tmp_path, verbose=False)

    snap = conn.execute("SELECT id, fetched_at_us FROM market_snapshots").fetchone()
    # Karardan SONRA çekilmiş bir snapshot'a dayanan karar yazmayı dene
    with pytest.raises(Exception):
        conn.execute(
            """INSERT INTO decisions
               (run_id, slot_id, venue, market_ticker, event_ticker, target_date,
                data_asof_us, data_asof_iso, decision_at_us, decision_at_iso,
                market_snapshot_id, forecast_basis, action, reason, model_prob,
                target_contracts)
               VALUES (1,1,'kalshi','X','X','2026-08-29',?,?,?,?,?,'[]','no_trade',
                       'test',0.5,0)""",
            (snap["fetched_at_us"], us_to_iso(snap["fetched_at_us"]),
             snap["fetched_at_us"] - 1, us_to_iso(snap["fetched_at_us"] - 1),
             snap["id"]),
        )


# ---------------------------------------------------------------------------
# Metadata tekrarını önleme — kayıpsız mı?
# ---------------------------------------------------------------------------


def test_delta_donusu_kayipsiz() -> None:
    """{**meta, **delta} tam metadata'yı geri vermeli."""
    meta = _market("A")
    now = _market("A", bid="0.5100")
    now["status"] = "active"                    # yeni alan
    delta = rawstore.market_delta(meta, now)
    assert rawstore.apply_delta(meta, delta) == now


def test_delta_yalnizca_degiseni_tasir() -> None:
    """Asıl kazanç: statik kural metni delta'ya girmemeli."""
    meta = _market("A")
    delta = rawstore.market_delta(meta, _market("A", bid="0.5100"))
    assert set(delta) == {"yes_bid_dollars"}
    assert "rules_primary" not in delta


def test_degismeyen_snapshot_bos_delta() -> None:
    meta = _market("A")
    assert rawstore.market_delta(meta, _market("A")) == {}


def test_delta_silinen_alani_yakalar() -> None:
    meta = _market("A")
    now = _market("A")
    del now["volume_fp"]
    delta = rawstore.market_delta(meta, now)
    assert delta["volume_fp"] is None
    assert rawstore.apply_delta(meta, delta) == now


def test_ingest_metadata_eksikse_patlar(tmp_path, conn) -> None:
    """market_meta yoksa sessizce eksik veriyle devam etmek yerine hata ver."""
    rawstore.append("market", _market_rec(ticker="Z"), tmp_path)   # meta yazılmadı
    with pytest.raises(ingest.IngestError, match="market_meta"):
        ingest.ingest_all(conn, tmp_path, verbose=False)


def test_ingest_metadatayi_geri_kurar(tmp_path, conn) -> None:
    """DB'ye yazılan metadata, orijinalinin aynısı olmalı."""
    rawstore.append("market_meta", _meta_rec(ticker="A"), tmp_path)
    rawstore.append("market", _market_rec(ticker="A", bid="0.5100"), tmp_path)
    ingest.ingest_all(conn, tmp_path, verbose=False)

    row = conn.execute("SELECT raw_market_json, yes_bid_dcents FROM market_snapshots").fetchone()
    stored = json.loads(row["raw_market_json"])
    assert stored == _market("A", bid="0.5100"), "metadata geri kurulamadı"
    assert row["yes_bid_dcents"] == 510


# ---------------------------------------------------------------------------
# İptal (karantina) — satır silmeden
# ---------------------------------------------------------------------------


def test_iptal_kaydi_kaydi_silmeden_devre_disi_birakir(tmp_path, conn) -> None:
    """Hatalı kuralla üretilmiş kayıtlar SİLİNMEZ, iptal edilir.

    İlk denemede satırları dosyadan silmiştim; iki sorun çıktı: (a) "ham veri
    append-only" şartını çiğniyor, (b) eşzamanlı bir CI koşusu aynı dosyaya
    eklerken git çakışması doğuruyor — gerçekten oldu.
    """
    rawstore.append("market_meta", _meta_rec(ticker="A"), tmp_path)
    rawstore.append("market", _market_rec(ticker="A", slot=1), tmp_path)
    ingest.ingest_all(conn, tmp_path, verbose=False)

    rawstore.append("invalidation", rawstore.invalidation_record(
        run_uid="test", target_kind="decision",
        keys=[["kalshi", "A", 1]], reason="test", at_us=T), tmp_path)

    keys = rawstore.invalidated_keys(tmp_path)
    assert ("kalshi", "A", 1) in keys["decision"]
    assert keys["fill"] == set()

    # Ham kayıt dosyada duruyor olmalı
    assert len(list(rawstore.read_day("market", "2026-08-28", tmp_path))) == 1


def test_iptal_yalnizca_turetilmis_kayitlar_icin() -> None:
    """Gözlem kayıtları (piyasa/tahmin/çözümleme) iptal edilemez — onlar
    kanıt, türetilmiş çıktı değil."""
    for kind in ("market", "forecast", "settlement", "market_meta"):
        with pytest.raises(ValueError, match="türetilmiş"):
            rawstore.invalidation_record(run_uid="t", target_kind=kind,
                                         keys=[], reason="r", at_us=T)


def test_iptalsiz_durumda_bos_kume(tmp_path) -> None:
    keys = rawstore.invalidated_keys(tmp_path)
    assert keys == {"decision": set(), "fill": set()}
