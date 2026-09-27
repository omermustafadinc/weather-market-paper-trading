========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-27T02:27:59.056856Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          54552
  orderbook seviyesi     2913855
  tahmin snapshot          36162
  karar                    11226
  simüle fill               2945
  çözümlenmiş kova          1260

## Brier skoru  (düşük = iyi, 1218 kova)
  model                  0.1313
  piyasa (mid)           0.1342   n=1218
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0029  ±0.0038  %95 [-0.0044, +0.0103]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=174  0.1360 / 0.2100   fark +0.0741
    CHI   n=174  0.1237 / 0.1155   fark -0.0082
    DEN   n=174  0.1495 / 0.2065   fark +0.0570
    LAX   n=174  0.1258 / 0.0936   fark -0.0322
    MIA   n=174  0.1365 / 0.1166   fark -0.0199
    NY    n=174  0.1090 / 0.0880   fark -0.0211
    PHL   n=174  0.1387 / 0.1094   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       445         0.035         0.054   +0.019
  0.1-0.2       317         0.151         0.196   +0.044
  0.2-0.3       263         0.247         0.247   +0.001
  0.3-0.4       131         0.345         0.229   -0.116
  0.4-0.5        47         0.435         0.298   -0.137
  0.5-0.6        11         0.550         0.364   -0.187
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (2839)
  işlem sayısı                    2839
  kazanan                         1171  (%41)
  ort. İDDİA EDİLEN edge       +15.58p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.98p   ±0.8p  %95 [+1.5p, +4.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   2848.78 $
  PnL fee ÖNCESİ             +24372.01 $
  PnL fee SONRASI            +21523.23 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7800.29 $   %90 aralık [-14230.35, -1736.62]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1342 (model 0.1313)

  bizim (fee sonrası)            +21523.23 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
