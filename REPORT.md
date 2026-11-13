========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-13T17:25:42.480509Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         119574
  orderbook seviyesi     6351867
  tahmin snapshot          80073
  karar                    24750
  simüle fill               6378
  çözümlenmiş kova          3246

## Brier skoru  (düşük = iyi, 3162 kova)
  model                  0.1317
  piyasa (mid)           0.1251   n=3162
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0066  ±0.0028  %95 [-0.0121, -0.0011]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=456  0.1211 / 0.1944   fark +0.0733
    CHI   n=450  0.1401 / 0.1061   fark -0.0341
    DEN   n=456  0.1411 / 0.1940   fark +0.0529
    LAX   n=450  0.1211 / 0.0848   fark -0.0363
    MIA   n=450  0.1382 / 0.1026   fark -0.0355
    NY    n=450  0.1104 / 0.0928   fark -0.0176
    PHL   n=450  0.1501 / 0.0995   fark -0.0505
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1282         0.032         0.053   +0.021
  0.1-0.2       715         0.150         0.200   +0.050
  0.2-0.3       575         0.247         0.268   +0.021
  0.3-0.4       361         0.345         0.235   -0.110
  0.4-0.5       158         0.440         0.297   -0.143
  0.5-0.6        45         0.549         0.356   -0.193
  0.6-0.7        17         0.637         0.412   -0.225
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6334)
  işlem sayısı                    6334
  kazanan                         2484  (%39)
  ort. İDDİA EDİLEN edge       +18.66p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.90p   ±0.5p  %95 [+0.9p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6478.36 $
  PnL fee ÖNCESİ             +51274.82 $
  PnL fee SONRASI            +44796.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14966.23 $   %90 aralık [-24501.71, -5089.47]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1251 (model 0.1317)

  bizim (fee sonrası)            +44796.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
