========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-01T15:04:33.576622Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         106062
  orderbook seviyesi     5663396
  tahmin snapshot          70623
  karar                    21900
  simüle fill               5665
  çözümlenmiş kova          2742

## Brier skoru  (düşük = iyi, 2658 kova)
  model                  0.1301
  piyasa (mid)           0.1252   n=2658
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0049  ±0.0030  %95 [-0.0107, +0.0009]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=384  0.1209 / 0.1967   fark +0.0758
    CHI   n=378  0.1396 / 0.1048   fark -0.0348
    DEN   n=384  0.1404 / 0.1900   fark +0.0496
    LAX   n=378  0.1203 / 0.0872   fark -0.0331
    MIA   n=378  0.1360 / 0.1016   fark -0.0344
    NY    n=378  0.1054 / 0.0902   fark -0.0152
    PHL   n=378  0.1479 / 0.1038   fark -0.0441
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1046         0.032         0.054   +0.021
  0.1-0.2       629         0.150         0.188   +0.038
  0.2-0.3       500         0.247         0.262   +0.015
  0.3-0.4       313         0.345         0.240   -0.106
  0.4-0.5       116         0.439         0.336   -0.103
  0.5-0.6        38         0.547         0.342   -0.204
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5602)
  işlem sayısı                    5602
  kazanan                         2198  (%39)
  ort. İDDİA EDİLEN edge       +18.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.6p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5736.40 $
  PnL fee ÖNCESİ             +47036.02 $
  PnL fee SONRASI            +41299.62 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15052.59 $   %90 aralık [-24862.04, -4882.00]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1252 (model 0.1301)

  bizim (fee sonrası)            +41299.62 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
