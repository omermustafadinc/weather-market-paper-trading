"""Fill simülasyonu ve fee modeli.

Bu dosyanın tek işi dürüst olmak. Mid fiyattan doldurmak, sonsuz derinlik
varsaymak veya fee'yi unutmak — hepsi sonucu güzelleştirir ve hepsi yalandır.

Orderbook semantiği (gerçek üretim verisiyle 16/16 doğrulandı)
--------------------------------------------------------------
Kalshi iki tarafta da *bekleyen alış* verir; ayrı bir satış tarafı yoktur.
p fiyatından YES satmak, (1−p) fiyatından NO almakla aynı şeydir. Dolayısıyla:

    YES almak  ->  kitabın NO tarafını yer,  fiyat = 1000 − no_bid
    NO almak   ->  kitabın YES tarafını yer, fiyat = 1000 − yes_bid

Doğrulama: API'nin verdiği `yes_ask` her seferinde `1000 − en_iyi_no_bid`e
eşit çıktı. Bu ilişkiyi varsaymak yerine ölçtük.

Fill kuralları
--------------
* Mid'den doldurma YOK. Karşı taraftaki merdiveni en ucuzdan başlayarak
  boyut kadar tüket, ağırlıklı ortalama fiyattan doldur.
* Derinlik yetmiyorsa kısmi fill, hiç yoksa fill yok.
* Görünür likiditenin en fazla %10'u alınır.
* Fill, karardan SONRA çekilmiş kitaba karşı hesaplanır (çağıran sorumluluğu;
  şemadaki CHECK kısıtı da bunu zorluyor).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Iterable, Sequence

DOLLAR_DCENTS = 1000

#: Bir piyasadaki görünür likiditenin alınabilecek en yüksek oranı.
MAX_LIQUIDITY_FRACTION = 0.10

#: Kalshi taker fee sabiti: fee = ceil(0.07 · C · P · (1−P) · 100) / 100 dolar.
#: Seri metadata'sındaki `fee_multiplier` ile çarpılır (hava serilerinde 1).
#: UYARI: Kalshi'nin resmi fee schedule'ına erişilemedi (kalshi.com engelli);
#: formül üçüncü taraf kaynaklardan ve API'nin `fee_type: quadratic` alanıyla
#: tutarlı. Bkz. DECISIONS.md §6 ve §7.2.
TAKER_FEE_COEFF = 0.07


@dataclass(frozen=True, slots=True)
class Level:
    price_dcents: int
    quantity: float


@dataclass(frozen=True, slots=True)
class Fill:
    side: str                      # 'yes' | 'no' — ALINAN taraf
    requested: float
    filled: float
    avg_price_dcents: float | None
    fee_dcents: float
    levels: tuple[tuple[int, float], ...]   # (fiyat, adet) tüketilen seviyeler
    status: str                    # 'full' | 'partial' | 'none'
    visible: float                 # merdivendeki toplam görünür adet
    capped_by_liquidity: bool
    note: str = ""

    @property
    def cost_dcents(self) -> float:
        """Kontrat maliyeti (fee hariç)."""
        return 0.0 if self.avg_price_dcents is None else self.avg_price_dcents * self.filled

    @property
    def total_cost_dcents(self) -> float:
        return self.cost_dcents + self.fee_dcents


# ---------------------------------------------------------------------------
# Merdiven kurma
# ---------------------------------------------------------------------------


def ask_ladder(levels: Iterable[Level], side: str) -> list[Level]:
    """`side` almak için tüketilecek merdiven, EN UCUZDAN pahalıya.

    `levels` ilgili tarafın bekleyen alışlarıdır: YES almak için 'no' seviyeleri,
    NO almak için 'yes' seviyeleri verilmelidir.
    """
    if side not in ("yes", "no"):
        raise ValueError(f"side 'yes' veya 'no' olmalı: {side!r}")
    out = [Level(DOLLAR_DCENTS - lv.price_dcents, lv.quantity)
           for lv in levels if lv.quantity > 0]
    # En iyi karşı-bid (en yüksek) -> bizim için en ucuz ask. Artan sırala.
    out.sort(key=lambda lv: lv.price_dcents)
    return out


def levels_from_book(book: dict, book_side: str) -> list[Level]:
    """Ham orderbook JSON'undan bir tarafın seviyeleri."""
    from .kalshi import parse_orderbook
    return [Level(lv.price_dcents, lv.quantity)
            for lv in parse_orderbook(book) if lv.side == book_side]


