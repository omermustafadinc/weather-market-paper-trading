========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-01T06:10:51.267802Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          59964
  orderbook seviyesi     3203158
  tahmin snapshot          40068
  karar                    12378
  simüle fill               3229
  çözümlenmiş kova          1428

## Brier skoru  (düşük = iyi, 1386 kova)
  model                  0.1312
  piyasa (mid)           0.1336   n=1386
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0025  ±0.0036  %95 [-0.0046, +0.0095]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=198  0.1340 / 0.2093   fark +0.0753
    CHI   n=198  0.1295 / 0.1139   fark -0.0156
    DEN   n=198  0.1447 / 0.2005   fark +0.0559
    LAX   n=198  0.1240 / 0.0973   fark -0.0268
    MIA   n=198  0.1393 / 0.1123   fark -0.0269
    NY    n=198  0.1086 / 0.0856   fark -0.0229
    PHL   n=198  0.1381 / 0.1164   fark -0.0218
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       510         0.034         0.055   +0.021
  0.1-0.2       358         0.151         0.193   +0.041
  0.2-0.3       295         0.247         0.247   +0.001
  0.3-0.4       147         0.346         0.238   -0.108
  0.4-0.5        58         0.435         0.310   -0.125
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3163)
  işlem sayısı                    3163
  kazanan                         1264  (%40)
  ort. İDDİA EDİLEN edge       +16.00p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.65p   ±0.7p  %95 [+0.2p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3160.93 $
  PnL fee ÖNCESİ             +24361.37 $
  PnL fee SONRASI            +21200.44 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8404.51 $   %90 aralık [-14296.51, -1735.75]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1336 (model 0.1312)

  bizim (fee sonrası)            +21200.44 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
