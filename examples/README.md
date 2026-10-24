# Examples

Small, dependency-free clients for the [DeFade API](../docs/api.md). Each one asks for a token's rug pull probability, waits until the score is final, and prints the verdict with the signals that weigh most.

You need an API key: a free 7-day trial key or a paid key from [defade.org/developers](https://defade.org/developers).

```bash
export DEFADE_API_KEY=df_...

# Node.js 18+
node node/rug-score.mjs <solana-mint>
node node/rug-score.mjs 0x... base

# Python 3.8+
python3 python/rug_score.py <solana-mint>

# curl (prints the raw JSON)
sh curl/rug-score.sh <solana-mint>
```

Example output:

```
HIGH RISK  72/100  (final)
  +18  Dev moved 20% of supply to a fresh wallet
  ...
```

A call costs 1 unit on Solana and 5 on an EVM chain. A retry that answers `504 module_timeout` while the scan is still running is not charged.

For a fuller client, use the official Node.js package: `npm install defade`.

The code in this folder is MIT licensed ([LICENSE](LICENSE)).
