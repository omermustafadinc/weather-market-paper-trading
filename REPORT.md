========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-25T20:02:45.136595Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         131244
  orderbook seviyesi     6946154
  tahmin snapshot          87633
  karar                    27144
  simüle fill               6965
  çözümlenmiş kova          3750

## Brier skoru  (düşük = iyi, 3630 kova)
  model                  0.1335
  piyasa (mid)           0.1240   n=3630
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0095  ±0.0027  %95 [-0.0147, -0.0042]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=528  0.1198 / 0.1910   fark +0.0713
    CHI   n=522  0.1461 / 0.1033   fark -0.0428
    DEN   n=528  0.1382 / 0.1913   fark +0.0530
    LAX   n=522  0.1202 / 0.0888   fark -0.0314
    MIA   n=510  0.1389 / 0.1007   fark -0.0382
    NY    n=510  0.1181 / 0.0926   fark -0.0255
    PHL   n=510  0.1534 / 0.0970   fark -0.0564
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1491         0.031         0.060   +0.029
  0.1-0.2       804         0.149         0.198   +0.048
  0.2-0.3       649         0.247         0.262   +0.015
  0.3-0.4       409         0.345         0.240   -0.105
  0.4-0.5       179         0.440         0.285   -0.155
  0.5-0.6        62         0.546         0.339   -0.208
  0.6-0.7        24         0.635         0.417   -0.219
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6918)
  işlem sayısı                    6918
  kazanan                         2716  (%39)
  ort. İDDİA EDİLEN edge       +19.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.54p   ±0.5p  %95 [+0.6p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   7032.43 $
  PnL fee ÖNCESİ             +49252.29 $
  PnL fee SONRASI            +42219.86 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16712.28 $   %90 aralık [-27791.87, -5797.03]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1240 (model 0.1335)

  bizim (fee sonrası)            +42219.86 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
