========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-10T01:41:25.390498Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          23082
  orderbook seviyesi     1233499
  tahmin snapshot          16254
  karar                     4602
  simüle fill               1190
  çözümlenmiş kova           540

## Brier skoru  (düşük = iyi, 498 kova)
  model                  0.1258
  piyasa (mid)           0.1287   n=498
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0029  ±0.0054  %95 [-0.0076, +0.0134]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 72  0.1499 / 0.2056   fark +0.0556
    CHI   n= 72  0.1253 / 0.0989   fark -0.0264
    DEN   n= 72  0.1451 / 0.2099   fark +0.0647
    LAX   n= 66  0.1038 / 0.0963   fark -0.0075
    MIA   n= 72  0.1215 / 0.1113   fark -0.0102
    NY    n= 72  0.1050 / 0.0809   fark -0.0241
    PHL   n= 72  0.1282 / 0.0954   fark -0.0328
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       190         0.033         0.037   +0.004
  0.1-0.2       117         0.151         0.188   +0.037
  0.2-0.3       113         0.247         0.292   +0.045
  0.3-0.4        52         0.347         0.250   -0.097
  0.4-0.5        16         0.438         0.125   -0.313
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         1         0.648         1.000   +0.352
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1082)
  işlem sayısı                    1082
  kazanan                          424  (%39)
  ort. İDDİA EDİLEN edge       +14.43p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -0.05p   ±1.2p  %95 [-2.4p, +2.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1077.81 $
  PnL fee ÖNCESİ              +2221.26 $
  PnL fee SONRASI             +1143.45 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1889.82 $   %90 aralık [-5579.98, +1820.59]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1287 (model 0.1258)

  bizim (fee sonrası)             +1143.45 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
