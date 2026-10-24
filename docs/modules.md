# The modules

DeFade runs 32 modules on every scan, on every chain it supports. This page explains what each one shows and how to read it. The [README](../README.md#the-verdict) explains how the findings add up to the verdict.

A free account gets the 7 core modules on every scan, plus the headline figures of Bundle Detection and Token Snipers. Pro unlocks the other 24.

- [Who holds it](#who-holds-it)
- [How it launched](#how-it-launched)
- [Who is behind the wallets](#who-is-behind-the-wallets)
- [What the dev did](#what-the-dev-did)
- [Can you get out](#can-you-get-out)
- [What the market is saying](#what-the-market-is-saying)
- [Reading a scan well](#reading-a-scan-well)

---

## Who holds it

**Holder Distribution.** The top holders and their share of supply. Pools, burn addresses, lockers, exchange wallets and contracts are labelled, so a pool or a locker is never mistaken for a whale. Read the top 5, 10 and 20 together: one large holder is a risk, and twenty mid-sized holders who turn out to be one person are a bigger one.

**Whale Alert.** Which wallets are big enough to move the price on their own, and what share each one controls. Ask what happens if the top one leaves.

**Bubble Map.** The holder base as a picture: one bubble per wallet, sized by holding, with lines where wallets are connected. Scattered, unconnected bubbles are a real crowd. A tight web of linked bubbles holding most of the supply is one group.

**Holder Overlap.** What else this token's top holders hold, for up to three tokens at once. A heavy overlap with one other token often means the same group is running both.

**Wallet Overlap.** Enter two or three tokens and see the wallets their top holders have in common. A handful of wallets sitting on top of every token you entered is the same-operator signal.

**Notable Holders.** Known traders and influencer wallets among the holders, from a curated wallet list.

## How it launched

**Bundle Detection.** Coordinated buying at launch: wallets that bought in the same block or slot, from shared funders, or in identical amounts. DeFade reads the launch window (180 seconds on Solana, 300 seconds on the EVM chains) and then sweeps the first 24 hours for groups that bought later.

- **Bundled at launch** is the share of supply the groups took. Every other card that mentions bundling repeats this one figure. When the groups' buys add up to more than the whole supply, the figure is the most they held at one time, so no card ever reads "100% bundled".
- **Bundled now** (or **Still held**) is what the groups hold today.
- **Transferred, unsold** is what the groups sent to other wallets, less what those wallets have since sold, still hold, or sent back. It never exceeds the supply or the bundled figure.
- When a meaningful part of the bundled supply was bought after the launch window, the label says so.

**Historical Bundles.** The same reading over the token's later life, for groups that formed after launch.

**Sniper Bot Detection.** Wallets that bought in the first 120 seconds, split into instant (10 seconds or less) and fast (30 seconds or less), and what they still hold. The risk level depends on the share the snipers still control, counting what they hold, moved and rotated.

**Fee Fingerprint.** Wallets that paid an identical, unusual fee setting (on Solana the compute-unit price or Jito tip, on EVM the priority fee or gas price), which usually means one bot configuration. It links wallets; it never counts as bundled supply on its own.

## Who is behind the wallets

**Fresh Wallet Detection.** How old each top holder's wallet was when the token launched, from under a day to 45 days, and whether it is holding, sold, or passed its tokens on. The **virgin check** goes further: an older wallet whose first token trade ever is this one is flagged too, whatever its age.

**Funding Origin.** The top 100 holders traced back, over several hops, to where their money came from: exchanges grouped by KYC tier, swap services, bridges and mixers. The card names the pattern, from broad retail funding to majority no-KYC or mixer-linked funding, and says when too few holders could be traced to be sure.

**Sybil Bands.** Holders funded from the same private wallet are collapsed into one band, with the supply that band controls. **Operator memory** recognises a funder that seeded bands on earlier launches, even after the wallets have been rotated.

**Holder Network.** The insider map: transfers and shared funders between the top holders, drawn as a graph. Dense clusters are the finding, above all one wired back to the deployer. If the walk ran out of budget before reaching every holder, the card says so: a partial scan with no links is not a clean token.

**Cross-Funding Graph.** Whether the top holders funded each other before the launch.

**Copy Trading Detection.** Wallets mirroring each other's trades on this token. That can be a crowd following one good wallet, or one operator running many; the funding and clustering modules tell which.

**Wallet Intelligence.** The holders flagged by two or more independent modules, for example a fresh wallet that is also in a bundle and an insider band. Agreement between modules weighs more than any single signal.

## What the dev did

**Dev Wallet Tracking.** What the creator did with their supply: still holding, sold, or moved to other wallets. Creating the pool or locking tokens is not counted as moving them.

**Deployer Reputation.** Every token the deployer launched, how many survived, and its rug history.

**Wallet Profiler.** Any holder's trades, win rate, PnL and history, one click from the holder list.

**Token Lifecycle.** What has happened to the token since it was created, on a timeline. Age is context for everything else: a concentrated holder base on a two-year-old token is normal, and the same picture two hours after launch is not.

## Can you get out

**LP and Liquidity.** Pool depth, and whether the liquidity is burned, locked or free to pull, including position-based v3 and v4 pools.

**Exit Liquidity Calculator.** The price impact of selling $100 up to $100,000 into the pool, rated from safe to severe, and the largest sell that stays reasonable.

**Dump impact.** What happens if the largest operator (a bundle group, a sybil band or a known bundler fleet) sold its whole position into the pool: how far the price would fall and how much they would take out.

**Contract Safety** (EVM). Owner, mint and tax controls that are still live on the contract. On Solana, mint and freeze authority are part of the base scan.

## What the market is saying

**Smart Money Tracker** and **Smart Money Signals.** Profitable wallets among the holders, and what they are doing.

**Social links.** The token's website and social accounts, as published.

**Social Sentiment timeline** and **X Community.** How the conversation around the token has moved.

**AI summary.** A short written summary of the scan's findings.

---

## Reading a scan well

- **Read the findings, not just the number.** The score sums what is present today; the findings under it say what that is.
- **Check the status line.** `PROVISIONAL` names the modules still running. Wait for `FINAL SCORE` before treating the number as settled.
- **Look for agreement.** One signal can have an innocent reason. The same wallets turning up in bundles, fresh wallets and a sybil band rarely do.
- **Trust the gaps.** When a module couldn't read something, the card says so. DeFade does not fill a gap with a guess, so a missing figure is a missing figure, not a clean one.
