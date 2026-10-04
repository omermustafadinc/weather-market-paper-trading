========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-04T22:09:02.707852Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          65172
  orderbook seviyesi     3483414
  tahmin snapshot          43470
  karar                    13470
  simüle fill               3494
  çözümlenmiş kova          1584

## Brier skoru  (düşük = iyi, 1542 kova)
  model                  0.1304
  piyasa (mid)           0.1334   n=1542
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0030  ±0.0034  %95 [-0.0037, +0.0097]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=222  0.1283 / 0.2023   fark +0.0740
    CHI   n=222  0.1336 / 0.1145   fark -0.0190
    DEN   n=216  0.1457 / 0.2013   fark +0.0556
    LAX   n=216  0.1260 / 0.0981   fark -0.0279
    MIA   n=222  0.1360 / 0.1140   fark -0.0221
    NY    n=222  0.1081 / 0.0880   fark -0.0201
    PHL   n=222  0.1354 / 0.1165   fark -0.0189
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       571         0.034         0.056   +0.022
  0.1-0.2       393         0.151         0.186   +0.034
  0.2-0.3       326         0.246         0.245   -0.001
  0.3-0.4       167         0.346         0.251   -0.095
  0.4-0.5        64         0.435         0.312   -0.122
  0.5-0.6        17         0.549         0.353   -0.196
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3434)
  işlem sayısı                    3434
  kazanan                         1386  (%40)
  ort. İDDİA EDİLEN edge       +16.07p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.83p   ±0.7p  %95 [+0.4p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3424.88 $
  PnL fee ÖNCESİ             +27242.40 $
  PnL fee SONRASI            +23817.52 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8870.97 $   %90 aralık [-14822.44, -2372.24]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1334 (model 0.1304)

  bizim (fee sonrası)            +23817.52 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
