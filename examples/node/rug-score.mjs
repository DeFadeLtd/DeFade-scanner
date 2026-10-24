#!/usr/bin/env node
// Rug pull probability for one token, waiting until the score is final.
//
//   DEFADE_API_KEY=df_... node rug-score.mjs <token address> [chain]
//
// chain is omitted for Solana, or one of: ethereum base bsc robinhood arc hyperevm
// Node 18+ (built-in fetch), no dependencies.

const API = process.env.DEFADE_API_URL || 'https://api.defade.org/v1';
const key = process.env.DEFADE_API_KEY;
const [token, chain] = process.argv.slice(2);

if (!key || !token) {
  console.error('usage: DEFADE_API_KEY=df_... node rug-score.mjs <token address> [chain]');
  process.exit(1);
}

async function rugScore(address, { chain, wait = 'full' } = {}) {
  const url = new URL(`${API}/rug-score/${address}`);
  url.searchParams.set('wait', wait);
  if (chain) url.searchParams.set('chain', chain);

  const res = await fetch(url, {
    headers: { 'x-api-key': key },
    signal: AbortSignal.timeout(60_000),
  });
  const body = await res.json().catch(() => ({}));

  // 504 module_timeout: the scan is still running on DeFade's side. Not charged.
  if (res.status === 504) return { retryAfterSec: body.retryAfterSec || 10, pending: body.pending };
  if (!res.ok) {
    console.error(`${res.status} ${body.error || res.statusText}`);
    process.exit(1);
  }
  return body;
}

// The first call on a fresh token starts every module; later calls read what has landed.
let result;
for (let attempt = 1; attempt <= 6; attempt++) {
  result = await rugScore(token, { chain });
  if (result.complete && !result.failed) break;
  const waitSec = result.retryAfterSec || 10;
  console.error(`still running: ${(result.pending || []).join(', ') || 'modules'} (retry in ${waitSec}s)`);
  await new Promise(r => setTimeout(r, waitSec * 1000));
}

if (result.rugScore === undefined) {
  console.error('The scan did not finish in time; try again in a minute.');
  process.exit(2);
}

const final = result.complete && !result.failed;
console.log(`${result.verdict}  ${result.rugScore}/100  ${final ? '(final)' : '(provisional)'}`);
for (const s of [...(result.signals || [])].sort((a, b) => b.weight - a.weight).slice(0, 8)) {
  console.log(`  ${s.weight >= 0 ? '+' : ''}${s.weight}  ${s.label}`);
}
