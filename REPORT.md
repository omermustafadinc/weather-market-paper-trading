========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-05T20:58:06.373740Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          14346
  orderbook seviyesi      776168
  tahmin snapshot          10458
  karar                     2754
  simüle fill                725
  çözümlenmiş kova           354

## Brier skoru  (düşük = iyi, 312 kova)
  model                  0.1250
  piyasa (mid)           0.1305   n=312
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0055  ±0.0067  %95 [-0.0076, +0.0186]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 48  0.1527 / 0.2040   fark +0.0513
    CHI   n= 42  0.1108 / 0.1068   fark -0.0040
    DEN   n= 48  0.1484 / 0.2099   fark +0.0615
    LAX   n= 42  0.1201 / 0.0872   fark -0.0330
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 48  0.1094 / 0.0738   fark -0.0356
    PHL   n= 42  0.1076 / 0.0980   fark -0.0096
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       111         0.034         0.027   -0.007
  0.1-0.2        82         0.151         0.195   +0.044
  0.2-0.3        72         0.243         0.264   +0.021
  0.3-0.4        34         0.350         0.265   -0.085
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         4         0.560         0.750   +0.190
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (598)
  işlem sayısı                     598
  kazanan                          218  (%36)
  ort. İDDİA EDİLEN edge       +13.63p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.80p   ±1.6p  %95 [-3.8p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    635.22 $
  PnL fee ÖNCESİ               -441.25 $
  PnL fee SONRASI             -1076.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1077.09 $   %90 aralık [-4039.72, +2066.57]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1305 (model 0.1250)

  bizim (fee sonrası)             -1076.47 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
