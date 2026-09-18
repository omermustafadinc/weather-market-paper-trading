========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-18T15:43:54.807173Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          38922
  orderbook seviyesi     2080836
  tahmin snapshot          26838
  karar                     7902
  simüle fill               2064
  çözümlenmiş kova           894

## Brier skoru  (düşük = iyi, 852 kova)
  model                  0.1311
  piyasa (mid)           0.1358   n=852
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0047  ±0.0042  %95 [-0.0035, +0.0128]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=126  0.1494 / 0.2116   fark +0.0621
    CHI   n=120  0.1339 / 0.1156   fark -0.0183
    DEN   n=126  0.1506 / 0.2100   fark +0.0593
    LAX   n=120  0.1133 / 0.0969   fark -0.0164
    MIA   n=120  0.1313 / 0.1181   fark -0.0132
    NY    n=120  0.1075 / 0.0856   fark -0.0219
    PHL   n=120  0.1300 / 0.1055   fark -0.0245
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       310         0.034         0.055   +0.020
  0.1-0.2       219         0.151         0.192   +0.041
  0.2-0.3       188         0.245         0.261   +0.015
  0.3-0.4        93         0.343         0.215   -0.128
  0.4-0.5        30         0.432         0.233   -0.198
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1948)
  işlem sayısı                    1948
  kazanan                          773  (%40)
  ort. İDDİA EDİLEN edge       +15.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.72p   ±0.9p  %95 [-0.1p, +3.5p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1976.22 $
  PnL fee ÖNCESİ             +11874.52 $
  PnL fee SONRASI             +9898.30 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -4589.43 $   %90 aralık [-10066.50, +779.48]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1358 (model 0.1311)

  bizim (fee sonrası)             +9898.30 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
