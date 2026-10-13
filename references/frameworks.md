# Markus Framework Library

His complete operating systems, with exact numbers, tools, and steps. Video numbers reference the transcript library.

---

## 1. Product Research & Validation

**Product criteria (all must hold):**
- Solves a PAINFUL problem in a PASSIONATE market (lowest tiers of Maslow; hard outcomes: "more money, more sex, or lose weight"; pets: "the only thing people love more than themselves is their family and their pets")
- Margins: **price ≥ 3x landed COGS** AND **≥$20-30 absolute gross margin** (he raised $20→$30 over time as ad costs rose)
- Fits roughly in a shoebox (logistics)
- Evergreen, sells 365 days (no fidget spinners)
- Upsell/subscription potential designed in from day one ("start with the end in mind"; "a good product solves a problem and creates a new one — the upsell solves the new problem")
- Markets to enter: pain relief, gut health, supplements/nootropics, beauty (acne, hair loss/growth), pets. Avoid: apparel, gadget-class, jewelry.

**Validation (non-negotiable):** a competitor provably doing **≥$300k/month**. Proxy: SimilarWeb ≥300,000 visits/month. Math: `revenue ≈ visits × 2% CVR (conservative; 1.5-3.5% range) × AOV`. Example: 300,000 × 2% × $60 = $360k/mo. Never trust spy-tool revenue estimates (big brands checkout on Funnelish/Checkout Champ, invisible to Shopify trackers).

