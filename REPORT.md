========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-23T10:35:42.831679Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          47796
  orderbook seviyesi     2558443
  tahmin snapshot          32130
  karar                     9738
  simüle fill               2551
  çözümlenmiş kova          1092

## Brier skoru  (düşük = iyi, 1050 kova)
  model                  0.1315
  piyasa (mid)           0.1356   n=1050
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0041  ±0.0038  %95 [-0.0034, +0.0116]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=150  0.1440 / 0.2120   fark +0.0680
    CHI   n=150  0.1277 / 0.1154   fark -0.0123
    DEN   n=150  0.1518 / 0.2099   fark +0.0581
    LAX   n=150  0.1177 / 0.0963   fark -0.0214
    MIA   n=150  0.1353 / 0.1136   fark -0.0217
    NY    n=150  0.1102 / 0.0915   fark -0.0187
    PHL   n=150  0.1337 / 0.1105   fark -0.0233
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       374         0.035         0.051   +0.015
  0.1-0.2       282         0.151         0.195   +0.044
  0.2-0.3       231         0.246         0.260   +0.014
  0.3-0.4       115         0.343         0.209   -0.135
  0.4-0.5        36         0.432         0.278   -0.154
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2448)
  işlem sayısı                    2448
  kazanan                          994  (%41)
  ort. İDDİA EDİLEN edge       +15.28p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.56p   ±0.8p  %95 [+0.9p, +4.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2478.84 $
  PnL fee ÖNCESİ             +21065.96 $
  PnL fee SONRASI            +18587.12 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6561.75 $   %90 aralık [-13155.22, -461.16]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1356 (model 0.1315)

  bizim (fee sonrası)            +18587.12 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
