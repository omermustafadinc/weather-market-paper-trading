========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-28T17:32:41.472947Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          56568
  orderbook seviyesi     3021021
  tahmin snapshot          37800
  karar                    11646
  simüle fill               3046
  çözümlenmiş kova          1314

## Brier skoru  (düşük = iyi, 1272 kova)
  model                  0.1315
  piyasa (mid)           0.1347   n=1272
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0032  ±0.0038  %95 [-0.0042, +0.0106]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=186  0.1364 / 0.2107   fark +0.0743
    CHI   n=180  0.1259 / 0.1140   fark -0.0119
    DEN   n=186  0.1458 / 0.2037   fark +0.0578
    LAX   n=180  0.1244 / 0.0965   fark -0.0279
    MIA   n=180  0.1386 / 0.1149   fark -0.0237
    NY    n=180  0.1077 / 0.0862   fark -0.0215
    PHL   n=180  0.1409 / 0.1119   fark -0.0290
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       470         0.034         0.057   +0.023
  0.1-0.2       325         0.152         0.191   +0.039
  0.2-0.3       271         0.246         0.247   +0.001
  0.3-0.4       140         0.346         0.236   -0.111
  0.4-0.5        49         0.436         0.306   -0.130
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2948)
  işlem sayısı                    2948
  kazanan                         1197  (%41)
  ort. İDDİA EDİLEN edge       +15.86p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.47p   ±0.8p  %95 [+1.0p, +3.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2968.44 $
  PnL fee ÖNCESİ             +25099.28 $
  PnL fee SONRASI            +22130.84 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7846.11 $   %90 aralık [-13232.51, -1778.35]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1347 (model 0.1315)

  bizim (fee sonrası)            +22130.84 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
