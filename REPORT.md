========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-16T21:30:37.913879Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         123306
  orderbook seviyesi     6542290
  tahmin snapshot          82593
  karar                    25524
  simüle fill               6567
  çözümlenmiş kova          3372

## Brier skoru  (düşük = iyi, 3288 kova)
  model                  0.1318
  piyasa (mid)           0.1247   n=3288
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0071  ±0.0028  %95 [-0.0125, -0.0017]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=474  0.1210 / 0.1915   fark +0.0705
    CHI   n=468  0.1409 / 0.1077   fark -0.0333
    DEN   n=474  0.1410 / 0.1924   fark +0.0514
    LAX   n=468  0.1195 / 0.0878   fark -0.0317
    MIA   n=468  0.1379 / 0.1034   fark -0.0346
    NY    n=468  0.1128 / 0.0916   fark -0.0212
    PHL   n=468  0.1496 / 0.0971   fark -0.0525
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1340         0.031         0.055   +0.024
  0.1-0.2       737         0.150         0.194   +0.044
  0.2-0.3       595         0.247         0.267   +0.020
  0.3-0.4       374         0.345         0.241   -0.105
  0.4-0.5       164         0.440         0.311   -0.129
  0.5-0.6        48         0.549         0.354   -0.194
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6493)
  işlem sayısı                    6493
  kazanan                         2551  (%39)
  ort. İDDİA EDİLEN edge       +18.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.86p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6628.11 $
  PnL fee ÖNCESİ             +51619.97 $
  PnL fee SONRASI            +44991.86 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16221.20 $   %90 aralık [-27628.26, -5735.86]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1247 (model 0.1318)

  bizim (fee sonrası)            +44991.86 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
