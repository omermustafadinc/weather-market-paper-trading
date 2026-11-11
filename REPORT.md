========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-11T18:02:52.570665Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         117726
  orderbook seviyesi     6256869
  tahmin snapshot          78561
  karar                    24372
  simüle fill               6286
  çözümlenmiş kova          3162

## Brier skoru  (düşük = iyi, 3078 kova)
  model                  0.1312
  piyasa (mid)           0.1239   n=3078
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0073  ±0.0028  %95 [-0.0129, -0.0018]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=444  0.1210 / 0.1936   fark +0.0726
    CHI   n=438  0.1403 / 0.1050   fark -0.0353
    DEN   n=444  0.1409 / 0.1932   fark +0.0523
    LAX   n=438  0.1213 / 0.0845   fark -0.0368
    MIA   n=438  0.1374 / 0.1002   fark -0.0371
    NY    n=438  0.1073 / 0.0896   fark -0.0177
    PHL   n=438  0.1501 / 0.0991   fark -0.0511
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1244         0.032         0.052   +0.020
  0.1-0.2       698         0.150         0.198   +0.048
  0.2-0.3       563         0.246         0.266   +0.020
  0.3-0.4       354         0.345         0.240   -0.105
  0.4-0.5       151         0.440         0.305   -0.136
  0.5-0.6        44         0.548         0.341   -0.207
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6209)
  işlem sayısı                    6209
  kazanan                         2425  (%39)
  ort. İDDİA EDİLEN edge       +18.61p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.71p   ±0.5p  %95 [+0.7p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6346.27 $
  PnL fee ÖNCESİ             +50329.07 $
  PnL fee SONRASI            +43982.80 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15049.04 $   %90 aralık [-23835.39, -6394.41]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1239 (model 0.1312)

  bizim (fee sonrası)            +43982.80 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
