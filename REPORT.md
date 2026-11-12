========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-12T13:34:47.094692Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         118566
  orderbook seviyesi     6300652
  tahmin snapshot          79191
  karar                    24540
  simüle fill               6327
  çözümlenmiş kova          3192

## Brier skoru  (düşük = iyi, 3108 kova)
  model                  0.1315
  piyasa (mid)           0.1240   n=3108
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0075  ±0.0028  %95 [-0.0130, -0.0020]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=444  0.1210 / 0.1936   fark +0.0726
    CHI   n=444  0.1405 / 0.1051   fark -0.0354
    DEN   n=444  0.1409 / 0.1932   fark +0.0523
    LAX   n=444  0.1222 / 0.0852   fark -0.0370
    MIA   n=444  0.1371 / 0.1016   fark -0.0355
    NY    n=444  0.1088 / 0.0907   fark -0.0181
    PHL   n=444  0.1498 / 0.0984   fark -0.0514
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1258         0.032         0.052   +0.021
  0.1-0.2       704         0.150         0.199   +0.049
  0.2-0.3       565         0.246         0.269   +0.023
  0.3-0.4       360         0.345         0.236   -0.109
  0.4-0.5       152         0.441         0.303   -0.138
  0.5-0.6        44         0.548         0.341   -0.207
  0.6-0.7        16         0.633         0.438   -0.195
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6264)
  işlem sayısı                    6264
  kazanan                         2449  (%39)
  ort. İDDİA EDİLEN edge       +18.62p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.76p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6399.51 $
  PnL fee ÖNCESİ             +50743.41 $
  PnL fee SONRASI            +44343.90 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14702.35 $   %90 aralık [-23778.80, -4229.26]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1240 (model 0.1315)

  bizim (fee sonrası)            +44343.90 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
