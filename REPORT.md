========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-03T13:09:30.001446Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          62820
  orderbook seviyesi     3359204
  tahmin snapshot          42084
  karar                    12924
  simüle fill               3364
  çözümlenmiş kova          1524

## Brier skoru  (düşük = iyi, 1482 kova)
  model                  0.1309
  piyasa (mid)           0.1336   n=1482
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0027  ±0.0035  %95 [-0.0041, +0.0095]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=216  0.1305 / 0.2038   fark +0.0733
    CHI   n=210  0.1288 / 0.1135   fark -0.0153
    DEN   n=216  0.1457 / 0.2013   fark +0.0556
    LAX   n=210  0.1274 / 0.0973   fark -0.0301
    MIA   n=210  0.1374 / 0.1121   fark -0.0253
    NY    n=210  0.1084 / 0.0870   fark -0.0214
    PHL   n=210  0.1376 / 0.1162   fark -0.0214
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       548         0.034         0.055   +0.021
  0.1-0.2       375         0.151         0.189   +0.038
  0.2-0.3       319         0.246         0.248   +0.002
  0.3-0.4       158         0.345         0.247   -0.098
  0.4-0.5        64         0.435         0.312   -0.122
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3289)
  işlem sayısı                    3289
  kazanan                         1320  (%40)
  ort. İDDİA EDİLEN edge       +16.00p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.78p   ±0.7p  %95 [+0.4p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3283.75 $
  PnL fee ÖNCESİ             +26802.05 $
  PnL fee SONRASI            +23518.30 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8741.96 $   %90 aralık [-16102.00, -2209.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1336 (model 0.1309)

  bizim (fee sonrası)            +23518.30 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
