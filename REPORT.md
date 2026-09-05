========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-05T13:29:17.387266Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          13338
  orderbook seviyesi      724829
  tahmin snapshot           9954
  karar                     2502
  simüle fill                661
  çözümlenmiş kova           348

## Brier skoru  (düşük = iyi, 306 kova)
  model                  0.1259
  piyasa (mid)           0.1317   n=306
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0058  ±0.0068  %95 [-0.0076, +0.0192]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 48  0.1527 / 0.2040   fark +0.0513
    CHI   n= 42  0.1108 / 0.1068   fark -0.0040
    DEN   n= 48  0.1484 / 0.2099   fark +0.0615
    LAX   n= 42  0.1201 / 0.0872   fark -0.0330
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 42  0.1132 / 0.0738   fark -0.0394
    PHL   n= 42  0.1076 / 0.0980   fark -0.0096
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       109         0.034         0.028   -0.007
  0.1-0.2        80         0.151         0.200   +0.049
  0.2-0.3        71         0.242         0.268   +0.025
  0.3-0.4        33         0.349         0.242   -0.106
  0.4-0.5         8         0.441         0.125   -0.316
  0.5-0.6         4         0.560         0.750   +0.190
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (573)
  işlem sayısı                     573
  kazanan                          209  (%36)
  ort. İDDİA EDİLEN edge       +13.74p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.40p   ±1.6p  %95 [-3.5p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    614.05 $
  PnL fee ÖNCESİ               -184.42 $
  PnL fee SONRASI              -798.47 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1211.53 $   %90 aralık [-4045.45, +1845.55]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1317 (model 0.1259)

  bizim (fee sonrası)              -798.47 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
