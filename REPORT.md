========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-15T23:28:17.975727Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          34242
  orderbook seviyesi     1815950
  tahmin snapshot          23436
  karar                     6948
  simüle fill               1814
  çözümlenmiş kova           792

## Brier skoru  (düşük = iyi, 750 kova)
  model                  0.1287
  piyasa (mid)           0.1312   n=750
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0025  ±0.0043  %95 [-0.0060, +0.0110]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=108  0.1539 / 0.2106   fark +0.0567
    CHI   n=108  0.1288 / 0.1093   fark -0.0195
    DEN   n=108  0.1476 / 0.2094   fark +0.0618
    LAX   n=102  0.1053 / 0.0906   fark -0.0147
    MIA   n=108  0.1259 / 0.1105   fark -0.0154
    NY    n=108  0.1056 / 0.0839   fark -0.0217
    PHL   n=108  0.1327 / 0.1018   fark -0.0310
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       277         0.034         0.043   +0.010
  0.1-0.2       184         0.149         0.196   +0.046
  0.2-0.3       169         0.244         0.272   +0.028
  0.3-0.4        79         0.344         0.228   -0.116
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1751)
  işlem sayısı                    1751
  kazanan                          690  (%39)
  ort. İDDİA EDİLEN edge       +14.88p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.10p   ±1.0p  %95 [-0.8p, +3.0p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1781.77 $
  PnL fee ÖNCESİ              +9351.39 $
  PnL fee SONRASI             +7569.62 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3793.55 $   %90 aralık [-8485.48, +1091.49]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1312 (model 0.1287)

  bizim (fee sonrası)             +7569.62 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
