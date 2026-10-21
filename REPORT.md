========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-21T05:08:48.501865Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          88506
  orderbook seviyesi     4717916
  tahmin snapshot          58653
  karar                    18246
  simüle fill               4732
  çözümlenmiş kova          2268

## Brier skoru  (düşük = iyi, 2184 kova)
  model                  0.1323
  piyasa (mid)           0.1291   n=2184
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0033  ±0.0031  %95 [-0.0094, +0.0029]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=312  0.1290 / 0.2020   fark +0.0731
    CHI   n=312  0.1400 / 0.1083   fark -0.0317
    DEN   n=312  0.1495 / 0.2003   fark +0.0509
    LAX   n=312  0.1201 / 0.0894   fark -0.0307
    MIA   n=312  0.1365 / 0.1018   fark -0.0347
    NY    n=312  0.1075 / 0.0905   fark -0.0170
    PHL   n=312  0.1439 / 0.1111   fark -0.0328
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       837         0.033         0.062   +0.029
  0.1-0.2       539         0.150         0.191   +0.041
  0.2-0.3       433         0.247         0.256   +0.009
  0.3-0.4       244         0.345         0.209   -0.136
  0.4-0.5        91         0.439         0.308   -0.131
  0.5-0.6        28         0.549         0.357   -0.191
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4660)
  işlem sayısı                    4660
  kazanan                         1780  (%38)
  ort. İDDİA EDİLEN edge       +17.62p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.43p   ±0.6p  %95 [-0.7p, +1.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4740.59 $
  PnL fee ÖNCESİ             +26068.67 $
  PnL fee SONRASI            +21328.08 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11948.60 $   %90 aralık [-19075.48, -4411.10]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1291 (model 0.1323)

  bizim (fee sonrası)            +21328.08 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
