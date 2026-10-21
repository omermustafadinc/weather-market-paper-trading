========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-21T19:30:06.811532Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          89346
  orderbook seviyesi     4767056
  tahmin snapshot          59409
  karar                    18414
  simüle fill               4774
  çözümlenmiş kova          2280

## Brier skoru  (düşük = iyi, 2196 kova)
  model                  0.1322
  piyasa (mid)           0.1296   n=2196
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0026  ±0.0031  %95 [-0.0088, +0.0035]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=318  0.1280 / 0.2025   fark +0.0745
    CHI   n=312  0.1400 / 0.1083   fark -0.0317
    DEN   n=318  0.1493 / 0.2007   fark +0.0513
    LAX   n=312  0.1201 / 0.0894   fark -0.0307
    MIA   n=312  0.1365 / 0.1018   fark -0.0347
    NY    n=312  0.1075 / 0.0905   fark -0.0170
    PHL   n=312  0.1439 / 0.1111   fark -0.0328
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       843         0.033         0.062   +0.029
  0.1-0.2       541         0.150         0.190   +0.040
  0.2-0.3       434         0.247         0.258   +0.011
  0.3-0.4       245         0.345         0.208   -0.137
  0.4-0.5        92         0.439         0.315   -0.123
  0.5-0.6        29         0.548         0.345   -0.203
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4674)
  işlem sayısı                    4674
  kazanan                         1790  (%38)
  ort. İDDİA EDİLEN edge       +17.64p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.54p   ±0.6p  %95 [-0.6p, +1.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4755.70 $
  PnL fee ÖNCESİ             +28651.71 $
  PnL fee SONRASI            +23896.01 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11915.76 $   %90 aralık [-19916.21, -3704.95]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1296 (model 0.1322)

  bizim (fee sonrası)            +23896.01 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
