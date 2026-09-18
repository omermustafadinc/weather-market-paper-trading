========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-18T21:43:04.477626Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          39594
  orderbook seviyesi     2117805
  tahmin snapshot          27216
  karar                     8070
  simüle fill               2105
  çözümlenmiş kova           906

## Brier skoru  (düşük = iyi, 864 kova)
  model                  0.1312
  piyasa (mid)           0.1349   n=864
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0041  %95 [-0.0044, +0.0118]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=126  0.1494 / 0.2116   fark +0.0621
    CHI   n=120  0.1339 / 0.1156   fark -0.0183
    DEN   n=126  0.1506 / 0.2100   fark +0.0593
    LAX   n=120  0.1133 / 0.0969   fark -0.0164
    MIA   n=126  0.1323 / 0.1155   fark -0.0167
    NY    n=126  0.1081 / 0.0849   fark -0.0232
    PHL   n=120  0.1300 / 0.1055   fark -0.0245
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       314         0.035         0.054   +0.019
  0.1-0.2       223         0.151         0.193   +0.042
  0.2-0.3       191         0.245         0.262   +0.016
  0.3-0.4        94         0.344         0.213   -0.131
  0.4-0.5        30         0.432         0.233   -0.198
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2006)
  işlem sayısı                    2006
  kazanan                          784  (%39)
  ort. İDDİA EDİLEN edge       +15.25p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.13p   ±0.9p  %95 [-0.7p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2032.10 $
  PnL fee ÖNCESİ             +10925.13 $
  PnL fee SONRASI             +8893.03 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4567.72 $   %90 aralık [-9628.78, +574.96]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1349 (model 0.1312)

  bizim (fee sonrası)             +8893.03 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
