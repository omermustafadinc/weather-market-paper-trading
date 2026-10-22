========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-22T23:14:51.820034Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          91410
  orderbook seviyesi     4876796
  tahmin snapshot          60795
  karar                    18858
  simüle fill               4884
  çözümlenmiş kova          2346

## Brier skoru  (düşük = iyi, 2262 kova)
  model                  0.1322
  piyasa (mid)           0.1292   n=2262
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0029  ±0.0031  %95 [-0.0091, +0.0032]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=324  0.1274 / 0.2033   fark +0.0758
    CHI   n=324  0.1396 / 0.1079   fark -0.0317
    DEN   n=324  0.1475 / 0.1986   fark +0.0511
    LAX   n=318  0.1204 / 0.0889   fark -0.0315
    MIA   n=324  0.1353 / 0.1055   fark -0.0298
    NY    n=324  0.1080 / 0.0904   fark -0.0176
    PHL   n=324  0.1468 / 0.1093   fark -0.0375
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       870         0.033         0.062   +0.029
  0.1-0.2       554         0.150         0.190   +0.040
  0.2-0.3       446         0.247         0.253   +0.006
  0.3-0.4       256         0.345         0.219   -0.127
  0.4-0.5        93         0.439         0.312   -0.127
  0.5-0.6        31         0.548         0.355   -0.193
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4816)
  işlem sayısı                    4816
  kazanan                         1863  (%39)
  ort. İDDİA EDİLEN edge       +17.82p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.00p   ±0.6p  %95 [-0.2p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4909.34 $
  PnL fee ÖNCESİ             +33080.83 $
  PnL fee SONRASI            +28171.49 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12425.06 $   %90 aralık [-21217.52, -4383.36]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1292 (model 0.1322)

  bizim (fee sonrası)            +28171.49 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
