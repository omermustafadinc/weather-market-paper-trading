========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-27T13:21:33.719172Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         132588
  orderbook seviyesi     7018503
  tahmin snapshot          88389
  karar                    27396
  simüle fill               7026
  çözümlenmiş kova          3822

## Brier skoru  (düşük = iyi, 3702 kova)
  model                  0.1325
  piyasa (mid)           0.1235   n=3702
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0090  ±0.0027  %95 [-0.0142, -0.0038]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=534  0.1199 / 0.1916   fark +0.0717
    CHI   n=534  0.1443 / 0.1037   fark -0.0406
    DEN   n=534  0.1386 / 0.1916   fark +0.0530
    LAX   n=534  0.1201 / 0.0882   fark -0.0319
    MIA   n=522  0.1378 / 0.1009   fark -0.0369
    NY    n=522  0.1158 / 0.0909   fark -0.0248
    PHL   n=522  0.1511 / 0.0955   fark -0.0556
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1527         0.030         0.058   +0.028
  0.1-0.2       815         0.150         0.196   +0.047
  0.2-0.3       661         0.248         0.262   +0.014
  0.3-0.4       414         0.345         0.242   -0.103
  0.4-0.5       184         0.440         0.293   -0.146
  0.5-0.6        62         0.546         0.339   -0.208
  0.6-0.7        25         0.636         0.440   -0.196
  0.7-0.8         5         0.739         0.800   +0.061
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6987)
  işlem sayısı                    6987
  kazanan                         2754  (%39)
  ort. İDDİA EDİLEN edge       +19.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.69p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7106.79 $
  PnL fee ÖNCESİ             +49377.15 $
  PnL fee SONRASI            +42270.36 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16342.66 $   %90 aralık [-26867.17, -6254.22]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1235 (model 0.1325)

  bizim (fee sonrası)            +42270.36 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
