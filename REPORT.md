========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-17T00:15:41.523342Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          81072
  orderbook seviyesi     4316412
  tahmin snapshot          53361
  karar                    16716
  simüle fill               4337
  çözümlenmiş kova          2094

## Brier skoru  (düşük = iyi, 2010 kova)
  model                  0.1323
  piyasa (mid)           0.1302   n=2010
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0021  ±0.0032  %95 [-0.0083, +0.0041]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=288  0.1281 / 0.2036   fark +0.0755
    CHI   n=288  0.1393 / 0.1073   fark -0.0320
    DEN   n=288  0.1482 / 0.1984   fark +0.0502
    LAX   n=282  0.1258 / 0.0951   fark -0.0307
    MIA   n=288  0.1357 / 0.1025   fark -0.0332
    NY    n=288  0.1084 / 0.0895   fark -0.0190
    PHL   n=288  0.1407 / 0.1144   fark -0.0263
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       757         0.034         0.061   +0.027
  0.1-0.2       504         0.151         0.190   +0.040
  0.2-0.3       413         0.247         0.254   +0.008
  0.3-0.4       223         0.345         0.215   -0.129
  0.4-0.5        80         0.438         0.300   -0.138
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4252)
  işlem sayısı                    4252
  kazanan                         1632  (%38)
  ort. İDDİA EDİLEN edge       +16.96p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.36p   ±0.6p  %95 [-0.9p, +1.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4295.03 $
  PnL fee ÖNCESİ             +23329.58 $
  PnL fee SONRASI            +19034.55 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10272.05 $   %90 aralık [-18250.29, -2791.22]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1302 (model 0.1323)

  bizim (fee sonrası)            +19034.55 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
