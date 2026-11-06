========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-06T19:01:20.047655Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         111942
  orderbook seviyesi     5963656
  tahmin snapshot          74655
  karar                    23160
  simüle fill               5983
  çözümlenmiş kova          2952

## Brier skoru  (düşük = iyi, 2868 kova)
  model                  0.1300
  piyasa (mid)           0.1259   n=2868
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0041  ±0.0029  %95 [-0.0097, +0.0015]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=414  0.1226 / 0.1983   fark +0.0758
    CHI   n=408  0.1377 / 0.1069   fark -0.0308
    DEN   n=414  0.1377 / 0.1905   fark +0.0528
    LAX   n=408  0.1195 / 0.0845   fark -0.0350
    MIA   n=408  0.1368 / 0.1057   fark -0.0311
    NY    n=408  0.1080 / 0.0908   fark -0.0172
    PHL   n=408  0.1478 / 0.1027   fark -0.0451
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1143         0.032         0.052   +0.019
  0.1-0.2       664         0.150         0.191   +0.041
  0.2-0.3       533         0.247         0.265   +0.018
  0.3-0.4       337         0.345         0.243   -0.102
  0.4-0.5       131         0.439         0.321   -0.119
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5912)
  işlem sayısı                    5912
  kazanan                         2323  (%39)
  ort. İDDİA EDİLEN edge       +18.25p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.97p   ±0.5p  %95 [+0.9p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6040.75 $
  PnL fee ÖNCESİ             +50791.71 $
  PnL fee SONRASI            +44750.96 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15168.92 $   %90 aralık [-24713.01, -6127.74]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1259 (model 0.1300)

  bizim (fee sonrası)            +44750.96 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
