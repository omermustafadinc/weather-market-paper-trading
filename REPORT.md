========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-25T23:15:57.861738Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          52176
  orderbook seviyesi     2792854
  tahmin snapshot          34650
  karar                    10710
  simüle fill               2808
  çözümlenmiş kova          1212

## Brier skoru  (düşük = iyi, 1170 kova)
  model                  0.1314
  piyasa (mid)           0.1351   n=1170
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0036  ±0.0037  %95 [-0.0037, +0.0110]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=168  0.1394 / 0.2111   fark +0.0718
    CHI   n=168  0.1229 / 0.1152   fark -0.0077
    DEN   n=168  0.1489 / 0.2058   fark +0.0569
    LAX   n=162  0.1239 / 0.0977   fark -0.0263
    MIA   n=168  0.1375 / 0.1152   fark -0.0223
    NY    n=168  0.1099 / 0.0898   fark -0.0201
    PHL   n=168  0.1372 / 0.1092   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       423         0.035         0.054   +0.020
  0.1-0.2       309         0.151         0.191   +0.040
  0.2-0.3       252         0.247         0.254   +0.007
  0.3-0.4       128         0.345         0.219   -0.126
  0.4-0.5        46         0.435         0.304   -0.130
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2737)
  işlem sayısı                    2737
  kazanan                         1130  (%41)
  ort. İDDİA EDİLEN edge       +15.35p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.93p   ±0.8p  %95 [+1.4p, +4.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2743.42 $
  PnL fee ÖNCESİ             +25084.02 $
  PnL fee SONRASI            +22340.60 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7507.35 $   %90 aralık [-13935.94, -679.21]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1351 (model 0.1314)

  bizim (fee sonrası)            +22340.60 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
