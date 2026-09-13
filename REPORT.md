========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-13T05:56:30.965476Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          29394
  orderbook seviyesi     1544048
  tahmin snapshot          20412
  karar                     5910
  simüle fill               1540
  çözümlenmiş kova           672

## Brier skoru  (düşük = iyi, 630 kova)
  model                  0.1266
  piyasa (mid)           0.1309   n=630
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0044  ±0.0047  %95 [-0.0049, +0.0136]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 90  0.1553 / 0.2098   fark +0.0544
    CHI   n= 90  0.1264 / 0.1047   fark -0.0217
    DEN   n= 90  0.1448 / 0.2102   fark +0.0654
    LAX   n= 90  0.1016 / 0.0910   fark -0.0106
    MIA   n= 90  0.1243 / 0.1161   fark -0.0082
    NY    n= 90  0.1049 / 0.0826   fark -0.0223
    PHL   n= 90  0.1286 / 0.1021   fark -0.0265
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       236         0.033         0.038   +0.005
  0.1-0.2       152         0.149         0.191   +0.042
  0.2-0.3       143         0.245         0.280   +0.034
  0.3-0.4        62         0.344         0.242   -0.102
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1417)
  işlem sayısı                    1417
  kazanan                          565  (%40)
  ort. İDDİA EDİLEN edge       +14.73p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.19p   ±1.1p  %95 [-0.9p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1442.46 $
  PnL fee ÖNCESİ              +5954.65 $
  PnL fee SONRASI             +4512.19 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2934.86 $   %90 aralık [-6914.50, +1215.91]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1309 (model 0.1266)

  bizim (fee sonrası)             +4512.19 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
