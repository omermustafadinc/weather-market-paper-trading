========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-18T20:12:15.050666Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          84564
  orderbook seviyesi     4507410
  tahmin snapshot          55755
  karar                    17412
  simüle fill               4520
  çözümlenmiş kova          2154

## Brier skoru  (düşük = iyi, 2070 kova)
  model                  0.1324
  piyasa (mid)           0.1314   n=2070
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0009  ±0.0031  %95 [-0.0071, +0.0052]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=300  0.1295 / 0.2049   fark +0.0754
    CHI   n=294  0.1376 / 0.1092   fark -0.0284
    DEN   n=300  0.1484 / 0.1994   fark +0.0510
    LAX   n=294  0.1258 / 0.0937   fark -0.0321
    MIA   n=294  0.1366 / 0.1039   fark -0.0327
    NY    n=294  0.1083 / 0.0928   fark -0.0155
    PHL   n=294  0.1401 / 0.1134   fark -0.0267
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       781         0.034         0.061   +0.027
  0.1-0.2       521         0.150         0.190   +0.040
  0.2-0.3       418         0.247         0.256   +0.009
  0.3-0.4       233         0.345         0.215   -0.130
  0.4-0.5        84         0.438         0.298   -0.141
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4375)
  işlem sayısı                    4375
  kazanan                         1700  (%39)
  ort. İDDİA EDİLEN edge       +17.28p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.05p   ±0.6p  %95 [-0.2p, +2.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4432.04 $
  PnL fee ÖNCESİ             +26822.18 $
  PnL fee SONRASI            +22390.14 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10863.99 $   %90 aralık [-18680.61, -2762.26]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1314 (model 0.1324)

  bizim (fee sonrası)            +22390.14 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
