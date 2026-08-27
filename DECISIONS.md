# DECISIONS.md — Faz 0: Araştırma Bulguları

**Tarih:** 2026-08-27
**Durum:** Faz 0 tamamlandı. Kod yazılmadı. **Faz 1'e geçmeden önce bir kararın gerekiyor (§8).**

Bu belgedeki her "erişilebilir / erişilemez" ifadesi bu makineden yapılmış gerçek HTTP
isteklerine dayanıyor. Ham çıktılar: [research/reachability.txt](research/reachability.txt).
Doğrulayamadığım şeyleri §7'de ayrıca listeledim — oraları tahminle doldurmadım.

---

## 1. Özet — ve baştan söylenmesi gereken sorun

Teknik tarafta net bir kazanan var: **Kalshi + Open-Meteo çoklu-model ensemble + NWS ground truth.**

Ama araştırmanın en önemli bulgusu teknik değil, ağ tarafında:

> **Kalshi'nin ve Polymarket'in canlı API'lerine bu makineden erişilemiyor.**
> Türk Telekom DNS'i tüm `kalshi.com` ve `polymarket.com` hostlarını
> `195.175.254.2` (BTK sinkhole) adresine yönlendiriyor. Bu sadece DNS engeli de değil:
> `curl --resolve` ile gerçek IP'ye doğru SNI ile bağlanmayı denedim, o da başarısız.

Senin hedefin "bir edge'in var olup olmadığını dürüst şekilde ölçmek". Edge'in tanımı
`model_olasılık − piyasa_olasılığı`. **Piyasa olasılığına erişemezsem ölçülecek bir şey yok.**
Bu yüzden Faz 1'e geçmeden bunu çözmemiz gerekiyor; §8'de üç seçenek var.

Kötü haberi baştan veriyorum çünkü sonradan "aslında veri sahteydi" demek istemiyorum.

---

## 2. Platform kararı

### Seçilen: **Kalshi** (erişim çözülmesi şartıyla)

| Kriter | Kalshi | Polymarket | Manifold |
|---|---|---|---|
| Public read-only API (auth'suz) | ✅ evet, doğrulandı | ✅ var (CLOB/Gamma) | ✅ var |
| Orderbook derinliği | ✅ `/markets/{ticker}/orderbook?depth=N`, tüm seviyeler | ✅ CLOB book | ⚠️ ağırlıklı CPMM/AMM |
| Hava durumu piyasası | ✅ **364 "Climate and Weather" serisi** | ⚠️ seyrek, tutarsız | ⚠️ birkaç tane |
| Likidite | ✅ 2026'da ~$564M hava hacmi (§7'de kaynak notu) | düşük (hava tarafında) | ❌ oyun parası |
| Net settlement kuralı | ✅ resmi klimatolojik rapor | değişken | topluluk çözümlemesi |
| Fee yapısı modellenebilir mi | ✅ formül + API'den seri bazlı çarpan | ✅ | — |
| **Bu makineden erişim** | ❌ **ENGELLİ** | ❌ **ENGELLİ** | ✅ erişilebilir |

**Neden Kalshi:** Hava durumu piyasası konusunda ciddi olan tek borsa. Kontratlar
birbirini dışlayan sıcaklık kovalarına bölünmüş — bu, "nokta tahmini değil dağılım
istiyorum" isteğinle birebir örtüşüyor: ensemble'dan çıkan dağılımı kova sınırlarında
integre edip doğrudan 6 olasılık üretiyorum ve bunları 6 piyasa fiyatıyla karşılaştırıyorum.
Ayrıca settlement kaynağı tek ve resmi, yani model hatası ile çözümleme belirsizliği
birbirine karışmıyor.

**Neden Polymarket değil:** Hava piyasaları hem seyrek hem sığ; asıl ağırlık kripto/siyaset.
Erişim durumu Kalshi ile aynı (engelli), yani engeli aşmak Polymarket'i tercih sebebi yapmıyor.
Ayrıca on-chain (Polygon RPC — erişilebilir) sadece gerçekleşmiş işlemleri verir, **orderbook
off-chain**; senin istediğin derinlik oradan gelmiyor.

