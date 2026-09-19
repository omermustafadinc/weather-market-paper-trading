========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-19T17:42:25.001926Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          41136
  orderbook seviyesi     2205056
  tahmin snapshot          28224
  karar                     8382
  simüle fill               2191
  çözümlenmiş kova           936

## Brier skoru  (düşük = iyi, 894 kova)
  model                  0.1309
  piyasa (mid)           0.1357   n=894
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0048  ±0.0041  %95 [-0.0033, +0.0128]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=132  0.1466 / 0.2119   fark +0.0653
    CHI   n=126  0.1314 / 0.1153   fark -0.0161
    DEN   n=132  0.1502 / 0.2096   fark +0.0594
    LAX   n=126  0.1138 / 0.0948   fark -0.0190
    MIA   n=126  0.1323 / 0.1155   fark -0.0167
    NY    n=126  0.1081 / 0.0849   fark -0.0232
    PHL   n=126  0.1323 / 0.1106   fark -0.0218
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       325         0.035         0.055   +0.021
  0.1-0.2       231         0.151         0.190   +0.039
  0.2-0.3       197         0.246         0.259   +0.013
  0.3-0.4        99         0.344         0.222   -0.122
  0.4-0.5        30         0.432         0.233   -0.198
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2050)
  işlem sayısı                    2050
  kazanan                          812  (%40)
  ort. İDDİA EDİLEN edge       +15.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.50p   ±0.9p  %95 [-0.3p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2069.12 $
  PnL fee ÖNCESİ             +11575.38 $
  PnL fee SONRASI             +9506.26 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4912.05 $   %90 aralık [-10191.16, +435.31]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1357 (model 0.1309)

  bizim (fee sonrası)             +9506.26 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
