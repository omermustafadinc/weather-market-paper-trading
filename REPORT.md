========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-04T23:28:46.041227Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         109926
  orderbook seviyesi     5860076
  tahmin snapshot          73143
  karar                    22740
  simüle fill               5877
  çözümlenmiş kova          2892

## Brier skoru  (düşük = iyi, 2808 kova)
  model                  0.1296
  piyasa (mid)           0.1251   n=2808
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0045  ±0.0029  %95 [-0.0102, +0.0012]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=402  0.1214 / 0.1979   fark +0.0765
    CHI   n=402  0.1383 / 0.1057   fark -0.0326
    DEN   n=402  0.1366 / 0.1896   fark +0.0530
    LAX   n=396  0.1195 / 0.0850   fark -0.0346
    MIA   n=402  0.1374 / 0.1041   fark -0.0332
    NY    n=402  0.1066 / 0.0903   fark -0.0164
    PHL   n=402  0.1471 / 0.1026   fark -0.0444
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1115         0.032         0.052   +0.020
  0.1-0.2       656         0.150         0.188   +0.038
  0.2-0.3       520         0.247         0.265   +0.018
  0.3-0.4       333         0.345         0.243   -0.102
  0.4-0.5       126         0.439         0.325   -0.114
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        12         0.631         0.583   -0.047
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5833)
  işlem sayısı                    5833
  kazanan                         2276  (%39)
  ort. İDDİA EDİLEN edge       +18.16p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.62p   ±0.5p  %95 [+0.6p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5959.19 $
  PnL fee ÖNCESİ             +47593.90 $
  PnL fee SONRASI            +41634.71 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14840.97 $   %90 aralık [-24901.24, -5547.45]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1251 (model 0.1296)

  bizim (fee sonrası)            +41634.71 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
