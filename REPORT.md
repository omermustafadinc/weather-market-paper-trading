========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-25T23:02:13.561382Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          96918
  orderbook seviyesi     5174767
  tahmin snapshot          64827
  karar                    20016
  simüle fill               5183
  çözümlenmiş kova          2472

## Brier skoru  (düşük = iyi, 2388 kova)
  model                  0.1315
  piyasa (mid)           0.1286   n=2388
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0029  ±0.0031  %95 [-0.0089, +0.0032]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=342  0.1251 / 0.2052   fark +0.0801
    CHI   n=342  0.1408 / 0.1054   fark -0.0354
    DEN   n=342  0.1469 / 0.1945   fark +0.0476
    LAX   n=336  0.1203 / 0.0885   fark -0.0318
    MIA   n=342  0.1336 / 0.1047   fark -0.0289
    NY    n=342  0.1075 / 0.0919   fark -0.0156
    PHL   n=342  0.1460 / 0.1093   fark -0.0366
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       926         0.033         0.058   +0.026
  0.1-0.2       575         0.150         0.190   +0.040
  0.2-0.3       461         0.247         0.258   +0.011
  0.3-0.4       282         0.346         0.230   -0.115
  0.4-0.5       100         0.439         0.310   -0.129
  0.5-0.6        32         0.548         0.344   -0.204
  0.6-0.7         7         0.640         0.571   -0.068
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         3         0.868         1.000   +0.132
  0.9-1.0         1         0.958         1.000   +0.042
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (5107)
  işlem sayısı                    5107
  kazanan                         1987  (%39)
  ort. İDDİA EDİLEN edge       +18.10p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.28p   ±0.6p  %95 [+0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   5236.95 $
  PnL fee ÖNCESİ             +38114.87 $
  PnL fee SONRASI            +32877.92 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -12791.52 $   %90 aralık [-22180.10, -5089.22]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1286 (model 0.1315)

  bizim (fee sonrası)            +32877.92 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
