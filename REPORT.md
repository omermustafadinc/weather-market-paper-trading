========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-19T15:10:50.197079Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          86082
  orderbook seviyesi     4587227
  tahmin snapshot          57015
  karar                    17748
  simüle fill               4600
  çözümlenmiş kova          2196

## Brier skoru  (düşük = iyi, 2112 kova)
  model                  0.1321
  piyasa (mid)           0.1311   n=2112
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0009  ±0.0031  %95 [-0.0071, +0.0052]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=306  0.1280 / 0.2052   fark +0.0771
    CHI   n=300  0.1377 / 0.1089   fark -0.0289
    DEN   n=306  0.1491 / 0.1998   fark +0.0508
    LAX   n=300  0.1247 / 0.0928   fark -0.0319
    MIA   n=300  0.1361 / 0.1036   fark -0.0325
    NY    n=300  0.1076 / 0.0924   fark -0.0152
    PHL   n=300  0.1410 / 0.1125   fark -0.0285
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       800         0.034         0.061   +0.027
  0.1-0.2       529         0.150         0.189   +0.039
  0.2-0.3       423         0.247         0.255   +0.008
  0.3-0.4       237         0.345         0.215   -0.129
  0.4-0.5        89         0.439         0.303   -0.135
  0.5-0.6        25         0.548         0.400   -0.148
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4476)
  işlem sayısı                    4476
  kazanan                         1735  (%39)
  ort. İDDİA EDİLEN edge       +17.37p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.03p   ±0.6p  %95 [-0.2p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4548.32 $
  PnL fee ÖNCESİ             +29025.71 $
  PnL fee SONRASI            +24477.39 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11246.83 $   %90 aralık [-21667.04, -2105.46]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1311 (model 0.1321)

  bizim (fee sonrası)            +24477.39 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
