========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-12T19:53:27.601640Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          74520
  orderbook seviyesi     3978617
  tahmin snapshot          49623
  karar                    15372
  simüle fill               3977
  çözümlenmiş kova          1902

## Brier skoru  (düşük = iyi, 1818 kova)
  model                  0.1332
  piyasa (mid)           0.1333   n=1818
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0001  ±0.0033  %95 [-0.0063, +0.0065]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=264  0.1302 / 0.2054   fark +0.0752
    CHI   n=258  0.1386 / 0.1096   fark -0.0290
    DEN   n=264  0.1505 / 0.2027   fark +0.0522
    LAX   n=258  0.1271 / 0.0972   fark -0.0300
    MIA   n=258  0.1348 / 0.1098   fark -0.0249
    NY    n=258  0.1097 / 0.0905   fark -0.0191
    PHL   n=258  0.1410 / 0.1145   fark -0.0265
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       682         0.033         0.063   +0.030
  0.1-0.2       457         0.151         0.193   +0.042
  0.2-0.3       376         0.247         0.245   -0.002
  0.3-0.4       198         0.346         0.227   -0.118
  0.4-0.5        77         0.437         0.299   -0.138
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3906)
  işlem sayısı                    3906
  kazanan                         1547  (%40)
  ort. İDDİA EDİLEN edge       +16.62p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.21p   ±0.7p  %95 [-0.1p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3941.94 $
  PnL fee ÖNCESİ             +25437.77 $
  PnL fee SONRASI            +21495.83 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9611.24 $   %90 aralık [-17552.24, -2562.73]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1333 (model 0.1332)

  bizim (fee sonrası)            +21495.83 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
