========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-10T16:54:14.423864Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          71748
  orderbook seviyesi     3835684
  tahmin snapshot          47880
  karar                    14784
  simüle fill               3829
  çözümlenmiş kova          1818

## Brier skoru  (düşük = iyi, 1734 kova)
  model                  0.1336
  piyasa (mid)           0.1333   n=1734
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0003  ±0.0033  %95 [-0.0069, +0.0062]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=252  0.1319 / 0.2048   fark +0.0730
    CHI   n=246  0.1377 / 0.1114   fark -0.0263
    DEN   n=252  0.1509 / 0.2021   fark +0.0512
    LAX   n=246  0.1303 / 0.0978   fark -0.0324
    MIA   n=246  0.1351 / 0.1091   fark -0.0259
    NY    n=246  0.1088 / 0.0921   fark -0.0167
    PHL   n=246  0.1403 / 0.1121   fark -0.0282
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       653         0.033         0.064   +0.031
  0.1-0.2       436         0.151         0.193   +0.042
  0.2-0.3       351         0.247         0.242   -0.005
  0.3-0.4       191         0.346         0.236   -0.111
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3746)
  işlem sayısı                    3746
  kazanan                         1504  (%40)
  ort. İDDİA EDİLEN edge       +16.45p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.44p   ±0.7p  %95 [+0.1p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3727.87 $
  PnL fee ÖNCESİ             +25851.56 $
  PnL fee SONRASI            +22123.69 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9370.82 $   %90 aralık [-16641.88, -1684.05]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1333 (model 0.1336)

  bizim (fee sonrası)            +22123.69 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
