========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-10T23:35:47.208863Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          24618
  orderbook seviyesi     1308361
  tahmin snapshot          17136
  karar                     4908
  simüle fill               1268
  çözümlenmiş kova           582

## Brier skoru  (düşük = iyi, 540 kova)
  model                  0.1259
  piyasa (mid)           0.1297   n=540
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0038  ±0.0052  %95 [-0.0064, +0.0140]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 78  0.1515 / 0.2074   fark +0.0559
    CHI   n= 78  0.1249 / 0.1047   fark -0.0201
    DEN   n= 78  0.1448 / 0.2120   fark +0.0671
    LAX   n= 72  0.0971 / 0.0907   fark -0.0063
    MIA   n= 78  0.1230 / 0.1080   fark -0.0150
    NY    n= 78  0.1077 / 0.0854   fark -0.0223
    PHL   n= 78  0.1304 / 0.0971   fark -0.0333
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       206         0.033         0.034   +0.001
  0.1-0.2       126         0.150         0.198   +0.048
  0.2-0.3       123         0.247         0.293   +0.046
  0.3-0.4        56         0.345         0.232   -0.113
  0.4-0.5        18         0.438         0.111   -0.326
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1190)
  işlem sayısı                    1190
  kazanan                          475  (%40)
  ort. İDDİA EDİLEN edge       +14.58p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.50p   ±1.2p  %95 [-1.8p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1195.11 $
  PnL fee ÖNCESİ              +2910.49 $
  PnL fee SONRASI             +1715.38 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2166.04 $   %90 aralık [-6213.15, +1578.05]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1297 (model 0.1259)

  bizim (fee sonrası)             +1715.38 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
