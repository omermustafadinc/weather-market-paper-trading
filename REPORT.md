========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-24T23:02:14.155646Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          50532
  orderbook seviyesi     2706173
  tahmin snapshot          33642
  karar                    10350
  simüle fill               2707
  çözümlenmiş kova          1164

## Brier skoru  (düşük = iyi, 1122 kova)
  model                  0.1308
  piyasa (mid)           0.1354   n=1122
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0046  ±0.0037  %95 [-0.0027, +0.0119]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=162  0.1410 / 0.2114   fark +0.0705
    CHI   n=162  0.1249 / 0.1125   fark -0.0124
    DEN   n=162  0.1485 / 0.2057   fark +0.0572
    LAX   n=156  0.1214 / 0.0982   fark -0.0232
    MIA   n=162  0.1346 / 0.1164   fark -0.0183
    NY    n=162  0.1090 / 0.0894   fark -0.0196
    PHL   n=156  0.1362 / 0.1121   fark -0.0241
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       405         0.035         0.052   +0.017
  0.1-0.2       296         0.151         0.189   +0.038
  0.2-0.3       243         0.246         0.259   +0.013
  0.3-0.4       122         0.344         0.221   -0.123
  0.4-0.5        44         0.434         0.295   -0.139
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2638)
  işlem sayısı                    2638
  kazanan                         1081  (%41)
  ort. İDDİA EDİLEN edge       +15.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.64p   ±0.8p  %95 [+1.1p, +4.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2646.74 $
  PnL fee ÖNCESİ             +23618.21 $
  PnL fee SONRASI            +20971.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7354.21 $   %90 aralık [-14190.90, -1162.10]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1354 (model 0.1308)

  bizim (fee sonrası)            +20971.47 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
