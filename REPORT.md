========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-15T00:50:14.618699Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         121422
  orderbook seviyesi     6444790
  tahmin snapshot          81081
  karar                    25170
  simüle fill               6478
  çözümlenmiş kova          3312

## Brier skoru  (düşük = iyi, 3228 kova)
  model                  0.1314
  piyasa (mid)           0.1245   n=3228
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0069  ±0.0028  %95 [-0.0123, -0.0015]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=462  0.1205 / 0.1933   fark +0.0728
    CHI   n=462  0.1400 / 0.1063   fark -0.0337
    DEN   n=462  0.1406 / 0.1919   fark +0.0513
    LAX   n=456  0.1204 / 0.0856   fark -0.0348
    MIA   n=462  0.1372 / 0.1033   fark -0.0339
    NY    n=462  0.1124 / 0.0924   fark -0.0200
    PHL   n=462  0.1485 / 0.0980   fark -0.0506
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1314         0.031         0.053   +0.021
  0.1-0.2       724         0.150         0.198   +0.047
  0.2-0.3       586         0.247         0.270   +0.023
  0.3-0.4       368         0.345         0.236   -0.109
  0.4-0.5       161         0.440         0.311   -0.129
  0.5-0.6        47         0.550         0.362   -0.188
  0.6-0.7        18         0.635         0.389   -0.246
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6418)
  işlem sayısı                    6418
  kazanan                         2527  (%39)
  ort. İDDİA EDİLEN edge       +18.69p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.94p   ±0.5p  %95 [+0.9p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6548.21 $
  PnL fee ÖNCESİ             +52292.08 $
  PnL fee SONRASI            +45743.87 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15521.25 $   %90 aralık [-24701.78, -4682.61]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1245 (model 0.1314)

  bizim (fee sonrası)            +45743.87 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
