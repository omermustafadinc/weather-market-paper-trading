========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-03T07:40:58.822597Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          62652
  orderbook seviyesi     3348581
  tahmin snapshot          41832
  karar                    12924
  simüle fill               3364
  çözümlenmiş kova          1512

## Brier skoru  (düşük = iyi, 1470 kova)
  model                  0.1311
  piyasa (mid)           0.1330   n=1470
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0019  ±0.0035  %95 [-0.0048, +0.0087]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=210  0.1317 / 0.2041   fark +0.0725
    CHI   n=210  0.1288 / 0.1135   fark -0.0153
    DEN   n=210  0.1461 / 0.2007   fark +0.0546
    LAX   n=210  0.1274 / 0.0973   fark -0.0301
    MIA   n=210  0.1374 / 0.1121   fark -0.0253
    NY    n=210  0.1084 / 0.0870   fark -0.0214
    PHL   n=210  0.1376 / 0.1162   fark -0.0214
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       543         0.034         0.055   +0.021
  0.1-0.2       374         0.152         0.190   +0.038
  0.2-0.3       316         0.246         0.247   +0.001
  0.3-0.4       155         0.345         0.245   -0.100
  0.4-0.5        64         0.435         0.312   -0.122
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3280)
  işlem sayısı                    3280
  kazanan                         1313  (%40)
  ort. İDDİA EDİLEN edge       +15.97p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.60p   ±0.7p  %95 [+0.2p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3266.53 $
  PnL fee ÖNCESİ             +24861.16 $
  PnL fee SONRASI            +21594.63 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8509.74 $   %90 aralık [-15611.86, -973.97]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1311)

  bizim (fee sonrası)            +21594.63 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
