========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-06T16:13:06.181725Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          15954
  orderbook seviyesi      859655
  tahmin snapshot          11592
  karar                     3054
  simüle fill                798
  çözümlenmiş kova           390

## Brier skoru  (düşük = iyi, 348 kova)
  model                  0.1246
  piyasa (mid)           0.1303   n=348
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0057  ±0.0063  %95 [-0.0067, +0.0181]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 54  0.1469 / 0.1995   fark +0.0526
    CHI   n= 48  0.1160 / 0.1070   fark -0.0091
    DEN   n= 54  0.1475 / 0.2085   fark +0.0610
    LAX   n= 48  0.1088 / 0.0869   fark -0.0218
    MIA   n= 48  0.1241 / 0.1207   fark -0.0034
    NY    n= 48  0.1094 / 0.0738   fark -0.0356
    PHL   n= 48  0.1139 / 0.0970   fark -0.0169
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       129         0.034         0.023   -0.011
  0.1-0.2        88         0.152         0.205   +0.052
  0.2-0.3        77         0.242         0.273   +0.030
  0.3-0.4        38         0.350         0.263   -0.086
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (677)
  işlem sayısı                     677
  kazanan                          264  (%39)
  ort. İDDİA EDİLEN edge       +13.77p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.22p   ±1.5p  %95 [-3.1p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    687.10 $
  PnL fee ÖNCESİ                +52.63 $
  PnL fee SONRASI              -634.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1203.32 $   %90 aralık [-4726.80, +2505.49]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1303 (model 0.1246)

  bizim (fee sonrası)              -634.47 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
