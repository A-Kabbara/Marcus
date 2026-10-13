# Markus KPI Benchmarks & Diagnosis Tree

His exact thresholds. Mental model: 12 sliders on a mixer — you don't need 100s across the board, **~75 average = profitable**. Metrics never exist in a vacuum. Ask one question: **"Where is the breakdown occurring?"** — ad side or funnel side.

## Soft metrics (ad side)

| Metric | KPI | Notes |
|---|---|---|
| Link CPC | **≤ $1.50 US** (≤$1.00 worldwide) | The ads-side "check engine light." Cost per LINK click, not per click. |
| Link CTR | **≥ 3%** (ideally ~4%) | 2% floor in some videos; 3% is his standard bar. |
| CPM | **$30-50 US healthy** | $80+ elevated; $100-150 = Facebook hates the ad (aggressive claims, before/afters, all-caps) or infrastructure issues. Cheap geos (e.g. €11-15 Italy) excuse a lower CTR if CPC holds. |
| Hook rate | **≥ 50%** | Custom metric: 3-second video plays ÷ impressions. "If hook rate is under 50%, I don't even want to talk about anything else." |
| Hold rate | **≥ 25%** | To 50% video view. Ignore for long VSLs. Only check when diagnosing one creative. |
| Frequency | **< 1.5 cold** | ~2 on cold = creative is self-retargeting. |

Out of KPI → **it's a creative problem 99% of the time** (occasionally audience). CTR-all should run 2-3x CTR-link; a huge gap = interested-but-not-committed → raise intent in the creative.

## Hard metrics (funnel side)

| Metric | KPI | Notes |
|---|---|---|
| CVR | **≥ 3%** minimum | The funnel's check engine light. 5% for $20-30 products, 4% mid-range, 3% at $90-100+. Advertorial/listicle funnels can run lower. |
| View content → ATC | **≥ 10%** | 8-9% ok for expensive products. Below = ad messaging or lander problem. |
| ATC → purchase | **≥ 30%** | Drop-off ATC→IC = cart page; IC→purchase = checkout. **QC your own checkout — buy from your own funnel before any cold traffic** (processor restrictions cause "300 initiate checkouts, nobody buying"). |
| AOV : front-end price | **≥ 2:1 minimum, 3-5x achievable** | 1:1 = "the 2018 bullshit ass way of running e-com." |
| LTV : AOV | **≥ 3:1** | Retention/email/SMS health. |
| LTV : CAC | **≥ 3:1** (7-10:1 high ticket) | |
| CAC | **< 50% of AOV** | ≈ 2x ROAS floor, margin-dependent. |

## Diagnostic combos

- **High CPM + high CPC + low CTR** → brutally competitive market AND weak creative.
- **CTR 6%+ but ATC ~3%** → "curiosity clickers" — baity ad pulling junk traffic; kills the pixel too.
- **Good CVR + bad AOV** → unit-economics problem; top brands win on economics, not ads.
- **All metrics in KPI** → "All you have to do now is run more ads. It's that simple."
- Bad front-end traffic trains the pixel badly and masquerades as a funnel problem — check the ad first.

## Other thresholds he uses

- Product validation: competitor **≥$300k/month** (SimilarWeb ≥300k visits/mo; revenue ≈ visits × 2% × AOV)
- Margins: **≥3x COGS AND ≥$20-30 gross margin**; test for ≥20% net margin
- Viral ad signal: **≥10,000 likes + ≥5,000 shares (2:1)**
- Quiz completion: **≥30%** (25% ok at scale); per-question drop-off spike ≥4% = rewrite
- Dry test opt-in: **≥10%** = pursue (8-9% for $100+ products); 4-5% = pass
- Creative volume: **20-50 net-new concepts/week** at scale (≥25/week minimum per his $10M-year lessons); 10-20/week when starting
- Test budget: CBO **never below $50/day**, **$10/day per ad minimum**; beginner: daily budget = product price, judge at 3 days
- Kill thresholds while testing: CPM ≥~$50, CPC >$2-3, CTR <1% = "your ads suck"
- Hook pre-validation: 10 text-only ads, kill each at 1,000 impressions, $50-100 total
- Break-even math: $50 price, $10 COGS → $40 break-even CAC; AOV $100 → break-even CAC ~$70
- Attribution: never trust in-platform CPA post-iOS14 (5-50% mis-attribution) — Triple Whale / Hyros; "when in doubt, zoom out" (7-day windows)
- Backend: email/SMS = +15-30% revenue; abandoned cart ≈ +15%/day; retargeting only after $500-1,000/day spend; average buyer needs 6-7 impressions
