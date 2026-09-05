========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-05T06:22:15.963213Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          13086
  orderbook seviyesi      711133
  tahmin snapshot           9702
  karar                     2502
  simüle fill                661
  çözümlenmiş kova           336

## Brier skoru  (düşük = iyi, 294 kova)
  model                  0.1253
  piyasa (mid)           0.1284   n=294
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0031  ±0.0069  %95 [-0.0103, +0.0166]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 42  0.1555 / 0.2031   fark +0.0476
    CHI   n= 42  0.1108 / 0.1068   fark -0.0040
    DEN   n= 42  0.1487 / 0.2097   fark +0.0610
    LAX   n= 42  0.1201 / 0.0872   fark -0.0330
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 42  0.1132 / 0.0738   fark -0.0394
    PHL   n= 42  0.1076 / 0.0980   fark -0.0096
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       105         0.035         0.029   -0.006
  0.1-0.2        78         0.151         0.192   +0.041
  0.2-0.3        66         0.242         0.273   +0.031
  0.3-0.4        32         0.347         0.250   -0.097
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         4         0.560         0.750   +0.190
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (559)
  işlem sayısı                     559
  kazanan                          200  (%36)
  ort. İDDİA EDİLEN edge       +13.55p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -1.25p   ±1.6p  %95 [-4.4p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    595.86 $
  PnL fee ÖNCESİ              -1328.19 $
  PnL fee SONRASI             -1924.05 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -884.32 $   %90 aralık [-3585.48, +1907.03]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1284 (model 0.1253)

  bizim (fee sonrası)             -1924.05 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
