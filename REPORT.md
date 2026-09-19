========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-19T22:02:06.199115Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          41640
  orderbook seviyesi     2231660
  tahmin snapshot          28476
  karar                     8508
  simüle fill               2223
  çözümlenmiş kova           954

## Brier skoru  (düşük = iyi, 912 kova)
  model                  0.1311
  piyasa (mid)           0.1354   n=912
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0042  ±0.0041  %95 [-0.0037, +0.0122]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=132  0.1466 / 0.2119   fark +0.0653
    CHI   n=126  0.1314 / 0.1153   fark -0.0161
    DEN   n=132  0.1502 / 0.2096   fark +0.0594
    LAX   n=126  0.1138 / 0.0948   fark -0.0190
    MIA   n=132  0.1333 / 0.1168   fark -0.0165
    NY    n=132  0.1094 / 0.0854   fark -0.0240
    PHL   n=132  0.1325 / 0.1113   fark -0.0213
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       331         0.035         0.054   +0.019
  0.1-0.2       236         0.152         0.191   +0.039
  0.2-0.3       202         0.245         0.262   +0.017
  0.3-0.4       100         0.344         0.220   -0.124
  0.4-0.5        31         0.432         0.226   -0.206
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2102)
  işlem sayısı                    2102
  kazanan                          825  (%39)
  ort. İDDİA EDİLEN edge       +15.14p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.15p   ±0.9p  %95 [-0.6p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2124.14 $
  PnL fee ÖNCESİ             +10760.62 $
  PnL fee SONRASI             +8636.48 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -5042.68 $   %90 aralık [-10773.59, +679.82]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1354 (model 0.1311)

  bizim (fee sonrası)             +8636.48 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
