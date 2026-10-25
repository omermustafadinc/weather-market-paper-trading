========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-25T14:32:46.439757Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          95910
  orderbook seviyesi     5121924
  tahmin snapshot          64197
  karar                    19764
  simüle fill               5120
  çözümlenmiş kova          2448

## Brier skoru  (düşük = iyi, 2364 kova)
  model                  0.1316
  piyasa (mid)           0.1289   n=2364
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0028  ±0.0031  %95 [-0.0088, +0.0033]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=342  0.1251 / 0.2052   fark +0.0801
    CHI   n=336  0.1401 / 0.1063   fark -0.0338
    DEN   n=342  0.1469 / 0.1945   fark +0.0476
    LAX   n=336  0.1203 / 0.0885   fark -0.0318
    MIA   n=336  0.1344 / 0.1054   fark -0.0290
    NY    n=336  0.1077 / 0.0919   fark -0.0158
    PHL   n=336  0.1467 / 0.1079   fark -0.0388
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       915         0.033         0.059   +0.026
  0.1-0.2       572         0.150         0.189   +0.039
  0.2-0.3       459         0.247         0.259   +0.012
  0.3-0.4       275         0.346         0.225   -0.120
  0.4-0.5        99         0.439         0.313   -0.126
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5010)
  işlem sayısı                    5010
  kazanan                         1946  (%39)
  ort. İDDİA EDİLEN edge       +18.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.39p   ±0.6p  %95 [+0.3p, +2.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5151.32 $
  PnL fee ÖNCESİ             +39077.00 $
  PnL fee SONRASI            +33925.68 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -13643.73 $   %90 aralık [-22894.06, -4902.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1289 (model 0.1316)

  bizim (fee sonrası)            +33925.68 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
