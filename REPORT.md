========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-10-07T19:26:18.683345Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          68100
  orderbook seviyesi     3642875
  tahmin snapshot          45612
  karar                    14010
  simüle fill               3637
  çözümlenmiş kova          1692

## Brier skoru  (düşük = iyi, 1608 kova)
  model                  0.1312
  piyasa (mid)           0.1335   n=1608
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0023  ±0.0034  %95 [-0.0043, +0.0089]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=234  0.1298 / 0.2033   fark +0.0735
    CHI   n=228  0.1346 / 0.1132   fark -0.0215
    DEN   n=234  0.1456 / 0.2003   fark +0.0546
    LAX   n=228  0.1266 / 0.0987   fark -0.0279
    MIA   n=228  0.1362 / 0.1130   fark -0.0232
    NY    n=228  0.1082 / 0.0872   fark -0.0209
    PHL   n=228  0.1367 / 0.1149   fark -0.0219
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       598         0.034         0.057   +0.023
  0.1-0.2       409         0.151         0.191   +0.039
  0.2-0.3       335         0.246         0.242   -0.004
  0.3-0.4       175         0.346         0.251   -0.095
  0.4-0.5        69         0.435         0.304   -0.130
  0.5-0.6        18         0.551         0.333   -0.218
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (3550)
  işlem sayısı                    3550
  kazanan                         1426  (%40)
  ort. İDDİA EDİLEN edge       +16.26p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.56p   ±0.7p  %95 [+0.2p, +2.9p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   3538.84 $
  PnL fee ÖNCESİ             +26693.26 $
  PnL fee SONRASI            +23154.42 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -9219.36 $   %90 aralık [-16748.40, -2409.59]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1335 (model 0.1312)

  bizim (fee sonrası)            +23154.42 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
