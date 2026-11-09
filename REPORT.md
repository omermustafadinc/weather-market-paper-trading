========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-09T09:20:26.687511Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         115374
  orderbook seviyesi     6138292
  tahmin snapshot          77049
  karar                    23868
  simüle fill               6162
  çözümlenmiş kova          3066

## Brier skoru  (düşük = iyi, 2982 kova)
  model                  0.1307
  piyasa (mid)           0.1244   n=2982
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0063  ±0.0028  %95 [-0.0119, -0.0007]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=426  0.1225 / 0.1954   fark +0.0729
    CHI   n=426  0.1383 / 0.1054   fark -0.0329
    DEN   n=426  0.1403 / 0.1918   fark +0.0515
    LAX   n=426  0.1204 / 0.0849   fark -0.0356
    MIA   n=426  0.1372 / 0.1022   fark -0.0349
    NY    n=426  0.1074 / 0.0912   fark -0.0162
    PHL   n=426  0.1490 / 0.0999   fark -0.0491
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1199         0.032         0.051   +0.019
  0.1-0.2       679         0.150         0.197   +0.047
  0.2-0.3       551         0.246         0.267   +0.020
  0.3-0.4       347         0.345         0.242   -0.103
  0.4-0.5       143         0.440         0.301   -0.139
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6102)
  işlem sayısı                    6102
  kazanan                         2385  (%39)
  ort. İDDİA EDİLEN edge       +18.46p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.77p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6235.89 $
  PnL fee ÖNCESİ             +48961.81 $
  PnL fee SONRASI            +42725.92 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15685.48 $   %90 aralık [-26265.36, -5662.51]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1244 (model 0.1307)

  bizim (fee sonrası)            +42725.92 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
