========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-16T19:34:24.787543Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          35610
  orderbook seviyesi     1895574
  tahmin snapshot          24318
  karar                     7212
  simüle fill               1886
  çözümlenmiş kova           810

## Brier skoru  (düşük = iyi, 768 kova)
  model                  0.1293
  piyasa (mid)           0.1330   n=768
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0037  ±0.0043  %95 [-0.0047, +0.0121]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=114  0.1554 / 0.2117   fark +0.0563
    CHI   n=108  0.1288 / 0.1093   fark -0.0195
    DEN   n=114  0.1464 / 0.2095   fark +0.0631
    LAX   n=108  0.1081 / 0.0959   fark -0.0123
    MIA   n=108  0.1259 / 0.1105   fark -0.0154
    NY    n=108  0.1056 / 0.0839   fark -0.0217
    PHL   n=108  0.1327 / 0.1018   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       281         0.033         0.043   +0.009
  0.1-0.2       193         0.150         0.197   +0.047
  0.2-0.3       172         0.244         0.273   +0.029
  0.3-0.4        81         0.345         0.222   -0.122
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
  (b) rastgele işlem (ort.)       -4266.75 $   %90 aralık [-9000.96, +871.00]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1330 (model 0.1293)

  bizim (fee sonrası)             +7896.73 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
