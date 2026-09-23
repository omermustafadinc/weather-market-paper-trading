========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-23T22:43:52.888387Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          48804
  orderbook seviyesi     2612631
  tahmin snapshot          32760
  karar                     9990
  simüle fill               2613
  çözümlenmiş kova          1128

## Brier skoru  (düşük = iyi, 1086 kova)
  model                  0.1308
  piyasa (mid)           0.1357   n=1086
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0049  ±0.0038  %95 [-0.0025, +0.0123]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=156  0.1431 / 0.2120   fark +0.0689
    CHI   n=156  0.1252 / 0.1137   fark -0.0115
    DEN   n=156  0.1484 / 0.2071   fark +0.0587
    LAX   n=150  0.1177 / 0.0963   fark -0.0214
    MIA   n=156  0.1351 / 0.1172   fark -0.0179
    NY    n=156  0.1094 / 0.0898   fark -0.0196
    PHL   n=156  0.1362 / 0.1121   fark -0.0241
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       390         0.035         0.051   +0.016
  0.1-0.2       288         0.151         0.191   +0.040
  0.2-0.3       237         0.246         0.257   +0.011
  0.3-0.4       119         0.344         0.218   -0.125
  0.4-0.5        40         0.434         0.300   -0.134
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2539)
  işlem sayısı                    2539
  kazanan                         1048  (%41)
  ort. İDDİA EDİLEN edge       +15.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +3.09p   ±0.8p  %95 [+1.5p, +4.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2558.93 $
  PnL fee ÖNCESİ             +24542.42 $
  PnL fee SONRASI            +21983.49 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7183.45 $   %90 aralık [-13289.78, -665.26]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1357 (model 0.1308)

  bizim (fee sonrası)            +21983.49 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
