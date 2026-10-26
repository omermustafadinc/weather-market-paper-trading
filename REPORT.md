========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-26T12:04:25.957494Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          97638
  orderbook seviyesi     5214382
  tahmin snapshot          65331
  karar                    20124
  simüle fill               5216
  çözümlenmiş kova          2478

## Brier skoru  (düşük = iyi, 2394 kova)
  model                  0.1314
  piyasa (mid)           0.1285   n=2394
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0030  ±0.0031  %95 [-0.0090, +0.0031]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=342  0.1251 / 0.2052   fark +0.0801
    CHI   n=342  0.1408 / 0.1054   fark -0.0354
    DEN   n=342  0.1469 / 0.1945   fark +0.0476
    LAX   n=342  0.1202 / 0.0881   fark -0.0321
    MIA   n=342  0.1336 / 0.1047   fark -0.0289
    NY    n=342  0.1075 / 0.0919   fark -0.0156
    PHL   n=342  0.1460 / 0.1093   fark -0.0366
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       927         0.033         0.058   +0.025
  0.1-0.2       578         0.149         0.189   +0.039
  0.2-0.3       462         0.247         0.260   +0.013
  0.3-0.4       283         0.346         0.230   -0.116
  0.4-0.5       100         0.439         0.310   -0.129
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5109)
  işlem sayısı                    5109
  kazanan                         1987  (%39)
  ort. İDDİA EDİLEN edge       +18.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.27p   ±0.6p  %95 [+0.1p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5239.22 $
  PnL fee ÖNCESİ             +38072.76 $
  PnL fee SONRASI            +32833.54 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13192.07 $   %90 aralık [-22485.21, -4547.14]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1285 (model 0.1314)

  bizim (fee sonrası)            +32833.54 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
