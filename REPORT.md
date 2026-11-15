========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-15T20:29:57.385101Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         122130
  orderbook seviyesi     6484031
  tahmin snapshot          81711
  karar                    25272
  simüle fill               6507
  çözümlenmiş kova          3330

## Brier skoru  (düşük = iyi, 3246 kova)
  model                  0.1313
  piyasa (mid)           0.1246   n=3246
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0067  ±0.0028  %95 [-0.0121, -0.0013]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=468  0.1200 / 0.1910   fark +0.0710
    CHI   n=462  0.1400 / 0.1063   fark -0.0337
    DEN   n=468  0.1412 / 0.1921   fark +0.0510
    LAX   n=462  0.1198 / 0.0871   fark -0.0327
    MIA   n=462  0.1372 / 0.1033   fark -0.0339
    NY    n=462  0.1124 / 0.0924   fark -0.0200
    PHL   n=462  0.1485 / 0.0980   fark -0.0506
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1319         0.031         0.053   +0.022
  0.1-0.2       732         0.150         0.195   +0.045
  0.2-0.3       588         0.247         0.269   +0.022
  0.3-0.4       370         0.345         0.238   -0.107
  0.4-0.5       162         0.440         0.315   -0.125
  0.5-0.6        47         0.550         0.362   -0.188
  0.6-0.7        18         0.635         0.389   -0.246
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6425)
  işlem sayısı                    6425
  kazanan                         2528  (%39)
  ort. İDDİA EDİLEN edge       +18.70p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.93p   ±0.5p  %95 [+0.9p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6557.35 $
  PnL fee ÖNCESİ             +52171.98 $
  PnL fee SONRASI            +45614.63 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15854.92 $   %90 aralık [-26005.35, -6638.65]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1246 (model 0.1313)

  bizim (fee sonrası)            +45614.63 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
