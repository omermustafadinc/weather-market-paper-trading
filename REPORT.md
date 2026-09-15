========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-15T20:43:51.840195Z
lead time     : 8 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot          33906
  orderbook seviyesi     1798158
  tahmin snapshot          23184
  karar                     6864
  simüle fill               1794
  çözümlenmiş kova           780

## Brier skoru  (düşük = iyi, 738 kova)
  model                  0.1281
  piyasa (mid)           0.1315   n=738
  klimatoloji (1/k)      0.1389
  sabit %50              0.2500

  fark (piyasa - model)   +0.0034  ±0.0044  %95 [-0.0051, +0.0120]
  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.
     Bu veriyle model piyasadan iyi de kötü de denemez.

  şehir bazında (model / piyasa):
    AUS   n=108  0.1539 / 0.2106   fark +0.0567
    CHI   n=102  0.1282 / 0.1109   fark -0.0173
    DEN   n=108  0.1476 / 0.2094   fark +0.0618
    LAX   n=102  0.1053 / 0.0906   fark -0.0147
    MIA   n=108  0.1259 / 0.1105   fark -0.0154
    NY    n=108  0.1056 / 0.0839   fark -0.0217
    PHL   n=102  0.1291 / 0.0998   fark -0.0293
    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)

## Kalibrasyon eğrisi (model)
  aralık          n   ort. tahmin   gerçekleşen     fark
  0.0-0.1       273         0.033         0.040   +0.007
  0.1-0.2       180         0.149         0.194   +0.045
  0.2-0.3       167         0.245         0.275   +0.031
  0.3-0.4        77         0.343         0.234   -0.109
  0.4-0.5        29         0.430         0.207   -0.223
  0.5-0.6         8         0.546         0.375   -0.171
  0.6-0.7         2         0.674         1.000   +0.326
  0.7-0.8         1         0.703         1.000   +0.297
  0.8-0.9         1         0.877         1.000   +0.123
  0.9-1.0         0             —             —        —
  (fark pozitif = model az tahmin ediyor, negatif = fazla)

## İşlemler (1722)
  işlem sayısı                    1722
  kazanan                          680  (%39)
  ort. İDDİA EDİLEN edge       +14.90p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         +1.35p   ±1.0p  %95 [-0.6p, +3.3p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                   1758.95 $
  PnL fee ÖNCESİ              +9690.46 $
  PnL fee SONRASI             +7931.51 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)       -3528.28 $   %90 aralık [-9110.58, +2068.68]  (200 deneme)
  (c) piyasayı doğru kabul et   Brier 0.1315 (model 0.1281)

  bizim (fee sonrası)             +7931.51 $

========================================================================
Bu rapor lookahead denetiminden geçmiş veriden üretildi.
Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.
