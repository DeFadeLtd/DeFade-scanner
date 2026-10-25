# The Telegram bot

[@DeFadeAnalyzerBot](https://t.me/DeFadeAnalyzerBot) runs DeFade scans in Telegram and tells you when hands it has seen before launch again.

## Commands

| Command | What it does |
|---|---|
| `/scan <address>` | A full risk analysis of any token, on any chain DeFade supports. Pasting an address works too |
| `/radar on` · `/radar off` | Start or stop Crew Radar alerts (Pro, below) |
| `/top <address>` | Follow a token and get a message as it nears its crew's usual top (Pro). On an EVM chain, add the chain if the bot can't find it: `/top 0x… base` |
| `/top` | The tokens you follow |
| `/untop <address>` | Stop following a token |
| `/trending` | Trending Solana tokens |
| `/connect` | Link your DeFade Pro account |
| `/stats` | The group's scan stats and leaderboard |
| `/help` | How to use the bot |

A scan comes back as one message: a card image, then the token, its verdict, chain and address, and each section of the report under its own title. Its buttons open each module (bundles, snipers, whales, insiders and more) and the full report on defade.org.

## Free and Pro

- **Free:** 3 scans a day in the [DeFade community](https://t.me/DeFadeChat).
- **Pro:** scans in a private chat with the bot, the Pro modules on every card, and Crew Radar.

To link Pro, send `/connect`, then paste the 6-digit code from your dashboard as a reply.

## Crew Radar

Crew Radar sends you an alert when hands DeFade has seen before launch a new token: a creator or its funder with rugs on record, an operator band, or a creator whose earlier launches reached a market. It listens to:

| Chain | Launchpads |
|---|---|
| **Solana** | pump.fun, bonk.fun and the other Raydium LaunchLab launchpads, Meteora's bonding curve (Jupiter Studio and others), boop.fun |
| **BSC, Base, Ethereum, Robinhood, Arc** | four.meme, flap.sh, Clanker, Zora and the Pons launchpads |

Each alert says why the launch was flagged and carries the crew's usual play from [Exit Playbook](modules.md#what-the-dev-did): where their earlier launches usually peaked, when, and how far they fell after. Its buttons scan the token in the bot, open it on DeFade, copy the whole address, or stop the alerts.

The bot then follows the launch for a day and messages you once as the market cap reaches 80% of the crew's usual peak, and once as the token reaches the age their launches usually peaked at. `/top` follows any other token the same way, up to 25 at a time.

A subscriber gets at most 40 launch alerts a day, and one per crew every three hours. When the daily limit is reached the bot says so, and when alerts resume; the tokens you follow keep messaging you.

## Watchlist

Watchlist alerts (`/watch`, `/watchlist`, `/unwatch`) are paused for now. Scan any token with `/scan` in the meantime.
