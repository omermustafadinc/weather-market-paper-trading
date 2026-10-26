========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-26T18:12:46.278278Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          97974
  orderbook seviyesi     5233071
  tahmin snapshot          65583
  karar                    20208
  simüle fill               5236
  çözümlenmiş kova          2490

## Brier skoru  (düşük = iyi, 2406 kova)
  model                  0.1311
  piyasa (mid)           0.1284   n=2406
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0026  ±0.0031  %95 [-0.0087, +0.0034]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=348  0.1243 / 0.2057   fark +0.0814
    CHI   n=342  0.1408 / 0.1054   fark -0.0354
    DEN   n=348  0.1450 / 0.1914   fark +0.0464
    LAX   n=342  0.1202 / 0.0881   fark -0.0321
    MIA   n=342  0.1336 / 0.1047   fark -0.0289
    NY    n=342  0.1075 / 0.0919   fark -0.0156
    PHL   n=342  0.1460 / 0.1093   fark -0.0366
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       934         0.033         0.058   +0.025
  0.1-0.2       579         0.149         0.188   +0.039
  0.2-0.3       463         0.247         0.259   +0.012
  0.3-0.4       284         0.346         0.229   -0.117
  0.4-0.5       101         0.439         0.317   -0.122
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5138)
  işlem sayısı                    5138
  kazanan                         2002  (%39)
  ort. İDDİA EDİLEN edge       +18.13p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.42p   ±0.6p  %95 [+0.3p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5280.68 $
  PnL fee ÖNCESİ             +42203.75 $
  PnL fee SONRASI            +36923.07 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13120.07 $   %90 aralık [-21753.77, -4301.31]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1284 (model 0.1311)

  bizim (fee sonrası)            +36923.07 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
