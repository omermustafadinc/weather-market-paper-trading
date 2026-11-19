========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-19T09:59:40.654777Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         125490
  orderbook seviyesi     6651192
  tahmin snapshot          84105
  karar                    25944
  simüle fill               6667
  çözümlenmiş kova          3486

## Brier skoru  (düşük = iyi, 3384 kova)
  model                  0.1332
  piyasa (mid)           0.1243   n=3384
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0088  ±0.0028  %95 [-0.0142, -0.0034]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=486  0.1214 / 0.1922   fark +0.0709
    CHI   n=486  0.1437 / 0.1053   fark -0.0384
    DEN   n=486  0.1406 / 0.1930   fark +0.0524
    LAX   n=486  0.1204 / 0.0884   fark -0.0320
    MIA   n=480  0.1390 / 0.1024   fark -0.0367
    NY    n=480  0.1156 / 0.0920   fark -0.0236
    PHL   n=480  0.1515 / 0.0961   fark -0.0554
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1384         0.031         0.057   +0.026
  0.1-0.2       758         0.150         0.197   +0.047
  0.2-0.3       605         0.247         0.269   +0.022
  0.3-0.4       385         0.345         0.236   -0.109
  0.4-0.5       168         0.440         0.304   -0.137
  0.5-0.6        52         0.548         0.327   -0.222
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6627)
  işlem sayısı                    6627
  kazanan                         2591  (%39)
  ort. İDDİA EDİLEN edge       +19.04p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.55p   ±0.5p  %95 [+0.6p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6750.15 $
  PnL fee ÖNCESİ             +49986.11 $
  PnL fee SONRASI            +43235.96 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15645.33 $   %90 aralık [-25837.52, -6457.83]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1243 (model 0.1332)

  bizim (fee sonrası)            +43235.96 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
