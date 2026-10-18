========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-18T22:23:42.917838Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          84900
  orderbook seviyesi     4523992
  tahmin snapshot          56007
  karar                    17496
  simüle fill               4540
  çözümlenmiş kova          2178

## Brier skoru  (düşük = iyi, 2094 kova)
  model                  0.1323
  piyasa (mid)           0.1309   n=2094
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0015  ±0.0031  %95 [-0.0076, +0.0047]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=300  0.1295 / 0.2049   fark +0.0754
    CHI   n=300  0.1377 / 0.1089   fark -0.0289
    DEN   n=300  0.1484 / 0.1994   fark +0.0510
    LAX   n=294  0.1258 / 0.0937   fark -0.0321
    MIA   n=300  0.1361 / 0.1036   fark -0.0325
    NY    n=300  0.1076 / 0.0924   fark -0.0152
    PHL   n=300  0.1410 / 0.1125   fark -0.0285
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       792         0.034         0.061   +0.026
  0.1-0.2       525         0.150         0.190   +0.040
  0.2-0.3       420         0.247         0.257   +0.010
  0.3-0.4       236         0.345         0.216   -0.128
  0.4-0.5        88         0.439         0.295   -0.143
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4461)
  işlem sayısı                    4461
  kazanan                         1725  (%39)
  ort. İDDİA EDİLEN edge       +17.32p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.88p   ±0.6p  %95 [-0.3p, +2.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4525.33 $
  PnL fee ÖNCESİ             +25572.31 $
  PnL fee SONRASI            +21046.98 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11404.57 $   %90 aralık [-20724.73, -3681.14]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1309 (model 0.1323)

  bizim (fee sonrası)            +21046.98 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
