========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-10T18:16:37.972173Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         116550
  orderbook seviyesi     6198527
  tahmin snapshot          77805
  karar                    24120
  simüle fill               6223
  çözümlenmiş kova          3120

## Brier skoru  (düşük = iyi, 3036 kova)
  model                  0.1308
  piyasa (mid)           0.1240   n=3036
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0068  ±0.0028  %95 [-0.0124, -0.0012]
  -> model piyasadan ANLAMLI ölçüde KÖTÜ
     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.

  şehir bazında (model / piyasa):
    AUS   n=438  0.1208 / 0.1933   fark +0.0725
    CHI   n=432  0.1393 / 0.1046   fark -0.0347
    DEN   n=438  0.1399 / 0.1927   fark +0.0528
    LAX   n=432  0.1210 / 0.0849   fark -0.0362
    MIA   n=432  0.1372 / 0.1012   fark -0.0360
    NY    n=432  0.1072 / 0.0904   fark -0.0167
    PHL   n=432  0.1501 / 0.0990   fark -0.0511
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1225         0.032         0.051   +0.020
  0.1-0.2       689         0.150         0.199   +0.049
  0.2-0.3       558         0.246         0.263   +0.017
  0.3-0.4       349         0.345         0.241   -0.104
  0.4-0.5       149         0.440         0.309   -0.131
  0.5-0.6        42         0.546         0.357   -0.189
  0.6-0.7        15         0.634         0.467   -0.168
  0.7-0.8         2         0.749         1.000   +0.251
  0.8-0.9         6         0.855         0.667   -0.189
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (6164)
  işlem sayısı                    6164
  kazanan                         2410  (%39)
  ort. İDDİA EDİLEN edge       +18.54p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.75p   ±0.5p  %95 [+0.7p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6295.56 $
  PnL fee ÖNCESİ             +48932.07 $
  PnL fee SONRASI            +42636.51 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -16167.15 $   %90 aralık [-26588.65, -6449.13]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1240 (model 0.1308)

  bizim (fee sonrası)            +42636.51 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
