========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-20T09:01:01.464310Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         126330
  orderbook seviyesi     6694737
  tahmin snapshot          84735
  karar                    26112
  simüle fill               6708
  çözümlenmiş kova          3528

## Brier skoru  (düşük = iyi, 3426 kova)
  model                  0.1336
  piyasa (mid)           0.1242   n=3426
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0094  ±0.0028  %95 [-0.0148, -0.0039]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=492  0.1221 / 0.1926   fark +0.0705
    CHI   n=492  0.1444 / 0.1052   fark -0.0393
    DEN   n=492  0.1399 / 0.1931   fark +0.0532
    LAX   n=492  0.1204 / 0.0879   fark -0.0324
    MIA   n=486  0.1396 / 0.1019   fark -0.0377
    NY    n=486  0.1164 / 0.0917   fark -0.0247
    PHL   n=486  0.1523 / 0.0961   fark -0.0562
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1400         0.031         0.058   +0.027
  0.1-0.2       770         0.150         0.197   +0.048
  0.2-0.3       609         0.247         0.269   +0.022
  0.3-0.4       389         0.345         0.237   -0.109
  0.4-0.5       173         0.439         0.295   -0.145
  0.5-0.6        53         0.548         0.321   -0.227
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6667)
  işlem sayısı                    6667
  kazanan                         2605  (%39)
  ort. İDDİA EDİLEN edge       +19.09p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.50p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6786.81 $
  PnL fee ÖNCESİ             +50107.44 $
  PnL fee SONRASI            +43320.63 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16499.09 $   %90 aralık [-27522.48, -6699.02]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1242 (model 0.1336)

  bizim (fee sonrası)            +43320.63 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
