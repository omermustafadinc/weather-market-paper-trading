========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-04T08:53:09.326108Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          64164
  orderbook seviyesi     3431823
  tahmin snapshot          42966
  karar                    13218
  simüle fill               3434
  çözümlenmiş kova          1554

## Brier skoru  (düşük = iyi, 1512 kova)
  model                  0.1303
  piyasa (mid)           0.1335   n=1512
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0031  ±0.0034  %95 [-0.0036, +0.0099]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=216  0.1305 / 0.2038   fark +0.0733
    CHI   n=216  0.1315 / 0.1145   fark -0.0170
    DEN   n=216  0.1457 / 0.2013   fark +0.0556
    LAX   n=216  0.1260 / 0.0981   fark -0.0279
    MIA   n=216  0.1358 / 0.1148   fark -0.0210
    NY    n=216  0.1066 / 0.0861   fark -0.0205
    PHL   n=216  0.1363 / 0.1156   fark -0.0207
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       561         0.034         0.055   +0.021
  0.1-0.2       384         0.152         0.185   +0.033
  0.2-0.3       321         0.246         0.246   +0.000
  0.3-0.4       162         0.346         0.259   -0.087
  0.4-0.5        64         0.435         0.312   -0.122
  0.5-0.6        16         0.550         0.312   -0.238
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3364)
  işlem sayısı                    3364
  kazanan                         1364  (%41)
  ort. İDDİA EDİLEN edge       +16.04p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.06p   ±0.7p  %95 [+0.7p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3351.81 $
  PnL fee ÖNCESİ             +28173.51 $
  PnL fee SONRASI            +24821.70 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9429.42 $   %90 aralık [-16147.58, -3074.58]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1335 (model 0.1303)

  bizim (fee sonrası)            +24821.70 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
