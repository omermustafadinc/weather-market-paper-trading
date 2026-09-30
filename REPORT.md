========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-30T00:12:21.163167Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          58248
  orderbook seviyesi     3111252
  tahmin snapshot          38808
  karar                    12024
  simüle fill               3141
  çözümlenmiş kova          1380

## Brier skoru  (düşük = iyi, 1338 kova)
  model                  0.1315
  piyasa (mid)           0.1338   n=1338
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0023  ±0.0037  %95 [-0.0049, +0.0095]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=192  0.1345 / 0.2103   fark +0.0758
    CHI   n=192  0.1298 / 0.1152   fark -0.0146
    DEN   n=192  0.1446 / 0.2016   fark +0.0570
    LAX   n=186  0.1241 / 0.0971   fark -0.0270
    MIA   n=192  0.1403 / 0.1129   fark -0.0273
    NY    n=192  0.1072 / 0.0843   fark -0.0229
    PHL   n=192  0.1398 / 0.1139   fark -0.0259
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       494         0.034         0.057   +0.023
  0.1-0.2       341         0.152         0.194   +0.042
  0.2-0.3       287         0.246         0.244   -0.003
  0.3-0.4       144         0.346         0.236   -0.110
  0.4-0.5        55         0.436         0.309   -0.127
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3087)
  işlem sayısı                    3087
  kazanan                         1235  (%40)
  ort. İDDİA EDİLEN edge       +16.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.83p   ±0.7p  %95 [+0.4p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3099.24 $
  PnL fee ÖNCESİ             +24176.55 $
  PnL fee SONRASI            +21077.31 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8394.27 $   %90 aralık [-14553.55, -1173.75]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1338 (model 0.1315)

  bizim (fee sonrası)            +21077.31 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
