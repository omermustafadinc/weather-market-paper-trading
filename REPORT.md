========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-13T22:52:34.523466Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         119910
  orderbook seviyesi     6367648
  tahmin snapshot          80199
  karar                    24834
  simüle fill               6398
  çözümlenmiş kova          3264

## Brier skoru  (düşük = iyi, 3180 kova)
  model                  0.1318
  piyasa (mid)           0.1249   n=3180
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0069  ±0.0028  %95 [-0.0124, -0.0014]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=456  0.1211 / 0.1944   fark +0.0733
    CHI   n=450  0.1401 / 0.1061   fark -0.0341
    DEN   n=456  0.1411 / 0.1940   fark +0.0529
    LAX   n=450  0.1211 / 0.0848   fark -0.0363
    MIA   n=456  0.1379 / 0.1020   fark -0.0358
    NY    n=456  0.1122 / 0.0929   fark -0.0193
    PHL   n=456  0.1488 / 0.0990   fark -0.0498
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1293         0.032         0.053   +0.022
  0.1-0.2       715         0.150         0.200   +0.050
  0.2-0.3       578         0.247         0.268   +0.022
  0.3-0.4       363         0.345         0.234   -0.111
  0.4-0.5       158         0.440         0.297   -0.143
  0.5-0.6        46         0.548         0.370   -0.179
  0.6-0.7        17         0.637         0.412   -0.225
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6355)
  işlem sayısı                    6355
  kazanan                         2490  (%39)
  ort. İDDİA EDİLEN edge       +18.66p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.82p   ±0.5p  %95 [+0.8p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6494.98 $
  PnL fee ÖNCESİ             +50991.34 $
  PnL fee SONRASI            +44496.36 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15581.63 $   %90 aralık [-24929.83, -6823.99]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1249 (model 0.1318)

  bizim (fee sonrası)            +44496.36 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
