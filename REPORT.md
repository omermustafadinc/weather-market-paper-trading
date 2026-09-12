========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-12T13:25:25.966732Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          27498
  orderbook seviyesi     1449300
  tahmin snapshot          19278
  karar                     5466
  simüle fill               1417
  çözümlenmiş kova           642

## Brier skoru  (düşük = iyi, 600 kova)
  model                  0.1260
  piyasa (mid)           0.1320   n=600
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0060  ±0.0049  %95 [-0.0036, +0.0155]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 90  0.1553 / 0.2098   fark +0.0544
    CHI   n= 84  0.1208 / 0.1022   fark -0.0186
    DEN   n= 90  0.1448 / 0.2102   fark +0.0654
    LAX   n= 84  0.0989 / 0.0902   fark -0.0087
    MIA   n= 84  0.1217 / 0.1124   fark -0.0093
    NY    n= 84  0.1055 / 0.0838   fark -0.0217
    PHL   n= 84  0.1316 / 0.1040   fark -0.0275
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       226         0.033         0.035   +0.002
  0.1-0.2       144         0.149         0.194   +0.045
  0.2-0.3       136         0.245         0.287   +0.041
  0.3-0.4        59         0.345         0.220   -0.124
  0.4-0.5        23         0.436         0.217   -0.218
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1320)
  işlem sayısı                    1320
  kazanan                          542  (%41)
  ort. İDDİA EDİLEN edge       +14.69p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.19p   ±1.1p  %95 [+0.0p, +4.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1334.95 $
  PnL fee ÖNCESİ              +7373.41 $
  PnL fee SONRASI             +6038.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2335.40 $   %90 aralık [-7703.39, +2105.07]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1320 (model 0.1260)

  bizim (fee sonrası)             +6038.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
