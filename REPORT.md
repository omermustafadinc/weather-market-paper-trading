========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-19T19:12:25.149314Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         125826
  orderbook seviyesi     6669355
  tahmin snapshot          84357
  karar                    26028
  simüle fill               6687
  çözümlenmiş kova          3498

## Brier skoru  (düşük = iyi, 3396 kova)
  model                  0.1332
  piyasa (mid)           0.1247   n=3396
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0085  ±0.0028  %95 [-0.0139, -0.0031]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=492  0.1221 / 0.1926   fark +0.0705
    CHI   n=486  0.1437 / 0.1053   fark -0.0384
    DEN   n=492  0.1399 / 0.1931   fark +0.0532
    LAX   n=486  0.1204 / 0.0884   fark -0.0320
    MIA   n=480  0.1390 / 0.1024   fark -0.0367
    NY    n=480  0.1156 / 0.0920   fark -0.0236
    PHL   n=480  0.1515 / 0.0961   fark -0.0554
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1387         0.031         0.057   +0.026
  0.1-0.2       764         0.150         0.196   +0.046
  0.2-0.3       605         0.247         0.269   +0.022
  0.3-0.4       387         0.345         0.238   -0.108
  0.4-0.5       169         0.440         0.302   -0.138
  0.5-0.6        52         0.548         0.327   -0.222
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6630)
  işlem sayısı                    6630
  kazanan                         2592  (%39)
  ort. İDDİA EDİLEN edge       +19.04p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.56p   ±0.5p  %95 [+0.6p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6755.65 $
  PnL fee ÖNCESİ             +50513.73 $
  PnL fee SONRASI            +43758.08 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15963.56 $   %90 aralık [-25348.57, -5356.77]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1247 (model 0.1332)

  bizim (fee sonrası)            +43758.08 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
