========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-20T17:48:23.918812Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         126666
  orderbook seviyesi     6711863
  tahmin snapshot          84861
  karar                    26196
  simüle fill               6729
  çözümlenmiş kova          3540

## Brier skoru  (düşük = iyi, 3438 kova)
  model                  0.1335
  piyasa (mid)           0.1246   n=3438
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0089  ±0.0028  %95 [-0.0144, -0.0035]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=498  0.1212 / 0.1930   fark +0.0717
    CHI   n=492  0.1444 / 0.1052   fark -0.0393
    DEN   n=498  0.1404 / 0.1935   fark +0.0531
    LAX   n=492  0.1204 / 0.0879   fark -0.0324
    MIA   n=486  0.1396 / 0.1019   fark -0.0377
    NY    n=486  0.1164 / 0.0917   fark -0.0247
    PHL   n=486  0.1523 / 0.0961   fark -0.0562
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1405         0.031         0.058   +0.028
  0.1-0.2       772         0.150         0.197   +0.047
  0.2-0.3       613         0.247         0.268   +0.020
  0.3-0.4       389         0.345         0.237   -0.109
  0.4-0.5       173         0.439         0.295   -0.145
  0.5-0.6        54         0.547         0.333   -0.214
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6668)
  işlem sayısı                    6668
  kazanan                         2606  (%39)
  ort. İDDİA EDİLEN edge       +19.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.51p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6786.96 $
  PnL fee ÖNCESİ             +50148.12 $
  PnL fee SONRASI            +43361.16 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16169.74 $   %90 aralık [-25047.58, -7506.24]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1246 (model 0.1335)

  bizim (fee sonrası)            +43361.16 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
