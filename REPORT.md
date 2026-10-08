========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-08T03:19:57.102182Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          68772
  orderbook seviyesi     3676898
  tahmin snapshot          45990
  karar                    14178
  simüle fill               3677
  çözümlenmiş kova          1722

## Brier skoru  (düşük = iyi, 1638 kova)
  model                  0.1315
  piyasa (mid)           0.1330   n=1638
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0015  ±0.0033  %95 [-0.0051, +0.0080]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=234  0.1298 / 0.2033   fark +0.0735
    CHI   n=234  0.1357 / 0.1119   fark -0.0238
    DEN   n=234  0.1456 / 0.2003   fark +0.0546
    LAX   n=234  0.1281 / 0.1006   fark -0.0274
    MIA   n=234  0.1357 / 0.1120   fark -0.0237
    NY    n=234  0.1093 / 0.0893   fark -0.0199
    PHL   n=234  0.1365 / 0.1135   fark -0.0230
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       608         0.034         0.056   +0.022
  0.1-0.2       418         0.151         0.194   +0.042
  0.2-0.3       340         0.246         0.244   -0.002
  0.3-0.4       180         0.346         0.244   -0.101
  0.4-0.5        70         0.436         0.300   -0.136
  0.5-0.6        18         0.551         0.333   -0.218
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3616)
  işlem sayısı                    3616
  kazanan                         1446  (%40)
  ort. İDDİA EDİLEN edge       +16.30p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.35p   ±0.7p  %95 [+0.0p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3604.04 $
  PnL fee ÖNCESİ             +25831.82 $
  PnL fee SONRASI            +22227.78 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9611.01 $   %90 aralık [-17251.62, -3272.52]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1315)

  bizim (fee sonrası)            +22227.78 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
