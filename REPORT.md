========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-23T01:36:08.953091Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          91578
  orderbook seviyesi     4884979
  tahmin snapshot          60921
  karar                    18900
  simüle fill               4894
  çözümlenmiş kova          2352

## Brier skoru  (düşük = iyi, 2268 kova)
  model                  0.1323
  piyasa (mid)           0.1291   n=2268
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0032  ±0.0031  %95 [-0.0093, +0.0030]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=324  0.1274 / 0.2033   fark +0.0758
    CHI   n=324  0.1396 / 0.1079   fark -0.0317
    DEN   n=324  0.1475 / 0.1986   fark +0.0511
    LAX   n=324  0.1213 / 0.0886   fark -0.0327
    MIA   n=324  0.1353 / 0.1055   fark -0.0298
    NY    n=324  0.1080 / 0.0904   fark -0.0176
    PHL   n=324  0.1468 / 0.1093   fark -0.0375
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       872         0.033         0.062   +0.029
  0.1-0.2       556         0.150         0.191   +0.041
  0.2-0.3       447         0.247         0.253   +0.006
  0.3-0.4       256         0.345         0.219   -0.127
  0.4-0.5        94         0.439         0.309   -0.130
  0.5-0.6        31         0.548         0.355   -0.193
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4824)
  işlem sayısı                    4824
  kazanan                         1865  (%39)
  ort. İDDİA EDİLEN edge       +17.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.97p   ±0.6p  %95 [-0.2p, +2.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4915.89 $
  PnL fee ÖNCESİ             +32972.13 $
  PnL fee SONRASI            +28056.24 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12336.06 $   %90 aralık [-21483.21, -4463.02]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1291 (model 0.1323)

  bizim (fee sonrası)            +28056.24 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
