========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-23T22:07:16.663727Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         129816
  orderbook seviyesi     6870971
  tahmin snapshot          86877
  karar                    26844
  simüle fill               6883
  çözümlenmiş kova          3684

## Brier skoru  (düşük = iyi, 3582 kova)
  model                  0.1337
  piyasa (mid)           0.1238   n=3582
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0099  ±0.0027  %95 [-0.0153, -0.0046]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=516  0.1195 / 0.1905   fark +0.0710
    CHI   n=510  0.1458 / 0.1037   fark -0.0421
    DEN   n=516  0.1394 / 0.1920   fark +0.0526
    LAX   n=510  0.1210 / 0.0883   fark -0.0327
    MIA   n=510  0.1389 / 0.1007   fark -0.0382
    NY    n=510  0.1181 / 0.0926   fark -0.0255
    PHL   n=510  0.1534 / 0.0970   fark -0.0564
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1466         0.031         0.061   +0.030
  0.1-0.2       799         0.150         0.196   +0.047
  0.2-0.3       642         0.247         0.262   +0.014
  0.3-0.4       404         0.345         0.238   -0.107
  0.4-0.5       177         0.440         0.288   -0.151
  0.5-0.6        59         0.547         0.339   -0.208
  0.6-0.7        23         0.635         0.391   -0.244
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6847)
  işlem sayısı                    6847
  kazanan                         2683  (%39)
  ort. İDDİA EDİLEN edge       +19.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.49p   ±0.5p  %95 [+0.5p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6954.90 $
  PnL fee ÖNCESİ             +49333.10 $
  PnL fee SONRASI            +42378.20 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15836.72 $   %90 aralık [-26366.59, -4870.97]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1238 (model 0.1337)

  bizim (fee sonrası)            +42378.20 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
