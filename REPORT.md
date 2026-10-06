========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-06T15:36:38.864796Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          66720
  orderbook seviyesi     3568603
  tahmin snapshot          44604
  karar                    13740
  simüle fill               3565
  çözümlenmiş kova          1644

## Brier skoru  (düşük = iyi, 1596 kova)
  model                  0.1310
  piyasa (mid)           0.1328   n=1596
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0018  ±0.0034  %95 [-0.0048, +0.0084]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=228  0.1291 / 0.2027   fark +0.0736
    CHI   n=228  0.1346 / 0.1132   fark -0.0215
    DEN   n=228  0.1459 / 0.2001   fark +0.0542
    LAX   n=228  0.1266 / 0.0987   fark -0.0279
    MIA   n=228  0.1362 / 0.1130   fark -0.0232
    NY    n=228  0.1082 / 0.0872   fark -0.0209
    PHL   n=228  0.1367 / 0.1149   fark -0.0219
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       595         0.034         0.057   +0.023
  0.1-0.2       405         0.151         0.190   +0.039
  0.2-0.3       331         0.246         0.242   -0.004
  0.3-0.4       175         0.346         0.251   -0.095
  0.4-0.5        68         0.435         0.309   -0.126
  0.5-0.6        18         0.551         0.333   -0.218
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3529)
  işlem sayısı                    3529
  kazanan                         1414  (%40)
  ort. İDDİA EDİLEN edge       +16.23p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.48p   ±0.7p  %95 [+0.1p, +2.8p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3518.95 $
  PnL fee ÖNCESİ             +25919.08 $
  PnL fee SONRASI            +22400.13 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9600.77 $   %90 aralık [-16545.01, -3223.97]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1328 (model 0.1310)

  bizim (fee sonrası)            +22400.13 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
