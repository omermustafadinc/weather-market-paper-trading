========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-20T13:37:23.643919Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          87426
  orderbook seviyesi     4658506
  tahmin snapshot          57897
  karar                    18000
  simüle fill               4660
  çözümlenmiş kova          2232

## Brier skoru  (düşük = iyi, 2148 kova)
  model                  0.1321
  piyasa (mid)           0.1301   n=2148
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0020  ±0.0031  %95 [-0.0081, +0.0041]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=306  0.1280 / 0.2052   fark +0.0771
    CHI   n=306  0.1390 / 0.1077   fark -0.0312
    DEN   n=312  0.1495 / 0.2003   fark +0.0509
    LAX   n=306  0.1224 / 0.0911   fark -0.0313
    MIA   n=306  0.1360 / 0.1026   fark -0.0334
    NY    n=306  0.1069 / 0.0913   fark -0.0156
    PHL   n=306  0.1426 / 0.1111   fark -0.0315
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       818         0.034         0.061   +0.027
  0.1-0.2       535         0.150         0.189   +0.039
  0.2-0.3       428         0.247         0.257   +0.010
  0.3-0.4       239         0.345         0.213   -0.131
  0.4-0.5        90         0.439         0.311   -0.128
  0.5-0.6        27         0.549         0.370   -0.179
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4580)
  işlem sayısı                    4580
  kazanan                         1765  (%39)
  ort. İDDİA EDİLEN edge       +17.51p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.74p   ±0.6p  %95 [-0.4p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4651.76 $
  PnL fee ÖNCESİ             +27466.59 $
  PnL fee SONRASI            +22814.83 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11191.48 $   %90 aralık [-20393.58, -1334.60]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1301 (model 0.1321)

  bizim (fee sonrası)            +22814.83 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
