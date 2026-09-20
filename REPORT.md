========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-20T23:44:11.642078Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          44004
  orderbook seviyesi     2354551
  tahmin snapshot          29862
  karar                     9018
  simüle fill               2352
  çözümlenmiş kova          1002

## Brier skoru  (düşük = iyi, 960 kova)
  model                  0.1304
  piyasa (mid)           0.1351   n=960
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0040  %95 [-0.0030, +0.0125]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=138  0.1449 / 0.2121   fark +0.0672
    CHI   n=138  0.1273 / 0.1158   fark -0.0114
    DEN   n=138  0.1500 / 0.2095   fark +0.0594
    LAX   n=132  0.1143 / 0.0961   fark -0.0181
    MIA   n=138  0.1346 / 0.1166   fark -0.0180
    NY    n=138  0.1080 / 0.0826   fark -0.0254
    PHL   n=138  0.1327 / 0.1112   fark -0.0215
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       344         0.035         0.052   +0.017
  0.1-0.2       257         0.151         0.187   +0.035
  0.2-0.3       211         0.246         0.256   +0.010
  0.3-0.4       102         0.344         0.235   -0.109
  0.4-0.5        34         0.431         0.265   -0.167
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2264)
  işlem sayısı                    2264
  kazanan                          907  (%40)
  ort. İDDİA EDİLEN edge       +15.20p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.85p   ±0.9p  %95 [+0.2p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2281.29 $
  PnL fee ÖNCESİ             +15123.75 $
  PnL fee SONRASI            +12842.46 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -6328.31 $   %90 aralık [-12560.98, +45.82]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1351 (model 0.1304)

  bizim (fee sonrası)            +12842.46 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
