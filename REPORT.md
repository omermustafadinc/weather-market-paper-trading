========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-11T10:32:08.640998Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          25242
  orderbook seviyesi     1339001
  tahmin snapshot          17766
  karar                     5010
  simüle fill               1296
  çözümlenmiş kova           588

## Brier skoru  (düşük = iyi, 546 kova)
  model                  0.1253
  piyasa (mid)           0.1285   n=546
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0032  ±0.0052  %95 [-0.0069, +0.0133]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n= 78  0.1515 / 0.2074   fark +0.0559
    CHI   n= 78  0.1249 / 0.1047   fark -0.0201
    DEN   n= 78  0.1448 / 0.2120   fark +0.0671
    LAX   n= 78  0.0948 / 0.0849   fark -0.0099
    MIA   n= 78  0.1230 / 0.1080   fark -0.0150
    NY    n= 78  0.1077 / 0.0854   fark -0.0223
    PHL   n= 78  0.1304 / 0.0971   fark -0.0333
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       209         0.034         0.033   -0.000
  0.1-0.2       128         0.150         0.195   +0.045
  0.2-0.3       123         0.247         0.293   +0.046
  0.3-0.4        56         0.345         0.232   -0.113
  0.4-0.5        19         0.437         0.158   -0.279
  0.5-0.6         7         0.552         0.429   -0.123
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1194)
  işlem sayısı                    1194
  kazanan                          475  (%40)
  ort. İDDİA EDİLEN edge       +14.63p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +0.48p   ±1.1p  %95 [-1.8p, +2.7p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1201.07 $
  PnL fee ÖNCESİ              +2819.81 $
  PnL fee SONRASI             +1618.74 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -1851.47 $   %90 aralık [-6233.13, +2691.44]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1285 (model 0.1253)

  bizim (fee sonrası)             +1618.74 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
