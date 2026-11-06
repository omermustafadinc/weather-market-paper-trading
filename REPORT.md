========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-06T04:20:46.101713Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         111438
  orderbook seviyesi     5936004
  tahmin snapshot          74277
  karar                    23076
  simüle fill               5961
  çözümlenmiş kova          2940

## Brier skoru  (düşük = iyi, 2856 kova)
  model                  0.1299
  piyasa (mid)           0.1256   n=2856
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0043  ±0.0029  %95 [-0.0100, +0.0013]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=408  0.1221 / 0.1984   fark +0.0763
    CHI   n=408  0.1377 / 0.1069   fark -0.0308
    DEN   n=408  0.1375 / 0.1902   fark +0.0527
    LAX   n=408  0.1195 / 0.0845   fark -0.0350
    MIA   n=408  0.1368 / 0.1057   fark -0.0311
    NY    n=408  0.1080 / 0.0908   fark -0.0172
    PHL   n=408  0.1478 / 0.1027   fark -0.0451
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1138         0.032         0.052   +0.020
  0.1-0.2       662         0.150         0.190   +0.040
  0.2-0.3       531         0.247         0.264   +0.017
  0.3-0.4       335         0.345         0.245   -0.100
  0.4-0.5       130         0.440         0.323   -0.117
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        14         0.632         0.500   -0.132
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5899)
  işlem sayısı                    5899
  kazanan                         2313  (%39)
  ort. İDDİA EDİLEN edge       +18.24p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.88p   ±0.5p  %95 [+0.8p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   6023.75 $
  PnL fee ÖNCESİ             +49120.10 $
  PnL fee SONRASI            +43096.35 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -15399.71 $   %90 aralık [-23913.75, -6777.95]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1256 (model 0.1299)

  bizim (fee sonrası)            +43096.35 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
