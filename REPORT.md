========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-11T16:07:58.806311Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          73176
  orderbook seviyesi     3907316
  tahmin snapshot          48762
  karar                    15120
  simüle fill               3913
  çözümlenmiş kova          1860

## Brier skoru  (düşük = iyi, 1776 kova)
  model                  0.1334
  piyasa (mid)           0.1330   n=1776
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   -0.0003  ±0.0033  %95 [-0.0068, +0.0061]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=258  0.1316 / 0.2057   fark +0.0740
    CHI   n=252  0.1381 / 0.1107   fark -0.0274
    DEN   n=258  0.1504 / 0.2023   fark +0.0519
    LAX   n=252  0.1272 / 0.0958   fark -0.0314
    MIA   n=252  0.1350 / 0.1080   fark -0.0270
    NY    n=252  0.1089 / 0.0917   fark -0.0173
    PHL   n=252  0.1418 / 0.1138   fark -0.0280
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       669         0.033         0.064   +0.031
  0.1-0.2       444         0.151         0.191   +0.041
  0.2-0.3       364         0.246         0.245   -0.002
  0.3-0.4       195         0.346         0.231   -0.115
  0.4-0.5        76         0.437         0.289   -0.148
  0.5-0.6        22         0.551         0.318   -0.233
  0.6-0.7         3         0.651         0.667   +0.016
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         2         0.884         1.000   +0.116
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3816)
  işlem sayısı                    3816
  kazanan                         1518  (%40)
  ort. İDDİA EDİLEN edge       +16.46p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.15p   ±0.7p  %95 [-0.2p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3814.20 $
  PnL fee ÖNCESİ             +24493.35 $
  PnL fee SONRASI            +20679.15 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9428.14 $   %90 aralık [-16350.77, -1632.01]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1334)

  bizim (fee sonrası)            +20679.15 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
