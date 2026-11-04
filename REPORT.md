========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-04T18:14:33.656762Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         109590
  orderbook seviyesi     5844809
  tahmin snapshot          72891
  karar                    22656
  simüle fill               5855
  çözümlenmiş kova          2868

## Brier skoru  (düşük = iyi, 2784 kova)
  model                  0.1294
  piyasa (mid)           0.1252   n=2784
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0041  ±0.0029  %95 [-0.0098, +0.0016]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=402  0.1214 / 0.1979   fark +0.0765
    CHI   n=396  0.1379 / 0.1043   fark -0.0336
    DEN   n=402  0.1366 / 0.1896   fark +0.0530
    LAX   n=396  0.1195 / 0.0850   fark -0.0346
    MIA   n=396  0.1371 / 0.1043   fark -0.0328
    NY    n=396  0.1058 / 0.0897   fark -0.0161
    PHL   n=396  0.1472 / 0.1037   fark -0.0435
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1106         0.032         0.052   +0.020
  0.1-0.2       649         0.150         0.185   +0.035
  0.2-0.3       517         0.247         0.265   +0.018
  0.3-0.4       329         0.345         0.246   -0.099
  0.4-0.5       125         0.439         0.328   -0.111
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        12         0.631         0.583   -0.047
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5781)
  işlem sayısı                    5781
  kazanan                         2264  (%39)
  ort. İDDİA EDİLEN edge       +18.18p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.70p   ±0.5p  %95 [+0.6p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5904.04 $
  PnL fee ÖNCESİ             +48159.47 $
  PnL fee SONRASI            +42255.43 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14834.16 $   %90 aralık [-25613.15, -4379.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1252 (model 0.1294)

  bizim (fee sonrası)            +42255.43 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
