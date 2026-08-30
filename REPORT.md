========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-08-30T19:16:18.888922Z
lead time     : 24 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot           3570
  orderbook seviyesi      198088
  tahmin snapshot           3024
  karar                      600
  simüle fill                140
  çözümlenmiş kova            96

## KALİBRASYON: VERİ YOK
  24 saatlik lead time'da değerlendirilebilir tahmin-sonuç çifti yok.

  Çözümlenmiş günler için ELDEKİ en uzun lead time:
    AUS   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -13.3 saat
    CHI   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -13.3 saat
    DEN   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -12.3 saat
    LAX   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -11.3 saat
    MIA   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    NY    2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    PHL   2026-08-28  en erken tahmin 2026-08-28T18:19Z  -> lead -14.3 saat
    AUS   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 10.7 saat
    CHI   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 10.7 saat
    DEN   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 11.7 saat
    LAX   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 12.7 saat
    MIA   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    NY    2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    PHL   2026-08-29  en erken tahmin 2026-08-28T18:19Z  -> lead 9.7 saat
    AUS   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 34.7 saat
    DEN   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 35.7 saat

  Daha uzun lead istiyorsak veri birikmesini beklemek gerek:
  toplama 2026-08-28 18:18Z'de başladı, o günün hedefleri için
  yeterince erken tahmin yok.

  Sayı uydurmuyoruz — biriktikçe rapor dolacak.

## İşlemler (30)
  işlem sayısı                      30
  kazanan                           19  (%63)
  ort. İDDİA EDİLEN edge       +17.21p   (beklenen değer)
  ort. GERÇEKLEŞEN edge        +26.92p   ±7.8p  %95 [+11.5p, +42.3p]
     -> iddia edilen değer bu aralığın İÇİNDE: ikisi tutarlı,
        aradaki fark bu örneklem büyüklüğünde gürültü.
  toplam fee                     34.15 $
  PnL fee ÖNCESİ              +1540.20 $
  PnL fee SONRASI             +1506.05 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)         +26.16 $   %90 aralık [-766.01, +722.77]  (200 deneme)

  bizim (fee sonrası)             +1506.05 $

  !! ÖRNEK ÇOK KÜÇÜK (n=30). Bu sayılardan sonuç çıkarılamaz.
     Hava piyasalarında tek bir günün sonucu neredeyse tamamen
     şanstır; anlamlı bir yargı için haftalarca veri gerekir.
