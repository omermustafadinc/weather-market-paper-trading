========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-28T23:02:53.890694Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          56904
  orderbook seviyesi     3038152
  tahmin snapshot          37926
  karar                    11730
  simüle fill               3067
  çözümlenmiş kova          1332

## Brier skoru  (düşük = iyi, 1290 kova)
  model                  0.1319
  piyasa (mid)           0.1340   n=1290
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0022  ±0.0037  %95 [-0.0052, +0.0095]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=186  0.1364 / 0.2107   fark +0.0743
    CHI   n=186  0.1269 / 0.1123   fark -0.0146
    DEN   n=186  0.1458 / 0.2037   fark +0.0578
    LAX   n=180  0.1244 / 0.0965   fark -0.0279
    MIA   n=186  0.1397 / 0.1137   fark -0.0261
    NY    n=180  0.1077 / 0.0862   fark -0.0215
    PHL   n=186  0.1412 / 0.1125   fark -0.0287
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       477         0.034         0.057   +0.022
  0.1-0.2       329         0.152         0.198   +0.046
  0.2-0.3       276         0.247         0.243   -0.004
  0.3-0.4       140         0.346         0.236   -0.111
  0.4-0.5        51         0.435         0.294   -0.141
  0.5-0.6        13         0.545         0.308   -0.237
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3009)
  işlem sayısı                    3009
  kazanan                         1213  (%40)
  ort. İDDİA EDİLEN edge       +16.02p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +2.13p   ±0.7p  %95 [+0.7p, +3.6p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3025.33 $
  PnL fee ÖNCESİ             +24240.14 $
  PnL fee SONRASI            +21214.81 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -7959.17 $   %90 aralık [-14503.40, -1885.88]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1340 (model 0.1319)

  bizim (fee sonrası)            +21214.81 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
