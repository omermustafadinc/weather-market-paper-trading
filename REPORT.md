========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-30T16:25:19.011088Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          59088
  orderbook seviyesi     3157098
  tahmin snapshot          39438
  karar                    12192
  simüle fill               3185
  çözümlenmiş kova          1398

## Brier skoru  (düşük = iyi, 1356 kova)
  model                  0.1316
  piyasa (mid)           0.1340   n=1356
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0025  ±0.0036  %95 [-0.0046, +0.0096]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=198  0.1340 / 0.2093   fark +0.0753
    CHI   n=192  0.1298 / 0.1152   fark -0.0146
    DEN   n=198  0.1447 / 0.2005   fark +0.0559
    LAX   n=192  0.1246 / 0.0976   fark -0.0270
    MIA   n=192  0.1403 / 0.1129   fark -0.0273
    NY    n=192  0.1072 / 0.0843   fark -0.0229
    PHL   n=192  0.1398 / 0.1139   fark -0.0259
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       497         0.034         0.056   +0.022
  0.1-0.2       351         0.151         0.194   +0.042
  0.2-0.3       290         0.247         0.245   -0.002
  0.3-0.4       146         0.346         0.233   -0.113
  0.4-0.5        55         0.436         0.309   -0.127
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3099)
  işlem sayısı                    3099
  kazanan                         1244  (%40)
  ort. İDDİA EDİLEN edge       +16.08p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.01p   ±0.7p  %95 [+0.6p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3110.62 $
  PnL fee ÖNCESİ             +25143.01 $
  PnL fee SONRASI            +22032.39 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8370.12 $   %90 aralık [-14935.48, -1517.92]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1340 (model 0.1316)

  bizim (fee sonrası)            +22032.39 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
