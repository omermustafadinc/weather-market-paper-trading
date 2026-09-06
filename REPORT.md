========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-06T09:20:17.789551Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          15450
  orderbook seviyesi      833726
  tahmin snapshot          11214
  karar                     2970
  simüle fill                776
  çözümlenmiş kova           378

## Brier skoru  (düşük = iyi, 336 kova)
  model                  0.1248
  piyasa (mid)           0.1285   n=336
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0064  %95 [-0.0089, +0.0163]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 48  0.1527 / 0.2040   fark +0.0513
    CHI   n= 48  0.1160 / 0.1070   fark -0.0091
    DEN   n= 48  0.1484 / 0.2099   fark +0.0615
    LAX   n= 48  0.1088 / 0.0869   fark -0.0218
    MIA   n= 48  0.1241 / 0.1207   fark -0.0034
    NY    n= 48  0.1094 / 0.0738   fark -0.0356
    PHL   n= 48  0.1139 / 0.0970   fark -0.0169
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       123         0.035         0.024   -0.010
  0.1-0.2        88         0.152         0.205   +0.052
  0.2-0.3        75         0.243         0.267   +0.024
  0.3-0.4        34         0.350         0.265   -0.085
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         6         0.560         0.500   -0.060
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (661)
  işlem sayısı                     661
  kazanan                          251  (%38)
  ort. İDDİA EDİLEN edge       +13.69p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -1.30p   ±1.5p  %95 [-4.2p, +1.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    673.09 $
  PnL fee ÖNCESİ               -757.57 $
  PnL fee SONRASI             -1430.66 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1064.73 $   %90 aralık [-4441.08, +2196.66]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1285 (model 0.1248)

  bizim (fee sonrası)             -1430.66 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
