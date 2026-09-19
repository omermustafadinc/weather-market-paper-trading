========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-19T11:20:03.406989Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          40632
  orderbook seviyesi     2178978
  tahmin snapshot          27972
  karar                     8256
  simüle fill               2159
  çözümlenmiş kova           924

## Brier skoru  (düşük = iyi, 882 kova)
  model                  0.1311
  piyasa (mid)           0.1347   n=882
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0035  ±0.0041  %95 [-0.0045, +0.0116]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=126  0.1494 / 0.2116   fark +0.0621
    CHI   n=126  0.1314 / 0.1153   fark -0.0161
    DEN   n=126  0.1506 / 0.2100   fark +0.0593
    LAX   n=126  0.1138 / 0.0948   fark -0.0190
    MIA   n=126  0.1323 / 0.1155   fark -0.0167
    NY    n=126  0.1081 / 0.0849   fark -0.0232
    PHL   n=126  0.1323 / 0.1106   fark -0.0218
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       322         0.035         0.056   +0.021
  0.1-0.2       225         0.151         0.191   +0.040
  0.2-0.3       196         0.245         0.260   +0.015
  0.3-0.4        97         0.344         0.216   -0.128
  0.4-0.5        30         0.432         0.233   -0.198
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2044)
  işlem sayısı                    2044
  kazanan                          808  (%40)
  ort. İDDİA EDİLEN edge       +15.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.39p   ±0.9p  %95 [-0.4p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2062.64 $
  PnL fee ÖNCESİ             +10908.30 $
  PnL fee SONRASI             +8845.66 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4611.14 $   %90 aralık [-10095.54, +541.62]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1347 (model 0.1311)

  bizim (fee sonrası)             +8845.66 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
