========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-01T18:04:22.696179Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          60300
  orderbook seviyesi     3223117
  tahmin snapshot          40446
  karar                    12420
  simüle fill               3239
  çözümlenmiş kova          1440

## Brier skoru  (düşük = iyi, 1398 kova)
  model                  0.1310
  piyasa (mid)           0.1334   n=1398
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0024  ±0.0036  %95 [-0.0045, +0.0094]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=204  0.1322 / 0.2039   fark +0.0718
    CHI   n=198  0.1295 / 0.1139   fark -0.0156
    DEN   n=204  0.1448 / 0.2004   fark +0.0556
    LAX   n=198  0.1240 / 0.0973   fark -0.0268
    MIA   n=198  0.1393 / 0.1123   fark -0.0269
    NY    n=198  0.1086 / 0.0856   fark -0.0229
    PHL   n=198  0.1381 / 0.1164   fark -0.0218
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       514         0.034         0.054   +0.020
  0.1-0.2       362         0.151         0.193   +0.042
  0.2-0.3       297         0.246         0.246   -0.001
  0.3-0.4       148         0.346         0.236   -0.109
  0.4-0.5        59         0.435         0.322   -0.112
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3181)
  işlem sayısı                    3181
  kazanan                         1268  (%40)
  ort. İDDİA EDİLEN edge       +15.98p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.62p   ±0.7p  %95 [+0.2p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3181.19 $
  PnL fee ÖNCESİ             +24418.28 $
  PnL fee SONRASI            +21237.09 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8423.25 $   %90 aralık [-15914.73, -2339.71]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1334 (model 0.1310)

  bizim (fee sonrası)            +21237.09 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
