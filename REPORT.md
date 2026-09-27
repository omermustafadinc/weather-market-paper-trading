========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-27T00:21:28.622250Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          54216
  orderbook seviyesi     2897379
  tahmin snapshot          35910
  karar                    11142
  simüle fill               2923
  çözümlenmiş kova          1254

## Brier skoru  (düşük = iyi, 1212 kova)
  model                  0.1311
  piyasa (mid)           0.1346   n=1212
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0035  ±0.0038  %95 [-0.0039, +0.0108]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=174  0.1360 / 0.2100   fark +0.0741
    CHI   n=174  0.1237 / 0.1155   fark -0.0082
    DEN   n=174  0.1495 / 0.2065   fark +0.0570
    LAX   n=168  0.1239 / 0.0945   fark -0.0295
    MIA   n=174  0.1365 / 0.1166   fark -0.0199
    NY    n=174  0.1090 / 0.0880   fark -0.0211
    PHL   n=174  0.1387 / 0.1094   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       442         0.035         0.054   +0.019
  0.1-0.2       316         0.151         0.193   +0.042
  0.2-0.3       262         0.247         0.248   +0.001
  0.3-0.4       131         0.345         0.229   -0.116
  0.4-0.5        47         0.435         0.298   -0.137
  0.5-0.6        10         0.549         0.400   -0.149
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2829)
  işlem sayısı                    2829
  kazanan                         1167  (%41)
  ort. İDDİA EDİLEN edge       +15.56p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +3.02p   ±0.8p  %95 [+1.5p, +4.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2841.28 $
  PnL fee ÖNCESİ             +24471.64 $
  PnL fee SONRASI            +21630.36 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7648.34 $   %90 aralık [-13732.92, -1016.79]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1346 (model 0.1311)

  bizim (fee sonrası)            +21630.36 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
