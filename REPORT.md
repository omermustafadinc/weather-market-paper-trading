========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-07T23:55:10.467604Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          68436
  orderbook seviyesi     3658895
  tahmin snapshot          45738
  karar                    14094
  simüle fill               3657
  çözümlenmiş kova          1716

## Brier skoru  (düşük = iyi, 1632 kova)
  model                  0.1313
  piyasa (mid)           0.1329   n=1632
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0015  ±0.0033  %95 [-0.0050, +0.0081]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=234  0.1298 / 0.2033   fark +0.0735
    CHI   n=234  0.1357 / 0.1119   fark -0.0238
    DEN   n=234  0.1456 / 0.2003   fark +0.0546
    LAX   n=228  0.1266 / 0.0987   fark -0.0279
    MIA   n=234  0.1357 / 0.1120   fark -0.0237
    NY    n=234  0.1093 / 0.0893   fark -0.0199
    PHL   n=234  0.1365 / 0.1135   fark -0.0230
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       606         0.034         0.056   +0.023
  0.1-0.2       415         0.151         0.193   +0.041
  0.2-0.3       340         0.246         0.244   -0.002
  0.3-0.4       180         0.346         0.244   -0.101
  0.4-0.5        69         0.435         0.304   -0.130
  0.5-0.6        18         0.551         0.333   -0.218
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3612)
  işlem sayısı                    3612
  kazanan                         1443  (%40)
  ort. İDDİA EDİLEN edge       +16.31p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.34p   ±0.7p  %95 [+0.0p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3602.17 $
  PnL fee ÖNCESİ             +25831.86 $
  PnL fee SONRASI            +22229.69 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9017.00 $   %90 aralık [-16478.25, -1521.73]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1329 (model 0.1313)

  bizim (fee sonrası)            +22229.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
