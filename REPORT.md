========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-22T20:02:07.181748Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          91074
  orderbook seviyesi     4860698
  tahmin snapshot          60543
  karar                    18774
  simüle fill               4864
  çözümlenmiş kova          2322

## Brier skoru  (düşük = iyi, 2238 kova)
  model                  0.1319
  piyasa (mid)           0.1294   n=2238
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0025  ±0.0031  %95 [-0.0086, +0.0036]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=324  0.1274 / 0.2033   fark +0.0758
    CHI   n=318  0.1392 / 0.1089   fark -0.0303
    DEN   n=324  0.1475 / 0.1986   fark +0.0511
    LAX   n=318  0.1204 / 0.0889   fark -0.0315
    MIA   n=318  0.1359 / 0.1031   fark -0.0328
    NY    n=318  0.1074 / 0.0896   fark -0.0179
    PHL   n=318  0.1452 / 0.1105   fark -0.0347
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       861         0.033         0.062   +0.028
  0.1-0.2       549         0.150         0.189   +0.040
  0.2-0.3       440         0.247         0.255   +0.007
  0.3-0.4       253         0.345         0.217   -0.128
  0.4-0.5        93         0.439         0.312   -0.127
  0.5-0.6        30         0.547         0.367   -0.181
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4741)
  işlem sayısı                    4741
  kazanan                         1826  (%39)
  ort. İDDİA EDİLEN edge       +17.73p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.79p   ±0.6p  %95 [-0.4p, +2.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4825.87 $
  PnL fee ÖNCESİ             +29037.10 $
  PnL fee SONRASI            +24211.23 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12208.96 $   %90 aralık [-21365.47, -3991.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1294 (model 0.1319)

  bizim (fee sonrası)            +24211.23 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