**Neden Manifold değil:** Erişilebilir olması cazip ama oyun parası. Fiyatları gerçek bir
teşvikle oluşmadığı için "piyasa olasılığı" saymak dürüst olmaz. Edge ölçümü anlamsızlaşır.

### Elenen ama denenen erişim yolları

**a) Kalshi DEMO ortamı — `demo-api.kalshi.co` (erişilebilir, ama kullanılamaz)**

`.co` uzantısı engelli değil ve auth'suz market data veriyor. Gerçek seri isimleri var:
`KXHIGHNY`, `KXHIGHCHI`, `KXHIGHMIA`, `KXHIGHAUS`, `KXHIGHDEN`, `KXHIGHLAX`, `KXHIGHPHIL`,
`KXRAINNYC`. Bu yüzden §5'teki mikroyapı bilgilerini oradan öğrendim.

**Ama orderbook'ları boş.** KXHIGHNY-26AUG28 kovalarının gerçek orderbook çıktıları:

```
KXHIGHNY-26AUG28-T87    {"no_dollars":[],"yes_dollars":[]}
KXHIGHNY-26AUG28-T80    {"no_dollars":[],"yes_dollars":[]}
KXHIGHNY-26AUG28-B86.5  {"no_dollars":[["0.7500","59.00"]],"yes_dollars":[]}
```

Bid 0.00, ask 1.00, hacim tek haneli, likidite alanı 0. Bunlar test botlarının izleri.
**Demo fiyatları piyasa olasılığı değil.** Demo'ya karşı ölçülen "edge" gürültüdür.
Pipeline'ı test etmek için iyi, sonuç üretmek için işe yaramaz.

**b) Kalshi public S3 — `kalshi-public-docs.s3.amazonaws.com` (erişilebilir, kısmen faydalı)**

`reporting/market_data_YYYY-MM-DD.json`, 2021-06-28'den 2026-07-29'a kadar günlük dosyalar.
Şema: `{date, ticker_name, open_interest, daily_volume, block_volume, high, low, status}`.

İki sınırı var:
- **Orderbook yok** — sadece günlük high/low. Senin en kritik istediğin şey (derinliği tüketen
  gerçekçi fill) bu veriyle yapılamaz.
- **~1 ay gecikme** — canlı ajan için kullanılamaz.

Yine de değerli: geçmiş için kaba bir "model günlük kapanış aralığını yenebiliyor mu"
çalışması yapılabilir. Fill gerçekçiliği olmadan, üst sınır tahmini olarak.

---

## 3. Tahmin kaynağı kararı

### Seçilen: **Open-Meteo Ensemble API** (birincil) + **NWS/api.weather.gov** (ground truth)

Her ikisi de bu makineden **sorunsuz çalışıyor** — canlı test edildi.

**Open-Meteo Ensemble — neden birincil:**

Tek istekle çoklu model, çoklu üye veriyor. NYC için canlı doğruladığım üye sayıları:

| model | üye | koşma sıklığı |
|---|---|---|
| `ecmwf_ifs025` | **51** | 6 saatte bir |
| `icon_seamless` | 40 | 3–6 saatte bir |
| `gfs025` | 31 | 6 saatte bir |
| `gem_global` | 21 | 12 saatte bir |
| `bom_access_global_ensemble` | 18 | 6 saatte bir |
| `ukmo_global_ensemble_20km` | 18 | — |

Toplam ~180 üye. Bu senin "ensemble spread'den dağılım" isteğinin tam karşılığı: nokta
tahmini değil, 180 senaryodan ampirik dağılım. Farklı merkezlerin modelleri olduğu için
tek merkezin sistematik hatasına da bağımlı kalmıyorum.

- **API key gerekmiyor**, non-commercial kullanım için.
- **Rate limit:** günde <10.000, saatte 5.000, dakikada 600 istek. Planladığım 15 dakikalık
  toplama döngüsü ~7 şehir × ~6 model = ~42 istek/döngü → günde ~4.000. Sınırın altında,
  rahat.
- **Lisans:** CC-BY 4.0, atıf gerekli.

**Kritik avantaj — lookahead'i yapısal olarak engelleyen iki ek endpoint (ikisi de test edildi):**

