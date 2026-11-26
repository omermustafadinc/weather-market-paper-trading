========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-26T21:08:14.281894Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         132084
  orderbook seviyesi     6990976
  tahmin snapshot          88011
  karar                    27312
  simüle fill               7006
  çözümlenmiş kova          3792

## Brier skoru  (düşük = iyi, 3672 kova)
  model                  0.1330
  piyasa (mid)           0.1241   n=3672
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0089  ±0.0027  %95 [-0.0141, -0.0036]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=534  0.1199 / 0.1916   fark +0.0717
    CHI   n=528  0.1452 / 0.1042   fark -0.0410
    DEN   n=534  0.1386 / 0.1916   fark +0.0530
    LAX   n=528  0.1201 / 0.0885   fark -0.0316
    MIA   n=516  0.1384 / 0.1011   fark -0.0373
    NY    n=516  0.1169 / 0.0919   fark -0.0250
    PHL   n=516  0.1520 / 0.0964   fark -0.0556
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1513         0.030         0.059   +0.028
  0.1-0.2       808         0.150         0.198   +0.048
  0.2-0.3       658         0.248         0.261   +0.014
  0.3-0.4       411         0.345         0.241   -0.104
  0.4-0.5       182         0.440         0.286   -0.154
  0.5-0.6        62         0.546         0.339   -0.208
  0.6-0.7        25         0.636         0.440   -0.196
  0.7-0.8         4         0.744         0.750   +0.006
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6955)
  işlem sayısı                    6955
  kazanan                         2746  (%39)
  ort. İDDİA EDİLEN edge       +19.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.72p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7067.25 $
  PnL fee ÖNCESİ             +49879.49 $
  PnL fee SONRASI            +42812.24 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16418.03 $   %90 aralık [-27994.44, -4795.17]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1241 (model 0.1330)

  bizim (fee sonrası)            +42812.24 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
