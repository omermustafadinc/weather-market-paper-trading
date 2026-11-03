========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-03T22:58:54.976451Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         108750
  orderbook seviyesi     5800736
  tahmin snapshot          72261
  karar                    22488
  simüle fill               5811
  çözümlenmiş kova          2850

## Brier skoru  (düşük = iyi, 2766 kova)
  model                  0.1296
  piyasa (mid)           0.1250   n=2766
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0046  ±0.0029  %95 [-0.0103, +0.0011]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=396  0.1211 / 0.1974   fark +0.0763
    CHI   n=396  0.1379 / 0.1043   fark -0.0336
    DEN   n=396  0.1381 / 0.1895   fark +0.0514
    LAX   n=390  0.1199 / 0.0857   fark -0.0342
    MIA   n=396  0.1371 / 0.1043   fark -0.0328
    NY    n=396  0.1058 / 0.0897   fark -0.0161
    PHL   n=396  0.1472 / 0.1037   fark -0.0435
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1097         0.032         0.053   +0.021
  0.1-0.2       647         0.150         0.184   +0.034
  0.2-0.3       513         0.247         0.267   +0.020
  0.3-0.4       328         0.345         0.244   -0.101
  0.4-0.5       124         0.439         0.331   -0.109
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        11         0.633         0.545   -0.088
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5768)
  işlem sayısı                    5768
  kazanan                         2258  (%39)
  ort. İDDİA EDİLEN edge       +18.15p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.66p   ±0.5p  %95 [+0.6p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5890.08 $
  PnL fee ÖNCESİ             +48160.36 $
  PnL fee SONRASI            +42270.28 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14745.79 $   %90 aralık [-23499.59, -6254.12]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1250 (model 0.1296)

  bizim (fee sonrası)            +42270.28 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
