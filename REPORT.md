========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-29T16:59:51.640216Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         102030
  orderbook seviyesi     5448285
  tahmin snapshot          68229
  karar                    21060
  simüle fill               5454
  çözümlenmiş kova          2616

## Brier skoru  (düşük = iyi, 2532 kova)
  model                  0.1304
  piyasa (mid)           0.1270   n=2532
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0034  ±0.0030  %95 [-0.0093, +0.0026]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=366  0.1227 / 0.2017   fark +0.0789
    CHI   n=360  0.1410 / 0.1042   fark -0.0368
    DEN   n=366  0.1406 / 0.1904   fark +0.0498
    LAX   n=360  0.1210 / 0.0885   fark -0.0326
    MIA   n=360  0.1347 / 0.1051   fark -0.0296
    NY    n=360  0.1057 / 0.0905   fark -0.0152
    PHL   n=360  0.1470 / 0.1066   fark -0.0404
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       990         0.032         0.056   +0.023
  0.1-0.2       602         0.150         0.189   +0.040
  0.2-0.3       484         0.247         0.258   +0.011
  0.3-0.4       296         0.346         0.230   -0.116
  0.4-0.5       110         0.439         0.336   -0.103
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5367)
  işlem sayısı                    5367
  kazanan                         2096  (%39)
  ort. İDDİA EDİLEN edge       +18.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.64p   ±0.6p  %95 [+0.5p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5504.72 $
  PnL fee ÖNCESİ             +44894.41 $
  PnL fee SONRASI            +39389.69 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14478.84 $   %90 aralık [-24128.96, -6074.43]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1270 (model 0.1304)

  bizim (fee sonrası)            +39389.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
