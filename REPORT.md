========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-16T21:55:26.683955Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          80736
  orderbook seviyesi     4300960
  tahmin snapshot          53109
  karar                    16632
  simüle fill               4317
  çözümlenmiş kova          2088

## Brier skoru  (düşük = iyi, 2004 kova)
  model                  0.1322
  piyasa (mid)           0.1305   n=2004
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0017  ±0.0031  %95 [-0.0078, +0.0045]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=288  0.1281 / 0.2036   fark +0.0755
    CHI   n=282  0.1384 / 0.1089   fark -0.0296
    DEN   n=288  0.1482 / 0.1984   fark +0.0502
    LAX   n=282  0.1258 / 0.0951   fark -0.0307
    MIA   n=288  0.1357 / 0.1025   fark -0.0332
    NY    n=288  0.1084 / 0.0895   fark -0.0190
    PHL   n=288  0.1407 / 0.1144   fark -0.0263
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       754         0.034         0.060   +0.026
  0.1-0.2       503         0.151         0.191   +0.040
  0.2-0.3       412         0.247         0.255   +0.008
  0.3-0.4       222         0.345         0.216   -0.129
  0.4-0.5        80         0.438         0.300   -0.138
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4229)
  işlem sayısı                    4229
  kazanan                         1632  (%39)
  ort. İDDİA EDİLEN edge       +16.89p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.46p   ±0.6p  %95 [-0.8p, +1.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4267.36 $
  PnL fee ÖNCESİ             +23812.19 $
  PnL fee SONRASI            +19544.83 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10359.42 $   %90 aralık [-18198.76, -3002.04]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1305 (model 0.1322)

  bizim (fee sonrası)            +19544.83 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
