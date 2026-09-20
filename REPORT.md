========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-20T19:24:10.578745Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          43332
  orderbook seviyesi     2322170
  tahmin snapshot          29610
  karar                     8850
  simüle fill               2308
  çözümlenmiş kova           978

## Brier skoru  (düşük = iyi, 936 kova)
  model                  0.1308
  piyasa (mid)           0.1364   n=936
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0057  ±0.0040  %95 [-0.0023, +0.0136]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=138  0.1449 / 0.2121   fark +0.0672
    CHI   n=132  0.1295 / 0.1171   fark -0.0124
    DEN   n=138  0.1500 / 0.2095   fark +0.0594
    LAX   n=132  0.1143 / 0.0961   fark -0.0181
    MIA   n=132  0.1333 / 0.1168   fark -0.0165
    NY    n=132  0.1094 / 0.0854   fark -0.0240
    PHL   n=132  0.1325 / 0.1113   fark -0.0213
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       338         0.035         0.053   +0.018
  0.1-0.2       246         0.151         0.187   +0.036
  0.2-0.3       206         0.245         0.262   +0.017
  0.3-0.4       102         0.344         0.235   -0.109
  0.4-0.5        32         0.433         0.219   -0.214
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2188)
  işlem sayısı                    2188
  kazanan                          889  (%41)
  ort. İDDİA EDİLEN edge       +15.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.27p   ±0.9p  %95 [+0.6p, +4.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2203.67 $
  PnL fee ÖNCESİ             +16112.76 $
  PnL fee SONRASI            +13909.09 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4807.00 $   %90 aralık [-10696.41, +1276.81]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1364 (model 0.1308)

  bizim (fee sonrası)            +13909.09 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
