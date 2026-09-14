========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-14T20:59:16.832987Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          32214
  orderbook seviyesi     1701866
  tahmin snapshot          22176
  karar                     6522
  simüle fill               1709
  çözümlenmiş kova           738

## Brier skoru  (düşük = iyi, 696 kova)
  model                  0.1273
  piyasa (mid)           0.1313   n=696
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0040  ±0.0045  %95 [-0.0048, +0.0128]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=102  0.1533 / 0.2104   fark +0.0571
    CHI   n= 96  0.1244 / 0.1050   fark -0.0195
    DEN   n=102  0.1487 / 0.2108   fark +0.0621
    LAX   n= 96  0.1040 / 0.0919   fark -0.0121
    MIA   n=102  0.1239 / 0.1107   fark -0.0133
    NY    n=102  0.1071 / 0.0827   fark -0.0244
    PHL   n= 96  0.1284 / 0.1023   fark -0.0261
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       259         0.033         0.039   +0.005
  0.1-0.2       167         0.149         0.198   +0.049
  0.2-0.3       159         0.245         0.270   +0.026
  0.3-0.4        74         0.343         0.243   -0.100
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1636)
  işlem sayısı                    1636
  kazanan                          643  (%39)
  ort. İDDİA EDİLEN edge       +14.87p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.00p   ±1.0p  %95 [-1.0p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1673.15 $
  PnL fee ÖNCESİ              +7220.27 $
  PnL fee SONRASI             +5547.12 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3573.64 $   %90 aralık [-8426.37, +1690.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1313 (model 0.1273)

  bizim (fee sonrası)             +5547.12 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
