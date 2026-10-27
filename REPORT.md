========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-27T22:59:24.174808Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          99678
  orderbook seviyesi     5322657
  tahmin snapshot          66591
  karar                    20556
  simüle fill               5325
  çözümlenmiş kova          2550

## Brier skoru  (düşük = iyi, 2466 kova)
  model                  0.1306
  piyasa (mid)           0.1271   n=2466
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0035  ±0.0030  %95 [-0.0094, +0.0025]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=354  0.1237 / 0.2047   fark +0.0810
    CHI   n=354  0.1394 / 0.1042   fark -0.0352
    DEN   n=354  0.1431 / 0.1898   fark +0.0466
    LAX   n=348  0.1208 / 0.0870   fark -0.0338
    MIA   n=354  0.1342 / 0.1031   fark -0.0311
    NY    n=354  0.1063 / 0.0914   fark -0.0149
    PHL   n=348  0.1466 / 0.1086   fark -0.0380
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       961         0.032         0.056   +0.024
  0.1-0.2       592         0.150         0.189   +0.039
  0.2-0.3       468         0.247         0.259   +0.011
  0.3-0.4       292         0.346         0.233   -0.113
  0.4-0.5       105         0.439         0.314   -0.124
  0.5-0.6        35         0.548         0.371   -0.176
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5276)
  işlem sayısı                    5276
  kazanan                         2056  (%39)
  ort. İDDİA EDİLEN edge       +18.12p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.40p   ±0.6p  %95 [+0.3p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5412.38 $
  PnL fee ÖNCESİ             +41669.03 $
  PnL fee SONRASI            +36256.65 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13722.96 $   %90 aralık [-23069.65, -5263.34]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1271 (model 0.1306)

  bizim (fee sonrası)            +36256.65 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
