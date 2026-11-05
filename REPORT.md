========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-11-05T18:53:38.646441Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot         110766
  orderbook seviyesi     5903506
  tahmin snapshot          73773
  karar                    22908
  simüle fill               5921
  çözümlenmiş kova          2910

## Brier skoru  (düşük = iyi, 2826 kova)
  model                  0.1298
  piyasa (mid)           0.1254   n=2826
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0044  ±0.0029  %95 [-0.0101, +0.0012]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=408  0.1221 / 0.1984   fark +0.0763
    CHI   n=402  0.1383 / 0.1057   fark -0.0326
    DEN   n=408  0.1375 / 0.1902   fark +0.0527
    LAX   n=402  0.1197 / 0.0843   fark -0.0354
    MIA   n=402  0.1374 / 0.1041   fark -0.0332
    NY    n=402  0.1066 / 0.0903   fark -0.0164
    PHL   n=402  0.1471 / 0.1026   fark -0.0444
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1      1122         0.032         0.053   +0.020
  0.1-0.2       659         0.150         0.188   +0.038
  0.2-0.3       526         0.247         0.264   +0.017
  0.3-0.4       333         0.345         0.243   -0.102
  0.4-0.5       128         0.440         0.320   -0.119
  0.5-0.6        39         0.545         0.359   -0.186
  0.6-0.7        12         0.631         0.583   -0.047
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         5         0.861         0.800   -0.061
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5854)
  işlem sayısı                    5854
  kazanan                         2288  (%39)
  ort. İDDİA EDİLEN edge       +18.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.69p   ±0.5p  %95 [+0.6p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5976.28 $
  PnL fee ÖNCESİ             +47612.99 $
  PnL fee SONRASI            +41636.71 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -14919.15 $   %90 aralık [-23748.05, -5930.48]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1254 (model 0.1298)

  bizim (fee sonrası)            +41636.71 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
