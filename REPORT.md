========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-17T21:54:38.718667Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         124146
  orderbook seviyesi     6585857
  tahmin snapshot          83223
  karar                    25692
  simüle fill               6607
  çözümlenmiş kova          3432

## Brier skoru  (düşük = iyi, 3348 kova)
  model                  0.1328
  piyasa (mid)           0.1245   n=3348
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0083  ±0.0028  %95 [-0.0137, -0.0029]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=480  0.1213 / 0.1919   fark +0.0707
    CHI   n=474  0.1416 / 0.1067   fark -0.0350
    DEN   n=480  0.1403 / 0.1926   fark +0.0523
    LAX   n=474  0.1205 / 0.0893   fark -0.0312
    MIA   n=480  0.1390 / 0.1024   fark -0.0367
    NY    n=480  0.1156 / 0.0920   fark -0.0236
    PHL   n=480  0.1515 / 0.0961   fark -0.0554
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1371         0.031         0.056   +0.025
  0.1-0.2       748         0.150         0.198   +0.048
  0.2-0.3       598         0.247         0.268   +0.021
  0.3-0.4       381         0.345         0.239   -0.107
  0.4-0.5       167         0.440         0.305   -0.134
  0.5-0.6        51         0.548         0.333   -0.214
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6578)
  işlem sayısı                    6578
  kazanan                         2577  (%39)
  ort. İDDİA EDİLEN edge       +18.97p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.66p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6702.61 $
  PnL fee ÖNCESİ             +50606.05 $
  PnL fee SONRASI            +43903.44 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15561.05 $   %90 aralık [-26391.41, -6270.08]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1245 (model 0.1328)

  bizim (fee sonrası)            +43903.44 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
