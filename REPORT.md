========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-23T20:31:35.697266Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          92622
  orderbook seviyesi     4944056
  tahmin snapshot          61803
  karar                    19086
  simüle fill               4945
  çözümlenmiş kova          2364

## Brier skoru  (düşük = iyi, 2280 kova)
  model                  0.1323
  piyasa (mid)           0.1296   n=2280
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0027  ±0.0031  %95 [-0.0088, +0.0035]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=330  0.1268 / 0.2039   fark +0.0771
    CHI   n=324  0.1396 / 0.1079   fark -0.0317
    DEN   n=330  0.1483 / 0.1990   fark +0.0508
    LAX   n=324  0.1213 / 0.0886   fark -0.0327
    MIA   n=324  0.1353 / 0.1055   fark -0.0298
    NY    n=324  0.1080 / 0.0904   fark -0.0176
    PHL   n=324  0.1468 / 0.1093   fark -0.0375
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       878         0.033         0.062   +0.029
  0.1-0.2       558         0.150         0.192   +0.042
  0.2-0.3       447         0.247         0.253   +0.006
  0.3-0.4       259         0.345         0.220   -0.125
  0.4-0.5        94         0.439         0.309   -0.130
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4833)
  işlem sayısı                    4833
  kazanan                         1870  (%39)
  ort. İDDİA EDİLEN edge       +17.83p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.01p   ±0.6p  %95 [-0.1p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4925.26 $
  PnL fee ÖNCESİ             +33599.79 $
  PnL fee SONRASI            +28674.53 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12885.05 $   %90 aralık [-21369.70, -2963.32]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1296 (model 0.1323)

  bizim (fee sonrası)            +28674.53 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
