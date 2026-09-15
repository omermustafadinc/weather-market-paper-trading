========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-15T07:18:53.976538Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          33066
  orderbook seviyesi     1750745
  tahmin snapshot          22806
  karar                     6696
  simüle fill               1754
  çözümlenmiş kova           756

## Brier skoru  (düşük = iyi, 714 kova)
  model                  0.1279
  piyasa (mid)           0.1308   n=714
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0029  ±0.0044  %95 [-0.0058, +0.0116]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=102  0.1533 / 0.2104   fark +0.0571
    CHI   n=102  0.1282 / 0.1109   fark -0.0173
    DEN   n=102  0.1487 / 0.2108   fark +0.0621
    LAX   n=102  0.1053 / 0.0906   fark -0.0147
    MIA   n=102  0.1239 / 0.1107   fark -0.0133
    NY    n=102  0.1071 / 0.0827   fark -0.0244
    PHL   n=102  0.1291 / 0.0998   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       266         0.033         0.041   +0.008
  0.1-0.2       170         0.149         0.194   +0.045
  0.2-0.3       164         0.245         0.274   +0.030
  0.3-0.4        75         0.343         0.240   -0.103
  0.4-0.5        27         0.432         0.185   -0.247
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1665)
  işlem sayısı                    1665
  kazanan                          657  (%39)
  ort. İDDİA EDİLEN edge       +14.80p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.19p   ±1.0p  %95 [-0.8p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1701.35 $
  PnL fee ÖNCESİ              +8042.87 $
  PnL fee SONRASI             +6341.52 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3402.68 $   %90 aralık [-7802.04, +1186.82]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1308 (model 0.1279)

  bizim (fee sonrası)             +6341.52 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
