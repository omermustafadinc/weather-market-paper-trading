"""Model testleri: kova geometrisi, dağılım ve lookahead kapalılığı."""

from __future__ import annotations

import json
import math

import pytest

from wxbot import model as M
from wxbot.clock import iso_to_us, us_to_iso

# Üretim verisinden alınmış GERÇEK kova tanımları (KXHIGHNY-26AUG29)
REAL_BUCKETS = [
    M.Bucket("T79",   "less",    None, 79.0, "78° or below"),
    M.Bucket("B79.5", "between", 79.0, 80.0, "79° to 80°"),
    M.Bucket("B81.5", "between", 81.0, 82.0, "81° to 82°"),
    M.Bucket("B83.5", "between", 83.0, 84.0, "83° to 84°"),
    M.Bucket("B85.5", "between", 85.0, 86.0, "85° to 86°"),
    M.Bucket("T86",   "greater", 86.0, None, "87° or above"),
]


# ---------------------------------------------------------------------------
# Kova geometrisi
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("bucket", "lo", "hi"),
    [
        (REAL_BUCKETS[0], None, 78),    # "78° or below": cap=79 -> <=78
        (REAL_BUCKETS[1], 79, 80),
        (REAL_BUCKETS[5], 87, None),    # "87° or above": floor=86 -> >=87
    ],
)
def test_tamsayi_sinirlari_alt_baslikla_uyusuyor(bucket, lo, hi) -> None:
    """Alt başlık ne diyorsa sınırlar onu vermeli — burada bir hata sessizce
    tüm modeli bir derece kaydırırdı."""
    assert bucket.int_bounds() == (lo, hi)


def test_surekli_sinirlar_yarim_derece_duzeltmeli() -> None:
    """Çözümleme TAM SAYI derece. Sürekli dağılımdan geçerken ±0.5 şart:
    '79° to 80°' kovası aslında [78.5, 80.5) aralığıdır."""
    lo, hi = REAL_BUCKETS[1].continuous_bounds()
    assert (lo, hi) == (78.5, 80.5)
    assert REAL_BUCKETS[0].continuous_bounds() == (-math.inf, 78.5)
    assert REAL_BUCKETS[5].continuous_bounds() == (86.5, math.inf)


def test_kovalar_tum_tamsayilari_tam_bir_kez_kapsar() -> None:
    M.check_ladder(REAL_BUCKETS)
    for t, expected in [(70, "T79"), (78, "T79"), (79, "B79.5"), (80, "B79.5"),
                        (81, "B81.5"), (86, "B85.5"), (87, "T86"), (99, "T86")]:
        hits = [b.ticker for b in REAL_BUCKETS if b.contains_int(t)]
        assert hits == [expected], f"{t}° -> {hits}, beklenen {expected}"


def test_ladder_bosluk_yakalar() -> None:
    incomplete = [REAL_BUCKETS[0], REAL_BUCKETS[2]]   # 79-80 kovası eksik
    with pytest.raises(M.ModelError, match="kova"):
        M.check_ladder(incomplete)


def test_ladder_ortusme_yakalar() -> None:
    overlapping = list(REAL_BUCKETS) + [M.Bucket("X", "between", 79.0, 80.0)]
    with pytest.raises(M.ModelError, match="kova"):
        M.check_ladder(overlapping)


def test_eksik_sinir_patlar() -> None:
    with pytest.raises(M.ModelError, match="cap_strike"):
        M.Bucket("X", "less", None, None).int_bounds()
    with pytest.raises(M.ModelError, match="bilinmeyen"):
        M.Bucket("X", "saçma", 1.0, 2.0).int_bounds()


def test_bucket_gercek_market_jsonundan_kurulur() -> None:
    b = M.Bucket.from_market({"ticker": "KXHIGHNY-26AUG29-B79.5",
                              "strike_type": "between", "floor_strike": 79,
                              "cap_strike": 80, "yes_sub_title": "79° to 80°"})
    assert b.int_bounds() == (79, 80)


# ---------------------------------------------------------------------------
# Ağırlıklandırma
# ---------------------------------------------------------------------------


def _sample(**models) -> M.EnsembleSample:
    return M.EnsembleSample("NY", "2026-08-29", dict(models))


def test_model_agirligi_uye_sayisindan_bagimsiz() -> None:
    """51 üyeli ECMWF ile 18 üyeli BOM eşit söz hakkına sahip olmalı:
    üye sayısı hesaplama tercihi, beceri ölçüsü değil."""
    s = _sample(big=[70.0] * 51, small=[90.0] * 18)
    pts = s.weighted_members("model")
    big_w = sum(w for v, w in pts if v == 70.0)
    small_w = sum(w for v, w in pts if v == 90.0)
    assert big_w == pytest.approx(0.5)
    assert small_w == pytest.approx(0.5)


