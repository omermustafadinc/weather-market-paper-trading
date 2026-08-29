#!/usr/bin/env bash
# Ham veriyi commit'le ve push et.
#
# Her döngüden sonra çağrılıyor: koşu yarıda kesilirse önceki döngülerin
# verisi kaybolmasın. Ham veri append-only olduğu için rebase güvenli.
set -u

if [ -z "$(git status --porcelain data/raw)" ]; then
  echo "  commit: değişiklik yok"
  exit 0
fi

git add data/raw
git commit -q -m "veri: $(date -u '+%Y-%m-%dT%H:%MZ') toplama"

for i in 1 2 3 4 5; do
  if git pull --rebase --autostash -q origin main && git push -q origin main; then
    echo "  commit: push tamam"
    exit 0
  fi
  echo "  commit: push denemesi $i başarısız"
  sleep $((i * 3))
done
echo "  commit: push başarısız" >&2
exit 1