# ---------------------------------------------------------------------------
# Fee
# ---------------------------------------------------------------------------


def taker_fee_dcents(contracts: float, price_dcents: float,
                     *, multiplier: float = 1.0) -> float:
    """Kalshi taker fee, desi-sent cinsinden.

    fee = ceil(0.07 · mult · C · P · (1−P) · 100) / 100  dolar
    (sente yukarı yuvarlanır; 50 sentte kontrat başına ~1.75 sent tavan)
    """
    if contracts <= 0:
        return 0.0
    p = price_dcents / DOLLAR_DCENTS
    raw_dollars = TAKER_FEE_COEFF * multiplier * contracts * p * (1.0 - p)
    cents = math.ceil(raw_dollars * 100 - 1e-9)      # sente yukarı yuvarla
    return cents * 10.0                               # sent -> desi-sent


# ---------------------------------------------------------------------------
# Fill
# ---------------------------------------------------------------------------


def simulate_fill(
    levels: Sequence[Level], side: str, requested: float, *,
    fee_multiplier: float = 1.0,
    max_liquidity_fraction: float = MAX_LIQUIDITY_FRACTION,
    max_price_dcents: int | None = None,
) -> Fill:
    """Merdiveni tüketerek gerçekçi fill üret.

    `levels`: karşı tarafın bekleyen alışları (YES almak için 'no' seviyeleri).
    `max_price_dcents`: limit fiyat; bundan pahalı seviyeler yenmez.
    """
    ladder = ask_ladder(levels, side)
    visible = sum(lv.quantity for lv in ladder)

    if requested <= 0 or not ladder or visible <= 0:
        return Fill(side, max(requested, 0.0), 0.0, None, 0.0, (), "none",
                    visible, False, "merdiven boş" if visible <= 0 else "talep sıfır")

    # Görünür likiditenin %10'undan fazlasını alma.
    cap = visible * max_liquidity_fraction
    # "Likidite tavanı bağladı" demek için kuralın GERÇEKTEN bağlaması lazım:
    # tavan görünür derinliğin altındaysa ve talep tavanı aşıyorsa. Aksi hâlde
    # kısmi fill'in sebebi derinliğin bitmesidir; ikisini karıştırmak fill
    # raporunu yanlış gerekçelendirirdi.
    capped = requested > cap and cap < visible
    target = min(requested, cap)

    taken: list[tuple[int, float]] = []
    filled = 0.0
    notional = 0.0
    for lv in ladder:
        if filled >= target - 1e-12:
            break
        if max_price_dcents is not None and lv.price_dcents > max_price_dcents:
            break
        take = min(lv.quantity, target - filled)
        if take <= 0:
            continue
        taken.append((lv.price_dcents, take))
        filled += take
        notional += lv.price_dcents * take

    if filled <= 0:
        note = "limit fiyatın altında seviye yok" if max_price_dcents is not None else "fill yok"
        return Fill(side, requested, 0.0, None, 0.0, (), "none", visible, capped, note)

    avg = notional / filled
    # Fee, gerçekleşen her seviye için ayrı hesaplanıp toplanır: Kalshi ücreti
    # işlem başına alıyor ve yukarı yuvarlıyor. Tek ortalama fiyattan hesaplamak
    # tek yuvarlama yapar ve maliyeti OLDUĞUNDAN AZ gösterir; burada tutucu
    # olanı seçtik (bkz. DECISIONS.md §6 — resmi fee schedule'a erişilemedi).
    fee = sum(taker_fee_dcents(q, p, multiplier=fee_multiplier) for p, q in taken)

    status = "full" if filled >= requested - 1e-9 else "partial"
    notes = []
    if capped:
        notes.append(f"likidite tavanı: görünür {visible:.0f}, alınabilir {cap:.0f}")
    if status == "partial" and not capped:
        notes.append("derinlik yetmedi")

    return Fill(side, requested, filled, avg, fee, tuple(taken), status,
                visible, capped, "; ".join(notes))
