========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-18T20:07:19.386521Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         124986
  orderbook seviyesi     6629882
  tahmin snapshot          83853
  karar                    25860
  simüle fill               6647
  çözümlenmiş kova          3456

## Brier skoru  (düşük = iyi, 3372 kova)
  model                  0.1330
  piyasa (mid)           0.1246   n=3372
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0084  ±0.0028  %95 [-0.0139, -0.0030]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=486  0.1214 / 0.1922   fark +0.0709
    CHI   n=480  0.1426 / 0.1056   fark -0.0369
    DEN   n=486  0.1406 / 0.1930   fark +0.0524
    LAX   n=480  0.1206 / 0.0891   fark -0.0315
    MIA   n=480  0.1390 / 0.1024   fark -0.0367
    NY    n=480  0.1156 / 0.0920   fark -0.0236
    PHL   n=480  0.1515 / 0.0961   fark -0.0554
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1379         0.031         0.057   +0.026
  0.1-0.2       756         0.150         0.197   +0.047
  0.2-0.3       603         0.247         0.269   +0.022
  0.3-0.4       383         0.345         0.238   -0.108
  0.4-0.5       167         0.440         0.305   -0.134
  0.5-0.6        52         0.548         0.327   -0.222
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6595)
  işlem sayısı                    6595
  kazanan                         2582  (%39)
  ort. İDDİA EDİLEN edge       +18.99p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.64p   ±0.5p  %95 [+0.6p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6722.41 $
  PnL fee ÖNCESİ             +50308.42 $
  PnL fee SONRASI            +43586.01 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15558.77 $   %90 aralık [-25127.92, -5268.19]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1246 (model 0.1330)

  bizim (fee sonrası)            +43586.01 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
