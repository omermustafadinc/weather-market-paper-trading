========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-07T17:12:27.818514Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         113118
  orderbook seviyesi     6021925
  tahmin snapshot          75285
  karar                    23412
  simüle fill               6044
  çözümlenmiş kova          2994

## Brier skoru  (düşük = iyi, 2910 kova)
  model                  0.1302
  piyasa (mid)           0.1260   n=2910
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0042  ±0.0028  %95 [-0.0098, +0.0014]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=420  0.1226 / 0.1975   fark +0.0749
    CHI   n=414  0.1368 / 0.1067   fark -0.0301
    DEN   n=420  0.1389 / 0.1912   fark +0.0522
    LAX   n=414  0.1194 / 0.0857   fark -0.0337
    MIA   n=414  0.1368 / 0.1044   fark -0.0324
    NY    n=414  0.1089 / 0.0925   fark -0.0164
    PHL   n=414  0.1477 / 0.1019   fark -0.0458
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1162         0.032         0.052   +0.019
  0.1-0.2       670         0.150         0.191   +0.041
  0.2-0.3       541         0.247         0.266   +0.019
  0.3-0.4       341         0.345         0.243   -0.102
  0.4-0.5       136         0.440         0.316   -0.124
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5980)
  işlem sayısı                    5980
  kazanan                         2351  (%39)
  ort. İDDİA EDİLEN edge       +18.27p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.01p   ±0.5p  %95 [+1.0p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6107.58 $
  PnL fee ÖNCESİ             +50690.58 $
  PnL fee SONRASI            +44583.00 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15118.68 $   %90 aralık [-24997.59, -6128.30]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1260 (model 0.1302)

  bizim (fee sonrası)            +44583.00 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
