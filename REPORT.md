========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-27T22:17:59.308826Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         132924
  orderbook seviyesi     7033657
  tahmin snapshot          88641
  karar                    27480
  simüle fill               7047
  çözümlenmiş kova          3852

## Brier skoru  (düşük = iyi, 3732 kova)
  model                  0.1327
  piyasa (mid)           0.1239   n=3732
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0087  ±0.0026  %95 [-0.0139, -0.0035]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=540  0.1209 / 0.1921   fark +0.0712
    CHI   n=534  0.1443 / 0.1037   fark -0.0406
    DEN   n=540  0.1391 / 0.1919   fark +0.0528
    LAX   n=534  0.1201 / 0.0882   fark -0.0319
    MIA   n=528  0.1378 / 0.1002   fark -0.0376
    NY    n=528  0.1159 / 0.0922   fark -0.0237
    PHL   n=528  0.1507 / 0.0968   fark -0.0538
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1541         0.030         0.059   +0.029
  0.1-0.2       820         0.150         0.195   +0.045
  0.2-0.3       665         0.248         0.263   +0.016
  0.3-0.4       418         0.345         0.242   -0.103
  0.4-0.5       186         0.440         0.290   -0.150
  0.5-0.6        63         0.546         0.333   -0.213
  0.6-0.7        25         0.636         0.440   -0.196
  0.7-0.8         5         0.739         0.800   +0.061
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (7011)
  işlem sayısı                    7011
  kazanan                         2761  (%39)
  ort. İDDİA EDİLEN edge       +19.25p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.69p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7140.71 $
  PnL fee ÖNCESİ             +49213.92 $
  PnL fee SONRASI            +42073.21 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16697.67 $   %90 aralık [-28905.69, -6914.09]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1239 (model 0.1327)

  bizim (fee sonrası)            +42073.21 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
