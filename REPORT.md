========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-10T11:56:24.986801Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          71412
  orderbook seviyesi     3817447
  tahmin snapshot          47754
  karar                    14700
  simüle fill               3809
  çözümlenmiş kova          1806

## Brier skoru  (düşük = iyi, 1722 kova)
  model                  0.1336
  piyasa (mid)           0.1326   n=1722
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0010  ±0.0033  %95 [-0.0075, +0.0055]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=246  0.1338 / 0.2044   fark +0.0706
    CHI   n=246  0.1377 / 0.1114   fark -0.0263
    DEN   n=246  0.1493 / 0.2015   fark +0.0522
    LAX   n=246  0.1303 / 0.0978   fark -0.0324
    MIA   n=246  0.1351 / 0.1091   fark -0.0259
    NY    n=246  0.1088 / 0.0921   fark -0.0167
    PHL   n=246  0.1403 / 0.1121   fark -0.0282
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       645         0.033         0.064   +0.030
  0.1-0.2       436         0.151         0.193   +0.042
  0.2-0.3       351         0.247         0.242   -0.005
  0.3-0.4       189         0.346         0.238   -0.108
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        20         0.551         0.300   -0.251
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3737)
  işlem sayısı                    3737
  kazanan                         1497  (%40)
  ort. İDDİA EDİLEN edge       +16.40p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.30p   ±0.7p  %95 [-0.0p, +2.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3721.89 $
  PnL fee ÖNCESİ             +25197.91 $
  PnL fee SONRASI            +21476.02 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9942.94 $   %90 aralık [-17937.91, -1847.27]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1326 (model 0.1336)

  bizim (fee sonrası)            +21476.02 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
