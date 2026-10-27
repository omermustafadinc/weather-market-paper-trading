========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-27T12:59:45.510083Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          99006
  orderbook seviyesi     5289781
  tahmin snapshot          66339
  karar                    20388
  simüle fill               5282
  çözümlenmiş kova          2532

## Brier skoru  (düşük = iyi, 2448 kova)
  model                  0.1308
  piyasa (mid)           0.1274   n=2448
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0034  ±0.0031  %95 [-0.0094, +0.0026]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=354  0.1237 / 0.2047   fark +0.0810
    CHI   n=348  0.1402 / 0.1047   fark -0.0354
    DEN   n=354  0.1431 / 0.1898   fark +0.0466
    LAX   n=348  0.1208 / 0.0870   fark -0.0338
    MIA   n=348  0.1341 / 0.1034   fark -0.0306
    NY    n=348  0.1069 / 0.0911   fark -0.0158
    PHL   n=348  0.1466 / 0.1086   fark -0.0380
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       952         0.033         0.057   +0.024
  0.1-0.2       590         0.150         0.190   +0.040
  0.2-0.3       465         0.247         0.258   +0.011
  0.3-0.4       291         0.346         0.230   -0.116
  0.4-0.5       103         0.439         0.320   -0.118
  0.5-0.6        34         0.548         0.353   -0.195
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5235)
  işlem sayısı                    5235
  kazanan                         2037  (%39)
  ort. İDDİA EDİLEN edge       +18.12p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.32p   ±0.6p  %95 [+0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5371.59 $
  PnL fee ÖNCESİ             +41632.65 $
  PnL fee SONRASI            +36261.06 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13149.79 $   %90 aralık [-22544.95, -4078.58]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1274 (model 0.1308)

  bizim (fee sonrası)            +36261.06 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
