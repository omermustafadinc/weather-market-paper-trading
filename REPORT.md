========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-04T15:09:51.931890Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          11370
  orderbook seviyesi      623093
  tahmin snapshot           8694
  karar                     2106
  simüle fill                559
  çözümlenmiş kova           306

## Brier skoru  (düşük = iyi, 264 kova)
  model                  0.1241
  piyasa (mid)           0.1336   n=264
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0095  ±0.0071  %95 [-0.0044, +0.0235]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 42  0.1555 / 0.2031   fark +0.0476
    CHI   n= 36  0.1105 / 0.1089   fark -0.0016
    DEN   n= 42  0.1487 / 0.2097   fark +0.0610
    LAX   n= 36  0.1138 / 0.0940   fark -0.0198
    MIA   n= 36  0.1203 / 0.1285   fark +0.0082
    NY    n= 36  0.1099 / 0.0654   fark -0.0444
    PHL   n= 36  0.1007 / 0.1012   fark +0.0005
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1        96         0.035         0.031   -0.003
  0.1-0.2        69         0.152         0.188   +0.037
  0.2-0.3        56         0.242         0.268   +0.026
  0.3-0.4        32         0.347         0.250   -0.097
  0.4-0.5         6         0.439         0.167   -0.273
  0.5-0.6         4         0.560         0.750   +0.190
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (472)
  işlem sayısı                     472
  kazanan                          171  (%36)
  ort. İDDİA EDİLEN edge       +13.67p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.11p   ±1.8p  %95 [-3.3p, +3.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    519.96 $
  PnL fee ÖNCESİ               -344.93 $
  PnL fee SONRASI              -864.89 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -679.10 $   %90 aralık [-3566.56, +2406.55]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1336 (model 0.1241)

  bizim (fee sonrası)              -864.89 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
