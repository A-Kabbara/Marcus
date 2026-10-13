# CLAUDE.md — Marcus Foundational Docs

You are an agent that has just been handed this repo. You know nothing about the user yet. This file tells you exactly what to do, in order, from zero. Follow it top to bottom.

**The job:** Based on everything you know about the user, about their business, and what they are selling (their product), use these Foundational Docs to produce finished advertising work for them.

If you know nothing about the user yet, Phase 0 fixes that. Do not skip it.

## What is in this repo

| Path | What it is |
|------|-----------|
| `Foundational Docs/01 - Foundational Docs SOP.txt` | Mark Builds Brands' master workflow: Research → Avatar Sheet → Offer Brief → Necessary Beliefs. Written for ChatGPT with manual uploads. This CLAUDE.md is the same workflow adapted so you can run it yourself. |
| `Foundational Docs/02 - The Brand Builders Engine...txt` | His system for generating, testing and scaling 20 winning AI ads a week, and the philosophy behind it. Read in full before Phase 5. |
| `Foundational Docs/03 - The Direct Response Headline Engine.txt` | How to write headlines and hooks. Read before Phase 6. |
| `Foundational Docs/04 - 100 Greatest Headlines Ever Used.txt` | Swipe file. Model the structure, never copy the words. |
| `Foundational Docs/05 - How to Create Unlimited Hooks with AI.txt` | A research-scrape prompt that pulls real first-person customer language, then turns it into hooks. |
| `Foundational Docs/06 - AI Video Ad Creation SOP.txt` | Script → starting frame → image-to-video, scene by scene. Read before producing video. |
| `Foundational Docs/07 - 349 Great Headlines - Halbert Swipe File.pdf` | Second swipe file. |
| `templates/` | The four templates the SOP refers to as "attach this template", plus the intake sheet. Where the SOP says "[ATTACH THIS AVATAR SHEET TEMPLATE]" use `templates/02-avatar-sheet.md`, and so on. |
| `SKILL.md` + `references/` | A skill that thinks and writes like Mark. `references/frameworks.md` is the full framework library. `references/kpi-benchmarks.md` has his metric thresholds. `references/voice-guide.md` is his voice. `references/video-index.md` maps topics to transcripts. |
| `transcripts/` | 104 full transcripts of his videos. Grep these when you need his exact words. |
| `output/` | Where you write everything you produce. Create it. |

## Phase 0 — Intake. Learn the user, the business, the product.

1. Check what you already know: your memory, any project files, any CLAUDE.md or notes in the user's own folder, anything they pasted. Pull every fact you can from those.
2. Open `templates/00-intake.md`. For every field you cannot fill from what you already know, ask the user. Ask all the questions in one message, grouped as in the template.
3. Write the completed sheet to `output/00-intake.md`. Show it to the user and ask them to correct anything wrong.
4. Pick one product for this run. If they sell several, ask which one comes first.

Done when `output/00-intake.md` exists and the user has confirmed it.

## Phase 1 — Research Doc

1. Read `templates/01-research-brief.md` and section 3, "Foundational Docs SOP", of `references/frameworks.md`.
2. Fill the brief's brackets from the intake.
3. If you can search the web, do the research yourself: real quotes, real sources, cited. If you cannot, write the brief out as a complete deep-research prompt, give it to the user to run in ChatGPT Deep Research or Gemini Deep Research, and ask them to paste the result back.
4. Write `output/01-research-doc.md`. Minimum 6 pages. Verbatim quotes beat paraphrase. No invented quotes.

Done when the research doc has a quote bank of at least 30 verbatim customer quotes with sources.

## Phase 2 — Avatar Sheet

1. Read `templates/02-avatar-sheet.md`.
2. Fill every section from the research doc only. Where the research is silent, write "not found in research" rather than inventing.
3. Write `output/02-avatar-sheet.md`.

## Phase 3 — Offer Brief

1. Read `templates/03-offer-brief.md`.
2. Fill it from the intake, the research doc and the avatar sheet. The awareness level and sophistication stage must be justified, not guessed. Name the unique mechanism.
3. Write `output/03-offer-brief.md`.

## Phase 4 — Necessary Beliefs

1. Read `templates/04-necessary-beliefs.md`.
2. Read the research doc, avatar sheet and offer brief together.
3. Write no more than six "I believe that..." statements in the order the prospect must adopt them.
4. Write `output/04-necessary-beliefs.md`.

At this point the foundation is built. The SOP calls these the foundational documents because you build them once and every later asset is written from them. Every asset below must be checked against the necessary beliefs before it is finished.

## Phase 5 — Find the message

1. Read `Foundational Docs/02 - The Brand Builders Engine...txt` in full.
2. Using the offer brief's five angles and the avatar's quote bank, write 10 candidate sales messages. A message is one belief-shifting idea that can become many ads, not an ad.
3. Rank them by how directly they come from the research, and recommend three to test first.
4. Write `output/05-messages.md`.

## Phase 6 — Headlines and hooks

1. Read `Foundational Docs/03 - The Direct Response Headline Engine.txt`. Skim `04` and `07` for structure.
2. For each of the three chosen messages, write 20 headlines and 20 hooks. Use the avatar's verbatim quotes as raw material. Follow the laws and headline types in doc 03 (open loop, name the wound, new promise, specificity, simplicity, credibility, compress time). Cross-check each headline against the 4-criteria formula in `references/frameworks.md` section 6 (self-interest, news, curiosity, quick and easy) and the hook checklist in section 9.
3. If the user can run the scrape prompt in `Foundational Docs/05`, offer it as a way to get more raw language.
4. Write `output/06-headlines-and-hooks.md`.

## Phase 7 — Creative

1. Image ads first. Follow The Brand Builder's Engine: for each message, concepts for static image ads with the hook as headline, the image prompt, and the primary text. Aim for 20 concepts across the three messages. Write the image prompts for whichever image model the user said they have in intake; if they named none, write them for Nano Banana Pro (doc 02's default) and say so.
2. Video ads second, only after the user has a winning message from image ads or asks for video anyway. Follow `Foundational Docs/06`: locked script, scene list, text-to-image prompt per scene, image-to-video prompt per scene.
3. Write `output/07-image-ads.md` and, when done, `output/08-video-ads.md`.

## Phase 8 — Landing page, advertorial, or VSL (only if asked for in intake)

Use `references/frameworks.md`: section 5 Sales Page Anatomy, section 6 Advertorial SOP, or the Mini-VSL 9 ingredients in section 8 Video Ads. Structure the asset around the necessary beliefs in order. Write to `output/09-<asset>.md`.

## Rules that apply to every phase

- Research before creative, always. Never write an ad before Phase 4 is done.
- Argument before words. Lead the prospect to one belief at a time, then introduce the offer.
- Sell outcomes, not features. People buy on emotion and justify with logic.
- Write in the customer's words, from the quote bank, not the brand's words.
- Use the user's real product, real price, real proof. No placeholders in finished work. If proof is missing, say so and ask.
- Model structure from the swipe files, never lift the copy.
- When a doc gives a specific number, tool or step, use that. Do not substitute generic marketing advice.
- Save every output as its own file in `output/`. Tell the user the file name each time.
- If the user wants Mark's voice in the deliverables, load `references/voice-guide.md` first. Otherwise keep his thinking and structure and write in a clean register.

## If the user only has five minutes

Run Phase 0, then write the deep-research prompt from Phase 1 and hand it to them. That is the one thing they cannot skip. Everything else can wait for the research to come back.
