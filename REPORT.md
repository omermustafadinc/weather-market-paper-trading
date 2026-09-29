========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-29T15:41:27.171157Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          57744
  orderbook seviyesi     3085476
  tahmin snapshot          38430
  karar                    11898
  simüle fill               3109
  çözümlenmiş kova          1356

## Brier skoru  (düşük = iyi, 1314 kova)
  model                  0.1312
  piyasa (mid)           0.1337   n=1314
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0025  ±0.0037  %95 [-0.0047, +0.0098]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=192  0.1345 / 0.2103   fark +0.0758
    CHI   n=186  0.1269 / 0.1123   fark -0.0146
    DEN   n=192  0.1446 / 0.2016   fark +0.0570
    LAX   n=186  0.1241 / 0.0971   fark -0.0270
    MIA   n=186  0.1397 / 0.1137   fark -0.0261
    NY    n=186  0.1069 / 0.0842   fark -0.0228
    PHL   n=186  0.1412 / 0.1125   fark -0.0287
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       486         0.034         0.056   +0.022
  0.1-0.2       335         0.152         0.194   +0.042
  0.2-0.3       281         0.247         0.246   -0.001
  0.3-0.4       141         0.346         0.234   -0.112
  0.4-0.5        54         0.436         0.315   -0.121
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3030)
  işlem sayısı                    3030
  kazanan                         1216  (%40)
  ort. İDDİA EDİLEN edge       +16.08p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.08p   ±0.7p  %95 [+0.6p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3049.64 $
  PnL fee ÖNCESİ             +24804.50 $
  PnL fee SONRASI            +21754.86 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -8470.18 $   %90 aralık [-15659.68, -678.54]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1337 (model 0.1312)

  bizim (fee sonrası)            +21754.86 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
