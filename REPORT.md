========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-11T02:50:13.285682Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         117222
  orderbook seviyesi     6229615
  tahmin snapshot          78183
  karar                    24288
  simüle fill               6264
  çözümlenmiş kova          3144

## Brier skoru  (düşük = iyi, 3060 kova)
  model                  0.1310
  piyasa (mid)           0.1236   n=3060
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0074  ±0.0028  %95 [-0.0130, -0.0018]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=438  0.1208 / 0.1933   fark +0.0725
    CHI   n=438  0.1403 / 0.1050   fark -0.0353
    DEN   n=438  0.1399 / 0.1927   fark +0.0528
    LAX   n=432  0.1210 / 0.0849   fark -0.0362
    MIA   n=438  0.1374 / 0.1002   fark -0.0371
    NY    n=438  0.1073 / 0.0896   fark -0.0177
    PHL   n=438  0.1501 / 0.0991   fark -0.0511
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1237         0.032         0.052   +0.020
  0.1-0.2       693         0.150         0.198   +0.048
  0.2-0.3       561         0.246         0.266   +0.019
  0.3-0.4       351         0.345         0.242   -0.103
  0.4-0.5       150         0.440         0.307   -0.134
  0.5-0.6        44         0.548         0.341   -0.207
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6202)
  işlem sayısı                    6202
  kazanan                         2420  (%39)
  ort. İDDİA EDİLEN edge       +18.61p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.66p   ±0.5p  %95 [+0.6p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6334.22 $
  PnL fee ÖNCESİ             +48405.53 $
  PnL fee SONRASI            +42071.31 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15607.99 $   %90 aralık [-25062.23, -6166.44]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1236 (model 0.1310)

  bizim (fee sonrası)            +42071.31 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
