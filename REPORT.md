========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-28T12:52:33.946535Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         133428
  orderbook seviyesi     7059495
  tahmin snapshot          89019
  karar                    27564
  simüle fill               7067
  çözümlenmiş kova          3864

## Brier skoru  (düşük = iyi, 3744 kova)
  model                  0.1325
  piyasa (mid)           0.1240   n=3744
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0085  ±0.0026  %95 [-0.0137, -0.0033]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=540  0.1209 / 0.1921   fark +0.0712
    CHI   n=540  0.1436 / 0.1044   fark -0.0391
    DEN   n=540  0.1391 / 0.1919   fark +0.0528
    LAX   n=540  0.1201 / 0.0888   fark -0.0313
    MIA   n=528  0.1378 / 0.1002   fark -0.0376
    NY    n=528  0.1159 / 0.0922   fark -0.0237
    PHL   n=528  0.1507 / 0.0968   fark -0.0538
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1545         0.030         0.059   +0.028
  0.1-0.2       824         0.150         0.194   +0.044
  0.2-0.3       668         0.248         0.263   +0.016
  0.3-0.4       418         0.345         0.242   -0.103
  0.4-0.5       187         0.440         0.294   -0.146
  0.5-0.6        63         0.546         0.333   -0.213
  0.6-0.7        25         0.636         0.440   -0.196
  0.7-0.8         5         0.739         0.800   +0.061
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (7026)
  işlem sayısı                    7026
  kazanan                         2772  (%39)
  ort. İDDİA EDİLEN edge       +19.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.5p  %95 [+0.8p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7156.36 $
  PnL fee ÖNCESİ             +49343.81 $
  PnL fee SONRASI            +42187.45 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16698.92 $   %90 aralık [-26670.96, -8317.75]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1240 (model 0.1325)

  bizim (fee sonrası)            +42187.45 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
