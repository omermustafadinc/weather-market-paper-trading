========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-06T22:10:55.404192Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          16962
  orderbook seviyesi      911667
  tahmin snapshot          12348
  karar                     3306
  simüle fill                860
  çözümlenmiş kova           414

## Brier skoru  (düşük = iyi, 372 kova)
  model                  0.1261
  piyasa (mid)           0.1296   n=372
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0036  ±0.0061  %95 [-0.0084, +0.0156]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 54  0.1469 / 0.1995   fark +0.0526
    CHI   n= 54  0.1244 / 0.1053   fark -0.0191
    DEN   n= 54  0.1475 / 0.2085   fark +0.0610
    LAX   n= 48  0.1088 / 0.0869   fark -0.0218
    MIA   n= 54  0.1239 / 0.1158   fark -0.0081
    NY    n= 54  0.1077 / 0.0784   fark -0.0294
    PHL   n= 54  0.1214 / 0.1083   fark -0.0131
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       137         0.034         0.036   +0.002
  0.1-0.2        94         0.151         0.191   +0.041
  0.2-0.3        83         0.243         0.265   +0.022
  0.3-0.4        41         0.348         0.268   -0.080
  0.4-0.5         9         0.441         0.111   -0.330
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (773)
  işlem sayısı                     773
  kazanan                          304  (%39)
  ort. İDDİA EDİLEN edge       +14.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.22p   ±1.4p  %95 [-2.9p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    773.79 $
  PnL fee ÖNCESİ               -589.79 $
  PnL fee SONRASI             -1363.58 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1329.42 $   %90 aralık [-4470.66, +1880.04]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1296 (model 0.1261)

  bizim (fee sonrası)             -1363.58 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
