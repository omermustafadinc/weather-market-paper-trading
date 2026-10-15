========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-15T10:38:13.132732Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          77976
  orderbook seviyesi     4162980
  tahmin snapshot          51597
  karar                    16008
  simüle fill               4155
  çözümlenmiş kova          2016

## Brier skoru  (düşük = iyi, 1932 kova)
  model                  0.1325
  piyasa (mid)           0.1312   n=1932
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0013  ±0.0032  %95 [-0.0075, +0.0049]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=276  0.1297 / 0.2057   fark +0.0760
    CHI   n=276  0.1382 / 0.1086   fark -0.0295
    DEN   n=276  0.1497 / 0.1990   fark +0.0493
    LAX   n=276  0.1250 / 0.0947   fark -0.0303
    MIA   n=276  0.1349 / 0.1051   fark -0.0298
    NY    n=276  0.1096 / 0.0915   fark -0.0181
    PHL   n=276  0.1402 / 0.1136   fark -0.0266
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       727         0.034         0.061   +0.027
  0.1-0.2       482         0.151         0.191   +0.040
  0.2-0.3       404         0.247         0.252   +0.006
  0.3-0.4       210         0.345         0.224   -0.121
  0.4-0.5        78         0.438         0.295   -0.143
  0.5-0.6        23         0.550         0.348   -0.203
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4057)
  işlem sayısı                    4057
  kazanan                         1589  (%39)
  ort. İDDİA EDİLEN edge       +16.76p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.79p   ±0.6p  %95 [-0.5p, +2.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4092.83 $
  PnL fee ÖNCESİ             +23476.19 $
  PnL fee SONRASI            +19383.36 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10007.32 $   %90 aralık [-18407.18, -2136.79]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1312 (model 0.1325)

  bizim (fee sonrası)            +19383.36 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
