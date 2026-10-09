========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-09T15:45:50.106207Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          70368
  orderbook seviyesi     3762944
  tahmin snapshot          47124
  karar                    14514
  simüle fill               3759
  çözümlenmiş kova          1776

## Brier skoru  (düşük = iyi, 1692 kova)
  model                  0.1331
  piyasa (mid)           0.1335   n=1692
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0003  ±0.0033  %95 [-0.0062, +0.0068]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=246  0.1338 / 0.2044   fark +0.0706
    CHI   n=240  0.1361 / 0.1106   fark -0.0254
    DEN   n=246  0.1493 / 0.2015   fark +0.0522
    LAX   n=240  0.1292 / 0.0998   fark -0.0294
    MIA   n=240  0.1355 / 0.1110   fark -0.0246
    NY    n=240  0.1093 / 0.0912   fark -0.0181
    PHL   n=240  0.1385 / 0.1123   fark -0.0262
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       631         0.033         0.062   +0.029
  0.1-0.2       432         0.151         0.192   +0.041
  0.2-0.3       345         0.247         0.243   -0.003
  0.3-0.4       187         0.346         0.241   -0.106
  0.4-0.5        73         0.437         0.288   -0.149
  0.5-0.6        20         0.551         0.300   -0.251
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3697)
  işlem sayısı                    3697
  kazanan                         1481  (%40)
  ort. İDDİA EDİLEN edge       +16.41p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.42p   ±0.7p  %95 [+0.1p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3687.78 $
  PnL fee ÖNCESİ             +25518.77 $
  PnL fee SONRASI            +21830.99 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9015.94 $   %90 aralık [-17004.76, -1117.68]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1335 (model 0.1331)

  bizim (fee sonrası)            +21830.99 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
