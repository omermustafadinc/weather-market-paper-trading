========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-16T00:12:06.907523Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         122466
  orderbook seviyesi     6499409
  tahmin snapshot          81963
  karar                    25356
  simüle fill               6527
  çözümlenmiş kova          3354

## Brier skoru  (düşük = iyi, 3270 kova)
  model                  0.1318
  piyasa (mid)           0.1243   n=3270
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0074  ±0.0028  %95 [-0.0128, -0.0020]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=468  0.1200 / 0.1910   fark +0.0710
    CHI   n=468  0.1409 / 0.1077   fark -0.0333
    DEN   n=468  0.1412 / 0.1921   fark +0.0510
    LAX   n=462  0.1198 / 0.0871   fark -0.0327
    MIA   n=468  0.1379 / 0.1034   fark -0.0346
    NY    n=468  0.1128 / 0.0916   fark -0.0212
    PHL   n=468  0.1496 / 0.0971   fark -0.0525
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1333         0.031         0.055   +0.023
  0.1-0.2       734         0.150         0.195   +0.045
  0.2-0.3       589         0.247         0.268   +0.022
  0.3-0.4       373         0.345         0.239   -0.107
  0.4-0.5       163         0.440         0.313   -0.127
  0.5-0.6        48         0.549         0.354   -0.194
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6480)
  işlem sayısı                    6480
  kazanan                         2546  (%39)
  ort. İDDİA EDİLEN edge       +18.81p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.83p   ±0.5p  %95 [+0.8p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6610.58 $
  PnL fee ÖNCESİ             +51646.44 $
  PnL fee SONRASI            +45035.86 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15867.72 $   %90 aralık [-26183.04, -6381.87]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1243 (model 0.1318)

  bizim (fee sonrası)            +45035.86 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
