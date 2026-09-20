========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-20T07:25:38.146394Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          42492
  orderbook seviyesi     2276146
  tahmin snapshot          29106
  karar                     8682
  simüle fill               2266
  çözümlenmiş kova           966

## Brier skoru  (düşük = iyi, 924 kova)
  model                  0.1308
  piyasa (mid)           0.1354   n=924
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0046  ±0.0040  %95 [-0.0033, +0.0125]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=132  0.1466 / 0.2119   fark +0.0653
    CHI   n=132  0.1295 / 0.1171   fark -0.0124
    DEN   n=132  0.1502 / 0.2096   fark +0.0594
    LAX   n=132  0.1143 / 0.0961   fark -0.0181
    MIA   n=132  0.1333 / 0.1168   fark -0.0165
    NY    n=132  0.1094 / 0.0854   fark -0.0240
    PHL   n=132  0.1325 / 0.1113   fark -0.0213
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       334         0.035         0.054   +0.018
  0.1-0.2       241         0.151         0.187   +0.035
  0.2-0.3       205         0.245         0.263   +0.018
  0.3-0.4       101         0.344         0.228   -0.116
  0.4-0.5        31         0.432         0.226   -0.206
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2159)
  işlem sayısı                    2159
  kazanan                          869  (%40)
  ort. İDDİA EDİLEN edge       +15.13p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.80p   ±0.9p  %95 [+0.1p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2169.54 $
  PnL fee ÖNCESİ             +12428.47 $
  PnL fee SONRASI            +10258.93 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4740.24 $   %90 aralık [-10370.67, +1211.39]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1354 (model 0.1308)

  bizim (fee sonrası)            +10258.93 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