- `previous-runs-api.open-meteo.com` — `temperature_2m_previous_day1..7` değişkenleriyle
  *önceki model koşularının* tahminlerini veriyor. Yani "3 gün önce bu gün için ne
  diyordu"yu geçmişe dönük çekebiliyorum.
- `historical-forecast-api.open-meteo.com` — arşivlenmiş geçmiş tahminler.

Bu ikisi olmasa backtest yapmak için ya beklemek ya da kaçınılmaz olarak sızıntı riskine
girmek gerekirdi.

**NWS (`api.weather.gov`) — neden ground truth:**

- Auth yok, açıklayıcı User-Agent zorunlu (senin kısıtınla zaten uyumlu).
- **CLI (Climatological Report) ürünleri:** `/products/types/CLI/locations/NYC` — 629 lokasyon
  listelendi, NYC için canlı çekildi. Resmi günlük maksimum burada yayınlanıyor.
- **İstasyon gözlemleri:** `/stations/KNYC/observations` — Central Park saatlik, çalışıyor.
- Kalshi'nin settlement zinciri de buraya dayanıyor (§4).

**Elenenler:**

| Kaynak | Neden elendi |
|---|---|
| GFS/GEFS ham GRIB (NOMADS) | Erişilebilir ama yavaş (>12s). GRIB indirme+çözme ağır; Open-Meteo aynı GEFS'i işlenmiş veriyor. Tekrar iş. |
| ECMWF open data (`data.ecmwf.int`) | Erişilebilir. Ama IFS ENS'i Open-Meteo zaten 51 üyeyle veriyor. Yedek olarak dursun. |
| Synoptic Data | HTTP 401 — API key gerekiyor. Elendi. |
| The Weather Company API | Asıl settlement kaynağı ama public/dokümante ücretsiz API'si yok (§4, §7). |

---

## 4. Settlement kaynağı — modelin neyi tahmin etmesi gerektiği

Bu, demo API'yi kurcalarken çıkan ve kolayca gözden kaçacak bir ayrıntı. Kalshi'nin
`KXHIGHNY` serisi metadata'sından **birebir alıntı**:

> "Effective Friday, August 14th, daily temperature markets will transition their settlement
> source from the National Weather Service (NWS) to The Weather Company. The Weather Company
> utilizes NWS as its primary underlying source, and official settlement data will be
> accessible at https://weather.com/kalshi."

Yani:

- **Günlük sıcaklık piyasaları** (`KXHIGHNY`, `KXHIGHCHI`, …): settlement kaynağı artık
  **The Weather Company**, NWS değil. TWC alttan NWS kullanıyor ama aracı bir katman var.
