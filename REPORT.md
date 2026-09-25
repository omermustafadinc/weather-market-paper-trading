========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-25T05:59:45.336320Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          51084
  orderbook seviyesi     2735686
  tahmin snapshot          34020
  karar                    10458
  simüle fill               2743
  çözümlenmiş kova          1176

## Brier skoru  (düşük = iyi, 1134 kova)
  model                  0.1311
  piyasa (mid)           0.1348   n=1134
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0036  ±0.0037  %95 [-0.0037, +0.0109]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=162  0.1410 / 0.2114   fark +0.0705
    CHI   n=162  0.1249 / 0.1125   fark -0.0124
    DEN   n=162  0.1485 / 0.2057   fark +0.0572
    LAX   n=162  0.1239 / 0.0977   fark -0.0263
    MIA   n=162  0.1346 / 0.1164   fark -0.0183
    NY    n=162  0.1090 / 0.0894   fark -0.0196
    PHL   n=162  0.1361 / 0.1104   fark -0.0257
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       410         0.035         0.054   +0.019
  0.1-0.2       298         0.151         0.188   +0.037
  0.2-0.3       246         0.246         0.260   +0.014
  0.3-0.4       124         0.344         0.218   -0.127
  0.4-0.5        44         0.434         0.295   -0.139
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2644)
  işlem sayısı                    2644
  kazanan                         1083  (%41)
  ort. İDDİA EDİLEN edge       +15.28p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.61p   ±0.8p  %95 [+1.0p, +4.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2651.95 $
  PnL fee ÖNCESİ             +23547.46 $
  PnL fee SONRASI            +20895.51 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6936.69 $   %90 aralık [-12687.41, -1238.54]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1348 (model 0.1311)

  bizim (fee sonrası)            +20895.51 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
