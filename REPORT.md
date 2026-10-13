========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-13T21:56:26.432455Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          75528
  orderbook seviyesi     4033663
  tahmin snapshot          50211
  karar                    15540
  simüle fill               4021
  çözümlenmiş kova          1968

## Brier skoru  (düşük = iyi, 1884 kova)
  model                  0.1328
  piyasa (mid)           0.1321   n=1884
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0007  ±0.0032  %95 [-0.0071, +0.0056]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=270  0.1295 / 0.2056   fark +0.0761
    CHI   n=270  0.1381 / 0.1092   fark -0.0289
    DEN   n=270  0.1497 / 0.2014   fark +0.0517
    LAX   n=264  0.1271 / 0.0968   fark -0.0303
    MIA   n=270  0.1351 / 0.1067   fark -0.0283
    NY    n=270  0.1094 / 0.0918   fark -0.0176
    PHL   n=270  0.1405 / 0.1120   fark -0.0285
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       707         0.034         0.062   +0.029
  0.1-0.2       474         0.151         0.190   +0.039
  0.2-0.3       390         0.247         0.249   +0.002
  0.3-0.4       206         0.345         0.228   -0.117
  0.4-0.5        77         0.437         0.299   -0.138
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3977)
  işlem sayısı                    3977
  kazanan                         1572  (%40)
  ort. İDDİA EDİLEN edge       +16.76p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.08p   ±0.6p  %95 [-0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4011.66 $
  PnL fee ÖNCESİ             +24675.66 $
  PnL fee SONRASI            +20664.00 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10033.51 $   %90 aralık [-17680.87, -2763.14]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1321 (model 0.1328)

  bizim (fee sonrası)            +20664.00 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
