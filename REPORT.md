========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-22T19:48:59.707592Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          46740
  orderbook seviyesi     2500929
  tahmin snapshot          31500
  karar                     9546
  simüle fill               2492
  çözümlenmiş kova          1062

## Brier skoru  (düşük = iyi, 1020 kova)
  model                  0.1309
  piyasa (mid)           0.1364   n=1020
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0055  ±0.0039  %95 [-0.0021, +0.0130]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=150  0.1440 / 0.2120   fark +0.0680
    CHI   n=144  0.1253 / 0.1140   fark -0.0113
    DEN   n=150  0.1518 / 0.2099   fark +0.0581
    LAX   n=144  0.1169 / 0.0979   fark -0.0190
    MIA   n=144  0.1340 / 0.1148   fark -0.0192
    NY    n=144  0.1089 / 0.0880   fark -0.0208
    PHL   n=144  0.1343 / 0.1120   fark -0.0223
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       363         0.035         0.052   +0.017
  0.1-0.2       274         0.151         0.190   +0.039
  0.2-0.3       224         0.246         0.259   +0.013
  0.3-0.4       112         0.343         0.214   -0.129
  0.4-0.5        35         0.431         0.286   -0.145
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2397)
  işlem sayısı                    2397
  kazanan                          973  (%41)
  ort. İDDİA EDİLEN edge       +15.28p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.70p   ±0.8p  %95 [+1.1p, +4.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2433.64 $
  PnL fee ÖNCESİ             +20882.90 $
  PnL fee SONRASI            +18449.26 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6970.24 $   %90 aralık [-13099.86, +73.54]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1364 (model 0.1309)

  bizim (fee sonrası)            +18449.26 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
