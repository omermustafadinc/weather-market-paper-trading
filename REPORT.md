========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-12T21:23:51.615589Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          28506
  orderbook seviyesi     1498794
  tahmin snapshot          19782
  karar                     5718
  simüle fill               1482
  çözümlenmiş kova           654

## Brier skoru  (düşük = iyi, 612 kova)
  model                  0.1261
  piyasa (mid)           0.1317   n=612
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0056  ±0.0048  %95 [-0.0038, +0.0150]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 90  0.1553 / 0.2098   fark +0.0544
    CHI   n= 84  0.1208 / 0.1022   fark -0.0186
    DEN   n= 90  0.1448 / 0.2102   fark +0.0654
    LAX   n= 84  0.0989 / 0.0902   fark -0.0087
    MIA   n= 90  0.1243 / 0.1161   fark -0.0082
    NY    n= 90  0.1049 / 0.0826   fark -0.0223
    PHL   n= 84  0.1316 / 0.1040   fark -0.0275
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       229         0.033         0.035   +0.001
  0.1-0.2       149         0.149         0.195   +0.045
  0.2-0.3       139         0.245         0.281   +0.035
  0.3-0.4        60         0.344         0.233   -0.111
  0.4-0.5        23         0.436         0.217   -0.218
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1373)
  işlem sayısı                    1373
  kazanan                          556  (%40)
  ort. İDDİA EDİLEN edge       +14.63p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.85p   ±1.1p  %95 [-0.3p, +4.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1396.78 $
  PnL fee ÖNCESİ              +6625.51 $
  PnL fee SONRASI             +5228.73 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2413.33 $   %90 aralık [-7177.66, +2133.40]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1317 (model 0.1261)

  bizim (fee sonrası)             +5228.73 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
