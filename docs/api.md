# The DeFade API

The same analysis that powers [defade.org](https://defade.org), over REST. This page gets you started; the full reference, with every field of every response, is at [defade.org/api-docs](https://defade.org/api-docs).

## Base URL and key

```
https://api.defade.org/v1
```

Send your key in the `x-api-key` header on every call, or as an `api_key` query parameter when you can't set headers.

```bash
curl -H "x-api-key: $DEFADE_API_KEY" \
  "https://api.defade.org/v1/rug-score/<solana-mint>"
```

**Getting a key.**

- **Paid plans** are self-serve on [defade.org/developers](https://defade.org/developers). Pay by card or in crypto, and the key arrives the moment payment clears.
- **Free 7-day trial keys** are issued on request from the same page. They reach six endpoints (`analyze`, `rug-score`, `token-price`, `holders`, `kol`, `trending`) plus `usage`, on every chain, at 10 requests a minute, 100 a day and 3,000 units a month.

## Chains

Every endpoint defaults to Solana. Add `?chain=` to run it on an EVM chain:

| `?chain=` | Chain |
|---|---|
| *(none)* | Solana |
| `ethereum` | Ethereum |
| `base` | Base |
| `bsc` | BSC |
| `robinhood` | Robinhood Chain |
| `arc` | Arc |
| `hyperevm` | Hyperliquid (HyperEVM) |

```bash
curl -H "x-api-key: $DEFADE_API_KEY" \
  "https://api.defade.org/v1/rug-score/0x...?chain=base"
```

Two endpoints are exceptions: `/v1/bundles` is Solana-only (its EVM counterpart is `/v1/bundles-pro`), and `/v1/usage` reports on your key, so it takes no chain.

## Units and plans

Every paid plan reaches all 27 endpoints on every chain. Plans differ in their monthly allowance, which is counted in units, and in rate limits.

- A call costs **1 unit**.
- Five calls cost **5 units on an EVM chain**, because they read far more: `rug-score`, `funding-origin`, `funding-graph`, `sybil-cluster` and `fresh-wallets`.
- The errors marked below as not charged cost nothing.

| Plan | Units a month |
|---|---|
| Lite | 650 |
| Starter | 5,000 |
| Growth | 10,000 |
| Pro | 20,000 |
| Enterprise | 100,000 |

Prices and rate limits are on [defade.org/api-docs#pricing](https://defade.org/api-docs#pricing). Past your allowance, buy overage credits from the dashboard rather than upgrading.

## Endpoints

`:mint` is a token address: a Solana mint, or a `0x` address together with `?chain=`.

| Endpoint | What it returns |
|---|---|
| `GET /v1/analyze/:mint` | The full token scan |
| `GET /v1/rug-score/:mint` | The rug pull probability, its verdict and every signal behind it |
| `GET /v1/token-price/:mint` | Price and OHLCV candles |
| `GET /v1/holders/:mint` | Holder distribution |
| `GET /v1/whales/:mint` | Whale wallets |
| `GET /v1/liquidity/:mint` | Pool depth, locks and burns |
| `GET /v1/bundles-pro/:mint` | Bundle Detection |
| `GET /v1/bundles/:mint` | Legacy bundle detection (Solana) |
| `GET /v1/historical-bundles/:mint` | Bundles formed after launch |
| `GET /v1/snipers/:mint` | Sniper detection |
| `GET /v1/fee-fingerprint/:mint` | Wallets sharing one bot's fee settings |
| `GET /v1/fresh-wallets/:mint` | Supply held by newly created wallets |
| `GET /v1/funding-origin/:mint` | Where the top holders' funds came from, by KYC tier |
| `GET /v1/funding-graph/:mint` | The cross-funding graph |
| `GET /v1/sybil-cluster/:mint` | Sybil bands of holders with a shared funder |
| `GET /v1/insider-network/:mint` | The insider wallet map |
| `GET /v1/copy-traders/:mint` | Copy-trading detection |
| `GET /v1/dev-tracker/:mint` | The developer wallet's history |
| `GET /v1/deployer-reputation/:mint` | The deployer's launch record |
| `GET /v1/smart-money/:mint` | Smart money signals |
| `GET /v1/kol/:mint` | Notable holders |
| `GET /v1/socials/:mint` | Social links and metadata |
| `GET /v1/holder-overlap` | Holder overlap across tokens |
| `GET /v1/wallet-overlap` | Wallets holding several tokens |
| `GET /v1/wallet-reputation/:wallet` | A wallet's cross-token rug history |
| `GET /v1/trending` | Trending tokens |
| `GET /v1/usage` | Your usage and credit balance |

## The rug score, done right

Call `/v1/rug-score` first. It starts every module scan for the token, so the per-module calls you make after it answer from cache.

It answers within a time budget, 5 seconds by default. Modules that haven't finished by then are named in `pending` and keep running on our side, so a second call, or one with `?wait=full`, returns the complete score.

```json
{
  "rugScore": 72,
  "verdict": "HIGH RISK",
  "signals": [
    { "weight": 18, "label": "Dev moved 20% of supply to a fresh wallet", "severity": "warning" }
  ],
  "coverage": "partial",
  "pending": ["snipers"],
  "complete": false
}
```

- Treat the score as final when `complete` is `true` and there is no `failed` array.
- `?wait=` takes a number of seconds (0 to 25) or `full`.
- Give the HTTP call a 60-second timeout.
- A `504` with `module_timeout` is not charged: retry after `retryAfterSec`.

| `rugScore` | `verdict` |
|---|---|
| 0–24 | `PROBABLY SAFE` |
| 25–44 | `SOME RISK` |
| 45–59 | `ELEVATED RISK` |
| 60–74 | `HIGH RISK` |
| 75–100 | `EXTREME RISK` |

`verdict` can also be a state that replaces the band: `RUGGED / DEAD`, `ABANDONED / DEAD`, or `NEVER BONDED` (Solana).

> [!IMPORTANT]
> **Two scores point in opposite directions.** `rugScore` is a rug probability: higher is worse. On Solana, `/v1/analyze` also returns `risk.score`, which is a *safety* score: higher is better. Never show one as the other.

Working clients are in [`examples/`](../examples).

## Errors

| Status | Meaning |
|---|---|
| `400` | A bad address, for example a wallet sent where a token was expected. Not charged. |
| `403` | Your plan doesn't include this endpoint. |
| `429` | Past your rate, daily or monthly limit. The body says which. |
| `502` | An upstream source didn't answer. Not charged. |
| `504` | `module_timeout`: the scan is still running. Not charged; retry after `retryAfterSec`. |

## Also available

- **A Node.js client:** `npm install defade` ([defade-sdk](https://github.com/DeFadeLtd/defade-sdk)).
- **An MCP connector** for AI assistants, on the same keys: see [mcp.md](mcp.md).
