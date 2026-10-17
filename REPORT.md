========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-17T22:05:25.083802Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          82692
  orderbook seviyesi     4404267
  tahmin snapshot          54621
  karar                    17022
  simüle fill               4417
  çözümlenmiş kova          2136

## Brier skoru  (düşük = iyi, 2052 kova)
  model                  0.1322
  piyasa (mid)           0.1309   n=2052
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0013  ±0.0031  %95 [-0.0074, +0.0049]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=294  0.1295 / 0.2043   fark +0.0748
    CHI   n=294  0.1376 / 0.1092   fark -0.0284
    DEN   n=294  0.1483 / 0.1989   fark +0.0506
    LAX   n=288  0.1248 / 0.0933   fark -0.0315
    MIA   n=294  0.1366 / 0.1039   fark -0.0327
    NY    n=294  0.1083 / 0.0928   fark -0.0155
    PHL   n=294  0.1401 / 0.1134   fark -0.0267
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       774         0.034         0.062   +0.028
  0.1-0.2       515         0.151         0.188   +0.038
  0.2-0.3       417         0.247         0.254   +0.007
  0.3-0.4       231         0.345         0.216   -0.128
  0.4-0.5        82         0.438         0.305   -0.133
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4357)
  işlem sayısı                    4357
  kazanan                         1692  (%39)
  ort. İDDİA EDİLEN edge       +17.22p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.03p   ±0.6p  %95 [-0.2p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4414.97 $
  PnL fee ÖNCESİ             +26995.28 $
  PnL fee SONRASI            +22580.31 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11045.04 $   %90 aralık [-19393.79, -3358.58]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1309 (model 0.1322)

  bizim (fee sonrası)            +22580.31 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
