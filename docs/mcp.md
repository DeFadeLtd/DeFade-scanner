# DeFade over MCP

DeFade speaks the [Model Context Protocol](https://modelcontextprotocol.io), so an AI assistant can run real DeFade scans inside a conversation instead of describing DeFade from memory.

```
https://api.defade.org/mcp
```

It is a remote server over streamable HTTP. Add it as a custom connector in any assistant or MCP client that supports one.

## Keys

Send a key in the `x-api-key` header. A client that can't set headers can append `?api_key=YOUR_KEY` to the URL instead. Two kinds of key work:

- **A DeFade API key** (`df_…`). Every tool call is metered against the key's plan exactly like a REST call: same endpoints, chains, units and rate limits. See [api.md](api.md).
- **The connector key included with DeFade Pro.** Issue it from your [dashboard](https://defade.org/dashboard). It spends your plan's monthly scan allowance.

Connecting and listing the tools work without a key. The scan tools answer with instructions to get one until you supply it.

## Tools

15 read-only tools: one per module, plus a usage check. None of them can move funds or change anything.

| Tool | What it returns |
|---|---|
| `get_rug_score` | The rug pull probability (higher is worse), the verdict and the signals behind it |
| `get_token_scan` | The full scan. On Solana it carries a **safety** score (higher is better) |
| `get_holders` | Holder distribution |
| `get_whales` | Whale wallets |
| `get_liquidity` | Pool depth, locks and burns |
| `get_launch_bundles` | Bundle Detection |
| `get_launch_snipers` | Snipers |
| `get_wallet_links` | Proven links between wallets: who funded whom, who transferred to whom, coordinated timing |
| `get_lookalike_clusters` | Wallets that behave as one actor, with buys sized and timed alike, even when no funding link connects them |
| `get_funding_sources` | Where the holders' funds came from |
| `get_fee_fingerprint` | Wallets sharing one bot's fee settings |
| `get_dev_tracker` | What the developer did with their supply |
| `get_smart_money` | Smart money among the holders |
| `get_token_price` | Price and candles |
| `get_usage` | What the key has used and has left |

> [!IMPORTANT]
> `get_rug_score` and `get_token_scan` point in opposite directions on Solana. Every result says which kind of score it carries in its first line, and an assistant should repeat that. On an EVM chain the scan carries no score; ask for `get_rug_score`.

Results are trimmed to fit an assistant's context and say when they were. The full payload is always available from the [REST API](api.md).

## Try it

Once the connector is added, ask in plain words:

- "Is `<token address>` on Base a rug? Show me the bundles and the dev wallet."
- "Who funded the top holders of `<mint>`?"
- "Compare the snipers on these two tokens."
