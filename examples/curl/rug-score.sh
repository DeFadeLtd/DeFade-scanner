#!/usr/bin/env sh
# Rug pull probability for one token.
#
#   DEFADE_API_KEY=df_... ./rug-score.sh <token address> [chain]
#
# chain is omitted for Solana, or one of: ethereum base bsc robinhood arc hyperevm
# ?wait=full waits up to 25 s for the modules. If "complete" is false, run it
# again: the scan keeps running on DeFade's side and the next call reads it.
set -eu

: "${DEFADE_API_KEY:?set DEFADE_API_KEY}"
TOKEN="${1:?usage: rug-score.sh <token address> [chain]}"
CHAIN="${2:-}"

URL="https://api.defade.org/v1/rug-score/${TOKEN}?wait=full"
[ -n "$CHAIN" ] && URL="${URL}&chain=${CHAIN}"

curl -sS --max-time 60 -H "x-api-key: ${DEFADE_API_KEY}" "$URL"
echo
