========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-01T01:36:12.488865Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         105726
  orderbook seviyesi     5642713
  tahmin snapshot          70371
  karar                    21900
  simüle fill               5665
  çözümlenmiş kova          2724

## Brier skoru  (düşük = iyi, 2640 kova)
  model                  0.1300
  piyasa (mid)           0.1251   n=2640
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0050  ±0.0030  %95 [-0.0108, +0.0009]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=378  0.1212 / 0.1966   fark +0.0754
    CHI   n=378  0.1396 / 0.1048   fark -0.0348
    DEN   n=378  0.1395 / 0.1899   fark +0.0504
    LAX   n=372  0.1204 / 0.0880   fark -0.0324
    MIA   n=378  0.1360 / 0.1016   fark -0.0344
    NY    n=378  0.1054 / 0.0902   fark -0.0152
    PHL   n=378  0.1479 / 0.1038   fark -0.0441
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1038         0.032         0.053   +0.021
  0.1-0.2       626         0.150         0.188   +0.039
  0.2-0.3       498         0.247         0.263   +0.016
  0.3-0.4       308         0.346         0.237   -0.108
  0.4-0.5       116         0.439         0.336   -0.103
  0.5-0.6        38         0.547         0.342   -0.204
  0.6-0.7         9         0.637         0.556   -0.082
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5578)
  işlem sayısı                    5578
  kazanan                         2183  (%39)
  ort. İDDİA EDİLEN edge       +18.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.62p   ±0.6p  %95 [+0.5p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5707.71 $
  PnL fee ÖNCESİ             +44467.86 $
  PnL fee SONRASI            +38760.15 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13851.20 $   %90 aralık [-23491.94, -5338.31]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1251 (model 0.1300)

  bizim (fee sonrası)            +38760.15 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
