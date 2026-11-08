========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-08T18:32:42.073517Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         114534
  orderbook seviyesi     6095657
  tahmin snapshot          76293
  karar                    23700
  simüle fill               6122
  çözümlenmiş kova          3036

## Brier skoru  (düşük = iyi, 2952 kova)
  model                  0.1305
  piyasa (mid)           0.1253   n=2952
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0052  ±0.0028  %95 [-0.0108, +0.0003]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=426  0.1225 / 0.1954   fark +0.0729
    CHI   n=420  0.1373 / 0.1059   fark -0.0313
    DEN   n=426  0.1403 / 0.1918   fark +0.0515
    LAX   n=420  0.1199 / 0.0855   fark -0.0343
    MIA   n=420  0.1371 / 0.1031   fark -0.0340
    NY    n=420  0.1088 / 0.0923   fark -0.0165
    PHL   n=420  0.1478 / 0.1009   fark -0.0469
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1184         0.032         0.052   +0.019
  0.1-0.2       674         0.150         0.194   +0.044
  0.2-0.3       545         0.247         0.268   +0.021
  0.3-0.4       347         0.345         0.242   -0.103
  0.4-0.5       142         0.440         0.303   -0.137
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6050)
  işlem sayısı                    6050
  kazanan                         2368  (%39)
  ort. İDDİA EDİLEN edge       +18.35p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.83p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6182.80 $
  PnL fee ÖNCESİ             +49607.39 $
  PnL fee SONRASI            +43424.59 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15259.20 $   %90 aralık [-24636.40, -6529.67]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1253 (model 0.1305)

  bizim (fee sonrası)            +43424.59 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
