========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-14T09:56:58.706674Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         120414
  orderbook seviyesi     6395007
  tahmin snapshot          80451
  karar                    24918
  simüle fill               6418
  çözümlenmiş kova          3276

## Brier skoru  (düşük = iyi, 3192 kova)
  model                  0.1317
  piyasa (mid)           0.1250   n=3192
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0067  ±0.0028  %95 [-0.0122, -0.0013]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=456  0.1211 / 0.1944   fark +0.0733
    CHI   n=456  0.1405 / 0.1070   fark -0.0335
    DEN   n=456  0.1411 / 0.1940   fark +0.0529
    LAX   n=456  0.1204 / 0.0856   fark -0.0348
    MIA   n=456  0.1379 / 0.1020   fark -0.0358
    NY    n=456  0.1122 / 0.0929   fark -0.0193
    PHL   n=456  0.1488 / 0.0990   fark -0.0498
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1299         0.032         0.053   +0.021
  0.1-0.2       716         0.150         0.200   +0.050
  0.2-0.3       581         0.246         0.269   +0.022
  0.3-0.4       363         0.345         0.234   -0.111
  0.4-0.5       159         0.440         0.302   -0.138
  0.5-0.6        47         0.550         0.362   -0.188
  0.6-0.7        17         0.637         0.412   -0.225
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6358)
  işlem sayısı                    6358
  kazanan                         2491  (%39)
  ort. İDDİA EDİLEN edge       +18.66p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.82p   ±0.5p  %95 [+0.8p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6497.26 $
  PnL fee ÖNCESİ             +50986.28 $
  PnL fee SONRASI            +44489.02 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15551.67 $   %90 aralık [-24100.44, -6254.03]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1250 (model 0.1317)

  bizim (fee sonrası)            +44489.02 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
