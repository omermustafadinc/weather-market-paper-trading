========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-01T22:31:36.453990Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          60636
  orderbook seviyesi     3239985
  tahmin snapshot          40698
  karar                    12504
  simüle fill               3260
  çözümlenmiş kova          1464

## Brier skoru  (düşük = iyi, 1422 kova)
  model                  0.1308
  piyasa (mid)           0.1332   n=1422
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0024  ±0.0035  %95 [-0.0044, +0.0093]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=204  0.1322 / 0.2039   fark +0.0718
    CHI   n=204  0.1287 / 0.1146   fark -0.0141
    DEN   n=204  0.1448 / 0.2004   fark +0.0556
    LAX   n=198  0.1240 / 0.0973   fark -0.0268
    MIA   n=204  0.1381 / 0.1124   fark -0.0257
    NY    n=204  0.1094 / 0.0865   fark -0.0228
    PHL   n=204  0.1382 / 0.1164   fark -0.0217
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       522         0.034         0.054   +0.019
  0.1-0.2       367         0.151         0.191   +0.039
  0.2-0.3       304         0.246         0.247   +0.001
  0.3-0.4       152         0.346         0.243   -0.102
  0.4-0.5        59         0.435         0.322   -0.112
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3222)
  işlem sayısı                    3222
  kazanan                         1292  (%40)
  ort. İDDİA EDİLEN edge       +15.94p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.71p   ±0.7p  %95 [+0.3p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3213.95 $
  PnL fee ÖNCESİ             +24411.44 $
  PnL fee SONRASI            +21197.49 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8276.34 $   %90 aralık [-15381.04, -1728.44]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1332 (model 0.1308)

  bizim (fee sonrası)            +21197.49 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
