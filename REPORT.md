========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-24T10:41:02.175406Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          49524
  orderbook seviyesi     2652756
  tahmin snapshot          33264
  karar                    10098
  simüle fill               2644
  çözümlenmiş kova          1134

## Brier skoru  (düşük = iyi, 1092 kova)
  model                  0.1313
  piyasa (mid)           0.1357   n=1092
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0045  ±0.0038  %95 [-0.0029, +0.0119]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=156  0.1431 / 0.2120   fark +0.0689
    CHI   n=156  0.1252 / 0.1137   fark -0.0115
    DEN   n=156  0.1484 / 0.2071   fark +0.0587
    LAX   n=156  0.1214 / 0.0982   fark -0.0232
    MIA   n=156  0.1351 / 0.1172   fark -0.0179
    NY    n=156  0.1094 / 0.0898   fark -0.0196
    PHL   n=156  0.1362 / 0.1121   fark -0.0241
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       393         0.035         0.053   +0.018
  0.1-0.2       289         0.151         0.190   +0.039
  0.2-0.3       238         0.246         0.256   +0.010
  0.3-0.4       119         0.344         0.218   -0.125
  0.4-0.5        41         0.436         0.293   -0.143
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2551)
  işlem sayısı                    2551
  kazanan                         1054  (%41)
  ort. İDDİA EDİLEN edge       +15.25p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +3.06p   ±0.8p  %95 [+1.5p, +4.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2568.68 $
  PnL fee ÖNCESİ             +24441.49 $
  PnL fee SONRASI            +21872.81 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7104.16 $   %90 aralık [-13285.16, -406.54]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1357 (model 0.1313)

  bizim (fee sonrası)            +21872.81 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
