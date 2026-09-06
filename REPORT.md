========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-06T00:29:03.472086Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          15018
  orderbook seviyesi      809887
  tahmin snapshot          10836
  karar                     2922
  simüle fill                755
  çözümlenmiş kova           366

## Brier skoru  (düşük = iyi, 324 kova)
  model                  0.1262
  piyasa (mid)           0.1294   n=324
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0032  ±0.0066  %95 [-0.0097, +0.0161]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 48  0.1527 / 0.2040   fark +0.0513
    CHI   n= 48  0.1160 / 0.1070   fark -0.0091
    DEN   n= 48  0.1484 / 0.2099   fark +0.0615
    LAX   n= 42  0.1201 / 0.0872   fark -0.0330
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 48  0.1094 / 0.0738   fark -0.0356
    PHL   n= 48  0.1139 / 0.0970   fark -0.0169
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       118         0.034         0.025   -0.009
  0.1-0.2        84         0.152         0.202   +0.050
  0.2-0.3        73         0.243         0.274   +0.031
  0.3-0.4        34         0.350         0.265   -0.085
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (629)
  işlem sayısı                     629
  kazanan                          238  (%38)
  ort. İDDİA EDİLEN edge       +13.59p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -1.09p   ±1.5p  %95 [-4.0p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    648.12 $
  PnL fee ÖNCESİ               -599.90 $
  PnL fee SONRASI             -1248.02 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1367.91 $   %90 aralık [-4823.89, +1871.74]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1294 (model 0.1262)

  bizim (fee sonrası)             -1248.02 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
