========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-28T14:44:32.800059Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         100518
  orderbook seviyesi     5368336
  tahmin snapshot          67095
  karar                    20724
  simüle fill               5368
  çözümlenmiş kova          2574

## Brier skoru  (düşük = iyi, 2490 kova)
  model                  0.1305
  piyasa (mid)           0.1273   n=2490
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0032  ±0.0030  %95 [-0.0092, +0.0028]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=360  0.1237 / 0.2044   fark +0.0807
    CHI   n=354  0.1394 / 0.1042   fark -0.0352
    DEN   n=360  0.1419 / 0.1901   fark +0.0482
    LAX   n=354  0.1208 / 0.0882   fark -0.0326
    MIA   n=354  0.1342 / 0.1031   fark -0.0311
    NY    n=354  0.1063 / 0.0914   fark -0.0149
    PHL   n=354  0.1473 / 0.1076   fark -0.0397
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       971         0.032         0.056   +0.023
  0.1-0.2       596         0.150         0.190   +0.040
  0.2-0.3       474         0.247         0.259   +0.012
  0.3-0.4       294         0.346         0.231   -0.114
  0.4-0.5       106         0.439         0.321   -0.118
  0.5-0.6        36         0.548         0.361   -0.186
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5296)
  işlem sayısı                    5296
  kazanan                         2072  (%39)
  ort. İDDİA EDİLEN edge       +18.14p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.61p   ±0.6p  %95 [+0.5p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5429.88 $
  PnL fee ÖNCESİ             +42804.17 $
  PnL fee SONRASI            +37374.29 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13694.37 $   %90 aralık [-23158.15, -5276.52]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1273 (model 0.1305)

  bizim (fee sonrası)            +37374.29 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
