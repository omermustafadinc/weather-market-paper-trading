========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-17T22:20:39.907840Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          37566
  orderbook seviyesi     2004272
  tahmin snapshot          25704
  karar                     7644
  simüle fill               1997
  çözümlenmiş kova           876

## Brier skoru  (düşük = iyi, 834 kova)
  model                  0.1309
  piyasa (mid)           0.1350   n=834
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0041  ±0.0041  %95 [-0.0040, +0.0122]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=120  0.1536 / 0.2115   fark +0.0580
    CHI   n=120  0.1339 / 0.1156   fark -0.0183
    DEN   n=120  0.1482 / 0.2096   fark +0.0614
    LAX   n=114  0.1108 / 0.0972   fark -0.0136
    MIA   n=120  0.1313 / 0.1181   fark -0.0132
    NY    n=120  0.1075 / 0.0856   fark -0.0219
    PHL   n=120  0.1300 / 0.1055   fark -0.0245
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       303         0.035         0.053   +0.018
  0.1-0.2       214         0.151         0.192   +0.041
  0.2-0.3       186         0.245         0.263   +0.018
  0.3-0.4        90         0.343         0.222   -0.121
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1932)
  işlem sayısı                    1932
  kazanan                          762  (%39)
  ort. İDDİA EDİLEN edge       +15.07p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.34p   ±0.9p  %95 [-0.5p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1955.91 $
  PnL fee ÖNCESİ              +9348.82 $
  PnL fee SONRASI             +7392.91 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4166.53 $   %90 aralık [-10244.18, +1021.82]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1350 (model 0.1309)

  bizim (fee sonrası)             +7392.91 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
