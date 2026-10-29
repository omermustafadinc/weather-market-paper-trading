========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-29T21:58:05.206434Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         102366
  orderbook seviyesi     5464914
  tahmin snapshot          68355
  karar                    21144
  simüle fill               5475
  çözümlenmiş kova          2640

## Brier skoru  (düşük = iyi, 2556 kova)
  model                  0.1304
  piyasa (mid)           0.1267   n=2556
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0037  ±0.0030  %95 [-0.0096, +0.0022]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=366  0.1227 / 0.2017   fark +0.0789
    CHI   n=366  0.1406 / 0.1047   fark -0.0359
    DEN   n=366  0.1406 / 0.1904   fark +0.0498
    LAX   n=360  0.1210 / 0.0885   fark -0.0326
    MIA   n=366  0.1351 / 0.1040   fark -0.0311
    NY    n=366  0.1061 / 0.0911   fark -0.0150
    PHL   n=366  0.1464 / 0.1059   fark -0.0405
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1001         0.032         0.055   +0.023
  0.1-0.2       607         0.150         0.189   +0.040
  0.2-0.3       485         0.247         0.260   +0.013
  0.3-0.4       300         0.345         0.233   -0.112
  0.4-0.5       113         0.439         0.327   -0.111
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5432)
  işlem sayısı                    5432
  kazanan                         2125  (%39)
  ort. İDDİA EDİLEN edge       +18.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.70p   ±0.6p  %95 [+0.6p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5569.86 $
  PnL fee ÖNCESİ             +44766.33 $
  PnL fee SONRASI            +39196.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13751.86 $   %90 aralık [-23696.21, -4374.87]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1267 (model 0.1304)

  bizim (fee sonrası)            +39196.47 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
