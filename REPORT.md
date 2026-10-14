========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-14T23:08:58.385902Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          77256
  orderbook seviyesi     4124210
  tahmin snapshot          51093
  karar                    15900
  simüle fill               4122
  çözümlenmiş kova          2010

## Brier skoru  (düşük = iyi, 1926 kova)
  model                  0.1327
  piyasa (mid)           0.1315   n=1926
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0012  ±0.0032  %95 [-0.0075, +0.0050]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=276  0.1297 / 0.2057   fark +0.0760
    CHI   n=276  0.1382 / 0.1086   fark -0.0295
    DEN   n=276  0.1497 / 0.1990   fark +0.0493
    LAX   n=270  0.1267 / 0.0961   fark -0.0305
    MIA   n=276  0.1349 / 0.1051   fark -0.0298
    NY    n=276  0.1096 / 0.0915   fark -0.0181
    PHL   n=276  0.1402 / 0.1136   fark -0.0266
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       724         0.034         0.061   +0.027
  0.1-0.2       481         0.151         0.191   +0.040
  0.2-0.3       403         0.247         0.253   +0.006
  0.3-0.4       210         0.345         0.224   -0.121
  0.4-0.5        78         0.438         0.295   -0.143
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4052)
  işlem sayısı                    4052
  kazanan                         1587  (%39)
  ort. İDDİA EDİLEN edge       +16.77p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.79p   ±0.6p  %95 [-0.5p, +2.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4088.45 $
  PnL fee ÖNCESİ             +23515.12 $
  PnL fee SONRASI            +19426.67 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9519.86 $   %90 aralık [-17451.91, -2128.27]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1315 (model 0.1327)

  bizim (fee sonrası)            +19426.67 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
