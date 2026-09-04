========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-04T23:54:25.271605Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          12546
  orderbook seviyesi      683188
  tahmin snapshot           9324
  karar                     2400
  simüle fill                631
  çözümlenmiş kova           330

## Brier skoru  (düşük = iyi, 288 kova)
  model                  0.1246
  piyasa (mid)           0.1301   n=288
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0055  ±0.0068  %95 [-0.0078, +0.0188]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 42  0.1555 / 0.2031   fark +0.0476
    CHI   n= 42  0.1108 / 0.1068   fark -0.0040
    DEN   n= 42  0.1487 / 0.2097   fark +0.0610
    LAX   n= 36  0.1138 / 0.0940   fark -0.0198
    MIA   n= 42  0.1211 / 0.1203   fark -0.0008
    NY    n= 42  0.1132 / 0.0738   fark -0.0394
    PHL   n= 42  0.1076 / 0.0980   fark -0.0096
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       103         0.035         0.029   -0.006
  0.1-0.2        76         0.152         0.184   +0.033
  0.2-0.3        65         0.242         0.277   +0.035
  0.3-0.4        32         0.347         0.250   -0.097
  0.4-0.5         7         0.438         0.143   -0.295
  0.5-0.6         4         0.560         0.750   +0.190
  0.6-0.7         0             —             —        —
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         0             —             —        —
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (551)
  işlem sayısı                     551
  kazanan                          200  (%36)
  ort. İDDİA EDİLEN edge       +13.46p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.97p   ±1.6p  %95 [-4.1p, +2.2p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    587.09 $
  PnL fee ÖNCESİ              -1172.29 $
  PnL fee SONRASI             -1759.38 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1000.95 $   %90 aralık [-3969.98, +2458.55]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1301 (model 0.1246)

  bizim (fee sonrası)             -1759.38 $

  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
