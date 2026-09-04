"""Değerlendirme raporu.

İlk kural: `assert_no_lookahead` geçmeden hiçbir sayı basılmaz. Rapor
üretmek, verinin temiz olduğunu iddia etmektir.

İkinci kural: sonuç kötüyse kötü raporlanır. Eşik, model veya şehir seçimi
sonuca bakarak değiştirilmez. Bu yüzden rapor tek bir eşiğin sonucunu değil,
eşiğe duyarlılığın tamamını gösterir.

Ne ölçülüyor
------------
* **Brier skoru** — model, piyasa ve iki naif referans için ayrı ayrı.
  Piyasadan daha kötü bir Brier, edge iddiasını daha baştan bitirir.
* **Kalibrasyon eğrisi** — model %70 dediğinde gerçekten %70 oluyor mu.
* **İddia edilen vs gerçekleşen edge** — fill ve fee sonrası ne kalıyor.
* **PnL** — fee'den önce ve sonra, ayrı ayrı.
* **Baseline'lar** — hiç işlem yapmamak, rastgele işlem, piyasaya güvenmek.

Model olasılıkları depolanmış kararlardan DEĞİL, saklanan tahminlerden
yeniden hesaplanır. Böylece işlem yapılmamış kovalar da değerlendirmeye
girer — yalnızca işlem yapılanlara bakmak seçim yanlılığı olurdu.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from . import config as cfg
from . import db, model
from .clock import iso_to_us, us_to_iso
from .fills import DOLLAR_DCENTS, taker_fee_dcents


# ---------------------------------------------------------------------------
# Tahmin-sonuç eşleştirme
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class Case:
    """Bir kova için: model olasılığı, piyasa olasılığı, gerçekleşen sonuç."""

    city: str
    target_date: str
    event_ticker: str
    market_ticker: str
    model_prob: float
    market_prob: float | None
    outcome: int
    as_of_iso: str
    lead_hours: float


def build_cases(conn: sqlite3.Connection, *, lead_hours: float = 24.0,
                verbose: bool = False) -> list[Case]:
    """Her (şehir, hedef gün) için, hedef günün başlangıcından `lead_hours`
    önceki bilgiyle model ve piyasa olasılıklarını kur, sonuçla eşleştir.

    Sabit lead time şart: farklı lead'lerdeki tahminleri karıştırmak beceriyi
    olduğundan iyi veya kötü gösterir.
    """
    cases: list[Case] = []

    events = list(conn.execute(
        """SELECT DISTINCT s.event_ticker, s.series_ticker, s.target_date
           FROM (SELECT m.event_ticker, m.series_ticker, st.target_date
                 FROM market_snapshots m
                 JOIN settlements st ON st.market_ticker = m.market_ticker) s"""))

    for ev in events:
        city = cfg.CITY_BY_SERIES.get(ev["series_ticker"])
        if city is None:
            continue
        target = ev["target_date"]

        # Hedef günün YEREL başlangıcı; as-of bunun `lead_hours` öncesi.
        from zoneinfo import ZoneInfo
        day_start = datetime.fromisoformat(target + "T00:00:00").replace(
            tzinfo=ZoneInfo(city.tz))
        as_of_us = int((day_start - timedelta(hours=lead_hours)).timestamp() * 1e6)

        sample = model.load_ensemble_sample(conn, city.key, target, as_of_us=as_of_us)
        if sample.member_count == 0:
            if verbose:
                print(f"  {ev['event_ticker']}: lead {lead_hours}s için tahmin yok")
            continue

        buckets = model.load_buckets(conn, ev["event_ticker"], as_of_us=as_of_us)
        if not buckets:
            continue
        try:
            model.check_ladder(buckets)
            probs = model.bucket_probabilities(model.build_distribution(sample), buckets)
        except model.ModelError:
            continue

        market_probs = _market_probs(conn, ev["event_ticker"], as_of_us)

        for b in buckets:
            st = conn.execute(
                "SELECT outcome FROM settlements WHERE market_ticker = ?",
                (b.ticker,)).fetchone()
            if st is None or st["outcome"] is None:
                continue
            cases.append(Case(
                city.key, target, ev["event_ticker"], b.ticker,
                probs[b.ticker], market_probs.get(b.ticker), int(st["outcome"]),
                us_to_iso(as_of_us), lead_hours))
    return cases


def available_leads(conn: sqlite3.Connection) -> list[dict]:
    """Çözümlenmiş her (şehir, hedef gün) için eldeki en uzun lead time.

    "Neden sonuç yok" sorusunu tahminle değil veriyle cevaplamak için.
    """
    from zoneinfo import ZoneInfo

    rows = list(conn.execute(
        """SELECT DISTINCT m.series_ticker, st.target_date
           FROM market_snapshots m
           JOIN settlements st ON st.market_ticker = m.market_ticker"""))
    out = []
    for r in rows:
        city = cfg.CITY_BY_SERIES.get(r["series_ticker"])
        if city is None:
            continue
        f = conn.execute(
            """SELECT min(fetched_at_us) mn, min(fetched_at_iso) iso
               FROM forecast_snapshots
               WHERE location_key = ? AND target_date = ?""",
            (city.key, r["target_date"])).fetchone()
        if f is None or f["mn"] is None:
            continue
        day_start = datetime.fromisoformat(r["target_date"] + "T00:00:00").replace(
            tzinfo=ZoneInfo(city.tz))
        lead = (day_start.timestamp() * 1e6 - f["mn"]) / 3.6e9
        out.append({"city": city.key, "target_date": r["target_date"],
                    "earliest_iso": f["iso"], "max_lead_hours": lead})
    return sorted(out, key=lambda x: (x["target_date"], x["city"]))


def _market_probs(conn: sqlite3.Connection, event_ticker: str,
                  as_of_us: int) -> dict[str, float]:
    """Piyasanın örtük olasılıkları: mid fiyatlar, toplamı 1'e normalize.

    Normalizasyon gerekli çünkü spread yüzünden mid'ler toplamı 1 etmiyor
    (ölçtük: 0.99 ve 1.02). Normalize etmeden Brier karşılaştırması piyasaya
    haksızlık ederdi.
    """
    rows = list(conn.execute(
        """SELECT market_ticker, yes_bid_dcents, yes_ask_dcents,
                  max(fetched_at_us) AS t
           FROM market_snapshots
           WHERE event_ticker = ? AND fetched_at_us <= ? AND purpose = 'decision'
           GROUP BY market_ticker""",
        (event_ticker, as_of_us)))
    mids = {}
    for r in rows:
        b, a = r["yes_bid_dcents"], r["yes_ask_dcents"]
        if b is None or a is None:
            continue
        mids[r["market_ticker"]] = (b + a) / 2.0 / DOLLAR_DCENTS
    total = sum(mids.values())
    if total <= 0:
        return {}
    return {k: v / total for k, v in mids.items()}


# ---------------------------------------------------------------------------
# Metrikler
# ---------------------------------------------------------------------------


def brier(pairs: list[tuple[float, int]]) -> float | None:
    if not pairs:
        return None
    return sum((p - o) ** 2 for p, o in pairs) / len(pairs)


def calibration(pairs: list[tuple[float, int]], bins: int = 10) -> list[dict]:
    """Kalibrasyon eğrisi: her kovada ortalama tahmin vs gerçekleşen oran."""
    out = []
    for i in range(bins):
        lo, hi = i / bins, (i + 1) / bins
        sel = [(p, o) for p, o in pairs if (lo <= p < hi or (i == bins - 1 and p == 1.0))]
        if not sel:
            out.append({"bin": f"{lo:.1f}-{hi:.1f}", "n": 0,
                        "mean_pred": None, "observed": None})
            continue
        out.append({
            "bin": f"{lo:.1f}-{hi:.1f}", "n": len(sel),
            "mean_pred": sum(p for p, _ in sel) / len(sel),
            "observed": sum(o for _, o in sel) / len(sel),
        })
    return out


def climatology_prob(cases: list[Case]) -> float:
    """En naif referans: her kova için taban oran (kaç kova varsa 1/n)."""
    if not cases:
        return 0.0
    per_event = {}
    for c in cases:
        per_event.setdefault(c.event_ticker, 0)
        per_event[c.event_ticker] += 1
    return sum(1.0 / n for n in per_event.values()) / len(per_event) if per_event else 0.0


# ---------------------------------------------------------------------------
# İşlem değerlendirmesi
# ---------------------------------------------------------------------------


@dataclass
class TradeResult:
    market_ticker: str
    side: str
    contracts: float
    avg_price_dcents: float
    fee_dcents: float
    outcome: int
    claimed_edge: float
    #: Kontrat kazanırsa 1.00 $ (1000 desi-sent) öder.
    payoff_dcents: float = 0.0
    pnl_before_fee_dcents: float = 0.0
    pnl_after_fee_dcents: float = 0.0

    def compute(self) -> "TradeResult":
        win = self.outcome if self.side == "yes" else (1 - self.outcome)
        self.payoff_dcents = win * DOLLAR_DCENTS * self.contracts
        cost = self.avg_price_dcents * self.contracts
        self.pnl_before_fee_dcents = self.payoff_dcents - cost
        self.pnl_after_fee_dcents = self.pnl_before_fee_dcents - self.fee_dcents
        return self


def trade_results(conn: sqlite3.Connection) -> list[TradeResult]:
    rows = conn.execute(
        """SELECT d.market_ticker, d.edge, f.side, f.filled_contracts,
                  f.avg_price_dcents, f.fee_dcents, s.outcome
           FROM sim_fills f
           JOIN decisions d ON d.id = f.decision_id
           JOIN settlements s ON s.market_ticker = d.market_ticker
           WHERE f.filled_contracts > 0 AND s.outcome IS NOT NULL""").fetchall()
    return [TradeResult(r["market_ticker"], r["side"], r["filled_contracts"],
                        r["avg_price_dcents"], r["fee_dcents"], int(r["outcome"]),
                        r["edge"] or 0.0).compute() for r in rows]


def random_baseline(conn: sqlite3.Connection, sizes: list[float], *,
                    seed: int = 0, trials: int = 200) -> dict | None:
    """Rastgele işlem: aynı sayıda, AYNI BÜYÜKLÜKTE, rastgele piyasa ve yön.

    `sizes` bizim gerçek işlemlerimizin kontrat adetleri. Büyüklüğü eşitlemek
    şart: ilk sürümde baseline tek kontratla işlem yapıyordu ve bizim ~200
    kontratlık pozisyonlarımızla karşılaştırılıyordu — 200 katlık farkı beceri
    gibi gösteriyordu. Böyle bir karşılaştırma hiçbir şey ölçmez.

    Tek bir rastgele koşu gürültüdür; dağılımı görmek için çok kez tekrarlanıyor.
    """
    pool = conn.execute(
        """SELECT m.market_ticker, m.yes_bid_dcents, m.yes_ask_dcents, s.outcome
           FROM market_snapshots m
           JOIN settlements s ON s.market_ticker = m.market_ticker
           WHERE m.purpose = 'decision' AND s.outcome IS NOT NULL
             AND m.yes_ask_dcents IS NOT NULL
           GROUP BY m.market_ticker""").fetchall()
    if not pool or not sizes:
        return None

    rng = random.Random(seed)
    totals = []
    for _ in range(trials):
        total = 0.0
        for size in sizes:
            r = rng.choice(pool)
            side = rng.choice(("yes", "no"))
            price = r["yes_ask_dcents"] if side == "yes" else (
                DOLLAR_DCENTS - (r["yes_bid_dcents"] or 0))
            if not price or price <= 0 or price >= DOLLAR_DCENTS:
                continue
            win = r["outcome"] if side == "yes" else (1 - r["outcome"])
            # Aynı kontrat adediyle; fee de dahil, bizimkinde de dahil.
            total += size * (win * DOLLAR_DCENTS - price)
            total -= taker_fee_dcents(size, price)
        totals.append(total)
    totals.sort()
    return {"mean": sum(totals) / len(totals), "p05": totals[len(totals) // 20],
            "p95": totals[-len(totals) // 20 - 1], "trials": trials}


# ---------------------------------------------------------------------------
# Rapor
# ---------------------------------------------------------------------------


def _fmt(x: float | None, w: int = 8, d: int = 4) -> str:
    return f"{'—':>{w}}" if x is None else f"{x:>{w}.{d}f}"


def render(conn: sqlite3.Connection, *, lead_hours: float = 24.0,
           bins: int = 10) -> str:
    """Raporu üret. Lookahead denetimi geçmeden çağrılmamalı."""
    out: list[str] = []
    w = out.append

    w("=" * 72)
    w("HAVA DURUMU KÂĞIT-İŞLEM RAPORU")
    w(f"üretim zamanı : {us_to_iso(iso_to_us(datetime.now().astimezone().isoformat()))}")
    w(f"lead time     : {lead_hours:.0f} saat (hedef günün yerel başlangıcından önce)")
    w("=" * 72)

    # --- veri hacmi ---
    w("\n## Veri")
    for t, label in (("market_snapshots", "piyasa snapshot"),
                     ("orderbook_levels", "orderbook seviyesi"),
                     ("forecast_snapshots", "tahmin snapshot"),
                     ("decisions", "karar"),
                     ("sim_fills", "simüle fill"),
                     ("settlements", "çözümlenmiş kova")):
        n = conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
        w(f"  {label:<22} {n:>7}")

    cases = build_cases(conn, lead_hours=lead_hours)
    if not cases:
        w("\n## KALİBRASYON: VERİ YOK")
        w(f"  {lead_hours:.0f} saatlik lead time'da değerlendirilebilir "
          "tahmin-sonuç çifti yok.")
        avail = available_leads(conn)
        if avail:
            w("\n  Çözümlenmiş günler için ELDEKİ en uzun lead time:")
            for row in avail:
                w(f"    {row['city']:<5} {row['target_date']}  "
                  f"en erken tahmin {row['earliest_iso'][:16]}Z  "
                  f"-> lead {row['max_lead_hours']:.1f} saat")
            w("\n  DİKKAT: bu bir veri eksikliği olmayabilir. Kalshi günlük")
            w("  sıcaklık olaylarını hedef günden ~1 gün önce (~09:30Z) açıyor,")
            w("  yani hedef günün yerel başlangıcına ~12-16 saat kala. Daha uzun")
            w("  lead'de PİYASA HENÜZ YOK; model-piyasa karşılaştırması tanımı")
            w("  gereği yapılamaz. Ölçülebilir en uzun lead şehre göre ~8-16 saat.")
        else:
            w("  Henüz çözümlenmiş hedef gün yok.")
        w("\n  Sayı uydurmuyoruz — biriktikçe rapor dolacak.")
        w(_trades_section(conn, None, None))
        return "\n".join(out)

    model_pairs = [(c.model_prob, c.outcome) for c in cases]
    market_pairs = [(c.market_prob, c.outcome) for c in cases if c.market_prob is not None]

    # --- Brier ---
    w(f"\n## Brier skoru  (düşük = iyi, {len(cases)} kova)")
    clim = climatology_prob(cases)
    b_model = brier(model_pairs)
    b_market = brier(market_pairs)
    b_clim = brier([(clim, o) for _, o in model_pairs])
    b_half = brier([(0.5, o) for _, o in model_pairs])

    w(f"  model                {_fmt(b_model)}")
    w(f"  piyasa (mid)         {_fmt(b_market)}   n={len(market_pairs)}")
    w(f"  klimatoloji (1/k)    {_fmt(b_clim)}")
    w(f"  sabit %50            {_fmt(b_half)}")

    if b_model is not None and b_market is not None and len(market_pairs) > 1:
        # EŞLEŞTİRİLMİŞ karşılaştırma: aynı kova için iki tahminin hatası.
        # Ham farkı belirsizlik olmadan bildirmek yanıltıcı -- 264 kovada
        # 0.01'lik bir fark rahatlıkla gürültü olabilir.
        paired = [(c.market_prob - c.outcome) ** 2 - (c.model_prob - c.outcome) ** 2
                  for c in cases if c.market_prob is not None]
        mean_d = sum(paired) / len(paired)
        var = sum((x - mean_d) ** 2 for x in paired) / (len(paired) - 1)
        se = math.sqrt(var / len(paired))
        lo, hi = mean_d - 1.96 * se, mean_d + 1.96 * se
        w("")
        w(f"  fark (piyasa - model)  {mean_d:>+8.4f}  ±{se:.4f}  "
          f"%95 [{lo:+.4f}, {hi:+.4f}]")
        if lo > 0:
            w("  -> model piyasadan ANLAMLI ölçüde iyi")
        elif hi < 0:
            w("  -> model piyasadan ANLAMLI ölçüde KÖTÜ")
            w("     Piyasayı yenemeyen bir modelde edge aramanın anlamı yok.")
        else:
            w("  -> FARK ANLAMSIZ: güven aralığı sıfırı içeriyor.")
            w("     Bu veriyle model piyasadan iyi de kötü de denemez.")

        # Şehir bazında: ortalama gürültüyü gizleyebilir.
        w("\n  şehir bazında (model / piyasa):")
        import collections as _c
        by = _c.defaultdict(list)
        for c_ in cases:
            if c_.market_prob is not None:
                by[c_.city].append(c_)
        for k in sorted(by):
            v = by[k]
            bm = sum((x.model_prob - x.outcome) ** 2 for x in v) / len(v)
            bp = sum((x.market_prob - x.outcome) ** 2 for x in v) / len(v)
            w(f"    {k:<5} n={len(v):>3}  {bm:.4f} / {bp:.4f}   fark {bp-bm:+.4f}")
        w("    (tek bir şehri seçip 'edge bulduk' demek parametre ayarlamaktır)")

    # --- kalibrasyon ---
    w("\n## Kalibrasyon eğrisi (model)")
    w(f"  {'aralık':<12}{'n':>5}{'ort. tahmin':>14}{'gerçekleşen':>14}{'fark':>9}")
    for row in calibration(model_pairs, bins):
        if row["n"] == 0:
            w(f"  {row['bin']:<12}{0:>5}{'—':>14}{'—':>14}{'—':>9}")
            continue
        d = row["observed"] - row["mean_pred"]
        w(f"  {row['bin']:<12}{row['n']:>5}{row['mean_pred']:>14.3f}"
          f"{row['observed']:>14.3f}{d:>+9.3f}")
    w("  (fark pozitif = model az tahmin ediyor, negatif = fazla)")

    w(_trades_section(conn, b_model, b_market))

    w("\n" + "=" * 72)
    w("Bu rapor lookahead denetiminden geçmiş veriden üretildi.")
    w("Eşik/model/şehir seçimi sonuca bakarak değiştirilmedi.")
    return "\n".join(out)


def _trades_section(conn: sqlite3.Connection, b_model: float | None,
                    b_market: float | None) -> str:
    """İşlem sonuçları. Kalibrasyon verisinden BAĞIMSIZ.

    Erken sürümde rapor kalibrasyon verisi yoksa hiç buraya gelmiyordu;
    çözümlenmiş fill'ler varken bile 'sonuç yok' diyordu. Ayrıldı.
    """
    out: list[str] = []
    w = out.append
    trades = trade_results(conn)
    w(f"\n## İşlemler ({len(trades)})")
    if not trades:
        w("  Çözümlenmiş, geçerli fill yok.")
        w("  Not: kararlar yalnızca gelecek hedef günlerde veriliyor; sonuçları")
        w("  ertesi sabah NWS CLI raporuyla geliyor.")
        return "\n".join(out)
    if True:
        n = len(trades)
        claimed = sum(t.claimed_edge for t in trades) / n
        realized = sum((t.payoff_dcents - t.avg_price_dcents * t.contracts)
                       / (t.contracts * DOLLAR_DCENTS) for t in trades) / n
        pnl_b = sum(t.pnl_before_fee_dcents for t in trades)
        pnl_a = sum(t.pnl_after_fee_dcents for t in trades)
        fees = sum(t.fee_dcents for t in trades)
        wins = sum(1 for t in trades if t.pnl_after_fee_dcents > 0)

        w(f"  işlem sayısı              {n:>10}")
        w(f"  kazanan                   {wins:>10}  (%{100*wins/n:.0f})")
        w(f"  ort. İDDİA EDİLEN edge    {claimed*100:>+9.2f}p   (beklenen değer)")
        # Gerçekleşen edge 0/1 sonuçlardan geliyor: tek işlem ya +85p ya -15p.
        # Standart hatayı göstermeden bu sayıyı iddia edilenin yanına koymak,
        # gürültüyü sinyal gibi okutur.
        if n > 1:
            import statistics as _st
            per = [(t.payoff_dcents / (t.contracts * DOLLAR_DCENTS))
                   - t.avg_price_dcents / DOLLAR_DCENTS for t in trades]
            se = _st.stdev(per) / math.sqrt(n)
            lo, hi = realized - 1.96 * se, realized + 1.96 * se
            w(f"  ort. GERÇEKLEŞEN edge     {realized*100:>+9.2f}p   "
              f"±{se*100:.1f}p  %95 [{lo*100:+.1f}p, {hi*100:+.1f}p]")
            if lo <= claimed <= hi:
                w("     -> iddia edilen değer bu aralığın İÇİNDE: ikisi tutarlı,")
                w("        aradaki fark bu örneklem büyüklüğünde gürültü.")
            else:
                w("     -> iddia edilen değer aralığın DIŞINDA: model sistematik")
                w("        olarak yanlış kalibre veya hesapta sorun var.")
        else:
            w(f"  ort. GERÇEKLEŞEN edge     {realized*100:>+9.2f}p")
        w(f"  toplam fee                {fees/DOLLAR_DCENTS:>10.2f} $")
        w(f"  PnL fee ÖNCESİ            {pnl_b/DOLLAR_DCENTS:>+10.2f} $")
        w(f"  PnL fee SONRASI           {pnl_a/DOLLAR_DCENTS:>+10.2f} $")

        # --- baseline'lar ---
        w("\n## Baseline karşılaştırması")
        w(f"  (a) hiç işlem yapmamak        {0.0:>+10.2f} $")
        rb = random_baseline(conn, [t.contracts for t in trades])
        if rb:
            w(f"  (b) rastgele işlem (ort.)     {rb['mean']/DOLLAR_DCENTS:>+10.2f} $"
              f"   %90 aralık [{rb['p05']/DOLLAR_DCENTS:+.2f}, "
              f"{rb['p95']/DOLLAR_DCENTS:+.2f}]  ({rb['trials']} deneme)")
        if b_market is not None and b_model is not None:
            w(f"  (c) piyasayı doğru kabul et   Brier {b_market:.4f} "
              f"(model {b_model:.4f})")
        w(f"\n  bizim (fee sonrası)           {pnl_a/DOLLAR_DCENTS:>+10.2f} $")

        if n < 100:
            w(f"\n  !! ÖRNEK ÇOK KÜÇÜK (n={n}). Bu sayılardan sonuç çıkarılamaz.")
            w("     Hava piyasalarında tek bir günün sonucu neredeyse tamamen")
            w("     şanstır; anlamlı bir yargı için haftalarca veri gerekir.")

        if pnl_a <= 0:
            w("\n  -> Fee sonrası kâr yok. İşlem yapmamak daha iyiydi.")
        elif rb and pnl_a <= rb["p95"]:
            w("\n  -> Kâr rastgele işlemin %95 aralığının içinde. Beceriye")
            w("     bağlanamaz; bu kadar örnekle şans ile ayırt edilemez.")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Değerlendirme raporu")
    ap.add_argument("--db", default=str(db.DEFAULT_DB_PATH))
    ap.add_argument("--lead-hours", type=float, default=24.0)
    ap.add_argument("--bins", type=int, default=10)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    conn = db.connect(args.db, read_only=True)
    try:
        # Rapor üretmek, verinin temiz olduğunu iddia etmektir.
        db.assert_no_lookahead(conn)
        text = render(conn, lead_hours=args.lead_hours, bins=args.bins)
    finally:
        conn.close()

    print(text)
    if args.out:
        from pathlib import Path
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
