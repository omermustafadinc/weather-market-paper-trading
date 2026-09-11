========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-11T23:00:59.995587Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          26586
  orderbook seviyesi     1402154
  tahmin snapshot          18396
  karar                     5346
  simüle fill               1382
  çözümlenmiş kova           624

## Brier skoru  (düşük = iyi, 582 kova)
  model                  0.1251
  piyasa (mid)           0.1302   n=582
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0052  ±0.0050  %95 [-0.0046, +0.0149]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 84  0.1542 / 0.2086   fark +0.0544
    CHI   n= 84  0.1208 / 0.1022   fark -0.0186
    DEN   n= 84  0.1447 / 0.2124   fark +0.0676
    LAX   n= 78  0.0948 / 0.0849   fark -0.0099
    MIA   n= 84  0.1217 / 0.1124   fark -0.0093
    NY    n= 84  0.1055 / 0.0838   fark -0.0217
    PHL   n= 84  0.1316 / 0.1040   fark -0.0275
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       220         0.033         0.036   +0.003
  0.1-0.2       138         0.149         0.188   +0.039
  0.2-0.3       133         0.246         0.286   +0.040
  0.3-0.4        58         0.345         0.224   -0.121
  0.4-0.5        22         0.437         0.227   -0.210
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1292)
  işlem sayısı                    1292
  kazanan                          528  (%41)
  ort. İDDİA EDİLEN edge       +14.61p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.55p   ±1.1p  %95 [-0.6p, +3.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1301.78 $
  PnL fee ÖNCESİ              +4648.71 $
  PnL fee SONRASI             +3346.93 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2349.55 $   %90 aralık [-6348.63, +2313.48]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1302 (model 0.1251)

  bizim (fee sonrası)             +3346.93 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
