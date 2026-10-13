========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-13T02:05:53.542887Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          74688
  orderbook seviyesi     3987277
  tahmin snapshot          49833
  karar                    15372
  simüle fill               3977
  çözümlenmiş kova          1932

## Brier skoru  (düşük = iyi, 1848 kova)
  model                  0.1333
  piyasa (mid)           0.1327   n=1848
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0007  ±0.0032  %95 [-0.0070, +0.0057]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=264  0.1302 / 0.2054   fark +0.0752
    CHI   n=264  0.1406 / 0.1105   fark -0.0301
    DEN   n=264  0.1505 / 0.2027   fark +0.0522
    LAX   n=264  0.1271 / 0.0968   fark -0.0303
    MIA   n=264  0.1347 / 0.1085   fark -0.0262
    NY    n=264  0.1098 / 0.0911   fark -0.0188
    PHL   n=264  0.1404 / 0.1136   fark -0.0268
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       695         0.033         0.063   +0.030
  0.1-0.2       461         0.151         0.191   +0.040
  0.2-0.3       385         0.247         0.249   +0.003
  0.3-0.4       201         0.345         0.224   -0.122
  0.4-0.5        77         0.437         0.299   -0.138
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         4         0.652         0.500   -0.152
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
  (b) rastgele işlem (ort.)       -9452.22 $   %90 aralık [-16581.43, -1146.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1327 (model 0.1333)

  bizim (fee sonrası)            +20664.00 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