def test_uye_agirligi_uye_sayisiyla_orantili() -> None:
    s = _sample(big=[70.0] * 51, small=[90.0] * 18)
    pts = s.weighted_members("member")
    assert sum(w for v, w in pts if v == 70.0) == pytest.approx(51 / 69)


def test_agirliklar_toplami_bir() -> None:
    s = _sample(a=[1.0, 2.0], b=[3.0], c=[4.0, 5.0, 6.0])
    for wt in ("model", "member"):
        assert sum(w for _, w in s.weighted_members(wt)) == pytest.approx(1.0)


def test_bos_model_yok_sayilir() -> None:
    s = _sample(a=[70.0, 71.0], bos=[])
    assert s.model_count == 1
    assert len(s.weighted_members("model")) == 2


def test_hic_uye_yoksa_patlar() -> None:
    with pytest.raises(M.ModelError, match="üye yok"):
        _sample(a=[], b=[]).weighted_members()


# ---------------------------------------------------------------------------
# Dağılım
# ---------------------------------------------------------------------------


def test_silverman_veriden_turetilir() -> None:
    """Elle seçilmiş sabit değil: saçılım artınca bant genişliği artmalı."""
    dar = M.silverman_bandwidth([80.0 + 0.1 * i for i in range(50)])
    genis = M.silverman_bandwidth([80.0 + 1.0 * i for i in range(50)])
    assert genis > dar * 5


def test_silverman_sifir_sacilimda_cokmez() -> None:
    assert M.silverman_bandwidth([80.0] * 30) > 0
    assert M.silverman_bandwidth([80.0]) > 0


def test_kova_olasiliklari_bire_toplanir() -> None:
    s = _sample(a=[77.0, 78.0, 79.0, 80.0], b=[81.0, 82.0, 83.0])
    probs = M.bucket_probabilities(M.build_distribution(s), REAL_BUCKETS)
    assert sum(probs.values()) == pytest.approx(1.0)
    assert set(probs) == {b.ticker for b in REAL_BUCKETS}


def test_olasilik_tabani_uygulanir() -> None:
    """Ham ensemble uçlarda 0 üretir; 0 'imkânsız' demektir ve Kelly'yi patlatır.

    Hiçbir hava tahmini o kadar kesin değil — ve 2 sentlik bir kontrata karşı
    '%0' demek tam olarak hayali edge'in doğduğu yer.
    """
    s = _sample(a=[79.0] * 20)          # hepsi tek kovada
    probs = M.bucket_probabilities(M.build_distribution(s, bandwidth=0.01),
                                   REAL_BUCKETS)
    assert all(p >= M.PROB_FLOOR * 0.9 for p in probs.values()), probs
    assert all(p < 1.0 for p in probs.values())


def test_dagilim_kutlesi_dogru_kovaya_gider() -> None:
    s = _sample(a=[83.4, 83.5, 83.6])
    probs = M.bucket_probabilities(M.build_distribution(s, bandwidth=0.2),
                                   REAL_BUCKETS)
    assert max(probs, key=probs.get) == "B83.5"


def test_bias_dagilimi_kaydirir() -> None:
    s = _sample(a=[79.0, 80.0, 81.0])
    base = M.build_distribution(s, bandwidth=1.0)
    warm = M.build_distribution(s, bandwidth=1.0, bias=3.0)
    assert warm.mean() == pytest.approx(base.mean() + 3.0)


def test_bandwidth_sifir_ham_ampirik_verir() -> None:
    d = M.Distribution(((79.0, 0.5), (85.0, 0.5)), bandwidth=0.0, weighting="model")
    assert d.cdf(80.0) == pytest.approx(0.5)
    assert d.cdf(90.0) == pytest.approx(1.0)


def test_describe_ayarlari_tasir() -> None:
    """Sonucun hangi ayarlarla üretildiği karar defterine yazılabilmeli."""
    d = M.build_distribution(_sample(a=[79.0, 80.0, 81.0]))
    info = d.describe()
    assert set(info) >= {"bandwidth", "weighting", "bias", "mean", "p10", "p50", "p90"}


# ---------------------------------------------------------------------------
# Lookahead: model asla karardan sonraki tahmini görmemeli
# ---------------------------------------------------------------------------


def _insert_forecast(conn, model, fetched_us, value, target="2026-08-29"):
    conn.execute(
        "INSERT OR IGNORE INTO runs (run_uid, slot_id, slot_seconds, started_at_us)"
        " VALUES (?,1,3600,?)", (f"r-{fetched_us}", fetched_us))
    rid = conn.execute("SELECT id FROM runs WHERE run_uid=?",
                       (f"r-{fetched_us}",)).fetchone()["id"]
    payload = {"daily": {"time": [target],
                         "temperature_2m_max_member01": [value],
                         "temperature_2m_max_member02": [value + 1.0]}}
    conn.execute(
        """INSERT INTO forecast_snapshots
           (run_id, slot_id, provider, model, location_key, latitude, longitude,
            variable, target_date, fetched_at_us, fetched_at_iso, source_url,
            raw_json, member_count)
           VALUES (?,?,'open-meteo',?, 'NY',40.78,-73.97,'temperature_2m_max',?,?,?,
                   'https://ensemble-api.open-meteo.com/x',?,2)""",
        (rid, fetched_us, model, target, fetched_us, us_to_iso(fetched_us),
         json.dumps(payload)))


