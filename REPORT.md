========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-02T08:00:39.789271Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          61140
  orderbook seviyesi     3268036
  tahmin snapshot          41076
  karar                    12588
  simüle fill               3280
  çözümlenmiş kova          1470

## Brier skoru  (düşük = iyi, 1428 kova)
  model                  0.1311
  piyasa (mid)           0.1330   n=1428
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0019  ±0.0035  %95 [-0.0050, +0.0088]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=204  0.1322 / 0.2039   fark +0.0718
    CHI   n=204  0.1287 / 0.1146   fark -0.0141
    DEN   n=204  0.1448 / 0.2004   fark +0.0556
    LAX   n=204  0.1262 / 0.0966   fark -0.0297
    MIA   n=204  0.1381 / 0.1124   fark -0.0257
    NY    n=204  0.1094 / 0.0865   fark -0.0228
    PHL   n=204  0.1382 / 0.1164   fark -0.0217
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       524         0.034         0.055   +0.021
  0.1-0.2       369         0.151         0.190   +0.038
  0.2-0.3       305         0.246         0.246   -0.000
  0.3-0.4       153         0.346         0.242   -0.104
  0.4-0.5        59         0.435         0.322   -0.112
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3229)
  işlem sayısı                    3229
  kazanan                         1294  (%40)
  ort. İDDİA EDİLEN edge       +15.95p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.67p   ±0.7p  %95 [+0.3p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3219.89 $
  PnL fee ÖNCESİ             +24333.58 $
  PnL fee SONRASI            +21113.69 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8554.82 $   %90 aralık [-15892.91, -823.24]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1311)

  bizim (fee sonrası)            +21113.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
