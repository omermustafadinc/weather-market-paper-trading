========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-12T05:28:25.978566Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          27162
  orderbook seviyesi     1430250
  tahmin snapshot          18900
  karar                     5466
  simüle fill               1417
  çözümlenmiş kova           630

## Brier skoru  (düşük = iyi, 588 kova)
  model                  0.1253
  piyasa (mid)           0.1305   n=588
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0052  ±0.0049  %95 [-0.0045, +0.0148]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 84  0.1542 / 0.2086   fark +0.0544
    CHI   n= 84  0.1208 / 0.1022   fark -0.0186
    DEN   n= 84  0.1447 / 0.2124   fark +0.0676
    LAX   n= 84  0.0989 / 0.0902   fark -0.0087
    MIA   n= 84  0.1217 / 0.1124   fark -0.0093
    NY    n= 84  0.1055 / 0.0838   fark -0.0217
    PHL   n= 84  0.1316 / 0.1040   fark -0.0275
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       223         0.033         0.036   +0.003
  0.1-0.2       139         0.149         0.187   +0.038
  0.2-0.3       134         0.246         0.291   +0.045
  0.3-0.4        58         0.345         0.224   -0.121
  0.4-0.5        22         0.437         0.227   -0.210
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1296)
  işlem sayısı                    1296
  kazanan                          530  (%41)
  ort. İDDİA EDİLEN edge       +14.62p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.65p   ±1.1p  %95 [-0.5p, +3.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1306.63 $
  PnL fee ÖNCESİ              +4734.29 $
  PnL fee SONRASI             +3427.66 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2352.10 $   %90 aralık [-6981.16, +1597.25]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1305 (model 0.1253)

  bizim (fee sonrası)             +3427.66 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
