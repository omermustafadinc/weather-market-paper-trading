========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-09-02T20:15:07.293607Z
lead time     : 24 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot           8430
  orderbook seviyesi      468020
  tahmin snapshot           6804
  karar                     1560
  simüle fill                398
  çözümlenmiş kova           222

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
    CHI   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 34.7 saat
    DEN   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 35.7 saat
    LAX   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 36.7 saat
    MIA   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    NY    2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    PHL   2026-08-30  en erken tahmin 2026-08-28T18:19Z  -> lead 33.7 saat
    AUS   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 46.5 saat
    CHI   2026-08-31  en erken tahmin 2026-08-29T06:27Z  -> lead 46.5 saat
    DEN   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 47.5 saat
    LAX   2026-08-31  en erken tahmin 2026-08-29T07:06Z  -> lead 47.9 saat
    MIA   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat
    NY    2026-08-31  en erken tahmin 2026-08-29T06:27Z  -> lead 45.5 saat
    PHL   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 45.5 saat
    AUS   2026-09-01  en erken tahmin 2026-08-30T05:55Z  -> lead 47.1 saat
    CHI   2026-09-01  en erken tahmin 2026-08-30T05:54Z  -> lead 47.1 saat
    DEN   2026-09-01  en erken tahmin 2026-08-30T06:20Z  -> lead 47.7 saat
    LAX   2026-09-01  en erken tahmin 2026-08-30T11:48Z  -> lead 43.2 saat
    MIA   2026-09-01  en erken tahmin 2026-08-30T05:54Z  -> lead 46.1 saat
    NY    2026-09-01  en erken tahmin 2026-08-30T05:54Z  -> lead 46.1 saat
    PHL   2026-09-01  en erken tahmin 2026-08-30T05:55Z  -> lead 46.1 saat
    AUS   2026-09-02  en erken tahmin 2026-08-31T05:21Z  -> lead 47.6 saat
    DEN   2026-09-02  en erken tahmin 2026-08-31T11:41Z  -> lead 42.3 saat

  Daha uzun lead istiyorsak veri birikmesini beklemek gerek:
  toplama 2026-08-28 18:18Z'de başladı, o günün hedefleri için
  yeterince erken tahmin yok.

  Sayı uydurmuyoruz — biriktikçe rapor dolacak.

## İşlemler (289)
  işlem sayısı                     289
  kazanan                          101  (%35)
  ort. İDDİA EDİLEN edge       +13.36p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -2.20p   ±2.4p  %95 [-6.8p, +2.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    334.95 $
  PnL fee ÖNCESİ               +968.40 $
  PnL fee SONRASI              +633.45 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -597.14 $   %90 aralık [-3084.37, +1480.85]  (200 deneme)

  bizim (fee sonrası)              +633.45 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.
