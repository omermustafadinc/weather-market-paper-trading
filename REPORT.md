========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-30T20:56:18.268330Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          59424
  orderbook seviyesi     3174475
  tahmin snapshot          39564
  karar                    12276
  simüle fill               3207
  çözümlenmiş kova          1410

## Brier skoru  (düşük = iyi, 1368 kova)
  model                  0.1315
  piyasa (mid)           0.1338   n=1368
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0023  ±0.0036  %95 [-0.0048, +0.0093]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=198  0.1340 / 0.2093   fark +0.0753
    CHI   n=192  0.1298 / 0.1152   fark -0.0146
    DEN   n=198  0.1447 / 0.2005   fark +0.0559
    LAX   n=192  0.1246 / 0.0976   fark -0.0270
    MIA   n=198  0.1393 / 0.1123   fark -0.0269
    NY    n=198  0.1086 / 0.0856   fark -0.0229
    PHL   n=192  0.1398 / 0.1139   fark -0.0259
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       500         0.034         0.056   +0.022
  0.1-0.2       356         0.151         0.194   +0.043
  0.2-0.3       293         0.247         0.246   -0.001
  0.3-0.4       146         0.346         0.233   -0.113
  0.4-0.5        56         0.435         0.304   -0.132
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3149)
  işlem sayısı                    3149
  kazanan                         1259  (%40)
  ort. İDDİA EDİLEN edge       +16.00p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.76p   ±0.7p  %95 [+0.3p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3152.60 $
  PnL fee ÖNCESİ             +24521.74 $
  PnL fee SONRASI            +21369.14 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7909.26 $   %90 aralık [-14862.38, -1286.87]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1338 (model 0.1315)

  bizim (fee sonrası)            +21369.14 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
