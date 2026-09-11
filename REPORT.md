========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-11T20:35:16.972493Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          26250
  orderbook seviyesi     1387344
  tahmin snapshot          18270
  karar                     5262
  simüle fill               1361
  çözümlenmiş kova           612

## Brier skoru  (düşük = iyi, 570 kova)
  model                  0.1254
  piyasa (mid)           0.1302   n=570
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0051  %95 [-0.0052, +0.0147]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 84  0.1542 / 0.2086   fark +0.0544
    CHI   n= 78  0.1249 / 0.1047   fark -0.0201
    DEN   n= 84  0.1447 / 0.2124   fark +0.0676
    LAX   n= 78  0.0948 / 0.0849   fark -0.0099
    MIA   n= 84  0.1217 / 0.1124   fark -0.0093
    NY    n= 84  0.1055 / 0.0838   fark -0.0217
    PHL   n= 78  0.1304 / 0.0971   fark -0.0333
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       216         0.033         0.037   +0.004
  0.1-0.2       135         0.149         0.185   +0.036
  0.2-0.3       130         0.246         0.292   +0.046
  0.3-0.4        57         0.346         0.228   -0.117
  0.4-0.5        21         0.436         0.190   -0.246
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1271)
  işlem sayısı                    1271
  kazanan                          519  (%41)
  ort. İDDİA EDİLEN edge       +14.73p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.77p   ±1.1p  %95 [-0.4p, +4.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1287.63 $
  PnL fee ÖNCESİ              +4870.20 $
  PnL fee SONRASI             +3582.57 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2430.32 $   %90 aralık [-6581.88, +1339.95]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1302 (model 0.1254)

  bizim (fee sonrası)             +3582.57 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
