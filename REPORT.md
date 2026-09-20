========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-19T23:59:51.392454Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          41976
  orderbook seviyesi     2248236
  tahmin snapshot          28602
  karar                     8592
  simüle fill               2244
  çözümlenmiş kova           960

## Brier skoru  (düşük = iyi, 918 kova)
  model                  0.1309
  piyasa (mid)           0.1355   n=918
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0046  ±0.0040  %95 [-0.0033, +0.0126]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=132  0.1466 / 0.2119   fark +0.0653
    CHI   n=132  0.1295 / 0.1171   fark -0.0124
    DEN   n=132  0.1502 / 0.2096   fark +0.0594
    LAX   n=126  0.1138 / 0.0948   fark -0.0190
    MIA   n=132  0.1333 / 0.1168   fark -0.0165
    NY    n=132  0.1094 / 0.0854   fark -0.0240
    PHL   n=132  0.1325 / 0.1113   fark -0.0213
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       333         0.035         0.054   +0.019
  0.1-0.2       238         0.151         0.189   +0.038
  0.2-0.3       203         0.245         0.261   +0.016
  0.3-0.4       101         0.344         0.228   -0.116
  0.4-0.5        31         0.432         0.226   -0.206
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2151)
  işlem sayısı                    2151
  kazanan                          865  (%40)
  ort. İDDİA EDİLEN edge       +15.14p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.81p   ±0.9p  %95 [+0.1p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2164.58 $
  PnL fee ÖNCESİ             +12466.37 $
  PnL fee SONRASI            +10301.79 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -5056.59 $   %90 aralık [-10879.52, +135.67]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1355 (model 0.1309)

  bizim (fee sonrası)            +10301.79 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
