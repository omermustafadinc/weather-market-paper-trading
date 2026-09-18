========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-18T02:07:57.484903Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          38238
  orderbook seviyesi     2040426
  tahmin snapshot          26208
  karar                     7812
  simüle fill               2040
  çözümlenmiş kova           882

## Brier skoru  (düşük = iyi, 840 kova)
  model                  0.1311
  piyasa (mid)           0.1347   n=840
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0036  ±0.0041  %95 [-0.0045, +0.0117]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=120  0.1536 / 0.2115   fark +0.0580
    CHI   n=120  0.1339 / 0.1156   fark -0.0183
    DEN   n=120  0.1482 / 0.2096   fark +0.0614
    LAX   n=120  0.1133 / 0.0969   fark -0.0164
    MIA   n=120  0.1313 / 0.1181   fark -0.0132
    NY    n=120  0.1075 / 0.0856   fark -0.0219
    PHL   n=120  0.1300 / 0.1055   fark -0.0245
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       305         0.035         0.052   +0.018
  0.1-0.2       216         0.151         0.194   +0.044
  0.2-0.3       187         0.245         0.262   +0.017
  0.3-0.4        91         0.343         0.220   -0.124
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1935)
  işlem sayısı                    1935
  kazanan                          763  (%39)
  ort. İDDİA EDİLEN edge       +15.08p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.32p   ±0.9p  %95 [-0.5p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1958.67 $
  PnL fee ÖNCESİ              +9314.70 $
  PnL fee SONRASI             +7356.03 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4091.52 $   %90 aralık [-9802.68, +1211.15]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1347 (model 0.1311)

  bizim (fee sonrası)             +7356.03 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
