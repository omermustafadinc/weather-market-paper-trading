========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-21T22:51:18.569306Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          45372
  orderbook seviyesi     2427181
  tahmin snapshot          30618
  karar                     9282
  simüle fill               2422
  çözümlenmiş kova          1044

## Brier skoru  (düşük = iyi, 1002 kova)
  model                  0.1304
  piyasa (mid)           0.1358   n=1002
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0054  ±0.0039  %95 [-0.0022, +0.0130]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=144  0.1443 / 0.2121   fark +0.0678
    CHI   n=144  0.1253 / 0.1140   fark -0.0113
    DEN   n=144  0.1497 / 0.2098   fark +0.0601
    LAX   n=138  0.1155 / 0.0980   fark -0.0175
    MIA   n=144  0.1340 / 0.1148   fark -0.0192
    NY    n=144  0.1089 / 0.0880   fark -0.0208
    PHL   n=144  0.1343 / 0.1120   fark -0.0223
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       358         0.035         0.050   +0.015
  0.1-0.2       268         0.151         0.190   +0.039
  0.2-0.3       221         0.246         0.258   +0.012
  0.3-0.4       108         0.343         0.222   -0.121
  0.4-0.5        35         0.431         0.286   -0.145
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2374)
  işlem sayısı                    2374
  kazanan                          964  (%41)
  ort. İDDİA EDİLEN edge       +15.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.63p   ±0.8p  %95 [+1.0p, +4.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2402.22 $
  PnL fee ÖNCESİ             +20511.39 $
  PnL fee SONRASI            +18109.17 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6583.33 $   %90 aralık [-12451.06, -548.11]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1358 (model 0.1304)

  bizim (fee sonrası)            +18109.17 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
