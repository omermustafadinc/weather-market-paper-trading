========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-16T06:39:19.493470Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          34770
  orderbook seviyesi     1846298
  tahmin snapshot          23688
  karar                     7044
  simüle fill               1842
  çözümlenmiş kova           798

## Brier skoru  (düşük = iyi, 756 kova)
  model                  0.1290
  piyasa (mid)           0.1316   n=756
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0027  ±0.0043  %95 [-0.0058, +0.0111]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=108  0.1539 / 0.2106   fark +0.0567
    CHI   n=108  0.1288 / 0.1093   fark -0.0195
    DEN   n=108  0.1476 / 0.2094   fark +0.0618
    LAX   n=108  0.1081 / 0.0959   fark -0.0123
    MIA   n=108  0.1259 / 0.1105   fark -0.0154
    NY    n=108  0.1056 / 0.0839   fark -0.0217
    PHL   n=108  0.1327 / 0.1018   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       278         0.033         0.043   +0.010
  0.1-0.2       188         0.150         0.197   +0.047
  0.2-0.3       170         0.245         0.271   +0.026
  0.3-0.4        79         0.344         0.228   -0.116
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1754)
  işlem sayısı                    1754
  kazanan                          693  (%40)
  ort. İDDİA EDİLEN edge       +14.88p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.20p   ±1.0p  %95 [-0.7p, +3.1p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1784.41 $
  PnL fee ÖNCESİ              +9681.14 $
  PnL fee SONRASI             +7896.73 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3921.87 $   %90 aralık [-9239.99, +1374.45]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1316 (model 0.1290)

  bizim (fee sonrası)             +7896.73 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
