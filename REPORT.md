========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-21T13:47:43.890700Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          44700
  orderbook seviyesi     2393195
  tahmin snapshot          30240
  karar                     9114
  simüle fill               2382
  çözümlenmiş kova          1020

## Brier skoru  (düşük = iyi, 978 kova)
  model                  0.1305
  piyasa (mid)           0.1361   n=978
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0056  ±0.0039  %95 [-0.0021, +0.0133]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=144  0.1443 / 0.2121   fark +0.0678
    CHI   n=138  0.1273 / 0.1158   fark -0.0114
    DEN   n=144  0.1497 / 0.2098   fark +0.0601
    LAX   n=138  0.1155 / 0.0980   fark -0.0175
    MIA   n=138  0.1346 / 0.1166   fark -0.0180
    NY    n=138  0.1080 / 0.0826   fark -0.0254
    PHL   n=138  0.1327 / 0.1112   fark -0.0215
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       349         0.035         0.052   +0.016
  0.1-0.2       262         0.151         0.191   +0.040
  0.2-0.3       217         0.246         0.253   +0.007
  0.3-0.4       104         0.343         0.231   -0.113
  0.4-0.5        34         0.431         0.265   -0.167
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2286)
  işlem sayısı                    2286
  kazanan                          922  (%40)
  ort. İDDİA EDİLEN edge       +15.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.26p   ±0.9p  %95 [+0.6p, +3.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2307.14 $
  PnL fee ÖNCESİ             +17479.46 $
  PnL fee SONRASI            +15172.32 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6359.63 $   %90 aralık [-12770.96, +97.62]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1361 (model 0.1305)

  bizim (fee sonrası)            +15172.32 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
