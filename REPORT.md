========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-22T22:49:48.251887Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          47076
  orderbook seviyesi     2517628
  tahmin snapshot          31626
  karar                     9630
  simüle fill               2513
  çözümlenmiş kova          1086

## Brier skoru  (düşük = iyi, 1044 kova)
  model                  0.1314
  piyasa (mid)           0.1360   n=1044
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0046  ±0.0038  %95 [-0.0029, +0.0120]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=150  0.1440 / 0.2120   fark +0.0680
    CHI   n=150  0.1277 / 0.1154   fark -0.0123
    DEN   n=150  0.1518 / 0.2099   fark +0.0581
    LAX   n=144  0.1169 / 0.0979   fark -0.0190
    MIA   n=150  0.1353 / 0.1136   fark -0.0217
    NY    n=150  0.1102 / 0.0915   fark -0.0187
    PHL   n=150  0.1337 / 0.1105   fark -0.0233
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       373         0.035         0.051   +0.016
  0.1-0.2       278         0.151         0.194   +0.044
  0.2-0.3       230         0.246         0.261   +0.015
  0.3-0.4       115         0.343         0.209   -0.135
  0.4-0.5        36         0.432         0.278   -0.154
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2443)
  işlem sayısı                    2443
  kazanan                          992  (%41)
  ort. İDDİA EDİLEN edge       +15.27p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.60p   ±0.8p  %95 [+1.0p, +4.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2475.51 $
  PnL fee ÖNCESİ             +21118.92 $
  PnL fee SONRASI            +18643.41 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6349.31 $   %90 aralık [-12259.90, +299.65]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1360 (model 0.1314)

  bizim (fee sonrası)            +18643.41 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