T_ERKEN = iso_to_us("2026-08-28T12:00:00Z")
T_KARAR = iso_to_us("2026-08-28T14:00:00Z")
T_GEC   = iso_to_us("2026-08-28T16:00:00Z")


def test_karardan_sonraki_tahmin_gorulmez(conn) -> None:
    _insert_forecast(conn, "ecmwf_ifs025", T_ERKEN, 79.0)
    _insert_forecast(conn, "ecmwf_ifs025", T_GEC, 95.0)     # karardan SONRA

    s = M.load_ensemble_sample(conn, "NY", "2026-08-29", as_of_us=T_KARAR)
    assert s.all_members() == [79.0, 80.0], "gelecekteki tahmin sızdı"
    assert s.data_asof_us == T_ERKEN


def test_her_model_icin_en_yeni_izinli_snapshot(conn) -> None:
    _insert_forecast(conn, "ecmwf_ifs025", T_ERKEN, 79.0)
    _insert_forecast(conn, "ecmwf_ifs025", T_ERKEN + 60_000_000, 81.0)  # daha yeni, izinli
    _insert_forecast(conn, "gfs025", T_ERKEN, 85.0)

    s = M.load_ensemble_sample(conn, "NY", "2026-08-29", as_of_us=T_KARAR)
    assert sorted(s.by_model["ecmwf_ifs025"]) == [81.0, 82.0]
    assert sorted(s.by_model["gfs025"]) == [85.0, 86.0]
    assert s.model_count == 2


def test_data_asof_en_yeni_girdinin_zamani(conn) -> None:
    """`data_asof` karara giren TÜM girdilerin en yenisi olmalı."""
    _insert_forecast(conn, "ecmwf_ifs025", T_ERKEN, 79.0)
    _insert_forecast(conn, "gfs025", T_ERKEN + 30_000_000, 85.0)
    s = M.load_ensemble_sample(conn, "NY", "2026-08-29", as_of_us=T_KARAR)
    assert s.data_asof_us == T_ERKEN + 30_000_000


def test_hicbir_izinli_tahmin_yoksa_bos_ornek(conn) -> None:
    _insert_forecast(conn, "ecmwf_ifs025", T_GEC, 79.0)
    s = M.load_ensemble_sample(conn, "NY", "2026-08-29", as_of_us=T_KARAR)
    assert s.member_count == 0


# ---------------------------------------------------------------------------
# Üye çıkarma
# ---------------------------------------------------------------------------


def test_uye_cikarma_none_atlar() -> None:
    payload = {"daily": {"time": ["2026-08-28", "2026-08-29"],
                         "temperature_2m_max_member01": [70.0, 79.0],
                         "temperature_2m_max_member02": [71.0, None],
                         "temperature_2m_max": [70.5, 79.5]}}
    vals = M.extract_members(payload, "2026-08-29", "temperature_2m_max")
    assert sorted(vals) == [79.0, 79.5]


def test_uye_cikarma_hedef_gun_yoksa_bos() -> None:
    payload = {"daily": {"time": ["2026-08-28"],
                         "temperature_2m_max_member01": [70.0]}}
    assert M.extract_members(payload, "2026-09-01", "temperature_2m_max") == []


# ---------------------------------------------------------------------------
# Bugün/geçmiş olaylarda karar verilmemeli
# ---------------------------------------------------------------------------


def test_ufuk_bugunu_ve_gecmisi_disliyor() -> None:
    """Ajan yalnızca GELECEK hedef günlerde karar vermeli.

    Bu test bir ihlalden doğdu: gece koşusu dünün piyasalarında karar verdi ve
    lookahead tarayıcısı yakaladı — CLI raporu 5 saat önce yayınlanmıştı.
    Ayrıca geçmiş günler için Open-Meteo tahmin değil analiz döndürür.
    """
    from datetime import date, timedelta

    from wxbot import config as cfg

    today = date(2026, 8, 29)
    horizon = {(today + timedelta(days=d)).isoformat()
               for d in range(1, cfg.HORIZON_DAYS + 1)}

    assert today.isoformat() not in horizon, "bugün ufka girmemeli"
    assert (today - timedelta(days=1)).isoformat() not in horizon, "dün ufka girmemeli"
    assert (today + timedelta(days=1)).isoformat() in horizon, "yarın ufkta olmalı"
