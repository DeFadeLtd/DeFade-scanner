# The Telegram bot

[@DeFadeAnalyzerBot](https://t.me/DeFadeAnalyzerBot) runs DeFade scans in Telegram and watches tokens for you.

## Commands

| Command | What it does |
|---|---|
| `/scan <address>` | A full risk analysis of any token, on any chain DeFade supports. Pasting an address works too |
| `/trending` | Trending Solana tokens |
| `/watch <address>` | Watch a token and get alerts (below) |
| `/watchlist` | The tokens you are watching |
| `/unwatch <address>` | Stop watching a token |
| `/connect` | Link your DeFade Pro account |
| `/stats` | The group's scan stats and leaderboard |
| `/help` | How to use the bot |

A scan comes back as a card with the score, the verdict and the main findings. Its buttons open each module (bundles, snipers, whales, insiders and more) and the full report on defade.org.

## Free and Pro

- **Free:** 3 scans a day in the [DeFade community](https://t.me/DeFadeChat).
- **Pro:** scans in a private chat with the bot, the Pro modules on every card, and the watchlist.

To link Pro, send `/connect`, then paste the 6-digit code from your dashboard as a reply.

## Watchlist alerts

Watch up to 10 Solana tokens, each for 7 days. Every watched token is checked every 20 minutes, and you get a message when:

| Alert | When it fires |
|---|---|
| **Liquidity pulled** | The pool falls to a fifth of its last reading, or under $1k |
| **Price collapse** | The price falls 70% or more between two checks |
| **Dev moved** | The dev wallet's balance drops by 30% or more |
| **Whale dump** | A top-20 holder with at least 1% of supply sells half their position |

Each alert fires once per token, so a slow bleed doesn't flood your chat.
