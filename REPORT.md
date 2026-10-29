========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-29T00:15:55.243214Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         101190
  orderbook seviyesi     5401968
  tahmin snapshot          67599
  karar                    20892
  simüle fill               5411
  çözümlenmiş kova          2598

## Brier skoru  (düşük = iyi, 2514 kova)
  model                  0.1307
  piyasa (mid)           0.1271   n=2514
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0036  ±0.0030  %95 [-0.0096, +0.0023]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=360  0.1237 / 0.2044   fark +0.0807
    CHI   n=360  0.1410 / 0.1042   fark -0.0368
    DEN   n=360  0.1419 / 0.1901   fark +0.0482
    LAX   n=354  0.1208 / 0.0882   fark -0.0326
    MIA   n=360  0.1347 / 0.1051   fark -0.0296
    NY    n=360  0.1057 / 0.0905   fark -0.0152
    PHL   n=360  0.1470 / 0.1066   fark -0.0404
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       983         0.032         0.056   +0.024
  0.1-0.2       598         0.150         0.191   +0.041
  0.2-0.3       479         0.247         0.259   +0.012
  0.3-0.4       296         0.346         0.230   -0.116
  0.4-0.5       108         0.439         0.324   -0.114
  0.5-0.6        37         0.547         0.351   -0.196
  0.6-0.7         8         0.639         0.625   -0.014
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5347)
  işlem sayısı                    5347
  kazanan                         2090  (%39)
  ort. İDDİA EDİLEN edge       +18.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.66p   ±0.6p  %95 [+0.6p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5487.62 $
  PnL fee ÖNCESİ             +44102.14 $
  PnL fee SONRASI            +38614.52 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13540.39 $   %90 aralık [-22524.64, -3976.47]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1271 (model 0.1307)

  bizim (fee sonrası)            +38614.52 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
