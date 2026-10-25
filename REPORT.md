========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-25T00:49:47.955416Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          95250
  orderbook seviyesi     5083267
  tahmin snapshot          63441
  karar                    19686
  simüle fill               5093
  çözümlenmiş kova          2430

## Brier skoru  (düşük = iyi, 2346 kova)
  model                  0.1319
  piyasa (mid)           0.1288   n=2346
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0031  ±0.0031  %95 [-0.0092, +0.0030]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=336  0.1260 / 0.2047   fark +0.0787
    CHI   n=336  0.1401 / 0.1063   fark -0.0338
    DEN   n=336  0.1476 / 0.1968   fark +0.0492
    LAX   n=330  0.1207 / 0.0879   fark -0.0328
    MIA   n=336  0.1344 / 0.1054   fark -0.0290
    NY    n=336  0.1077 / 0.0919   fark -0.0158
    PHL   n=336  0.1467 / 0.1079   fark -0.0388
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       908         0.033         0.059   +0.027
  0.1-0.2       568         0.150         0.190   +0.040
  0.2-0.3       456         0.247         0.259   +0.012
  0.3-0.4       272         0.346         0.224   -0.122
  0.4-0.5        98         0.439         0.306   -0.133
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4988)
  işlem sayısı                    4988
  kazanan                         1932  (%39)
  ort. İDDİA EDİLEN edge       +18.08p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.26p   ±0.6p  %95 [+0.1p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5121.88 $
  PnL fee ÖNCESİ             +36376.50 $
  PnL fee SONRASI            +31254.62 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13065.46 $   %90 aralık [-22933.29, -2837.41]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1288 (model 0.1319)

  bizim (fee sonrası)            +31254.62 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
