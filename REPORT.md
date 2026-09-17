========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-17T15:24:29.822616Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          36894
  orderbook seviyesi     1967837
  tahmin snapshot          25200
  karar                     7476
  simüle fill               1956
  çözümlenmiş kova           852

## Brier skoru  (düşük = iyi, 810 kova)
  model                  0.1305
  piyasa (mid)           0.1335   n=810
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0030  ±0.0042  %95 [-0.0052, +0.0113]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=120  0.1536 / 0.2115   fark +0.0580
    CHI   n=114  0.1311 / 0.1116   fark -0.0194
    DEN   n=120  0.1482 / 0.2096   fark +0.0614
    LAX   n=114  0.1108 / 0.0972   fark -0.0136
    MIA   n=114  0.1288 / 0.1121   fark -0.0167
    NY    n=114  0.1073 / 0.0841   fark -0.0233
    PHL   n=114  0.1314 / 0.1004   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       294         0.034         0.048   +0.014
  0.1-0.2       207         0.150         0.198   +0.048
  0.2-0.3       181         0.245         0.265   +0.020
  0.3-0.4        87         0.343         0.218   -0.125
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1852)
  işlem sayısı                    1852
  kazanan                          723  (%39)
  ort. İDDİA EDİLEN edge       +15.00p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.89p   ±1.0p  %95 [-1.0p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1876.27 $
  PnL fee ÖNCESİ              +9501.48 $
  PnL fee SONRASI             +7625.21 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3762.50 $   %90 aralık [-9094.89, +1428.34]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1335 (model 0.1305)

  bizim (fee sonrası)             +7625.21 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
