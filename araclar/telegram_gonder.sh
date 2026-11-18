#!/usr/bin/env bash
# Kullanım: telegram_gonder.sh "mesaj"
# TELEGRAM_BOT_TOKEN ortam değişkeninden, sohbet kimliği TELEGRAM_CHAT_ID'den (yoksa notlar/.telegram_chat_id) okunur.
set -euo pipefail
cd "$(dirname "$0")/.."
CHAT_ID="${TELEGRAM_CHAT_ID:-$(cat notlar/.telegram_chat_id 2>/dev/null || true)}"
[ -n "${TELEGRAM_BOT_TOKEN:-}" ] || { echo "TELEGRAM_BOT_TOKEN yok" >&2; exit 1; }
[ -n "$CHAT_ID" ] || { echo "Sohbet kimliği yok" >&2; exit 1; }
curl -sS -m 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  --data-urlencode "chat_id=${CHAT_ID}" --data-urlencode "text=$1" \
  -d disable_web_page_preview=true | grep -q '"ok":true' && echo "gönderildi"
