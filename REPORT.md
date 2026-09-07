========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-07T12:48:16.059606Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          17994
  orderbook seviyesi      967521
  tahmin snapshot          12978
  karar                     3486
  simüle fill                905
  çözümlenmiş kova           432

## Brier skoru  (düşük = iyi, 390 kova)
  model                  0.1270
  piyasa (mid)           0.1332   n=390
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0062  ±0.0061  %95 [-0.0057, +0.0180]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 60  0.1481 / 0.2020   fark +0.0539
    CHI   n= 54  0.1244 / 0.1053   fark -0.0191
    DEN   n= 60  0.1443 / 0.2085   fark +0.0642
    LAX   n= 54  0.1151 / 0.0981   fark -0.0170
    MIA   n= 54  0.1239 / 0.1158   fark -0.0081
    NY    n= 54  0.1077 / 0.0784   fark -0.0294
    PHL   n= 54  0.1214 / 0.1083   fark -0.0131
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       143         0.035         0.042   +0.007
  0.1-0.2       100         0.151         0.190   +0.039
  0.2-0.3        87         0.243         0.264   +0.021
  0.3-0.4        43         0.349         0.256   -0.093
  0.4-0.5         9         0.441         0.111   -0.330
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (813)
  işlem sayısı                     813
  kazanan                          330  (%41)
  ort. İDDİA EDİLEN edge       +14.39p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.07p   ±1.4p  %95 [-1.6p, +3.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    819.82 $
  PnL fee ÖNCESİ              +2269.33 $
  PnL fee SONRASI             +1449.51 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1535.09 $   %90 aralık [-5441.84, +2155.07]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1332 (model 0.1270)

  bizim (fee sonrası)             +1449.51 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
