# Hava durumu tahmin piyasaları — kâğıt üzerinde işlem araştırması

Hava durumu tahmin piyasalarında (Kalshi) **kâğıt üzerinde** işlem yapan otonom bir
araştırma ajanı. Amaç para kazanmak değil: **bir edge'in var olup olmadığını dürüst
şekilde ölçmek.**

Gerçek para yok, gerçek emir yok, cüzdan yok. Tüm "işlemler" yerel SQLite'a yazılır.

## Katı kısıtlar

Bunlar niyet beyanı değil, kodla zorlanıyor ve test ediliyor:

| Kısıt | Nerede zorlanıyor | Test |
|---|---|---|
| Yalnızca GET, emir gönderilemez | `wxbot/http.py` — `Fetcher`'da GET dışı fiil yok | `test_http_guard.py` |
| Yalnızca whitelist'teki hostlar | `ALLOWED_HOSTS` | `test_http_guard.py` |
| Hesap/emir uçlarına dokunulmaz | `DENIED_PATH_PATTERNS` (`/portfolio/*` vb.) | `test_http_guard.py` |
| `data_asof <= decision_at` | SQLite CHECK + tarayıcı | `test_no_lookahead.py` |
| Karar→fill arası ≥ 30 sn | SQLite CHECK + tarayıcı | `test_no_lookahead.py` |
| Fill, karardan sonraki kitaba karşı | SQLite CHECK + tarayıcı | `test_no_lookahead.py` |
| Her karar gerekçeli (işlem yapmama dahil) | SQLite CHECK | `test_no_lookahead.py` |
| Ham veri append-only | `raw_*_json` sütunları UPDATE edilmez | — |
| Fiyat kaybı yok (desi-sent) | `to_dcents`, ızgara dışı fiyat reddedilir | `test_prices.py` |

## Kurulum

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
```

## Veri akışı

```
Kalshi API  ─┐
Open-Meteo  ─┼─>  collect  ─>  data/raw/**.jsonl  ─>  ingest  ─>  data/wxbot.db
NWS         ─┘                 (append-only,           (doğrulama       (türetilmiş,
                                git'e commit)           kapısı)          silinebilir)
```

Toplayıcı GitHub Actions'ta 30 dakikada bir koşuyor (`.github/workflows/collect.yml`);
Kalshi API'si geliştirme makinesinin ağından erişilemiyor. Ham veriyi lokale çekmek için:

```bash
git pull && ./.venv/bin/python -m wxbot.ingest --rebuild
```

## Test

```bash
./.venv/bin/python -m pytest
```

`test_gercek_veritabani_temiz` diskteki gerçek DB'yi de tarar. **Bu paket geçmeden
hiçbir sonuç raporlanmaz.**

## Yapı

```
src/wxbot/
  clock.py     UTC + mikrosaniye tamsayı zaman
  http.py      tek HTTP kapısı: whitelist + yalnızca GET + rate limit
  schema.sql   SQLite şeması; lookahead kuralları CHECK kısıtı olarak
  db.py        bağlantı + lookahead tarayıcı (assert_no_lookahead)
  config.py    şehirler/istasyonlar (kontrat kurallarından doğrulanmış), modeller
  kalshi.py    read-only istemci + desi-sent fiyat normalizasyonu
  rawstore.py  append-only JSONL: tek doğru kaynak
  collect.py   idempotent, devam edebilen snapshot toplayıcı
  ingest.py    JSONL -> SQLite + lookahead doğrulama kapısı
  model.py     ensemble -> dağılım -> kova olasılıkları
  fills.py     orderbook yürüyerek gerçekçi fill + Kalshi fee modeli
  strategy.py  edge, eşik, kesirli Kelly, limitler
  agent.py     karar ver / gecikme sonrası doldur
  groundtruth.py  NWS CLI + NCEI gözlem
  bias.py      grid-istasyon bias çalışması
  settle.py    NWS CLI ile çözümleme (kova -> 0/1)
  report.py    Brier, kalibrasyon, PnL (fee öncesi/sonrası), baseline'lar
  quarantine.py  kirlenmiş türetilmiş kayıtları iptal et (silmeden)
  cycle.py     tam döngü: topla -> karar -> 45sn -> kitap -> fill -> doğrula
tests/         kısıtların testi
data/raw/      ham veri (append-only JSONL, repoya commit'lenir)
research/      Faz 0 ham erişilebilirlik kanıtları
DECISIONS.md   platform/veri kaynağı kararları ve gerekçeleri
```

## Nereye bakmalı

**[REPORT.md](REPORT.md)** — her koşuda otomatik güncellenir. Brier skoru,
kalibrasyon eğrisi, fee öncesi/sonrası PnL ve baseline karşılaştırmaları.
Değerlendirilecek veri yoksa bunu açıkça yazar ve nedenini gösterir.

Toplayıcı **GitHub Actions'ta** koşuyor, kimsenin bilgisayarında değil.

### Bilinen eksikler

* **Bias düzeltmesi uygulanmıyor.** Grid-istasyon sapması ölçüldü
  (LAX'ta ECMWF +9.4 °F, bkz. [research/bias_study_2026-08-28.txt](research/bias_study_2026-08-28.txt))
  ama modele henüz girmedi — doğrusu canlı veriden yürüyen pencereyle tahmin
  etmek ve o veri henüz yok. Rapor, model olasılıklarını ham tahminlerden
  yeniden hesapladığı için düzeltme sonradan geçmişe dönük uygulanabilir.
* **Tetikleme seyrek.** GitHub'ın schedule event'i ~%2 oranında tetikleniyor;
  günde ~2 toplama bekleniyor. Kalibrasyon için yeterli, işlem sinyali için yavaş.
* **Kalibre edilmemiş model.** Bant genişliği Silverman kuralından; ölçülmedi.

## Durum

- [x] **Faz 0** — araştırma, platform ve veri kaynağı kararı (`DECISIONS.md`)
- [x] **Faz 1** — iskelet: HTTP guard, şema, lookahead testi
- [x] **Faz 2** — collector (orderbook + tahmin snapshot'ları)
- [x] **Faz 3** — model (ensemble → dağılım → kova olasılıkları) — *kalibre edilmedi*
- [x] **Faz 4** — strategy + simulator (fill gerçekçiliği, fee, Kelly)
- [x] **Faz 5** — ledger + reporter + baseline'lar — *veri bekleniyor*

## Veri kaynakları

- Piyasa: [Kalshi](https://kalshi.com) public read-only API
- Tahmin: [Open-Meteo](https://open-meteo.com) Ensemble API (CC-BY 4.0)
- Ground truth: [NWS / api.weather.gov](https://api.weather.gov)

Gerekçeler ve elenen alternatifler için `DECISIONS.md`.
