========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-25T10:16:53.651063Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          95658
  orderbook seviyesi     5107463
  tahmin snapshot          63945
  karar                    19722
  simüle fill               5109
  çözümlenmiş kova          2436

## Brier skoru  (düşük = iyi, 2352 kova)
  model                  0.1318
  piyasa (mid)           0.1288   n=2352
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0031  ±0.0031  %95 [-0.0091, +0.0030]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=336  0.1260 / 0.2047   fark +0.0787
    CHI   n=336  0.1401 / 0.1063   fark -0.0338
    DEN   n=336  0.1476 / 0.1968   fark +0.0492
    LAX   n=336  0.1203 / 0.0885   fark -0.0318
    MIA   n=336  0.1344 / 0.1054   fark -0.0290
    NY    n=336  0.1077 / 0.0919   fark -0.0158
    PHL   n=336  0.1467 / 0.1079   fark -0.0388
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       911         0.033         0.059   +0.026
  0.1-0.2       568         0.150         0.190   +0.040
  0.2-0.3       457         0.247         0.258   +0.011
  0.3-0.4       274         0.346         0.226   -0.120
  0.4-0.5        98         0.439         0.306   -0.133
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4993)
  işlem sayısı                    4993
  kazanan                         1934  (%39)
  ort. İDDİA EDİLEN edge       +18.08p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.27p   ±0.6p  %95 [+0.1p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5126.87 $
  PnL fee ÖNCESİ             +36366.70 $
  PnL fee SONRASI            +31239.83 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13252.22 $   %90 aralık [-22907.04, -3645.29]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1288 (model 0.1318)

  bizim (fee sonrası)            +31239.83 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
