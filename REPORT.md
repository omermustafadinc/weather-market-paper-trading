========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-03T10:02:40.426796Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         108078
  orderbook seviyesi     5767490
  tahmin snapshot          72009
  karar                    22320
  simüle fill               5768
  çözümlenmiş kova          2814

## Brier skoru  (düşük = iyi, 2730 kova)
  model                  0.1295
  piyasa (mid)           0.1250   n=2730
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0045  ±0.0029  %95 [-0.0103, +0.0012]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=390  0.1209 / 0.1969   fark +0.0760
    CHI   n=390  0.1381 / 0.1045   fark -0.0335
    DEN   n=390  0.1395 / 0.1900   fark +0.0505
    LAX   n=390  0.1199 / 0.0857   fark -0.0342
    MIA   n=390  0.1361 / 0.1027   fark -0.0334
    NY    n=390  0.1055 / 0.0903   fark -0.0152
    PHL   n=390  0.1466 / 0.1047   fark -0.0419
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1080         0.032         0.053   +0.021
  0.1-0.2       643         0.150         0.184   +0.033
  0.2-0.3       505         0.247         0.265   +0.018
  0.3-0.4       324         0.345         0.247   -0.098
  0.4-0.5       122         0.439         0.336   -0.103
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
  (b) rastgele işlem (ort.)      -14393.82 $   %90 aralık [-22511.35, -3654.67]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1250 (model 0.1295)

  bizim (fee sonrası)            +42157.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
