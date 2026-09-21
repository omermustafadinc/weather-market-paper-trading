========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-21T07:00:21.865519Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          44532
  orderbook seviyesi     2382733
  tahmin snapshot          30114
  karar                     9114
  simüle fill               2382
  çözümlenmiş kova          1008

## Brier skoru  (düşük = iyi, 966 kova)
  model                  0.1304
  piyasa (mid)           0.1351   n=966
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0039  %95 [-0.0030, +0.0124]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=138  0.1449 / 0.2121   fark +0.0672
    CHI   n=138  0.1273 / 0.1158   fark -0.0114
    DEN   n=138  0.1500 / 0.2095   fark +0.0594
    LAX   n=138  0.1155 / 0.0980   fark -0.0175
    MIA   n=138  0.1346 / 0.1166   fark -0.0180
    NY    n=138  0.1080 / 0.0826   fark -0.0254
    PHL   n=138  0.1327 / 0.1112   fark -0.0215
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       345         0.035         0.052   +0.017
  0.1-0.2       260         0.151         0.188   +0.037
  0.2-0.3       212         0.246         0.255   +0.009
  0.3-0.4       103         0.344         0.233   -0.111
  0.4-0.5        34         0.431         0.265   -0.167
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2266)
  işlem sayısı                    2266
  kazanan                          909  (%40)
  ort. İDDİA EDİLEN edge       +15.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.89p   ±0.9p  %95 [+0.2p, +3.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2282.42 $
  PnL fee ÖNCESİ             +15150.31 $
  PnL fee SONRASI            +12867.89 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6350.01 $   %90 aralık [-12636.18, -504.87]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1351 (model 0.1304)

  bizim (fee sonrası)            +12867.89 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
