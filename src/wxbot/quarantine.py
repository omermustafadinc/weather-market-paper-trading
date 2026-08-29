"""Kirlenmiş türetilmiş kayıtları iptal et — silmeden.

Bir kural değiştiğinde (ya da bir hata bulunduğunda) eski kuralla üretilmiş
karar/fill kayıtlarını devre dışı bırakmak gerekir. Bu araç bunu **hiçbir şey
silmeden** yapar: dosyaya bir iptal kaydı ekler, ingest eşleşenleri atlar.

Neden silmiyoruz:
  * "Ham veri append-only, asla üzerine yazma" şartı.
  * Eşzamanlı bir CI koşusu aynı dosyaya eklerken git çakışması doğuyor —
    teorik değil, bir kez başımıza geldi.

Gözlem kayıtları (piyasa, tahmin, çözümleme) hiçbir koşulda iptal edilemez;
onlar kanıt. Yalnızca kendi ürettiğimiz karar ve fill kayıtları iptal edilebilir,
ve onlar zaten gözlemlerden yeniden üretilebilir.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import rawstore
from .clock import now_us


def find_contaminated(root: Path | None = None) -> tuple[list[list], list[list], list[str]]:
    """Hedef günü karar gününe eşit veya ondan önce olan kararları bul.

    Bu kural `db._CHECKS` içindeki `decision_on_past_or_today` ile aynı; burada
    hangi kayıtların iptal edileceğini belirlemek için kullanılıyor.
    """
    already = rawstore.invalidated_keys(root)
    dec_keys: list[list] = []
    reasons: list[str] = []

    for rec in rawstore.read_all("decision", root):
        key = (rec["venue"], rec["market_ticker"], rec["slot_id"])
        if key in already["decision"]:
            continue
        if rec["target_date"] <= rec["decision_at_iso"][:10]:
            dec_keys.append(list(key))

    bad = {tuple(k) for k in dec_keys}
    fill_keys = [list(k) for k in
                 {(r["venue"], r["market_ticker"], r["slot_id"])
                  for r in rawstore.read_all("fill", root)
                  if (r["venue"], r["market_ticker"], r["slot_id"]) in bad
                  and (r["venue"], r["market_ticker"], r["slot_id"])
                  not in already["fill"]}]
    return dec_keys, fill_keys, reasons


DEFAULT_REASON = (
    "Hedef günü karar gününe eşit veya ondan önce olan karar. Geçmiş/bugün "
    "hedefli kararlar iki nedenle geçersiz: (a) çözümleme (NWS CLI) karardan "
    "önce yayınlanmış olabilir — bir kez oldu, tarayıcı yakaladı; (b) geçmiş "
    "hedef günler için Open-Meteo tahmin değil analiz döndürüyor, model o "
    "kovalarda yapay olarak iyi görünür. Ajan artık yalnızca gelecek hedef "
    "günlerde karar veriyor."
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Kirlenmiş karar/fill kayıtlarını iptal et")
    ap.add_argument("--root", default=None)
    ap.add_argument("--reason", default=DEFAULT_REASON)
    ap.add_argument("--run-uid", default="quarantine-manual")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.root) if args.root else None
    dec_keys, fill_keys, _ = find_contaminated(root)

    if not dec_keys and not fill_keys:
        print("iptal edilecek kayıt yok")
        return 0

    print(f"iptal edilecek: {len(dec_keys)} karar, {len(fill_keys)} fill")
    for k in dec_keys[:5]:
        print(f"  {k[1]} (slot {k[2]})")
    if len(dec_keys) > 5:
        print(f"  ... ve {len(dec_keys) - 5} tane daha")

    if args.dry_run:
        print("(dry-run: yazılmadı)")
        return 0

    at = now_us()
    for kind, keys in (("decision", dec_keys), ("fill", fill_keys)):
        if keys:
            rawstore.append("invalidation", rawstore.invalidation_record(
                run_uid=args.run_uid, target_kind=kind, keys=keys,
                reason=args.reason, at_us=at), root)
    print("iptal kaydı yazıldı — hiçbir ham kayıt silinmedi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
