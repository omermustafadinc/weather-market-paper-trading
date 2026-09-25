========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-25T20:02:33.180584Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          51840
  orderbook seviyesi     2776897
  tahmin snapshot          34398
  karar                    10626
  simüle fill               2786
  çözümlenmiş kova          1188

## Brier skoru  (düşük = iyi, 1146 kova)
  model                  0.1311
  piyasa (mid)           0.1355   n=1146
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0044  ±0.0037  %95 [-0.0029, +0.0117]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=168  0.1394 / 0.2111   fark +0.0718
    CHI   n=162  0.1249 / 0.1125   fark -0.0124
    DEN   n=168  0.1489 / 0.2058   fark +0.0569
    LAX   n=162  0.1239 / 0.0977   fark -0.0263
    MIA   n=162  0.1346 / 0.1164   fark -0.0183
    NY    n=162  0.1090 / 0.0894   fark -0.0196
    PHL   n=162  0.1361 / 0.1104   fark -0.0257
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       415         0.035         0.053   +0.018
  0.1-0.2       301         0.151         0.189   +0.038
  0.2-0.3       248         0.246         0.258   +0.012
  0.3-0.4       126         0.345         0.222   -0.123
  0.4-0.5        44         0.434         0.295   -0.139
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2652)
  işlem sayısı                    2652
  kazanan                         1089  (%41)
  ort. İDDİA EDİLEN edge       +15.27p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.71p   ±0.8p  %95 [+1.1p, +4.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2660.18 $
  PnL fee ÖNCESİ             +24396.40 $
  PnL fee SONRASI            +21736.22 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7562.58 $   %90 aralık [-14700.92, -971.63]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1355 (model 0.1311)

  bizim (fee sonrası)            +21736.22 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
