# ContinuityDirector — AI Short Film & Short Drama Skill

[简体中文](README.zh-CN.md)

Create coherent AI short films, vertical dramas, episodic series, pet stories, animation, and branded narratives—without random clip piles, broken continuity, static dialogue, physics failures, voice drift, or fragmented sound.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skill v0.2.0](https://img.shields.io/badge/Skill-v0.2.0-blue)
![Provider neutral](https://img.shields.io/badge/providers-user--selectable-orange)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**ContinuityDirector** is a provider-neutral Agent Skill for AI video production. It turns an idea, script, manuscript, brief, storyboard, or reference asset pack into a continuity-first production: story contract, character/world locks, 15–30 second generation blocks, 2–8 second edit beats, model and provider routing, spend authorization, native dialogue/reference audio/dubbing, physical QA, smallest-unit repair, sound mixing, and cold-viewer review.

It does not require Atlas Cloud, any MCP, or any single website. Users choose official products, APIs, aggregators, local workflows, or web UIs. The skill routes from capabilities and checks the active surface before spending.

## What It Produces

- 15–45s social microshorts and hook-driven ads;
- 45–120s standalone short films;
- 1–4 minute live-action, animated, pet, fantasy, UGC, or branded narratives;
- recurring anthology/unit episodes;
- serialized short drama with season continuity;
- source adaptations with character, relationship, timeline, prop, and reveal state;
- generation prompts, paid-batch plans, voice bibles, review evidence, edit and sound maps.

## What Makes It Different

### Dual-timescale directing

A `generation_block` is the 8–30s model request; an `edit_beat` is the 2–8s story/camera/performance unit. This preserves fast pacing inside long outputs while reducing risky external joins.

### Continuity dependency graph

Independent assets, voices, music exploration, alternate hooks, and non-dependent inserts may run in parallel. A child scene cannot start from an unreviewed parent. Accepted tail state + canonical identity/material anchor + continuity ledger unlock the next block.

### Separate model, provider, and spend decisions

The creative route requests capabilities; the user chooses the channel/provider. Quality tiers (`Sketch` through `Premium`) are separate from authorization modes (`plan-only`, `single-test`, `approved-batch`, `autopilot-with-cap`). Saying “use Premium” never silently authorizes unlimited charges.

### Audio is its own production system

Choose per scene among native dialogue, reference-audio dialogue, external dubbing/TTS with lip sync, voice-over over B-roll, no-dialogue sound design, or hybrid. Generated music is not blindly concatenated; dialogue/Foley, ambience, score, loudness, reverb tails, and J/L cuts are rebuilt into one film.

### Technical QA cannot approve a confusing story

Every production has independent gates for narrative comprehension, identity/style, physics/continuity, and audio. A cold viewer who has not read the synopsis must be able to retell goal → obstacle → action/choice → result.

## Install

```bash
npx skills add xixihhhh/ai-short-drama-skill --skill continuity-director
```

Manual:

```bash
git clone https://github.com/xixihhhh/ai-short-drama-skill.git
cp -R ai-short-drama-skill/skills/continuity-director ~/.codex/skills/continuity-director
```

Example request:

```text
Use ContinuityDirector to plan a 90-second 9:16 live-action family short.
I can use Wan 3, Seedance 2.5, Seedance 2.0 Fast, and MiniMax H3 through providers I choose.
Offer Economy and Balanced routes, keep dialogue voices consistent, and do not generate a dependent block
until its parent passes narrative, continuity, physics, and audio review.
```

## Content Profiles

One primary profile plus optional specialist overlays changes constraints without changing the production state machine.

| Profile | Key locks |
|---|---|
| Live-action human drama | face, hands, wardrobe, eyelines, axis, performance, relationship knowledge |
| Pet/animal story | species anatomy, identity, scale, behavior, contact, human bond |
| Anthropomorphic/fantasy | body plan, degree of humanization, power trigger/limit/cost/consequence |
| Animation/motion comic | design grammar, line/shading, proportions, pose rhythm, background depth |
| Branded/product narrative | geometry, materials, claims, label-safe plates, product function in plot |
| UGC/talking-head/explainer | speaker, lens grammar, authentic imperfection, information density, room tone |

See [content profiles](skills/continuity-director/references/content-profiles.md).

## Formats

| Format | Typical length | Story contract |
|---|---:|---|
| Microshort | 15–45s | hook → attempt → escalation → payoff |
| Standalone short | 45–120s | complete goal, obstacle, change, release |
| Anthology/unit episode | 1–4 min | recurring world, self-contained problem and result |
| Serialized drama | 1–4 min/episode | episode payoff plus persistent season state |
| Branded story | 15–120s | audience problem → dramatic use → verifiable product consequence |

## Model Router: Wan 3, Seedance 2.5/2.0, MiniMax H3

These are starting hypotheses, not permanent rankings. Verify the selected provider's current schema, duration, reference limits, audio behavior, queue, retention policy, and price.

| Model family | First route to test | Main risk |
|---|---|---|
| Wan 3-class long generation | 20–30s multi-beat story blocks, fewer external seams | late-block style/identity/anatomy drift |
| Seedance 2.5-class multimodal | dialogue/reference audio, rich refs, edit/extend/repair, premium continuity | cost and over-constrained references |
| Seedance 2.0 | balanced 4–15s dialogue/action/transition blocks | more external joins in long films |
| Seedance 2.0 Fast | previews, coverage, alternates, economy tests | final use still requires strict QA |
| MiniMax H3-class audiovisual | 4–15s hero action, first/last/reference modes, native sound | expensive if used for all ordinary coverage |

The provider-neutral [model router](skills/continuity-director/references/model-router.md) separates capability selection from provider execution.

## Quality and Paid Modes

Quality tiers:

1. **Sketch** — lowest useful preview; validates story and blocking.
2. **Economy** — commonly 720p; long blocks and targeted rerenders.
3. **Balanced** — stronger model/reference/audio only where it changes acceptance probability.
4. **Premium** — rich multimodal controls, reference audio, edit/extend, selective higher resolution.
5. **Hero Insert** — concentrate spend on hook, fragile dialogue, transformation, action, reveal, or climax.
6. **Final Polish** — upscale and repair accepted ranges only.

Authorization modes:

- **plan-only:** zero paid requests or uploads;
- **single-test:** one named representative request;
- **approved-batch:** fixed providers, upload policy, request count, retry count, and cap;
- **autopilot-with-cap:** automatic routing/repair inside a hard cap; stop at scope, rights, provider, or P0 boundaries.

The spend ledger tracks quoted and actual cost plus `cost_per_accepted_second`, so different billing models can be compared fairly.

## Dialogue, Reference Audio, and Dubbing

- **Native dialogue:** best when model performance and lip sync are reliable; validate exact words, speaker, pace, emotion, and repeated tails with ASR plus listening.
- **Reference-audio generation:** use one rights-cleared voice anchor per recurring character; assign each reference a single primary role.
- **External dubbing/TTS:** lock the voice, then use lip sync, reactions, profiles, inserts, off-screen lines, or B-roll to protect visual credibility.
- **Hybrid:** retain strong native hero lines and Foley; replace narration, phone/off-screen lines, ambience, score, and problem audio in post.
- **No dialogue:** one continuous ambience/score plan plus curated Foley; no unrelated music restart at every generated boundary.

## Production State Machine

`brief → story contract → canonical assets → block/beat manifest → capability route → cost authorization → candidate → evidence review → accepted state → dependent generation → picture edit → audio mix → cold-viewer gate → delivery`

Candidates never become continuity anchors automatically. Promote only inspected media to canon.

## Evidence and Repair

For a 30-second candidate, capture the real file, metadata, 12-frame contact sheet, start/25/50/75/end frames, slow-motion contact notes, audio/ASR, and timestamped QA. Classify failures as narrative, asset, prompt, model, provider surface, edit, or audio.

Repair the smallest failing unit:

- edit/inpaint a localized defect;
- extend or bridge a broken transition;
- regenerate from canonical state for identity/anatomy failure;
- shorten a block that drifts late;
- rewrite a scene whose cause/effect is unreadable;
- remix rather than regenerate good picture for an audio discontinuity.

## Lessons From Real Production Failures

An anonymized local experiment found 20/36 fragmented short clips had severe or blocking visual/physical issues. Four tested 30-second outputs each contained 2–4 internal changes: long generation reduces external seams but still requires 4–6 timed beats. Native audio from twenty short units varied by 8.9 LU, with some boundaries exceeding 30 dB. Tail-frame chaining improved the next opening but did not prevent later wardrobe/anatomy drift. A technically improved cut still failed cold-viewer comprehension.

These observations became executable gates, not claims that one model is universally best. See [tested observations](benchmarks/tested-observations.md).

## Project Files

The core skill stays compact and loads deeper references only when needed:

- [SKILL.md](skills/continuity-director/SKILL.md)
- [Generation blocks vs edit beats](skills/continuity-director/references/generation-blocks-and-edit-beats.md)
- [Model router](skills/continuity-director/references/model-router.md)
- [Authorization and batch](skills/continuity-director/references/authorization-and-batch.md)
- [Budget and quality](skills/continuity-director/references/budget-and-quality.md)
- [Audio and dubbing](skills/continuity-director/references/audio-and-dubbing.md)
- [Continuity and transitions](skills/continuity-director/references/continuity-and-transitions.md)
- [Physics and failure modes](skills/continuity-director/references/physics-and-failure-modes.md)

## Tools

```bash
python3 scripts/validate_plan.py \
  --continuity skills/continuity-director/assets/templates/continuity-ledger.csv \
  --cost skills/continuity-director/assets/templates/cost-plan.csv

python3 scripts/estimate_cost.py skills/continuity-director/assets/templates/cost-plan.csv
bash scripts/make_contact_sheet.sh candidate.mp4 candidate_contact_12.jpg
bash scripts/extract_tail_frame.sh candidate.mp4 candidate_tail.png
```

## Examples

- [Live-action family microdrama](examples/live-action-90s/README.md)
- [Pet-led standalone short](examples/standalone-90s/README.md)
- [Anthology/unit episode](examples/anthology-episode/README.md)
- [Serialized drama](examples/serialized-episode/README.md)

The examples are fictional manifests, not claims that unreviewed generations are finished films.

## Research Positioning

Popular 2026 projects tend to specialize in one model/prompt dialect or provide a large application pipeline. ContinuityDirector is a lightweight installable skill that combines:

- cross-model, cross-provider, cross-format routing;
- long generation blocks with fast internal edit beats;
- explicit paid authorization and cost-per-accepted-second;
- native dialogue/reference audio/external dubbing as equal routes;
- accepted-media state transfer and physical causality;
- independent narrative comprehension after technical QA.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No third-party prompt packs or unlicensed schemas are redistributed.

The dated comparison is available in [AI Short-Film Workflow Landscape — 2026-08](research/2026-08-workflow-landscape.md).

## Independent Project

ContinuityDirector is not affiliated with ByteDance, Alibaba, MiniMax, Atlas Cloud, or any model/provider owner. Product names belong to their respective owners.

## License

MIT. See [LICENSE](LICENSE).
