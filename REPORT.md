========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-18T06:36:25.893311Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          83556
  orderbook seviyesi     4450379
  tahmin snapshot          54999
  karar                    17202
  simüle fill               4467
  çözümlenmiş kova          2142

## Brier skoru  (düşük = iyi, 2058 kova)
  model                  0.1323
  piyasa (mid)           0.1309   n=2058
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0014  ±0.0031  %95 [-0.0076, +0.0047]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=294  0.1295 / 0.2043   fark +0.0748
    CHI   n=294  0.1376 / 0.1092   fark -0.0284
    DEN   n=294  0.1483 / 0.1989   fark +0.0506
    LAX   n=294  0.1258 / 0.0937   fark -0.0321
    MIA   n=294  0.1366 / 0.1039   fark -0.0327
    NY    n=294  0.1083 / 0.0928   fark -0.0155
    PHL   n=294  0.1401 / 0.1134   fark -0.0267
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       775         0.034         0.062   +0.028
  0.1-0.2       519         0.150         0.189   +0.038
  0.2-0.3       417         0.247         0.254   +0.007
  0.3-0.4       231         0.345         0.216   -0.128
  0.4-0.5        83         0.438         0.301   -0.137
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4363)
  işlem sayısı                    4363
  kazanan                         1695  (%39)
  ort. İDDİA EDİLEN edge       +17.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.01p   ±0.6p  %95 [-0.2p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4418.73 $
  PnL fee ÖNCESİ             +26962.20 $
  PnL fee SONRASI            +22543.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10638.81 $   %90 aralık [-18488.60, -3399.24]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1309 (model 0.1323)

  bizim (fee sonrası)            +22543.47 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
