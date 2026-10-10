========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-10T20:45:16.076861Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          72084
  orderbook seviyesi     3852082
  tahmin snapshot          48006
  karar                    14868
  simüle fill               3850
  çözümlenmiş kova          1830

## Brier skoru  (düşük = iyi, 1746 kova)
  model                  0.1336
  piyasa (mid)           0.1328   n=1746
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0007  ±0.0033  %95 [-0.0072, +0.0058]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=252  0.1319 / 0.2048   fark +0.0730
    CHI   n=246  0.1377 / 0.1114   fark -0.0263
    DEN   n=252  0.1509 / 0.2021   fark +0.0512
    LAX   n=246  0.1303 / 0.0978   fark -0.0324
    MIA   n=252  0.1350 / 0.1080   fark -0.0270
    NY    n=252  0.1089 / 0.0917   fark -0.0173
    PHL   n=246  0.1403 / 0.1121   fark -0.0282
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       656         0.033         0.064   +0.031
  0.1-0.2       439         0.151         0.191   +0.041
  0.2-0.3       356         0.247         0.244   -0.002
  0.3-0.4       192         0.346         0.234   -0.112
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3782)
  işlem sayısı                    3782
  kazanan                         1507  (%40)
  ort. İDDİA EDİLEN edge       +16.42p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.24p   ±0.7p  %95 [-0.1p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3782.89 $
  PnL fee ÖNCESİ             +24933.67 $
  PnL fee SONRASI            +21150.78 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9542.23 $   %90 aralık [-16811.53, -1635.59]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1328 (model 0.1336)

  bizim (fee sonrası)            +21150.78 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
