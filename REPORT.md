========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-11T14:50:00.656534Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          25578
  orderbook seviyesi     1354995
  tahmin snapshot          17892
  karar                     5094
  simüle fill               1318
  çözümlenmiş kova           600

## Brier skoru  (düşük = iyi, 558 kova)
  model                  0.1262
  piyasa (mid)           0.1305   n=558
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0043  ±0.0051  %95 [-0.0058, +0.0144]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 84  0.1542 / 0.2086   fark +0.0544
    CHI   n= 78  0.1249 / 0.1047   fark -0.0201
    DEN   n= 84  0.1447 / 0.2124   fark +0.0676
    LAX   n= 78  0.0948 / 0.0849   fark -0.0099
    MIA   n= 78  0.1230 / 0.1080   fark -0.0150
    NY    n= 78  0.1077 / 0.0854   fark -0.0223
    PHL   n= 78  0.1304 / 0.0971   fark -0.0333
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       214         0.033         0.037   +0.004
  0.1-0.2       129         0.150         0.194   +0.043
  0.2-0.3       127         0.246         0.291   +0.046
  0.3-0.4        57         0.346         0.228   -0.117
  0.4-0.5        20         0.437         0.150   -0.287
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1226)
  işlem sayısı                    1226
  kazanan                          491  (%40)
  ort. İDDİA EDİLEN edge       +14.74p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.03p   ±1.1p  %95 [-1.2p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1244.18 $
  PnL fee ÖNCESİ              +4406.28 $
  PnL fee SONRASI             +3162.10 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -2102.55 $   %90 aralık [-5857.84, +1739.18]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1305 (model 0.1262)

  bizim (fee sonrası)             +3162.10 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
