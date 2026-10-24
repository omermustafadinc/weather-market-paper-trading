========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-24T12:04:52.712692Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          93570
  orderbook seviyesi     4995593
  tahmin snapshot          62307
  karar                    19266
  simüle fill               4993
  çözümlenmiş kova          2394

## Brier skoru  (düşük = iyi, 2310 kova)
  model                  0.1321
  piyasa (mid)           0.1292   n=2310
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0029  ±0.0031  %95 [-0.0090, +0.0032]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=330  0.1268 / 0.2039   fark +0.0771
    CHI   n=330  0.1397 / 0.1072   fark -0.0325
    DEN   n=330  0.1483 / 0.1990   fark +0.0508
    LAX   n=330  0.1207 / 0.0879   fark -0.0328
    MIA   n=330  0.1344 / 0.1068   fark -0.0276
    NY    n=330  0.1081 / 0.0909   fark -0.0171
    PHL   n=330  0.1468 / 0.1089   fark -0.0379
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       893         0.033         0.060   +0.027
  0.1-0.2       561         0.150         0.191   +0.041
  0.2-0.3       450         0.247         0.256   +0.009
  0.3-0.4       266         0.346         0.226   -0.120
  0.4-0.5        96         0.439         0.302   -0.137
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4904)
  işlem sayısı                    4904
  kazanan                         1899  (%39)
  ort. İDDİA EDİLEN edge       +17.93p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.07p   ±0.6p  %95 [-0.1p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4999.39 $
  PnL fee ÖNCESİ             +33424.10 $
  PnL fee SONRASI            +28424.71 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12749.72 $   %90 aralık [-19950.00, -4465.59]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1292 (model 0.1321)

  bizim (fee sonrası)            +28424.71 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
