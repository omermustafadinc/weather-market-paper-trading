========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-19T02:24:57.723445Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          85572
  orderbook seviyesi     4558063
  tahmin snapshot          56511
  karar                    17664
  simüle fill               4580
  çözümlenmiş kova          2184

## Brier skoru  (düşük = iyi, 2100 kova)
  model                  0.1321
  piyasa (mid)           0.1306   n=2100
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0015  ±0.0031  %95 [-0.0076, +0.0046]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=300  0.1295 / 0.2049   fark +0.0754
    CHI   n=300  0.1377 / 0.1089   fark -0.0289
    DEN   n=300  0.1484 / 0.1994   fark +0.0510
    LAX   n=300  0.1247 / 0.0928   fark -0.0319
    MIA   n=300  0.1361 / 0.1036   fark -0.0325
    NY    n=300  0.1076 / 0.0924   fark -0.0152
    PHL   n=300  0.1410 / 0.1125   fark -0.0285
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       794         0.034         0.060   +0.026
  0.1-0.2       527         0.150         0.190   +0.039
  0.2-0.3       421         0.247         0.257   +0.010
  0.3-0.4       236         0.345         0.216   -0.128
  0.4-0.5        89         0.439         0.303   -0.135
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4467)
  işlem sayısı                    4467
  kazanan                         1727  (%39)
  ort. İDDİA EDİLEN edge       +17.32p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.87p   ±0.6p  %95 [-0.3p, +2.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4530.82 $
  PnL fee ÖNCESİ             +25507.39 $
  PnL fee SONRASI            +20976.57 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11238.42 $   %90 aralık [-19258.55, -2704.50]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1306 (model 0.1321)

  bizim (fee sonrası)            +20976.57 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
