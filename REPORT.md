========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-26T22:24:53.011482Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          98310
  orderbook seviyesi     5250094
  tahmin snapshot          65835
  karar                    20292
  simüle fill               5256
  çözümlenmiş kova          2514

## Brier skoru  (düşük = iyi, 2430 kova)
  model                  0.1311
  piyasa (mid)           0.1277   n=2430
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0034  ±0.0031  %95 [-0.0094, +0.0026]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=348  0.1243 / 0.2057   fark +0.0814
    CHI   n=348  0.1402 / 0.1047   fark -0.0354
    DEN   n=348  0.1450 / 0.1914   fark +0.0464
    LAX   n=342  0.1202 / 0.0881   fark -0.0321
    MIA   n=348  0.1341 / 0.1034   fark -0.0306
    NY    n=348  0.1069 / 0.0911   fark -0.0158
    PHL   n=348  0.1466 / 0.1086   fark -0.0380
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       945         0.033         0.057   +0.025
  0.1-0.2       584         0.150         0.190   +0.041
  0.2-0.3       464         0.247         0.259   +0.012
  0.3-0.4       288         0.346         0.229   -0.117
  0.4-0.5       103         0.439         0.320   -0.118
  0.5-0.6        33         0.547         0.333   -0.213
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5210)
  işlem sayısı                    5210
  kazanan                         2018  (%39)
  ort. İDDİA EDİLEN edge       +18.13p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.17p   ±0.6p  %95 [+0.1p, +2.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5350.41 $
  PnL fee ÖNCESİ             +41051.97 $
  PnL fee SONRASI            +35701.56 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13357.32 $   %90 aralık [-22591.78, -4978.27]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1277 (model 0.1311)

  bizim (fee sonrası)            +35701.56 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
