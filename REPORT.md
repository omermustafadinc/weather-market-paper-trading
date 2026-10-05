========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-05T13:17:25.559612Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          65880
  orderbook seviyesi     3522435
  tahmin snapshot          44100
  karar                    13572
  simüle fill               3525
  çözümlenmiş kova          1608

## Brier skoru  (düşük = iyi, 1566 kova)
  model                  0.1304
  piyasa (mid)           0.1337   n=1566
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0032  ±0.0034  %95 [-0.0034, +0.0099]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=228  0.1291 / 0.2027   fark +0.0736
    CHI   n=222  0.1336 / 0.1145   fark -0.0190
    DEN   n=228  0.1459 / 0.2001   fark +0.0542
    LAX   n=222  0.1247 / 0.0963   fark -0.0283
    MIA   n=222  0.1360 / 0.1140   fark -0.0221
    NY    n=222  0.1081 / 0.0880   fark -0.0201
    PHL   n=222  0.1354 / 0.1165   fark -0.0189
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       582         0.034         0.057   +0.023
  0.1-0.2       398         0.152         0.186   +0.034
  0.2-0.3       328         0.246         0.244   -0.002
  0.3-0.4       171         0.346         0.251   -0.095
  0.4-0.5        66         0.436         0.318   -0.117
  0.5-0.6        17         0.549         0.353   -0.196
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3438)
  işlem sayısı                    3438
  kazanan                         1388  (%40)
  ort. İDDİA EDİLEN edge       +16.09p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.85p   ±0.7p  %95 [+0.5p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3429.70 $
  PnL fee ÖNCESİ             +27227.96 $
  PnL fee SONRASI            +23798.26 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9308.50 $   %90 aralık [-16974.68, -2565.46]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1337 (model 0.1304)

  bizim (fee sonrası)            +23798.26 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
