========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-29T20:34:02.122884Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          57912
  orderbook seviyesi     3094627
  tahmin snapshot          38556
  karar                    11940
  simüle fill               3119
  çözümlenmiş kova          1362

## Brier skoru  (düşük = iyi, 1320 kova)
  model                  0.1313
  piyasa (mid)           0.1335   n=1320
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0022  ±0.0037  %95 [-0.0050, +0.0095]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=192  0.1345 / 0.2103   fark +0.0758
    CHI   n=186  0.1269 / 0.1123   fark -0.0146
    DEN   n=192  0.1446 / 0.2016   fark +0.0570
    LAX   n=186  0.1241 / 0.0971   fark -0.0270
    MIA   n=192  0.1403 / 0.1129   fark -0.0273
    NY    n=186  0.1069 / 0.0842   fark -0.0228
    PHL   n=186  0.1412 / 0.1125   fark -0.0287
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       487         0.034         0.055   +0.021
  0.1-0.2       338         0.151         0.195   +0.044
  0.2-0.3       282         0.246         0.245   -0.002
  0.3-0.4       142         0.346         0.232   -0.114
  0.4-0.5        54         0.436         0.315   -0.121
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3047)
  işlem sayısı                    3047
  kazanan                         1221  (%40)
  ort. İDDİA EDİLEN edge       +16.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.97p   ±0.7p  %95 [+0.5p, +3.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3062.21 $
  PnL fee ÖNCESİ             +24586.93 $
  PnL fee SONRASI            +21524.72 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8356.65 $   %90 aralık [-15440.54, -1539.92]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1335 (model 0.1313)

  bizim (fee sonrası)            +21524.72 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
