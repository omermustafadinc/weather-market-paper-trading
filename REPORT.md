========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-14T17:01:16.988990Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          31878
  orderbook seviyesi     1683406
  tahmin snapshot          22050
  karar                     6438
  simüle fill               1687
  çözümlenmiş kova           726

## Brier skoru  (düşük = iyi, 684 kova)
  model                  0.1279
  piyasa (mid)           0.1322   n=684
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0044  ±0.0045  %95 [-0.0046, +0.0133]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=102  0.1533 / 0.2104   fark +0.0571
    CHI   n= 96  0.1244 / 0.1050   fark -0.0195
    DEN   n=102  0.1487 / 0.2108   fark +0.0621
    LAX   n= 96  0.1040 / 0.0919   fark -0.0121
    MIA   n= 96  0.1255 / 0.1122   fark -0.0133
    NY    n= 96  0.1079 / 0.0833   fark -0.0246
    PHL   n= 96  0.1284 / 0.1023   fark -0.0261
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       254         0.033         0.039   +0.006
  0.1-0.2       165         0.149         0.200   +0.051
  0.2-0.3       157         0.245         0.274   +0.029
  0.3-0.4        71         0.344         0.225   -0.118
  0.4-0.5        25         0.434         0.200   -0.234
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1569)
  işlem sayısı                    1569
  kazanan                          629  (%40)
  ort. İDDİA EDİLEN edge       +14.88p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.64p   ±1.0p  %95 [-0.4p, +3.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1598.84 $
  PnL fee ÖNCESİ              +8304.08 $
  PnL fee SONRASI             +6705.24 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3203.17 $   %90 aralık [-7934.63, +1563.09]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1322 (model 0.1279)

  bizim (fee sonrası)             +6705.24 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
