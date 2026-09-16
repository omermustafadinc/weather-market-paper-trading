========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-16T22:35:33.848267Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          35946
  orderbook seviyesi     1914110
  tahmin snapshot          24444
  karar                     7296
  simüle fill               1907
  çözümlenmiş kova           834

## Brier skoru  (düşük = iyi, 792 kova)
  model                  0.1300
  piyasa (mid)           0.1325   n=792
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0025  ±0.0042  %95 [-0.0058, +0.0108]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=114  0.1554 / 0.2117   fark +0.0563
    CHI   n=114  0.1311 / 0.1116   fark -0.0194
    DEN   n=114  0.1464 / 0.2095   fark +0.0631
    LAX   n=108  0.1081 / 0.0959   fark -0.0123
    MIA   n=114  0.1288 / 0.1121   fark -0.0167
    NY    n=114  0.1073 / 0.0841   fark -0.0233
    PHL   n=114  0.1314 / 0.1004   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       289         0.034         0.045   +0.011
  0.1-0.2       201         0.149         0.199   +0.050
  0.2-0.3       175         0.245         0.269   +0.024
  0.3-0.4        86         0.344         0.221   -0.123
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1834)
  işlem sayısı                    1834
  kazanan                          715  (%39)
  ort. İDDİA EDİLEN edge       +14.96p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.72p   ±1.0p  %95 [-1.1p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1857.48 $
  PnL fee ÖNCESİ              +8862.78 $
  PnL fee SONRASI             +7005.30 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4076.32 $   %90 aralık [-8716.33, +1042.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1325 (model 0.1300)

  bizim (fee sonrası)             +7005.30 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