- **`KXRAINNYC`**: hâlâ doğrudan **NWS Climatological Report**.
  Ek kural (metadata'dan): `'T'` (trace) veya `'R'` (record) değeri, sıfırdan büyükse
  "Yes" olarak çözümleniyor.

**Sonucu:** NWS CLI'yi ground truth almak %99 doğru olacak ama %100 değil. Aradaki fark
bir *basis riski* ve modelin hatasıyla karışabilir. Faz 3'te bunu ayrı bir metrik olarak
izleyeceğim: "NWS CLI ile settlement değerinin uyuşmadığı gün sayısı". Sıfır çıkarsa
görmezden gelirim; çıkmazsa raporda ayrı satır olur.

`weather.com/kalshi` sayfası bu makineden erişilebiliyor (HTTP 200, "Kalshi Weather Data
Climate Data Portal — Official Climate Reports"). Dokümante bir JSON API'si var mı,
doğrulamadım (§7).

---

## 5. Piyasa mikroyapısı (demo API'den doğrulanan gerçek yapı)

**Kontrat yapısı** — `KXHIGHNY-26AUG28`, `mutually_exclusive: true`:

```
KXHIGHNY-26AUG28-T80     79° veya altı      strike_type=less     cap=80
KXHIGHNY-26AUG28-B80.5   80° – 81°          strike_type=between  floor=80 cap=81
KXHIGHNY-26AUG28-B82.5   82° – 83°          strike_type=between  floor=82 cap=83
KXHIGHNY-26AUG28-B84.5   84° – 85°          strike_type=between  floor=84 cap=85
KXHIGHNY-26AUG28-B86.5   86° – 87°          strike_type=between  floor=86 cap=87
KXHIGHNY-26AUG28-T87     88° veya üstü      strike_type=greater  floor=87
```

2°F genişliğinde kovalar, uçlarda açık aralık. Toplam olasılık 1 olmalı — bu bedava bir
**tutarlılık kontrolü** veriyor: piyasa fiyatları toplamı 1'den ne kadar sapıyor (spread ve
fee'den sonra), ve modelimin kovaları toplamı 1 mi.

Diğer doğrulanan gerçekler:
- Orderbook endpoint'i **auth istemiyor**: `GET /trade-api/v2/markets/{ticker}/orderbook?depth=N`
- Şema `orderbook_fp: {yes_dollars: [[fiyat, miktar], ...], no_dollars: [...]}` — **tüm
  seviyeler**, mid değil. Senin şartını karşılıyor.
- API dolar cinsinden string döndürüyor (`"0.7500"`, `"59.00"`) → **Decimal kullanılacak,
  float değil.** Para hesabında float kullanmayacağım.
- Seri metadata'sında `fee_type: "quadratic"` ve `fee_multiplier: 1` alanları var → fee'yi
  hardcode etmek yerine API'den okuyacağım.
- Event `strike_date` UTC (`2026-08-29T05:00:00Z` = NY yerel gün sonu). **Zaman dilimi
  hatası buradan çıkar**; her şey UTC saklanacak, yerel saat sadece görüntüde.

---

## 6. Fee modeli

**Taker fee** (yaygın olarak belgelenen formül):

```
fee = ceil(0.07 × C × P × (1 − P) × 100) / 100
```

`C` = kontrat sayısı, `P` = fiyat (0.01–0.99). 50¢'te kontrat başına ~1.75¢ ile maksimum,
uçlarda küçülüyor. Yukarı yuvarlama **sente**.

Bu, edge eşiği için belirleyici: 50¢ civarında gidiş-dönüş maliyeti ~3.5¢ + spread.
Yani **3-4 puanın altındaki bir "edge" fee'nin altında kalır.** Eşiği buna göre kuracağım.

**Maker fee: BELİRSİZ.** Kaynaklar çelişiyor — kimi "taker'ın %25'i", kimi "sadece belirli
serilerde". Kalshi'nin resmi fee schedule PDF'i `kalshi.com` altında ve **erişemiyorum**.
Simülatörüm likidite alan (taker) tarafta çalışacağı için birincil etkisi yok; yine de
resting order modellersem bunu önce doğrulamam gerekir.

---

## 7. Doğrulayamadıklarım — uydurmadığım yerler

Bunları açıkça yazıyorum ki sonra "doğrulanmış" muamelesi görmesin:

1. **Kalshi canlı orderbook'unun gerçek derinliği.** Erişemedim. Demo boş. Yani "gerçekçi
   fill" simülasyonunun kalibre edileceği asıl veriyi henüz hiç görmedim.
2. **Kalshi'nin resmi fee schedule PDF'i.** `kalshi.com` engelli, WebFetch de "self signed
   certificate" ile döndü (blok sayfasının TLS araya girmesi). Formül üçüncü taraf
   kaynaklardan; API'den gelen `fee_type=quadratic, fee_multiplier=1` ile tutarlı ama
   birincil kaynaktan teyit edilmedi.
3. **Kalshi resmi API dokümantasyonu** (`docs.kalshi.com`) — engelli. §5'teki her şeyi
   canlı demo API'sinden gözlemleyerek çıkardım, dokümandan okuyarak değil.
4. **Hacim rakamı** ("2026'da ~$564M hava durumu hacmi, %500 YoY"). Web aramasından, üçüncü
   taraf. Kalshi'nin kendi verisiyle doğrulayamadım. Yön olarak doğru görünüyor, rakam
   olarak bana ait değil.
5. **Rate limit sayıları (Kalshi).** Doküman engelli. Demo'da agresif istek denemedim
   (bilerek). Faz 1'de temkinli başlayıp `429` gözlemleyerek ayarlayacağım.
6. **The Weather Company'nin public API'si.** `weather.com/kalshi` sayfası açılıyor ama
   arkasında dokümante, ücretsiz bir JSON endpoint'i var mı bakmadım.
7. **Polymarket'in hava piyasalarının bugünkü durumu.** API engelli; "seyrek ve sığ"
   değerlendirmem doğrudan gözlemden değil.

---

## 8. Senin kararın gereken nokta

Faz 1'e üç yoldan biriyle girebiliriz. Bu bir altyapı/hukuk tercihi, senin adına
karar vermem doğru olmaz:

**A) Toplayıcıyı yurtdışı bir VPS'te çalıştır** *(teknik olarak en temiz)*
Küçük bir VPS (Hetzner/DO/Fly, ~5$/ay) `collector`'ı koşar, SQLite'ı oraya yazar; sen
analizi lokalde yaparsın. Kalshi'ye gerçek erişim, tam orderbook, canlı. Mimari zaten
modüler olacağı için collector'ı ayırmak ek maliyet değil.
→ *Not: Kalshi işlem yapmayı ABD'li kişilere sınırlıyor. Biz kâğıt üzerinde ve read-only
kalıyoruz, hesap açmıyoruz — ama bunu bilerek karar ver.*

**B) Bu makinede kal, engeli sen çöz** (VPN vb.)
Ağ katmanını sen hallet, ben hiçbir dolanma mantığı yazmam. Basit ama koleksiyon
VPN bağlantısına bağımlı olur; ajan otonom ve kesintisiz çalışacaksa kırılgan.

