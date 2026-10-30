========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-30T14:53:08.366418Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         103206
  orderbook seviyesi     5511570
  tahmin snapshot          68733
  karar                    21312
  simüle fill               5519
  çözümlenmiş kova          2658

## Brier skoru  (düşük = iyi, 2574 kova)
  model                  0.1301
  piyasa (mid)           0.1264   n=2574
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0036  ±0.0030  %95 [-0.0095, +0.0023]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=372  0.1217 / 0.1988   fark +0.0770
    CHI   n=366  0.1406 / 0.1047   fark -0.0359
    DEN   n=372  0.1398 / 0.1902   fark +0.0504
    LAX   n=366  0.1207 / 0.0882   fark -0.0325
    MIA   n=366  0.1351 / 0.1040   fark -0.0311
    NY    n=366  0.1061 / 0.0911   fark -0.0150
    PHL   n=366  0.1464 / 0.1059   fark -0.0405
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1008         0.033         0.055   +0.022
  0.1-0.2       613         0.150         0.188   +0.038
  0.2-0.3       486         0.247         0.259   +0.012
  0.3-0.4       303         0.345         0.238   -0.108
  0.4-0.5       114         0.439         0.333   -0.106
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5455)
  işlem sayısı                    5455
  kazanan                         2134  (%39)
  ort. İDDİA EDİLEN edge       +18.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.6p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5594.31 $
  PnL fee ÖNCESİ             +45144.83 $
  PnL fee SONRASI            +39550.52 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13644.16 $   %90 aralık [-22646.30, -5054.75]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1264 (model 0.1301)

  bizim (fee sonrası)            +39550.52 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
