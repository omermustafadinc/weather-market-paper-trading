========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-28T00:22:35.207394Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          55896
  orderbook seviyesi     2983863
  tahmin snapshot          37170
  karar                    11520
  simüle fill               3016
  çözümlenmiş kova          1296

## Brier skoru  (düşük = iyi, 1254 kova)
  model                  0.1318
  piyasa (mid)           0.1342   n=1254
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0024  ±0.0038  %95 [-0.0050, +0.0098]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=180  0.1358 / 0.2105   fark +0.0747
    CHI   n=180  0.1259 / 0.1140   fark -0.0119
    DEN   n=180  0.1477 / 0.2071   fark +0.0594
    LAX   n=174  0.1258 / 0.0936   fark -0.0322
    MIA   n=180  0.1386 / 0.1149   fark -0.0237
    NY    n=180  0.1077 / 0.0862   fark -0.0215
    PHL   n=180  0.1409 / 0.1119   fark -0.0290
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       463         0.034         0.058   +0.024
  0.1-0.2       321         0.152         0.193   +0.042
  0.2-0.3       267         0.247         0.247   +0.001
  0.3-0.4       138         0.346         0.225   -0.121
  0.4-0.5        49         0.436         0.306   -0.130
  0.5-0.6        12         0.547         0.333   -0.213
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2945)
  işlem sayısı                    2945
  kazanan                         1194  (%41)
  ort. İDDİA EDİLEN edge       +15.85p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.38p   ±0.8p  %95 [+0.9p, +3.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2961.14 $
  PnL fee ÖNCESİ             +23793.73 $
  PnL fee SONRASI            +20832.59 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8119.97 $   %90 aralık [-13792.31, -1665.93]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1342 (model 0.1318)

  bizim (fee sonrası)            +20832.59 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