**C) Piyasa verisi olmadan başla — dürüst ama kısıtlı**
Open-Meteo + NWS ile **sadece model tarafını** kurup ölçerim: ensemble dağılımı üret,
NWS CLI ile karşılaştır, Brier skoru ve kalibrasyon eğrisi çıkar. Bu, "modelim kalibre
mi" sorusunu tam olarak cevaplar — ki bu, edge'in **ön koşulu**: kalibre olmayan bir model
zaten hiçbir piyasada edge üretemez. Ayrıca Kalshi S3'ten geçmiş günlük high/low çekip kaba
bir üst sınır bakışı eklenebilir.
Cevaplayamayacağı soru: gerçek edge ve gerçekçi fill sonrası PnL.

**Önerim: A.** İstediğin şeyi tam olarak veren tek yol o, ve ~5$/ay dışında maliyeti yok.
**A mümkün değilse C** — çünkü C dürüst bir kısmi sonuç verir, oysa demo verisiyle
çalışmak sahte bir tam sonuç verir. Demo'yu sadece pipeline testi için kullanacağım,
hiçbir rapor demo verisine dayanmayacak.

---

## 9. Karar verilince Faz 1 planı

Erişim yolu netleşince, sırayla:

1. **İskelet + kısıtların kodla zorlanması**
   - Tek bir HTTP katmanı; **whitelist dışına çıkamaz**, sadece `GET`.
     Emir endpoint'ini yanlışlıkla bile çağırmak mümkün olmayacak.
   - Rate limiter + açıklayıcı User-Agent.
   - Python SSL sertifika sorunu düzeltilecek (`certifi`).
2. **SQLite şeması + lookahead testi — kod yazmadan önce test**
   Her ledger satırında `data_asof` ve `decision_at`. `data_asof > decision_at` olan tek satır
   varsa hata. Bunu **CHECK constraint olarak DB seviyesinde** de koyacağım (uygulama hatası
   veriyi kirletemesin), üstüne test. Bu test geçmeden hiçbir sonuç raporlanmayacak — söz.
3. **collector** — append-only ham snapshot, tüm orderbook seviyeleri, idempotent.
4. **model** → **strategy** → **simulator** → **ledger** → **reporter**
5. **Baseline'lar en baştan** (işlem yapmama / rastgele / piyasaya güven) — sonradan
   eklenirse sonucu güzelleştirme baskısı oluşur. Baştan sabitlenecek.

Her fazdan sonra durup göstereceğim.
