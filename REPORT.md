========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-06T04:54:12.546211Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          15282
  orderbook seviyesi      824040
  tahmin snapshot          10962
  karar                     2970
  simüle fill                776
  çözümlenmiş kova           372

## Brier skoru  (düşük = iyi, 330 kova)
  model                  0.1244
  piyasa (mid)           0.1286   n=330
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0042  ±0.0065  %95 [-0.0085, +0.0169]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 48  0.1527 / 0.2040   fark +0.0513
    CHI   n= 48  0.1160 / 0.1070   fark -0.0091
    DEN   n= 48  0.1484 / 0.2099   fark +0.0615
    LAX   n= 48  0.1088 / 0.0869   fark -0.0218
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 48  0.1094 / 0.0738   fark -0.0356
    PHL   n= 48  0.1139 / 0.0970   fark -0.0169
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       121         0.034         0.025   -0.009
  0.1-0.2        86         0.152         0.198   +0.046
  0.2-0.3        73         0.243         0.274   +0.031
  0.3-0.4        34         0.350         0.265   -0.085
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (633)
  işlem sayısı                     633
  kazanan                          242  (%38)
  ort. İDDİA EDİLEN edge       +13.65p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.77p   ±1.5p  %95 [-3.7p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    650.92 $
  PnL fee ÖNCESİ               -521.56 $
  PnL fee SONRASI             -1172.48 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1155.17 $   %90 aralık [-4831.29, +2701.08]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1286 (model 0.1244)

  bizim (fee sonrası)             -1172.48 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
