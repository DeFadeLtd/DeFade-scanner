#!/usr/bin/env python3
"""Rug pull probability for one token, waiting until the score is final.

    DEFADE_API_KEY=df_... python3 rug_score.py <token address> [chain]

chain is omitted for Solana, or one of: ethereum base bsc robinhood arc hyperevm
Python 3.8+, standard library only.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("DEFADE_API_URL", "https://api.defade.org/v1")


def rug_score(address, key, chain=None, wait="full"):
    query = {"wait": wait}
    if chain:
        query["chain"] = chain
    url = f"{API}/rug-score/{address}?{urllib.parse.urlencode(query)}"
    req = urllib.request.Request(url, headers={"x-api-key": key})
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            return json.load(res)
    except urllib.error.HTTPError as err:
        body = json.loads(err.read() or b"{}")
        # 504 module_timeout: the scan is still running on DeFade's side. Not charged.
        if err.code == 504:
            return {"retryAfterSec": body.get("retryAfterSec", 10), "pending": body.get("pending")}
        raise SystemExit(f"{err.code} {body.get('error', err.reason)}")


def main():
    key = os.environ.get("DEFADE_API_KEY")
    if not key or len(sys.argv) < 2:
        raise SystemExit("usage: DEFADE_API_KEY=df_... python3 rug_score.py <token address> [chain]")
    token = sys.argv[1]
    chain = sys.argv[2] if len(sys.argv) > 2 else None

    # The first call on a fresh token starts every module; later calls read what has landed.
    result = {}
    for _ in range(6):
        result = rug_score(token, key, chain)
        if result.get("complete") and not result.get("failed"):
            break
        wait = result.get("retryAfterSec") or 10
        pending = ", ".join(result.get("pending") or []) or "modules"
        print(f"still running: {pending} (retry in {wait}s)", file=sys.stderr)
        time.sleep(wait)

    if "rugScore" not in result:
        raise SystemExit("The scan did not finish in time; try again in a minute.")

    final = result.get("complete") and not result.get("failed")
    print(f"{result['verdict']}  {result['rugScore']}/100  {'(final)' if final else '(provisional)'}")
    for s in sorted(result.get("signals") or [], key=lambda s: -s["weight"])[:8]:
        print(f"  {'+' if s['weight'] >= 0 else ''}{s['weight']}  {s['label']}")


if __name__ == "__main__":
    main()
