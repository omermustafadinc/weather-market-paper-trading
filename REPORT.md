========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-20T08:18:03.384644Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          87258
  orderbook seviyesi     4648081
  tahmin snapshot          57771
  karar                    18000
  simüle fill               4660
  çözümlenmiş kova          2226

## Brier skoru  (düşük = iyi, 2142 kova)
  model                  0.1320
  piyasa (mid)           0.1298   n=2142
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0022  ±0.0031  %95 [-0.0083, +0.0040]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=306  0.1280 / 0.2052   fark +0.0771
    CHI   n=306  0.1390 / 0.1077   fark -0.0312
    DEN   n=306  0.1491 / 0.1998   fark +0.0508
    LAX   n=306  0.1224 / 0.0911   fark -0.0313
    MIA   n=306  0.1360 / 0.1026   fark -0.0334
    NY    n=306  0.1069 / 0.0913   fark -0.0156
    PHL   n=306  0.1426 / 0.1111   fark -0.0315
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       815         0.034         0.061   +0.028
  0.1-0.2       534         0.150         0.189   +0.039
  0.2-0.3       427         0.247         0.255   +0.008
  0.3-0.4       239         0.345         0.213   -0.131
  0.4-0.5        90         0.439         0.311   -0.128
  0.5-0.6        27         0.549         0.370   -0.179
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4580)
  işlem sayısı                    4580
  kazanan                         1765  (%39)
  ort. İDDİA EDİLEN edge       +17.51p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.74p   ±0.6p  %95 [-0.4p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4651.76 $
  PnL fee ÖNCESİ             +27466.59 $
  PnL fee SONRASI            +22814.83 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11458.55 $   %90 aralık [-19313.28, -2165.49]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1298 (model 0.1320)

  bizim (fee sonrası)            +22814.83 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
