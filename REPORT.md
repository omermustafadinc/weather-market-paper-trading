========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-13T02:06:43.359421Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         119070
  orderbook seviyesi     6324228
  tahmin snapshot          79569
  karar                    24666
  simüle fill               6358
  çözümlenmiş kova          3228

## Brier skoru  (düşük = iyi, 3144 kova)
  model                  0.1319
  piyasa (mid)           0.1249   n=3144
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0070  ±0.0028  %95 [-0.0125, -0.0015]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=450  0.1217 / 0.1940   fark +0.0723
    CHI   n=450  0.1401 / 0.1061   fark -0.0341
    DEN   n=450  0.1408 / 0.1935   fark +0.0528
    LAX   n=444  0.1222 / 0.0852   fark -0.0370
    MIA   n=450  0.1382 / 0.1026   fark -0.0355
    NY    n=450  0.1104 / 0.0928   fark -0.0176
    PHL   n=450  0.1501 / 0.0995   fark -0.0505
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1274         0.032         0.053   +0.022
  0.1-0.2       710         0.150         0.200   +0.050
  0.2-0.3       573         0.247         0.269   +0.022
  0.3-0.4       361         0.345         0.235   -0.110
  0.4-0.5       156         0.441         0.295   -0.146
  0.5-0.6        44         0.548         0.341   -0.207
  0.6-0.7        17         0.637         0.412   -0.225
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6327)
  işlem sayısı                    6327
  kazanan                         2480  (%39)
  ort. İDDİA EDİLEN edge       +18.65p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.87p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6470.05 $
  PnL fee ÖNCESİ             +51300.43 $
  PnL fee SONRASI            +44830.38 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15325.98 $   %90 aralık [-25042.51, -5227.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1249 (model 0.1319)

  bizim (fee sonrası)            +44830.38 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
