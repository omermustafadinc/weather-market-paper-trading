========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-08T12:51:40.652214Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         114198
  orderbook seviyesi     6077761
  tahmin snapshot          76041
  karar                    23616
  simüle fill               6102
  çözümlenmiş kova          3024

## Brier skoru  (düşük = iyi, 2940 kova)
  model                  0.1303
  piyasa (mid)           0.1252   n=2940
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0051  ±0.0028  %95 [-0.0107, +0.0004]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=420  0.1226 / 0.1975   fark +0.0749
    CHI   n=420  0.1373 / 0.1059   fark -0.0313
    DEN   n=420  0.1389 / 0.1912   fark +0.0522
    LAX   n=420  0.1199 / 0.0855   fark -0.0343
    MIA   n=420  0.1371 / 0.1031   fark -0.0340
    NY    n=420  0.1088 / 0.0923   fark -0.0165
    PHL   n=420  0.1478 / 0.1009   fark -0.0469
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1177         0.032         0.051   +0.019
  0.1-0.2       674         0.150         0.194   +0.044
  0.2-0.3       543         0.247         0.267   +0.020
  0.3-0.4       346         0.345         0.243   -0.102
  0.4-0.5       140         0.440         0.307   -0.133
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6024)
  işlem sayısı                    6024
  kazanan                         2359  (%39)
  ort. İDDİA EDİLEN edge       +18.32p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.85p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6152.30 $
  PnL fee ÖNCESİ             +49902.76 $
  PnL fee SONRASI            +43750.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15231.85 $   %90 aralık [-24397.89, -6768.47]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1252 (model 0.1303)

  bizim (fee sonrası)            +43750.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
