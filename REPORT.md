========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-02T14:38:42.739989Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          61476
  orderbook seviyesi     3285062
  tahmin snapshot          41202
  karar                    12672
  simüle fill               3300
  çözümlenmiş kova          1482

## Brier skoru  (düşük = iyi, 1440 kova)
  model                  0.1313
  piyasa (mid)           0.1336   n=1440
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0024  ±0.0035  %95 [-0.0045, +0.0093]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=210  0.1317 / 0.2041   fark +0.0725
    CHI   n=204  0.1287 / 0.1146   fark -0.0141
    DEN   n=210  0.1461 / 0.2007   fark +0.0546
    LAX   n=204  0.1262 / 0.0966   fark -0.0297
    MIA   n=204  0.1381 / 0.1124   fark -0.0257
    NY    n=204  0.1094 / 0.0865   fark -0.0228
    PHL   n=204  0.1382 / 0.1164   fark -0.0217
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       529         0.034         0.057   +0.022
  0.1-0.2       371         0.151         0.189   +0.037
  0.2-0.3       308         0.246         0.247   +0.001
  0.3-0.4       154         0.346         0.240   -0.105
  0.4-0.5        60         0.434         0.317   -0.117
  0.5-0.6        14         0.546         0.286   -0.260
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3237)
  işlem sayısı                    3237
  kazanan                         1299  (%40)
  ort. İDDİA EDİLEN edge       +15.95p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.7p  %95 [+0.3p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3228.09 $
  PnL fee ÖNCESİ             +25332.73 $
  PnL fee SONRASI            +22104.64 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8543.28 $   %90 aralık [-15206.98, -1325.41]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1336 (model 0.1313)

  bizim (fee sonrası)            +22104.64 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
