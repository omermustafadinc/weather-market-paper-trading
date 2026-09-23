========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-23T15:28:54.006452Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          48132
  orderbook seviyesi     2577123
  tahmin snapshot          32382
  karar                     9822
  simüle fill               2573
  çözümlenmiş kova          1104

## Brier skoru  (düşük = iyi, 1062 kova)
  model                  0.1310
  piyasa (mid)           0.1360   n=1062
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0050  ±0.0038  %95 [-0.0025, +0.0125]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=156  0.1431 / 0.2120   fark +0.0689
    CHI   n=150  0.1277 / 0.1154   fark -0.0123
    DEN   n=156  0.1484 / 0.2071   fark +0.0587
    LAX   n=150  0.1177 / 0.0963   fark -0.0214
    MIA   n=150  0.1353 / 0.1136   fark -0.0217
    NY    n=150  0.1102 / 0.0915   fark -0.0187
    PHL   n=150  0.1337 / 0.1105   fark -0.0233
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       379         0.035         0.050   +0.015
  0.1-0.2       285         0.151         0.193   +0.042
  0.2-0.3       232         0.246         0.259   +0.012
  0.3-0.4       116         0.343         0.216   -0.128
  0.4-0.5        38         0.434         0.289   -0.144
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2460)
  işlem sayısı                    2460
  kazanan                         1004  (%41)
  ort. İDDİA EDİLEN edge       +15.30p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.79p   ±0.8p  %95 [+1.2p, +4.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2490.71 $
  PnL fee ÖNCESİ             +21932.06 $
  PnL fee SONRASI            +19441.35 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6857.11 $   %90 aralık [-12894.94, -683.38]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1360 (model 0.1310)

  bizim (fee sonrası)            +19441.35 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
