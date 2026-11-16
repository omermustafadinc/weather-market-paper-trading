========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-16T11:34:13.104251Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         122970
  orderbook seviyesi     6526316
  tahmin snapshot          82341
  karar                    25440
  simüle fill               6547
  çözümlenmiş kova          3360

## Brier skoru  (düşük = iyi, 3276 kova)
  model                  0.1317
  piyasa (mid)           0.1244   n=3276
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0073  ±0.0028  %95 [-0.0127, -0.0019]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=468  0.1200 / 0.1910   fark +0.0710
    CHI   n=468  0.1409 / 0.1077   fark -0.0333
    DEN   n=468  0.1412 / 0.1921   fark +0.0510
    LAX   n=468  0.1195 / 0.0878   fark -0.0317
    MIA   n=468  0.1379 / 0.1034   fark -0.0346
    NY    n=468  0.1128 / 0.0916   fark -0.0212
    PHL   n=468  0.1496 / 0.0971   fark -0.0525
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1336         0.031         0.055   +0.023
  0.1-0.2       735         0.150         0.195   +0.045
  0.2-0.3       589         0.247         0.268   +0.022
  0.3-0.4       374         0.345         0.241   -0.105
  0.4-0.5       164         0.440         0.311   -0.129
  0.5-0.6        48         0.549         0.354   -0.194
  0.6-0.7        20         0.635         0.350   -0.285
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6487)
  işlem sayısı                    6487
  kazanan                         2551  (%39)
  ort. İDDİA EDİLEN edge       +18.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.87p   ±0.5p  %95 [+0.9p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6617.30 $
  PnL fee ÖNCESİ             +51783.01 $
  PnL fee SONRASI            +45165.71 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15598.54 $   %90 aralık [-27023.63, -3495.37]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1244 (model 0.1317)

  bizim (fee sonrası)            +45165.71 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
