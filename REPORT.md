========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-13T15:10:05.749676Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          29898
  orderbook seviyesi     1571165
  tahmin snapshot          20916
  karar                     5994
  simüle fill               1562
  çözümlenmiş kova           684

## Brier skoru  (düşük = iyi, 642 kova)
  model                  0.1272
  piyasa (mid)           0.1325   n=642
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0053  ±0.0047  %95 [-0.0038, +0.0145]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 96  0.1551 / 0.2104   fark +0.0554
    CHI   n= 90  0.1264 / 0.1047   fark -0.0217
    DEN   n= 96  0.1464 / 0.2104   fark +0.0639
    LAX   n= 90  0.1016 / 0.0910   fark -0.0106
    MIA   n= 90  0.1243 / 0.1161   fark -0.0082
    NY    n= 90  0.1049 / 0.0826   fark -0.0223
    PHL   n= 90  0.1286 / 0.1021   fark -0.0265
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       240         0.033         0.037   +0.005
  0.1-0.2       155         0.149         0.200   +0.051
  0.2-0.3       145         0.245         0.276   +0.031
  0.3-0.4        65         0.344         0.231   -0.113
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1445)
  işlem sayısı                    1445
  kazanan                          582  (%40)
  ort. İDDİA EDİLEN edge       +14.78p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.61p   ±1.1p  %95 [-0.5p, +3.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1472.26 $
  PnL fee ÖNCESİ              +6490.18 $
  PnL fee SONRASI             +5017.92 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3024.31 $   %90 aralık [-8263.81, +1499.14]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1325 (model 0.1272)

  bizim (fee sonrası)             +5017.92 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
