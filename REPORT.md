========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-09T19:51:30.521022Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         115710
  orderbook seviyesi     6155049
  tahmin snapshot          77175
  karar                    23952
  simüle fill               6182
  çözümlenmiş kova          3078

## Brier skoru  (düşük = iyi, 2994 kova)
  model                  0.1307
  piyasa (mid)           0.1247   n=2994
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0060  ±0.0028  %95 [-0.0116, -0.0005]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=432  0.1218 / 0.1948   fark +0.0730
    CHI   n=426  0.1383 / 0.1054   fark -0.0329
    DEN   n=432  0.1408 / 0.1923   fark +0.0515
    LAX   n=426  0.1204 / 0.0849   fark -0.0356
    MIA   n=426  0.1372 / 0.1022   fark -0.0349
    NY    n=426  0.1074 / 0.0912   fark -0.0162
    PHL   n=426  0.1490 / 0.0999   fark -0.0491
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1203         0.032         0.051   +0.019
  0.1-0.2       683         0.150         0.198   +0.048
  0.2-0.3       553         0.246         0.266   +0.019
  0.3-0.4       347         0.345         0.242   -0.103
  0.4-0.5       145         0.439         0.303   -0.136
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6110)
  işlem sayısı                    6110
  kazanan                         2393  (%39)
  ort. İDDİA EDİLEN edge       +18.47p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.85p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6245.14 $
  PnL fee ÖNCESİ             +49619.19 $
  PnL fee SONRASI            +43374.05 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15788.52 $   %90 aralık [-25916.46, -4876.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1247 (model 0.1307)

  bizim (fee sonrası)            +43374.05 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
