========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-22T11:07:08.373546Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          90402
  orderbook seviyesi     4825658
  tahmin snapshot          60165
  karar                    18606
  simüle fill               4824
  çözümlenmiş kova          2310

## Brier skoru  (düşük = iyi, 2226 kova)
  model                  0.1322
  piyasa (mid)           0.1292   n=2226
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0030  ±0.0031  %95 [-0.0092, +0.0031]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=318  0.1280 / 0.2025   fark +0.0745
    CHI   n=318  0.1392 / 0.1089   fark -0.0303
    DEN   n=318  0.1493 / 0.2007   fark +0.0513
    LAX   n=318  0.1204 / 0.0889   fark -0.0315
    MIA   n=318  0.1359 / 0.1031   fark -0.0328
    NY    n=318  0.1074 / 0.0896   fark -0.0179
    PHL   n=318  0.1452 / 0.1105   fark -0.0347
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       856         0.033         0.062   +0.029
  0.1-0.2       547         0.150         0.190   +0.040
  0.2-0.3       437         0.247         0.256   +0.009
  0.3-0.4       252         0.345         0.214   -0.131
  0.4-0.5        93         0.439         0.312   -0.127
  0.5-0.6        29         0.548         0.345   -0.203
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4732)
  işlem sayısı                    4732
  kazanan                         1823  (%39)
  ort. İDDİA EDİLEN edge       +17.71p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.77p   ±0.6p  %95 [-0.4p, +1.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4814.57 $
  PnL fee ÖNCESİ             +29135.66 $
  PnL fee SONRASI            +24321.09 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -11790.28 $   %90 aralık [-20354.06, -2767.32]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1292 (model 0.1322)

  bizim (fee sonrası)            +24321.09 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
