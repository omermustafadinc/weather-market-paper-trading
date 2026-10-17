========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-17T14:29:17.506896Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          82020
  orderbook seviyesi     4368273
  tahmin snapshot          54243
  karar                    16854
  simüle fill               4373
  çözümlenmiş kova          2112

## Brier skoru  (düşük = iyi, 2028 kova)
  model                  0.1324
  piyasa (mid)           0.1305   n=2028
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0020  ±0.0031  %95 [-0.0081, +0.0042]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=294  0.1295 / 0.2043   fark +0.0748
    CHI   n=288  0.1393 / 0.1073   fark -0.0320
    DEN   n=294  0.1483 / 0.1989   fark +0.0506
    LAX   n=288  0.1248 / 0.0933   fark -0.0315
    MIA   n=288  0.1357 / 0.1025   fark -0.0332
    NY    n=288  0.1084 / 0.0895   fark -0.0190
    PHL   n=288  0.1407 / 0.1144   fark -0.0263
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       764         0.034         0.062   +0.027
  0.1-0.2       510         0.151         0.190   +0.040
  0.2-0.3       413         0.247         0.254   +0.008
  0.3-0.4       227         0.345         0.216   -0.129
  0.4-0.5        81         0.437         0.296   -0.141
  0.5-0.6        24         0.549         0.375   -0.174
  0.6-0.7         6         0.642         0.667   +0.025
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (4260)
  işlem sayısı                    4260
  kazanan                         1632  (%38)
  ort. İDDİA EDİLEN edge       +16.98p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.33p   ±0.6p  %95 [-0.9p, +1.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   4305.49 $
  PnL fee ÖNCESİ             +23159.99 $
  PnL fee SONRASI            +18854.50 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)      -10827.98 $   %90 aralık [-18589.94, -3927.50]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1305 (model 0.1324)

  bizim (fee sonrası)            +18854.50 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
