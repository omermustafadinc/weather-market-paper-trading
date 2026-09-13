========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-13T22:52:11.081319Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          30906
  orderbook seviyesi     1628114
  tahmin snapshot          21546
  karar                     6246
  simüle fill               1627
  çözümlenmiş kova           708

## Brier skoru  (düşük = iyi, 666 kova)
  model                  0.1273
  piyasa (mid)           0.1310   n=666
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0046  %95 [-0.0053, +0.0127]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 96  0.1551 / 0.2104   fark +0.0554
    CHI   n= 96  0.1244 / 0.1050   fark -0.0195
    DEN   n= 96  0.1464 / 0.2104   fark +0.0639
    LAX   n= 90  0.1016 / 0.0910   fark -0.0106
    MIA   n= 96  0.1255 / 0.1122   fark -0.0133
    NY    n= 96  0.1079 / 0.0833   fark -0.0246
    PHL   n= 96  0.1284 / 0.1023   fark -0.0261
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       247         0.033         0.036   +0.003
  0.1-0.2       162         0.149         0.204   +0.055
  0.2-0.3       152         0.244         0.270   +0.025
  0.3-0.4        68         0.343         0.235   -0.108
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1534)
  işlem sayısı                    1534
  kazanan                          608  (%40)
  ort. İDDİA EDİLEN edge       +14.78p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.96p   ±1.0p  %95 [-1.1p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1562.28 $
  PnL fee ÖNCESİ              +5254.80 $
  PnL fee SONRASI             +3692.52 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3196.28 $   %90 aralık [-8066.16, +1542.48]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1310 (model 0.1273)

  bizim (fee sonrası)             +3692.52 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
