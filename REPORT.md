========================================================================
HAVA DURUMU KÂĞIT-İŞLEM RAPORU
üretim zamanı : 2026-08-31T18:39:57.731139Z
lead time     : 24 saat (hedef günün yerel başlangıcından önce)
========================================================================

## Veri
  piyasa snapshot           4962
  orderbook seviyesi      273882
  tahmin snapshot           4032
  karar                      876
  simüle fill                219
  çözümlenmiş kova           138

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
    DEN   2026-08-31  en erken tahmin 2026-08-29T06:28Z  -> lead 47.5 saat

  Daha uzun lead istiyorsak veri birikmesini beklemek gerek:
  toplama 2026-08-28 18:18Z'de başladı, o günün hedefleri için
  yeterince erken tahmin yok.

  Sayı uydurmuyoruz — biriktikçe rapor dolacak.

## İşlemler (106)
  işlem sayısı                     106
  kazanan                           37  (%35)
  ort. İDDİA EDİLEN edge       +13.88p   (beklenen değer)
  ort. GERÇEKLEŞEN edge         -2.19p   ±3.9p  %95 [-9.8p, +5.4p]
     -> iddia edilen değer aralığın DIŞINDA: model sistematik
        olarak yanlış kalibre veya hesapta sorun var.
  toplam fee                    127.66 $
  PnL fee ÖNCESİ               +173.25 $
  PnL fee SONRASI               +45.59 $

## Baseline karşılaştırması
  (a) hiç işlem yapmamak             +0.00 $
  (b) rastgele işlem (ort.)        -201.66 $   %90 aralık [-1766.42, +1252.32]  (200 deneme)

  bizim (fee sonrası)               +45.59 $

  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye
     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.
