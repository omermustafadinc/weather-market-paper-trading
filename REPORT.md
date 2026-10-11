========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-11T00:13:22.236779Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          72420
  orderbook seviyesi     3867598
  tahmin snapshot          48258
  karar                    14952
  simüle fill               3871
  çözümlenmiş kova          1842

## Brier skoru  (düşük = iyi, 1758 kova)
  model                  0.1339
  piyasa (mid)           0.1328   n=1758
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0010  ±0.0033  %95 [-0.0075, +0.0054]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=252  0.1319 / 0.2048   fark +0.0730
    CHI   n=252  0.1381 / 0.1107   fark -0.0274
    DEN   n=252  0.1509 / 0.2021   fark +0.0512
    LAX   n=246  0.1303 / 0.0978   fark -0.0324
    MIA   n=252  0.1350 / 0.1080   fark -0.0270
    NY    n=252  0.1089 / 0.0917   fark -0.0173
    PHL   n=252  0.1418 / 0.1138   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       660         0.033         0.065   +0.032
  0.1-0.2       442         0.151         0.192   +0.042
  0.2-0.3       359         0.247         0.242   -0.004
  0.3-0.4       194         0.346         0.232   -0.114
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3805)
  işlem sayısı                    3805
  kazanan                         1513  (%40)
  ort. İDDİA EDİLEN edge       +16.43p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.13p   ±0.7p  %95 [-0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3805.61 $
  PnL fee ÖNCESİ             +24558.53 $
  PnL fee SONRASI            +20752.92 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9745.90 $   %90 aralık [-16737.93, -2864.23]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1328 (model 0.1339)

  bizim (fee sonrası)            +20752.92 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
