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
  collect.py   idempotent, devam edebilen snapshot toplayıcı
tests/         kısıtların testi
research/      Faz 0 ham erişilebilirlik kanıtları
DECISIONS.md   platform/veri kaynağı kararları ve gerekçeleri
```

## Durum

- [x] **Faz 0** — araştırma, platform ve veri kaynağı kararı (`DECISIONS.md`)
- [x] **Faz 1** — iskelet: HTTP guard, şema, lookahead testi
- [x] **Faz 2** — collector (orderbook + tahmin snapshot'ları)
- [ ] Faz 3 — model (ensemble → dağılım → kova olasılıkları)
- [ ] Faz 4 — strategy + simulator (fill gerçekçiliği, fee, Kelly)
- [ ] Faz 5 — ledger + reporter + baseline'lar

## Veri kaynakları

- Piyasa: [Kalshi](https://kalshi.com) public read-only API
- Tahmin: [Open-Meteo](https://open-meteo.com) Ensemble API (CC-BY 4.0)
- Ground truth: [NWS / api.weather.gov](https://api.weather.gov)

Gerekçeler ve elenen alternatifler için `DECISIONS.md`.
