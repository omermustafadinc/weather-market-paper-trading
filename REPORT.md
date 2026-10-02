========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-02T23:36:19.458050Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          62148
  orderbook seviyesi     3320620
  tahmin snapshot          41454
  karar                    12840
  simüle fill               3343
  çözümlenmiş kova          1506

## Brier skoru  (düşük = iyi, 1464 kova)
  model                  0.1309
  piyasa (mid)           0.1331   n=1464
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0021  ±0.0035  %95 [-0.0047, +0.0089]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=210  0.1317 / 0.2041   fark +0.0725
    CHI   n=210  0.1288 / 0.1135   fark -0.0153
    DEN   n=210  0.1461 / 0.2007   fark +0.0546
    LAX   n=204  0.1262 / 0.0966   fark -0.0297
    MIA   n=210  0.1374 / 0.1121   fark -0.0253
    NY    n=210  0.1084 / 0.0870   fark -0.0214
    PHL   n=210  0.1376 / 0.1162   fark -0.0214
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       541         0.034         0.055   +0.021
  0.1-0.2       371         0.151         0.189   +0.037
  0.2-0.3       316         0.246         0.247   +0.001
  0.3-0.4       155         0.345         0.245   -0.100
  0.4-0.5        63         0.434         0.317   -0.117
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3280)
  işlem sayısı                    3280
  kazanan                         1313  (%40)
  ort. İDDİA EDİLEN edge       +15.97p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.60p   ±0.7p  %95 [+0.2p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3266.53 $
  PnL fee ÖNCESİ             +24861.16 $
  PnL fee SONRASI            +21594.63 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8941.88 $   %90 aralık [-15025.72, -1813.04]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1331 (model 0.1309)

  bizim (fee sonrası)            +21594.63 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
