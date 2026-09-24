========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-24T15:45:02.238946Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          49860
  orderbook seviyesi     2671380
  tahmin snapshot          33390
  karar                    10182
  simüle fill               2664
  çözümlenmiş kova          1140

## Brier skoru  (düşük = iyi, 1098 kova)
  model                  0.1310
  piyasa (mid)           0.1361   n=1098
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0051  ±0.0038  %95 [-0.0024, +0.0125]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=162  0.1410 / 0.2114   fark +0.0705
    CHI   n=156  0.1252 / 0.1137   fark -0.0115
    DEN   n=156  0.1484 / 0.2071   fark +0.0587
    LAX   n=156  0.1214 / 0.0982   fark -0.0232
    MIA   n=156  0.1351 / 0.1172   fark -0.0179
    NY    n=156  0.1094 / 0.0898   fark -0.0196
    PHL   n=156  0.1362 / 0.1121   fark -0.0241
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       396         0.035         0.053   +0.018
  0.1-0.2       290         0.151         0.190   +0.039
  0.2-0.3       238         0.246         0.256   +0.010
  0.3-0.4       119         0.344         0.218   -0.125
  0.4-0.5        43         0.435         0.302   -0.133
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2552)
  işlem sayısı                    2552
  kazanan                         1055  (%41)
  ort. İDDİA EDİLEN edge       +15.25p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +3.09p   ±0.8p  %95 [+1.5p, +4.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2570.22 $
  PnL fee ÖNCESİ             +24598.14 $
  PnL fee SONRASI            +22027.92 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7484.99 $   %90 aralık [-13611.31, -851.08]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1361 (model 0.1310)

  bizim (fee sonrası)            +22027.92 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
