========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-27T14:24:07.571926Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          54888
  orderbook seviyesi     2933231
  tahmin snapshot          36540
  karar                    11268
  simüle fill               2955
  çözümlenmiş kova          1272

## Brier skoru  (düşük = iyi, 1230 kova)
  model                  0.1311
  piyasa (mid)           0.1351   n=1230
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0040  ±0.0038  %95 [-0.0034, +0.0114]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=180  0.1358 / 0.2105   fark +0.0747
    CHI   n=174  0.1237 / 0.1155   fark -0.0082
    DEN   n=180  0.1477 / 0.2071   fark +0.0594
    LAX   n=174  0.1258 / 0.0936   fark -0.0322
    MIA   n=174  0.1365 / 0.1166   fark -0.0199
    NY    n=174  0.1090 / 0.0880   fark -0.0211
    PHL   n=174  0.1387 / 0.1094   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       451         0.035         0.053   +0.019
  0.1-0.2       318         0.151         0.195   +0.044
  0.2-0.3       264         0.247         0.250   +0.003
  0.3-0.4       134         0.345         0.231   -0.114
  0.4-0.5        48         0.435         0.292   -0.143
  0.5-0.6        11         0.550         0.364   -0.187
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2842)
  işlem sayısı                    2842
  kazanan                         1173  (%41)
  ort. İDDİA EDİLEN edge       +15.59p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +3.03p   ±0.8p  %95 [+1.5p, +4.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2854.12 $
  PnL fee ÖNCESİ             +25418.77 $
  PnL fee SONRASI            +22564.65 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8011.64 $   %90 aralık [-14937.21, -2122.64]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1351 (model 0.1311)

  bizim (fee sonrası)            +22564.65 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
