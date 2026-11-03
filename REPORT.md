========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-03T02:30:30.319889Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         107910
  orderbook seviyesi     5758116
  tahmin snapshot          71883
  karar                    22320
  simüle fill               5768
  çözümlenmiş kova          2808

## Brier skoru  (düşük = iyi, 2724 kova)
  model                  0.1295
  piyasa (mid)           0.1252   n=2724
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0043  ±0.0029  %95 [-0.0101, +0.0014]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=390  0.1209 / 0.1969   fark +0.0760
    CHI   n=390  0.1381 / 0.1045   fark -0.0335
    DEN   n=390  0.1395 / 0.1900   fark +0.0505
    LAX   n=384  0.1197 / 0.0865   fark -0.0332
    MIA   n=390  0.1361 / 0.1027   fark -0.0334
    NY    n=390  0.1055 / 0.0903   fark -0.0152
    PHL   n=390  0.1466 / 0.1047   fark -0.0419
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1077         0.032         0.053   +0.021
  0.1-0.2       642         0.150         0.184   +0.034
  0.2-0.3       504         0.247         0.264   +0.017
  0.3-0.4       324         0.345         0.247   -0.098
  0.4-0.5       121         0.439         0.339   -0.100
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        10         0.635         0.500   -0.135
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5728)
  işlem sayısı                    5728
  kazanan                         2248  (%39)
  ort. İDDİA EDİLEN edge       +18.13p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.77p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5853.11 $
  PnL fee ÖNCESİ             +48010.80 $
  PnL fee SONRASI            +42157.69 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15501.47 $   %90 aralık [-25232.45, -7742.56]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1252 (model 0.1295)

  bizim (fee sonrası)            +42157.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
