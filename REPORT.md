========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-15T15:28:53.987736Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          78312
  orderbook seviyesi     4180649
  tahmin snapshot          51849
  karar                    16092
  simüle fill               4177
  çözümlenmiş kova          2028

## Brier skoru  (düşük = iyi, 1944 kova)
  model                  0.1325
  piyasa (mid)           0.1317   n=1944
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0008  ±0.0032  %95 [-0.0070, +0.0054]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=282  0.1283 / 0.2059   fark +0.0777
    CHI   n=276  0.1382 / 0.1086   fark -0.0295
    DEN   n=282  0.1506 / 0.1991   fark +0.0485
    LAX   n=276  0.1250 / 0.0947   fark -0.0303
    MIA   n=276  0.1349 / 0.1051   fark -0.0298
    NY    n=276  0.1096 / 0.0915   fark -0.0181
    PHL   n=276  0.1402 / 0.1136   fark -0.0266
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       732         0.034         0.061   +0.028
  0.1-0.2       485         0.151         0.190   +0.039
  0.2-0.3       405         0.247         0.252   +0.005
  0.3-0.4       212         0.345         0.222   -0.123
  0.4-0.5        78         0.438         0.295   -0.143
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4075)
  işlem sayısı                    4075
  kazanan                         1600  (%39)
  ort. İDDİA EDİLEN edge       +16.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.96p   ±0.6p  %95 [-0.3p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4112.10 $
  PnL fee ÖNCESİ             +25773.69 $
  PnL fee SONRASI            +21661.59 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9700.53 $   %90 aralık [-17199.36, -1371.62]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1317 (model 0.1325)

  bizim (fee sonrası)            +21661.59 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
