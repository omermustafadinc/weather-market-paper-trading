========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-14T21:14:07.547033Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         121086
  orderbook seviyesi     6429380
  tahmin snapshot          80955
  karar                    25086
  simüle fill               6458
  çözümlenmiş kova          3288

## Brier skoru  (düşük = iyi, 3204 kova)
  model                  0.1315
  piyasa (mid)           0.1248   n=3204
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0068  ±0.0028  %95 [-0.0122, -0.0013]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=462  0.1205 / 0.1933   fark +0.0728
    CHI   n=456  0.1405 / 0.1070   fark -0.0335
    DEN   n=462  0.1406 / 0.1919   fark +0.0513
    LAX   n=456  0.1204 / 0.0856   fark -0.0348
    MIA   n=456  0.1379 / 0.1020   fark -0.0358
    NY    n=456  0.1122 / 0.0929   fark -0.0193
    PHL   n=456  0.1488 / 0.0990   fark -0.0498
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1302         0.032         0.053   +0.021
  0.1-0.2       722         0.150         0.198   +0.048
  0.2-0.3       583         0.246         0.269   +0.023
  0.3-0.4       363         0.345         0.234   -0.111
  0.4-0.5       160         0.440         0.306   -0.134
  0.5-0.6        47         0.550         0.362   -0.188
  0.6-0.7        17         0.637         0.412   -0.225
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6366)
  işlem sayısı                    6366
  kazanan                         2499  (%39)
  ort. İDDİA EDİLEN edge       +18.65p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.88p   ±0.5p  %95 [+0.9p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6502.90 $
  PnL fee ÖNCESİ             +51209.36 $
  PnL fee SONRASI            +44706.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15210.30 $   %90 aralık [-24669.42, -5545.54]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1248 (model 0.1315)

  bizim (fee sonrası)            +44706.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
