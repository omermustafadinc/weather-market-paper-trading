========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-07T11:00:03.579074Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         112782
  orderbook seviyesi     6005173
  tahmin snapshot          75033
  karar                    23328
  simüle fill               6024
  çözümlenmiş kova          2982

## Brier skoru  (düşük = iyi, 2898 kova)
  model                  0.1300
  piyasa (mid)           0.1257   n=2898
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0043  ±0.0029  %95 [-0.0098, +0.0013]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=414  0.1226 / 0.1983   fark +0.0758
    CHI   n=414  0.1368 / 0.1067   fark -0.0301
    DEN   n=414  0.1377 / 0.1905   fark +0.0528
    LAX   n=414  0.1194 / 0.0857   fark -0.0337
    MIA   n=414  0.1368 / 0.1044   fark -0.0324
    NY    n=414  0.1089 / 0.0925   fark -0.0164
    PHL   n=414  0.1477 / 0.1019   fark -0.0458
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1156         0.032         0.051   +0.019
  0.1-0.2       669         0.150         0.191   +0.041
  0.2-0.3       538         0.247         0.266   +0.019
  0.3-0.4       341         0.345         0.243   -0.102
  0.4-0.5       134         0.439         0.321   -0.118
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5961)
  işlem sayısı                    5961
  kazanan                         2344  (%39)
  ort. İDDİA EDİLEN edge       +18.27p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.03p   ±0.5p  %95 [+1.0p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6091.44 $
  PnL fee ÖNCESİ             +50837.54 $
  PnL fee SONRASI            +44746.10 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14473.68 $   %90 aralık [-23047.83, -3713.74]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1257 (model 0.1300)

  bizim (fee sonrası)            +44746.10 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
