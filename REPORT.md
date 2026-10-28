========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-28T07:56:50.546779Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         100182
  orderbook seviyesi     5350952
  tahmin snapshot          66969
  karar                    20640
  simüle fill               5347
  çözümlenmiş kova          2562

## Brier skoru  (düşük = iyi, 2478 kova)
  model                  0.1307
  piyasa (mid)           0.1270   n=2478
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0037  ±0.0030  %95 [-0.0097, +0.0023]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=354  0.1237 / 0.2047   fark +0.0810
    CHI   n=354  0.1394 / 0.1042   fark -0.0352
    DEN   n=354  0.1431 / 0.1898   fark +0.0466
    LAX   n=354  0.1208 / 0.0882   fark -0.0326
    MIA   n=354  0.1342 / 0.1031   fark -0.0311
    NY    n=354  0.1063 / 0.0914   fark -0.0149
    PHL   n=354  0.1473 / 0.1076   fark -0.0397
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       966         0.032         0.056   +0.023
  0.1-0.2       595         0.150         0.190   +0.040
  0.2-0.3       470         0.247         0.260   +0.012
  0.3-0.4       293         0.346         0.232   -0.114
  0.4-0.5       105         0.439         0.314   -0.124
  0.5-0.6        36         0.548         0.361   -0.186
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5282)
  işlem sayısı                    5282
  kazanan                         2058  (%39)
  ort. İDDİA EDİLEN edge       +18.13p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.42p   ±0.6p  %95 [+0.3p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5419.67 $
  PnL fee ÖNCESİ             +41647.46 $
  PnL fee SONRASI            +36227.79 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13644.37 $   %90 aralık [-23991.50, -4601.19]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1270 (model 0.1307)

  bizim (fee sonrası)            +36227.79 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
