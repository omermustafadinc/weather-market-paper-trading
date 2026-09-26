========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-26T15:31:17.086965Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          53208
  orderbook seviyesi     2848049
  tahmin snapshot          35406
  karar                    10890
  simüle fill               2861
  çözümlenmiş kova          1230

## Brier skoru  (düşük = iyi, 1188 kova)
  model                  0.1311
  piyasa (mid)           0.1351   n=1188
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0040  ±0.0038  %95 [-0.0034, +0.0114]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=174  0.1360 / 0.2100   fark +0.0741
    CHI   n=168  0.1229 / 0.1152   fark -0.0077
    DEN   n=174  0.1495 / 0.2065   fark +0.0570
    LAX   n=168  0.1239 / 0.0945   fark -0.0295
    MIA   n=168  0.1375 / 0.1152   fark -0.0223
    NY    n=168  0.1099 / 0.0898   fark -0.0201
    PHL   n=168  0.1372 / 0.1092   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       430         0.035         0.053   +0.019
  0.1-0.2       314         0.151         0.191   +0.040
  0.2-0.3       256         0.246         0.254   +0.007
  0.3-0.4       128         0.345         0.219   -0.126
  0.4-0.5        46         0.435         0.304   -0.130
  0.5-0.6        10         0.549         0.400   -0.149
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2744)
  işlem sayısı                    2744
  kazanan                         1131  (%41)
  ort. İDDİA EDİLEN edge       +15.38p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.93p   ±0.8p  %95 [+1.4p, +4.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2751.72 $
  PnL fee ÖNCESİ             +24952.16 $
  PnL fee SONRASI            +22200.44 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7324.82 $   %90 aralık [-14282.41, -244.52]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1351 (model 0.1311)

  bizim (fee sonrası)            +22200.44 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
