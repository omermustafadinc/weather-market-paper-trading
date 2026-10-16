========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-16T18:43:51.858422Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          80400
  orderbook seviyesi     4285021
  tahmin snapshot          52983
  karar                    16548
  simüle fill               4296
  çözümlenmiş kova          2070

## Brier skoru  (düşük = iyi, 1986 kova)
  model                  0.1324
  piyasa (mid)           0.1310   n=1986
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0014  ±0.0032  %95 [-0.0076, +0.0048]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=288  0.1281 / 0.2036   fark +0.0755
    CHI   n=282  0.1384 / 0.1089   fark -0.0296
    DEN   n=288  0.1482 / 0.1984   fark +0.0502
    LAX   n=282  0.1258 / 0.0951   fark -0.0307
    MIA   n=282  0.1358 / 0.1041   fark -0.0317
    NY    n=282  0.1092 / 0.0910   fark -0.0182
    PHL   n=282  0.1408 / 0.1128   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       747         0.034         0.060   +0.026
  0.1-0.2       501         0.151         0.192   +0.041
  0.2-0.3       407         0.247         0.253   +0.006
  0.3-0.4       219         0.345         0.219   -0.126
  0.4-0.5        79         0.438         0.291   -0.147
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4185)
  işlem sayısı                    4185
  kazanan                         1631  (%39)
  ort. İDDİA EDİLEN edge       +16.81p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.64p   ±0.6p  %95 [-0.6p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4208.83 $
  PnL fee ÖNCESİ             +24783.25 $
  PnL fee SONRASI            +20574.42 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10476.66 $   %90 aralık [-18679.22, -2198.84]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1310 (model 0.1324)

  bizim (fee sonrası)            +20574.42 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
