========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-12T21:22:20.683904Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         118902
  orderbook seviyesi     6316526
  tahmin snapshot          79443
  karar                    24624
  simüle fill               6347
  çözümlenmiş kova          3204

## Brier skoru  (düşük = iyi, 3120 kova)
  model                  0.1316
  piyasa (mid)           0.1244   n=3120
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0072  ±0.0028  %95 [-0.0127, -0.0017]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=450  0.1217 / 0.1940   fark +0.0723
    CHI   n=444  0.1405 / 0.1051   fark -0.0354
    DEN   n=450  0.1408 / 0.1935   fark +0.0528
    LAX   n=444  0.1222 / 0.0852   fark -0.0370
    MIA   n=444  0.1371 / 0.1016   fark -0.0355
    NY    n=444  0.1088 / 0.0907   fark -0.0181
    PHL   n=444  0.1498 / 0.0984   fark -0.0514
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1263         0.032         0.052   +0.021
  0.1-0.2       706         0.150         0.200   +0.050
  0.2-0.3       568         0.247         0.269   +0.023
  0.3-0.4       360         0.345         0.236   -0.109
  0.4-0.5       154         0.441         0.299   -0.142
  0.5-0.6        44         0.548         0.341   -0.207
  0.6-0.7        16         0.633         0.438   -0.195
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6277)
  işlem sayısı                    6277
  kazanan                         2455  (%39)
  ort. İDDİA EDİLEN edge       +18.64p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.78p   ±0.5p  %95 [+0.8p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6415.19 $
  PnL fee ÖNCESİ             +50575.46 $
  PnL fee SONRASI            +44160.27 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16257.78 $   %90 aralık [-26936.14, -6610.44]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1244 (model 0.1316)

  bizim (fee sonrası)            +44160.27 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
