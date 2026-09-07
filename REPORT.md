========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-07T06:30:18.041278Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          17826
  orderbook seviyesi      957802
  tahmin snapshot          12852
  karar                     3486
  simüle fill                905
  çözümlenmiş kova           420

## Brier skoru  (düşük = iyi, 378 kova)
  model                  0.1267
  piyasa (mid)           0.1306   n=378
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0038  ±0.0061  %95 [-0.0080, +0.0157]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 54  0.1469 / 0.1995   fark +0.0526
    CHI   n= 54  0.1244 / 0.1053   fark -0.0191
    DEN   n= 54  0.1475 / 0.2085   fark +0.0610
    LAX   n= 54  0.1151 / 0.0981   fark -0.0170
    MIA   n= 54  0.1239 / 0.1158   fark -0.0081
    NY    n= 54  0.1077 / 0.0784   fark -0.0294
    PHL   n= 54  0.1214 / 0.1083   fark -0.0131
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       138         0.035         0.043   +0.009
  0.1-0.2        98         0.151         0.184   +0.033
  0.2-0.3        84         0.244         0.262   +0.018
  0.3-0.4        41         0.348         0.268   -0.080
  0.4-0.5         9         0.441         0.111   -0.330
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (776)
  işlem sayısı                     776
  kazanan                          306  (%39)
  ort. İDDİA EDİLEN edge       +14.09p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.06p   ±1.4p  %95 [-2.8p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    776.91 $
  PnL fee ÖNCESİ               -373.41 $
  PnL fee SONRASI             -1150.32 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1369.51 $   %90 aralık [-4798.08, +2209.69]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1306 (model 0.1267)

  bizim (fee sonrası)             -1150.32 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
