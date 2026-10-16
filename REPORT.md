========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-16T01:02:25.628599Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          79320
  orderbook seviyesi     4228303
  tahmin snapshot          52227
  karar                    16344
  simüle fill               4241
  çözümlenmiş kova          2052

## Brier skoru  (düşük = iyi, 1968 kova)
  model                  0.1326
  piyasa (mid)           0.1310   n=1968
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0016  ±0.0032  %95 [-0.0078, +0.0046]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=282  0.1283 / 0.2059   fark +0.0777
    CHI   n=282  0.1384 / 0.1089   fark -0.0296
    DEN   n=282  0.1506 / 0.1991   fark +0.0485
    LAX   n=276  0.1250 / 0.0947   fark -0.0303
    MIA   n=282  0.1358 / 0.1041   fark -0.0317
    NY    n=282  0.1092 / 0.0910   fark -0.0182
    PHL   n=282  0.1408 / 0.1128   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       740         0.034         0.061   +0.027
  0.1-0.2       494         0.151         0.192   +0.042
  0.2-0.3       406         0.247         0.251   +0.005
  0.3-0.4       217         0.345         0.221   -0.124
  0.4-0.5        79         0.438         0.291   -0.147
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         5         0.648         0.600   -0.048
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4147)
  işlem sayısı                    4147
  kazanan                         1614  (%39)
  ort. İDDİA EDİLEN edge       +16.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.63p   ±0.6p  %95 [-0.6p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4180.92 $
  PnL fee ÖNCESİ             +24670.32 $
  PnL fee SONRASI            +20489.40 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10339.02 $   %90 aralık [-17775.40, -3813.32]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1310 (model 0.1326)

  bizim (fee sonrası)            +20489.40 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
