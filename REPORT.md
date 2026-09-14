========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-14T11:02:54.653582Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          31542
  orderbook seviyesi     1665548
  tahmin snapshot          21924
  karar                     6354
  simüle fill               1665
  çözümlenmiş kova           714

## Brier skoru  (düşük = iyi, 672 kova)
  model                  0.1274
  piyasa (mid)           0.1308   n=672
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0034  ±0.0046  %95 [-0.0056, +0.0124]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 96  0.1551 / 0.2104   fark +0.0554
    CHI   n= 96  0.1244 / 0.1050   fark -0.0195
    DEN   n= 96  0.1464 / 0.2104   fark +0.0639
    LAX   n= 96  0.1040 / 0.0919   fark -0.0121
    MIA   n= 96  0.1255 / 0.1122   fark -0.0133
    NY    n= 96  0.1079 / 0.0833   fark -0.0246
    PHL   n= 96  0.1284 / 0.1023   fark -0.0261
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       249         0.033         0.036   +0.003
  0.1-0.2       163         0.149         0.202   +0.054
  0.2-0.3       154         0.244         0.273   +0.028
  0.3-0.4        69         0.343         0.232   -0.111
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1540)
  işlem sayısı                    1540
  kazanan                          610  (%40)
  ort. İDDİA EDİLEN edge       +14.80p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.93p   ±1.0p  %95 [-1.1p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1567.96 $
  PnL fee ÖNCESİ              +5215.00 $
  PnL fee SONRASI             +3647.04 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2925.21 $   %90 aralık [-8081.31, +1824.24]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1308 (model 0.1274)

  bizim (fee sonrası)             +3647.04 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
