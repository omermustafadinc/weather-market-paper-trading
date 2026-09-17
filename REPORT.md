========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-17T05:32:18.534741Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          36390
  orderbook seviyesi     1939107
  tahmin snapshot          24696
  karar                     7392
  simüle fill               1935
  çözümlenmiş kova           840

## Brier skoru  (düşük = iyi, 798 kova)
  model                  0.1302
  piyasa (mid)           0.1324   n=798
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0022  ±0.0042  %95 [-0.0061, +0.0105]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=114  0.1554 / 0.2117   fark +0.0563
    CHI   n=114  0.1311 / 0.1116   fark -0.0194
    DEN   n=114  0.1464 / 0.2095   fark +0.0631
    LAX   n=114  0.1108 / 0.0972   fark -0.0136
    MIA   n=114  0.1288 / 0.1121   fark -0.0167
    NY    n=114  0.1073 / 0.0841   fark -0.0233
    PHL   n=114  0.1314 / 0.1004   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       290         0.034         0.045   +0.011
  0.1-0.2       204         0.150         0.201   +0.051
  0.2-0.3       177         0.245         0.266   +0.021
  0.3-0.4        86         0.344         0.221   -0.123
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1842)
  işlem sayısı                    1842
  kazanan                          717  (%39)
  ort. İDDİA EDİLEN edge       +14.98p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.68p   ±1.0p  %95 [-1.2p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1865.63 $
  PnL fee ÖNCESİ              +8777.67 $
  PnL fee SONRASI             +6912.04 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3928.36 $   %90 aralık [-9390.18, +865.02]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1324 (model 0.1302)

  bizim (fee sonrası)             +6912.04 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
