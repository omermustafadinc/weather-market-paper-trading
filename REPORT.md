========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-18T23:53:29.280892Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          39930
  orderbook seviyesi     2136449
  tahmin snapshot          27342
  karar                     8154
  simüle fill               2125
  çözümlenmiş kova           918

## Brier skoru  (düşük = iyi, 876 kova)
  model                  0.1312
  piyasa (mid)           0.1352   n=876
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0040  ±0.0041  %95 [-0.0040, +0.0121]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=126  0.1494 / 0.2116   fark +0.0621
    CHI   n=126  0.1314 / 0.1153   fark -0.0161
    DEN   n=126  0.1506 / 0.2100   fark +0.0593
    LAX   n=120  0.1133 / 0.0969   fark -0.0164
    MIA   n=126  0.1323 / 0.1155   fark -0.0167
    NY    n=126  0.1081 / 0.0849   fark -0.0232
    PHL   n=126  0.1323 / 0.1106   fark -0.0218
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       319         0.035         0.056   +0.022
  0.1-0.2       225         0.151         0.191   +0.040
  0.2-0.3       194         0.245         0.258   +0.012
  0.3-0.4        96         0.344         0.219   -0.125
  0.4-0.5        30         0.432         0.233   -0.198
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2040)
  işlem sayısı                    2040
  kazanan                          807  (%40)
  ort. İDDİA EDİLEN edge       +15.19p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.41p   ±0.9p  %95 [-0.3p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2058.41 $
  PnL fee ÖNCESİ             +10959.83 $
  PnL fee SONRASI             +8901.42 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4795.98 $   %90 aralık [-10385.06, +1129.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1352 (model 0.1312)

  bizim (fee sonrası)             +8901.42 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
