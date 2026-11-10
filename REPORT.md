========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-10T02:52:23.495569Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         116046
  orderbook seviyesi     6171903
  tahmin snapshot          77301
  karar                    24036
  simüle fill               6202
  çözümlenmiş kova          3108

## Brier skoru  (düşük = iyi, 3024 kova)
  model                  0.1311
  piyasa (mid)           0.1239   n=3024
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0072  ±0.0028  %95 [-0.0128, -0.0016]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=432  0.1218 / 0.1948   fark +0.0730
    CHI   n=432  0.1393 / 0.1046   fark -0.0347
    DEN   n=432  0.1408 / 0.1923   fark +0.0515
    LAX   n=432  0.1210 / 0.0849   fark -0.0362
    MIA   n=432  0.1372 / 0.1012   fark -0.0360
    NY    n=432  0.1072 / 0.0904   fark -0.0167
    PHL   n=432  0.1501 / 0.0990   fark -0.0511
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1218         0.032         0.052   +0.020
  0.1-0.2       688         0.150         0.199   +0.049
  0.2-0.3       557         0.246         0.264   +0.017
  0.3-0.4       349         0.345         0.241   -0.104
  0.4-0.5       147         0.440         0.306   -0.133
  0.5-0.6        41         0.546         0.341   -0.205
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6162)
  işlem sayısı                    6162
  kazanan                         2408  (%39)
  ort. İDDİA EDİLEN edge       +18.54p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.73p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6293.83 $
  PnL fee ÖNCESİ             +48871.42 $
  PnL fee SONRASI            +42577.59 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15116.26 $   %90 aralık [-25239.64, -4881.52]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1239 (model 0.1311)

  bizim (fee sonrası)            +42577.59 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
