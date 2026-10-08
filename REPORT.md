========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-08T17:26:25.580466Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          69192
  orderbook seviyesi     3701125
  tahmin snapshot          46368
  karar                    14262
  simüle fill               3697
  çözümlenmiş kova          1734

## Brier skoru  (düşük = iyi, 1650 kova)
  model                  0.1322
  piyasa (mid)           0.1337   n=1650
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0015  ±0.0033  %95 [-0.0050, +0.0080]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=240  0.1316 / 0.2039   fark +0.0723
    CHI   n=234  0.1357 / 0.1119   fark -0.0238
    DEN   n=240  0.1479 / 0.2010   fark +0.0531
    LAX   n=234  0.1281 / 0.1006   fark -0.0274
    MIA   n=234  0.1357 / 0.1120   fark -0.0237
    NY    n=234  0.1093 / 0.0893   fark -0.0199
    PHL   n=234  0.1365 / 0.1135   fark -0.0230
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       614         0.033         0.059   +0.025
  0.1-0.2       420         0.151         0.193   +0.042
  0.2-0.3       341         0.247         0.243   -0.003
  0.3-0.4       182         0.346         0.242   -0.104
  0.4-0.5        70         0.436         0.300   -0.136
  0.5-0.6        19         0.552         0.316   -0.236
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3619)
  işlem sayısı                    3619
  kazanan                         1446  (%40)
  ort. İDDİA EDİLEN edge       +16.31p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.34p   ±0.7p  %95 [+0.0p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3608.48 $
  PnL fee ÖNCESİ             +25762.71 $
  PnL fee SONRASI            +22154.23 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9499.19 $   %90 aralık [-17420.92, -2756.86]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1337 (model 0.1322)

  bizim (fee sonrası)            +22154.23 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
