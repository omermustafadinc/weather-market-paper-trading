========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-14T23:54:36.217712Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          32550
  orderbook seviyesi     1720607
  tahmin snapshot          22302
  karar                     6606
  simüle fill               1730
  çözümlenmiş kova           750

## Brier skoru  (düşük = iyi, 708 kova)
  model                  0.1280
  piyasa (mid)           0.1313   n=708
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0034  ±0.0044  %95 [-0.0053, +0.0121]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=102  0.1533 / 0.2104   fark +0.0571
    CHI   n=102  0.1282 / 0.1109   fark -0.0173
    DEN   n=102  0.1487 / 0.2108   fark +0.0621
    LAX   n= 96  0.1040 / 0.0919   fark -0.0121
    MIA   n=102  0.1239 / 0.1107   fark -0.0133
    NY    n=102  0.1071 / 0.0827   fark -0.0244
    PHL   n=102  0.1291 / 0.0998   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       264         0.033         0.042   +0.008
  0.1-0.2       168         0.149         0.196   +0.047
  0.2-0.3       163         0.245         0.270   +0.025
  0.3-0.4        75         0.343         0.240   -0.103
  0.4-0.5        26         0.433         0.192   -0.241
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1657)
  işlem sayısı                    1657
  kazanan                          655  (%40)
  ort. İDDİA EDİLEN edge       +14.78p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.25p   ±1.0p  %95 [-0.7p, +3.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1693.41 $
  PnL fee ÖNCESİ              +8155.91 $
  PnL fee SONRASI             +6462.50 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3240.37 $   %90 aralık [-8457.59, +1762.39]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1313 (model 0.1280)

  bizim (fee sonrası)             +6462.50 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
