========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-14T15:48:17.440631Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          76584
  orderbook seviyesi     4090422
  tahmin snapshot          50715
  karar                    15732
  simüle fill               4078
  çözümlenmiş kova          1986

## Brier skoru  (düşük = iyi, 1902 kova)
  model                  0.1328
  piyasa (mid)           0.1320   n=1902
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0008  ±0.0032  %95 [-0.0071, +0.0055]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=276  0.1297 / 0.2057   fark +0.0760
    CHI   n=270  0.1381 / 0.1092   fark -0.0289
    DEN   n=276  0.1497 / 0.1990   fark +0.0493
    LAX   n=270  0.1267 / 0.0961   fark -0.0305
    MIA   n=270  0.1351 / 0.1067   fark -0.0283
    NY    n=270  0.1094 / 0.0918   fark -0.0176
    PHL   n=270  0.1405 / 0.1120   fark -0.0285
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       712         0.034         0.062   +0.028
  0.1-0.2       481         0.151         0.191   +0.040
  0.2-0.3       395         0.247         0.248   +0.001
  0.3-0.4       207         0.345         0.227   -0.118
  0.4-0.5        77         0.437         0.299   -0.138
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4001)
  işlem sayısı                    4001
  kazanan                         1579  (%39)
  ort. İDDİA EDİLEN edge       +16.77p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.08p   ±0.6p  %95 [-0.2p, +2.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4037.76 $
  PnL fee ÖNCESİ             +24446.55 $
  PnL fee SONRASI            +20408.79 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10229.64 $   %90 aralık [-17938.05, -2865.06]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1320 (model 0.1328)

  bizim (fee sonrası)            +20408.79 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
