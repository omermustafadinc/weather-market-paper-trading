========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-26T11:48:40.378421Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          52872
  orderbook seviyesi     2830708
  tahmin snapshot          35154
  karar                    10806
  simüle fill               2839
  çözümlenmiş kova          1218

## Brier skoru  (düşük = iyi, 1176 kova)
  model                  0.1314
  piyasa (mid)           0.1344   n=1176
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0030  ±0.0038  %95 [-0.0044, +0.0104]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=168  0.1394 / 0.2111   fark +0.0718
    CHI   n=168  0.1229 / 0.1152   fark -0.0077
    DEN   n=168  0.1489 / 0.2058   fark +0.0569
    LAX   n=168  0.1239 / 0.0945   fark -0.0295
    MIA   n=168  0.1375 / 0.1152   fark -0.0223
    NY    n=168  0.1099 / 0.0898   fark -0.0201
    PHL   n=168  0.1372 / 0.1092   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       424         0.035         0.054   +0.019
  0.1-0.2       312         0.151         0.189   +0.038
  0.2-0.3       254         0.247         0.256   +0.009
  0.3-0.4       128         0.345         0.219   -0.126
  0.4-0.5        46         0.435         0.304   -0.130
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2743)
  işlem sayısı                    2743
  kazanan                         1130  (%41)
  ort. İDDİA EDİLEN edge       +15.37p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.89p   ±0.8p  %95 [+1.4p, +4.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2751.71 $
  PnL fee ÖNCESİ             +24950.38 $
  PnL fee SONRASI            +22198.67 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7425.34 $   %90 aralık [-13663.87, +19.69]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1344 (model 0.1314)

  bizim (fee sonrası)            +22198.67 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
