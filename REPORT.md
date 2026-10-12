========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-12T03:03:21.366244Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          74184
  orderbook seviyesi     3958308
  tahmin snapshot          49266
  karar                    15372
  simüle fill               3977
  çözümlenmiş kova          1890

## Brier skoru  (düşük = iyi, 1806 kova)
  model                  0.1333
  piyasa (mid)           0.1328   n=1806
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0005  ±0.0033  %95 [-0.0069, +0.0059]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=258  0.1316 / 0.2057   fark +0.0740
    CHI   n=258  0.1386 / 0.1096   fark -0.0290
    DEN   n=258  0.1504 / 0.2023   fark +0.0519
    LAX   n=258  0.1271 / 0.0972   fark -0.0300
    MIA   n=258  0.1348 / 0.1098   fark -0.0249
    NY    n=258  0.1097 / 0.0905   fark -0.0191
    PHL   n=258  0.1410 / 0.1145   fark -0.0265
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       677         0.033         0.064   +0.030
  0.1-0.2       455         0.151         0.191   +0.041
  0.2-0.3       373         0.247         0.247   -0.000
  0.3-0.4       197         0.346         0.228   -0.117
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3893)
  işlem sayısı                    3893
  kazanan                         1540  (%40)
  ort. İDDİA EDİLEN edge       +16.59p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.09p   ±0.7p  %95 [-0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3921.17 $
  PnL fee ÖNCESİ             +23782.56 $
  PnL fee SONRASI            +19861.39 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9675.83 $   %90 aralık [-16926.97, -2644.86]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1328 (model 0.1333)

  bizim (fee sonrası)            +19861.39 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
