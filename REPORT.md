========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-23T01:49:03.217693Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         129312
  orderbook seviyesi     6845435
  tahmin snapshot          86499
  karar                    26760
  simüle fill               6862
  çözümlenmiş kova          3648

## Brier skoru  (düşük = iyi, 3546 kova)
  model                  0.1337
  piyasa (mid)           0.1241   n=3546
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0096  ±0.0027  %95 [-0.0150, -0.0043]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=510  0.1196 / 0.1913   fark +0.0717
    CHI   n=510  0.1458 / 0.1037   fark -0.0421
    DEN   n=510  0.1407 / 0.1940   fark +0.0532
    LAX   n=504  0.1203 / 0.0891   fark -0.0313
    MIA   n=504  0.1394 / 0.1000   fark -0.0393
    NY    n=504  0.1171 / 0.0920   fark -0.0252
    PHL   n=504  0.1529 / 0.0970   fark -0.0559
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1448         0.031         0.060   +0.029
  0.1-0.2       795         0.150         0.196   +0.047
  0.2-0.3       637         0.247         0.264   +0.017
  0.3-0.4       398         0.345         0.236   -0.109
  0.4-0.5       176         0.440         0.290   -0.150
  0.5-0.6        58         0.547         0.345   -0.202
  0.6-0.7        22         0.635         0.364   -0.271
  0.7-0.8         3         0.737         0.667   -0.070
  0.8-0.9         8         0.845         0.500   -0.345
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6805)
  işlem sayısı                    6805
  kazanan                         2661  (%39)
  ort. İDDİA EDİLEN edge       +19.18p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.43p   ±0.5p  %95 [+0.4p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6914.39 $
  PnL fee ÖNCESİ             +49074.05 $
  PnL fee SONRASI            +42159.66 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16094.00 $   %90 aralık [-26473.35, -4573.41]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1241 (model 0.1337)

  bizim (fee sonrası)            +42159.66 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