**Research methods (pick one):**
- **Native ads method**: incognito → weather.com / Fox News / CNN → "Paid Content" section (Taboola/Outbrain). Native = coldest, cheapest traffic ($3-10 CPM), so anything scaling there is a proven offer. Click through the advertorial, SimilarWeb the domain.
- **YouTube burner method** (068): fresh Google account → open dozens of niche videos muted-in-tab (not in player) → train the algorithm ~week → harvest in-stream ads from mid-size brands ($10-50M/yr). "Established brands start on Facebook, then move capital to YouTube" = pre-validated.
- **Facebook burner method** (095, 100): fresh account, follow/like/save top niche brand posts for ~1 week → hunt ads with **≥10,000 likes AND ≥5,000 shares** (2:1 — likes can be bought, shares can't).
- **GetHooked filters** (his SaaS; free alt = Meta Ad Library): 4-5 stars, still running, ≥7 days runtime, English, brand has **≥30 active ads** (ideally 100+; "you're not doing shit with 10 ads in your library"). Green flag: creative production scaling month over month.
- **AI-driven**: ChatGPT Deep Research with his product-research prompt (criteria baked in), or Claude + GetHooked MCP connector (003), or Claude Cowork project with his Product Finder SOP (009).
- **Problem research, not product research** (056, 077): find the scaling brand → identify the PROBLEM (neuropathy, not the shoe) → join ~10 Facebook support groups for that problem → read what sufferers buy and their exact pain language → sell into that.
- Triple-check (100): Keywords Everywhere ≥30,000 monthly searches; Google Trends 5-year view rising steadily (not spiking); SimilarWeb ≥300-400k.

## 2. Differentiation: Angles, Purple Ocean, Competitive Advantages

- **"Product saturation doesn't exist; angle saturation does."** Same product + untapped angle = new winner. Angle mining: export ~100 Amazon reviews of the equivalent product (review-export extension) → ChatGPT: "break down the real reasons people buy" → each reason = a sellable angle. Examples: barefoot shoes weight-loss → neuropathy angle; selfie stick 18-30 → 40-65 "take it on vacation"; Blissy pillowcase → overnight-acne prevention.
- **Purple Ocean Strategy**: enter a proven red-ocean market and carve a hyper-specific sub-market you own 100% (Primal Queen: organ supplements → postpartum/perimenopausal women; HIMS/HERS gender-split GLP-1).
- **Competitive advantage menu** (pick exactly ONE to out-compete a validated competitor on): budget ($100k+ spam-testing) · pixel/data history · backend economics (LTV/subscriptions — friend runs 0.7 front-end ROAS profitably at $100k/day spend) · front-end economics (AOV+CVR) · creatives (they test 2-3/week, you test 10-30+) · angles (free) · traffic source (they're FB-only → you take TikTok/YouTube/Google) · geography (translate winning US funnel to DE/NL) · time (broke: TikTok organic 4+ posts/day) · AI & automation · obsession.
- **Formula: validated product + unsaturated angle + Chad funnel.**

## 3. Foundational Docs SOP (research before ANY copy)

Four AI-generated documents, loaded into a Claude Project before any generation ("60-80% of copy time is research"):
1. **Research doc** — 20-60 pages of VOC via ChatGPT/Gemini Deep Research (use "AI inception": have ChatGPT write the deep-research prompt itself; require minimum 6 pages). Gemini 2.5 Pro DR beat Perplexity 226 sources/36pp vs ~55/7pp in his split test.
2. **Avatar sheet** — demographics, pains, goals, emotional drivers, verbatim customer quote bank.
3. **Offer brief** — product, price, funnel, upsells, objections, level of awareness, stage of sophistication, big idea, unique mechanism.
4. **Necessary beliefs doc** — max 6 "I believe that..." statements the prospect must hold before buying ("marketing at its core is a game of belief change work").
Setup: full-page-screenshot competitor sales page → PDF → 3-prompt chain (see his Foundational Docs SOP doc). Then upload all 4 to a Claude Project; afterwards prompt simply "like it's an employee."
Best research of all: **call your actual customers** — "What almost kept you from buying?" (never Facebook comments — survivorship bias + "where the biggest losers on the planet hang out"). Advanced: build an AI customer-avatar bot from the docs and interview it on walks.

## 4. The Chad Funnel (funnel scaling)

**Ad → pre-sell page (advertorial / listicle / quiz / VSL page) → sales page → order page → OTO1 → downsell popup (same product 50% off) → OTO2 → downsell → thank you.**
vs the "basic bitch funnel": ad → Shopify PDP → cart → checkout.

- Built on **Funnelish** (start) or **Checkout Champ** (volume) — NOT Shopify (post-purchase flow not customizable without Plus). Shopify still hosts orders. Cold traffic (~70-80%) → full funnel; warm/retargeting → PDP or straight to sales page.
- Advertorial sells the PROBLEM; sales page sells the OUTCOME; order page only collects payment + AOV boosters (quantity breaks, order bumps — $10-20 item at ~50% take = +$5-10 AOV, priority shipping, insurance).
- **OTO1 = highest price-elasticity point in the funnel.** Post-purchase anxiety window ≈ 24h; peak emotional state. Price up to **10x the front end** ($40 front → $400 OTO; 10% take = +$40 AOV). Downsell = popup, same offer 50% off. 1-4 OTOs sweet spot (some run 7).
- Upsell design rule: solve the same problem **better/faster/easier**, OR solve the **new problem the front-end product creates** (GLP-1 → keep-the-weight-off).
- **AOV target ≥2-3x front-end price** ($40 product → $80-120 AOV; overall sweet spot $100-400). Why: "the universal law of scaling — CPA only ever goes up." Dan Kennedy: whoever can spend the most to acquire a customer wins.
- Consumption logic: ad 2min + advertorial 3min + sales page 2min + order page 2min = 9 minutes vs ~3 on a PDP. More consumption = higher CVR and AOV. Advertorial-first ads hit 7-10% CTR vs ~3% direct.
- Advanced: after ≥500 buyers, create custom conversions optimizing for OTO-takers. Pixel gamification: fire browser-side Purchase only on front-end price, feed true value server-side via Hyros CAPI.

## 5. Sales Page Anatomy (001, 029, 104)

- **Headline formula: Outcome + Timeframe + Mechanism** ("fuller, smoother lips in five minutes with the micro lift system").
- **7-point headline/hook checklist — need ≥4**: curiosity · calls out pain · promises solution · specificity · simplicity (5th-8th grade, Hemingway app) · credibility · timeframe.
- Above the fold = 90% of energy. Carousel cadence: hero → before/after ("nothing fucking sells like a before and after") → objection-handler image → comparison/research/risk-reversal → social proof collage.
- Subheadline: "without" statements in sophistication-stage-4 markets, ordered by frequency of solutions already tried.
- Flow: ATF → offer/CTA/risk reversal → FAQs under offer → testimonials-as-transformations (demographically matched; each must overcome an objection or install a belief) → education blocks (mechanism UMP/UMS, ingredients+research, how-it-works GIFs — "GIF sections increase conversion rate every single time" — us-vs-them table) with social proof between every block → more FAQs → final offer card with urgency/scarcity.
- Offer structure: quantity breaks with one "most popular" + one decoy near the top price; every free gift must overcome an objection or speed the outcome.
- Rules: never more than one scroll from a CTA; identical CTA text on every button; emoji on CTA button lifts CVR; 95% of CRO in mobile view; prefer REMOVING elements; judge tests by **EPV (earnings per view)**, not CVR.
- **NEVER split test the first page your ads point to** (breaks Facebook's page-scan optimization) — launch new post IDs to a new URL instead; split test deeper pages 50/50.
- Authority caveat: in sophisticated health markets the medical system is often the ENEMY — the authority is "I've been there, tried it all, fuck the system."

## 6. Advertorial SOP (069, 087)

5 steps: Research → foundational docs → find swipe (webpage-to-PDF a competitor advertorial) → AI writes (in halves — token limits gut single-pass quality) → **chief it** (AI checks against necessary beliefs/awareness/sophistication, then read aloud 5-7x for the "slippery slide").
- **Headline = ~90% of advertorial success.** 4-criteria formula: **self-interest** (call out the exact avatar) · **news** (the word "new", breaking-news frame) · **curiosity** ("this", withholding; "why" beats "how") · **quick & easy**.
- Body sequence (PetLabCo teardown, 087): UMP → make pain tangible (Halbert if-then qualification: "if your dog itches, licks paws, shakes head...") → product intro with credibility → comparison table → expert-reviewed testimonials → outcome social proof → CTA as a **quiz** (micro-commitments), not "buy now."
- Types: story advertorial (problem-aware; PIG nightmare story, congruent with the ad), whistleblower angle (insider tells the truth), product-aware objection-stacker (can skip sales page → order page).

## 7. Quiz Funnel System (042)

Works via **micro-commitments** (yes-yes-yes hypnotic state) + **seeding** (belief-installing cards between questions) + **pre-handled objections** ("how quickly do you expect results?"). Build: foundational docs + screenshots of a winning competitor quiz (e.g. Bioma) → ChatGPT. Rules: 8-12 questions (3-20 viable) · never 2-3 same-format questions in a row · first question least invasive (gradualization) · no free-text · every question serves one of the 3 jobs or dies. KPIs: **30% completion** (25% ok at scale); per-question drop-off ~1-2% normal, ≥4% spike = rewrite. End: name+email for "personalized results" → 5-7 email sequence, branched by quiz answers.

## 8. Video Ads

**Holy Grail structure: Hook → Body (UMP/UMS mechanism + how it works, outcome-tied) → CTA1 (one sentence) → Social proof (each testimonial overcomes an objection or installs a belief — anything else is "smooth brain activity") → CTA2 (guarantee + true scarcity + offer).** 60-90s standard.
- **Hook = 90% of the ad. Composition: copy 70-80%, scroll-stopper clip 15-20%, audio 5-10%.** First 3-5 seconds. Scroll-stopper test: show your mom — if she says "what the fuck was that?" it's ready.
- **Mini-VSL (2-7min) 9 ingredients** (072): micro lead (2-5s) → lead (~20s PIG/nightmare open loop) → discovery story (hero's journey, "I was just like you, but worse") → UMP (explainable to an 8-year-old) → UMS → product reveal (features ≤5% of copy; outcomes) → price drop (anchor) → risk reversal → social proof. Writing process: Research → Brief → Swipe → Write → Source → Edit.
- **Production: Swipe → Script → Storyboard → Source/Prompt → Edit.** Swipe structure not words (Facebook metadata-detects 1:1 rips → bans). Storyboard: 1-2 script lines per clip; 30s ≈ 6-10 clips (hook / problem / mechanism / social proof / CTA). Hand editors a sheet with every line matched to its exact clip. Editing meta: minimalist, raw, fast cuts, captions — "so fast it almost feels a little rushed."
- Sourcing: Fiverr UGC ($50-100/script), AI UGC, Storyblocks/GridBank B-roll, buy the Amazon product and film on iPhone. First test ≈ $100-300 max.
- **Copy chiefing**: paste script into ElevenLabs, listen 3-5x, smooth every bump.
- **PIG method** (Chris Haddad): open with a punch-in-the-gut line in as few words as possible ("Is that a gray hair?").

## 9. Hooks

- **7-point checklist** (same as headlines): curiosity / pain / promise / specificity / simplicity / credibility / timeframe — need ≥4.
- **49-second AI hook machine** (025 + SOP doc): ChatGPT Agent Mode scrapes Reddit/forums for 20 verbatim first-person emotional quotes (sorted by emotional intensity) → Claude + headline-engine docs converts into exactly 20 DR headlines.
- **GenSpark TikTok mining** (065): find high-view/LOW-follower videos (proves the hook drove views, not the audience) in the problem niche → extract hook formulas → iterate with foundational docs = "the infinite hook glitch."
- **$50-100 hook pre-validation** (099): Traffic campaign, 1 ad set, 10 ads = plain white squares with the hook in black text, auto-rule off at 1,000 impressions → highest CTR hook goes into the real ad.
- Power moves: the word **"without"** (promise outcome + discredit the failed alternative) · discredit common solutions ("Please stop buying oral B12 for neuropathy") · familiarity bias (celebrities the avatar admires) · financially-qualify in the copy ("if you're a chiropractor struggling with back pain...") — "solve rich people problems."

## 10. AI Creative Production (the Brand Builder's Engine)

- **Message-first**: image ads are cheap hypotheses to find the winning sales message ($500 tests 20 angles in a week); only then graduate to video. "Trying to find your message via video first is expensive guessing."
- **Direct ↔ indirect spectrum**: direct (product, price, CTA) = retargeting/warm only; **indirect** (native-style scroll-stoppers, memes, weird before/afters — selling happens in primary text) = where cold-traffic scale lives, and exactly what AI makes easiest.
- **80/20 swipes/originals while hunting the message → flips to 80/20 originals/swipes once found.** Swipes inherit validated variables; originals are the moat ("nobody can swipe what you haven't published").
- **Image stack**: Claude Project (foundational docs + swipe-analysis instructions; Sonnet fine) → drop swipe image, no prompt → analysis + adapted text-to-image prompt → **Higgsfield, Nano Banana Pro, 4 variations, 1:1 feed / 9:16 stories, product PNG on white as reference** → fix near-misses with Canva Magic Layer (free, makes every element editable). Model niches: Higgsfield Soul = hyper-real/iPhone UGC; Flux Kontext = animated; GPT Image = text-heavy.
- **Video stack**: Nano Banana Pro starting frame → image-to-video. **Test with Kling 3.0 (workhorse) or Veo 3.1 (cheaper/faster); scale proven winners with Seedance 2.0 only** ("the credits will eat you alive" testing on it). Sora 2 pipeline (033): 15s max clips, two Claude Projects (script + prompts), "keep B-roll prompts stupid stupid simple," "simplicity scales" in video prompting.
- **Image ad hook = visual contrast (scroll stop) + headline copy (70-80% of the work) + implied curiosity (the click trigger).**
- **Realism is NOT the goal — attention is.** Winning formats: cartoon/animation ads, intentionally weird ("legs melting"), 1995-infomercial-style. **Look backwards** (TV ads from the 80s/90s/QVC), not at Twitter.
- **2-hour roadmap**: 0-30min swipe hunt (5 swipes + 2-3 originals) → 30-90min generation (~28-32 images, "don't get precious") → 90-120min pick 1-2 per concept, Canva-fix, filter through contrast/headline/curiosity → 5-8 finished ads = a week of testing.
- Why AI ads fail: shit research, shit prompting (dictate with voice → LLM writes the prompt), shit tool choice. "AI is a multiplier — multiply shit, get more shit."

## 11. Meta Ads: Setup, Testing, Scaling

**Post-Andromeda doctrine**: Andromeda rebuilt retrieval; it groups similar ads into containers → **variation spam is dead; creative DIVERSITY wins.** "The creative is the targeting" — FB's AI reads every element of the image, the copy sentiment, even your landing page source code. Media buying is "boring": broad, Advantage+, consolidate, "let it rip."

**Testing structure A — CBO (027)**: 1 CBO sales campaign, 3-5 ad sets where **each ad set = one unique concept**, 2-5 variations inside. **Minimum $10/day per ad; never run a CBO below $50/day.** Settings: Purchase optimization; 7-day click/1-day view; schedule 6am next day; broad 18-65+; Advantage+ placements; ALL Advantage+ creative enhancements OFF; CTA Learn More (slight lift over Shop Now); images OR videos per campaign, never mixed. 80% new concepts / 20% variations (pre-Andromeda it was the reverse).

**Testing structure B — ABO (077)**: 4 ad sets @ $50/day (2 US, 2 non-US tier-1; interest vs Advantage+ split), 3 ads per set = same body, 3 hooks. Judge at 2-3 days.

**Beginner SOP (101)**: BM + 2FA + domain verify + pixel via Datasets w/ CAPI, data sharing Maximum. Manual sales campaign, ABO, budget = product price/day, minimum 3 days before judging, one interest <100M audience, dynamic creative OFF, primary text is the #2 element (headline/description barely matter), no aggressive claims / all-caps (cost penalties), pay by credit card never PayPal, Triple Whale tracking.

**Scaling**: move the winning AD (use existing post — keeps social proof) into a new campaign testing audiences at **min $100/day per ad set**; raise budgets or duplicate+double. At ~$1k/day+, allocate 10-20% of spend to a creative-testing campaign (ABO, winning audience, 1 new creative per ad set @ $25-50/day, 3 days). **Test 20-50 net-new creatives/week at scale** (he tests 20-30/day on a scaling brand). Surf scaling: raise budgets intraday on winners, reset ~5pm/midnight. Don't scale at "mach fuck" (processor bans). Retargeting only after $500-1,000/day spend; buyer needs 6-7 impressions.

**8 Laws of Scale (048)**: AOV:CAC ≥2:1 (know before launch) · money loves speed · know thy numbers (break-even CAC & ROAS) · read data and fix the constraint ("90% of everything you test will fail") · ultimate emotional detachment ("the data doesn't care about your feelings" — he deleted the Shopify app) · know the customer better than they know themselves · be vicious (you compete with TikTok girls, not advertisers) · minimize variables (proven products only).

**5 Laws of Testing (030)**: know thy numbers (test for ≥20% net margin) · read data & adjust (ATC <10% = messaging/lander problem, fix and relaunch — improves 90% of the time) · **One Relaunch Rule** (one adjusted relaunch, then cut the product — opportunity cost) · minimize variables · law of ultimate detachment.

## 12. Backend & Infrastructure

- Email/SMS = "boring money": +15-30% revenue. Klaviyo + SMSBump. Pre-launch: abandoned-cart flows ONLY. Cadence: 3 broadcasts/week (sell in ~20%, value 80%), SMS biweekly. Abandoned cart alone ≈ +15%/day.
- Omnipresence: retarget on Google/YouTube/Gmail/Bing/TikTok/Snap = up to +20% "easiest money."
- Infrastructure: diverse BMs/pixels/pages/ad accounts — back up in under a day. Test payment processors (approval rates differ), ad accounts (fresh sometimes beats aged), pages (brand vs personality vs interest — VSLs suit personality pages). De-anonymization (retention.com), pixel enrichment, geo funnels (translate winning funnel to less-saturated countries).
- Dry testing / VCL (039): Builder.io vibe-coded lander in ~30min (structure → copy → branding → images, never one mega-prompt), buy button swapped for opt-in. **KPI: 10% opt-in = pursue** (8-9% for $100+ products); 4-5% = pass. 3 products testable per day.

## 13. Mindset OS (for motivational content in his voice)

- **XP farming**: compress years of failures into 90 days — 2-4h time-blocked deep work (Parkinson's law), internal reward loop (scripted victory self-talk, kill ANTs), pick work via goal → #1 constraint → "the one system that solves it forever."
- **Identity precedes action** (Psycho-Cybernetics): "I'm the type of person that ___" in present tense; "who do I need to become?" not "what do I need to do?"
- **Law of detachment**: set the goal once, mail it like an Amazon order, never refresh tracking; obsess over inputs. His proof: 50 failed products in a row, then everything back in 2-3 months.
- **Seasons**: winter (obsessive learning, zero results — where everyone quits) → spring (earning) → summer (multiplying into assets) → fall (reflecting). Mentors shorten winter.
- **Dopamine engineering**: chosen addictions via cue→routine→reward (beta-alanine = gym cue; bone broth + darkness + specific music = deep-work cue; caffeine as earned reward); dopamine loading (cheap dopamine only after work); wall-staring 20min pre-deep-work; grayscale screen; the Brick device; "discipline problems are usually stimulation problems."
- **Environment**: be the poorest guy in the room (paid rooms: he paid $100k/yr for a mastermind, 5x'd income in ~9 months); "if you surround yourself with four retards, you'll be the fifth"; cut the safety net; deliberately raise expenses.
- **One Thing Contract**: nightly, one non-negotiable task tomorrow, started ridiculously small.
- Anti-patterns he attacks: morning-routine theater, motivational content ("avid consumers of motivational content are not successful"), balance ("counterbalance" instead), "work smart not hard" ("work smart AND hard AND long"), preparation/mental masturbation, shiny objects, meshing gurus' strategies ("shit soup — follow ONE philosophy to the T").

## 14. Book Canon (for recommendations)

S-tier: Breakthrough Advertising (Schwartz — "the GOAT"), Gary Halbert Letters/Boron Letters, Great Leads (Masterson), Agora Big Black Book, Power vs Force, Meditations, Almanack of Naval Ravikant, Way of the Superior Man. A: $100M Offers, Influence (Cialdini), Psycho-Cybernetics, Adweek Copywriting Handbook (Sugarman), DotCom Secrets (source of his funnel philosophy), Mastery (Greene). D-tier: Rich Dad Poor Dad ("nothing tactical"), 4-Hour Workweek. Meta-rule: read → apply → read → apply; otherwise it's mental masturbation.
