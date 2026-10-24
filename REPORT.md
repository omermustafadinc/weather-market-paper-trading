========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-24T20:28:02.240312Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          94578
  orderbook seviyesi     5050313
  tahmin snapshot          63063
  karar                    19518
  simüle fill               5053
  çözümlenmiş kova          2406

## Brier skoru  (düşük = iyi, 2322 kova)
  model                  0.1319
  piyasa (mid)           0.1294   n=2322
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0025  ±0.0031  %95 [-0.0086, +0.0036]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=336  0.1260 / 0.2047   fark +0.0787
    CHI   n=330  0.1397 / 0.1072   fark -0.0325
    DEN   n=336  0.1476 / 0.1968   fark +0.0492
    LAX   n=330  0.1207 / 0.0879   fark -0.0328
    MIA   n=330  0.1344 / 0.1068   fark -0.0276
    NY    n=330  0.1081 / 0.0909   fark -0.0171
    PHL   n=330  0.1468 / 0.1089   fark -0.0379
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       897         0.033         0.060   +0.027
  0.1-0.2       565         0.150         0.189   +0.040
  0.2-0.3       452         0.247         0.257   +0.010
  0.3-0.4       267         0.346         0.225   -0.121
  0.4-0.5        97         0.439         0.309   -0.130
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4917)
  işlem sayısı                    4917
  kazanan                         1908  (%39)
  ort. İDDİA EDİLEN edge       +17.99p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.21p   ±0.6p  %95 [+0.1p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5028.80 $
  PnL fee ÖNCESİ             +37053.62 $
  PnL fee SONRASI            +32024.82 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12478.64 $   %90 aralık [-21414.94, -3566.93]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1294 (model 0.1319)

  bizim (fee sonrası)            +32024.82 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
