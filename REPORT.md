========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-09T02:15:35.397690Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         115206
  orderbook seviyesi     6127978
  tahmin snapshot          76797
  karar                    23868
  simüle fill               6162
  çözümlenmiş kova          3060

## Brier skoru  (düşük = iyi, 2976 kova)
  model                  0.1307
  piyasa (mid)           0.1246   n=2976
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0061  ±0.0028  %95 [-0.0117, -0.0005]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=426  0.1225 / 0.1954   fark +0.0729
    CHI   n=426  0.1383 / 0.1054   fark -0.0329
    DEN   n=426  0.1403 / 0.1918   fark +0.0515
    LAX   n=420  0.1199 / 0.0855   fark -0.0343
    MIA   n=426  0.1372 / 0.1022   fark -0.0349
    NY    n=426  0.1074 / 0.0912   fark -0.0162
    PHL   n=426  0.1490 / 0.0999   fark -0.0491
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1198         0.032         0.051   +0.019
  0.1-0.2       677         0.150         0.196   +0.046
  0.2-0.3       548         0.246         0.268   +0.022
  0.3-0.4       347         0.345         0.242   -0.103
  0.4-0.5       143         0.440         0.301   -0.139
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6098)
  işlem sayısı                    6098
  kazanan                         2384  (%39)
  ort. İDDİA EDİLEN edge       +18.46p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.77p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6231.36 $
  PnL fee ÖNCESİ             +49025.13 $
  PnL fee SONRASI            +42793.77 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14933.59 $   %90 aralık [-25254.04, -7243.32]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1246 (model 0.1307)

  bizim (fee sonrası)            +42793.77 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
