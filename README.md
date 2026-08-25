# PawDirector — AI Pet Short Video & Drama Skill

[简体中文](README.zh-CN.md)

Turn pet photos into coherent 15–120s AI shorts or episodic dramas—without anime drift, random jump cuts, broken physics, static talking heads, or fragmented sound.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skill v0.1.0](https://img.shields.io/badge/Skill-v0.1.0-blue)
![Models](https://img.shields.io/badge/routes-Wan%203%20%7C%20Seedance%202.5%2F2.0%20%7C%20MiniMax%20H3-orange)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**PawDirector** is a provider-neutral agent skill for AI pet video, AI cat video, short drama, and pet-led micro-cinema. It combines pet identity locks, 15–30 second story-block choreography, model-aware routing, native audio/reference-audio choices, continuity state transfer, physical-realism QA, cost tiers, and smallest-unit repair.

It does not require Atlas Cloud or any other vendor. Use an official product, API, aggregator, web app, or MCP that exposes the capabilities you need.

## Why PawDirector?

- **The pet drives the plot.** Hooks, conflict, action, and payoff come from feline anatomy, instinct, personality, and relationship—not decorative cat cutaways.
- **Continuity is evidence-based.** Accepted tail frame + canonical master + state ledger; downstream clips stay locked until their parent is reviewed.
- **Production, not prompt dumping.** Story, model route, paid mode, dialogue/dubbing, generation, contact-sheet review, sound edit, and cold-viewer QA live in one workflow.

## Install

Copy `skills/pawdirector` into your agent's skill directory, or install from the repository with a compatible skill manager:

```bash
npx skills add <OWNER>/ai-pet-short-video-skill --skill pawdirector
```

Manual install:

```bash
git clone https://github.com/<OWNER>/ai-pet-short-video-skill.git
cp -R ai-pet-short-video-skill/skills/pawdirector ~/.codex/skills/pawdirector
```

Example request:

```text
Use PawDirector to turn my two cat photos into a 90-second 9:16 live-action hybrid short.
The cats should feel cute, but the fur, clothes, apartment and physics must remain real.
Choose the provider and paid mode from my available tools, use native dialogue only where it improves lip sync,
and do not unlock a dependent block until the previous output passes contact-sheet and continuity review.
```

## Supported Productions

| Format | Typical length | Structure |
|---|---:|---|
| Standalone microshort | 15–45s | hook → attempt → escalation → payoff |
| Standalone short | 45–120s | 2–4 coherent story blocks |
| Anthology/unit episode | 1–4 min | recurring pet/world, self-contained episode |
| Serialized drama | 1–4 min/episode | episode payoff plus persistent season state |

## Model Router: MiniMax H3 vs Wan 3 vs Seedance 2.5 vs 2.0

These routes are capability hypotheses, not permanent rankings. Verify the current provider schema and price before generation.

| Model family | Best starting use | Typical block strategy |
|---|---|---|
| Wan 3 | long narrative pet blocks, fewer external joins | choreographed 20–30s blocks with 4–6 beats |
| Seedance 2.5 | premium multimodal reference, dialogue/audio, edit/extend | dialogue, repair, continuation, reference-audio scenes |
| Seedance 2.0 | balanced shorter dialogue/action/transition | controlled 4–15s units |
| Seedance 2.0 Fast | preview, alternate, coverage, budget draft | strict QA before final use |
| MiniMax H3 | hero action, transformation, macro paws, selective high resolution | high-control 4–15s inserts |

See the provider-neutral [model router](skills/pawdirector/references/model-router.md).

## Quality and Paid Modes

PawDirector supports six spend modes:

1. **Sketch** — lowest useful resolution, one candidate, story/motion validation.
2. **Economy** — usually 720p, long blocks, targeted retries.
3. **Balanced** — stronger references/audio; extra candidates only for hook and climax.
4. **Premium** — reference audio, multimodal edit/extend, selective high resolution.
5. **Hero Insert** — concentrate spend on one spectacular or fragile shot.
6. **Final Polish** — upscale and repair accepted takes only.

Current prices are supplied by the user's chosen provider. The included estimator calculates request count and a best/expected/capped production plan without binding the workflow to one platform.

## Native Audio, Reference Audio, and Dubbing

PawDirector routes each scene among:

- no dialogue: continuous post BGM + ambience + Foley;
- model-native speech for lip-synced performance;
- reference-audio generation for recurring voice consistency;
- external dubbing or TTS with lip-sync/cutaway strategy;
- hybrid: native hero lines, post-produced narration/phone/off-screen lines and final mix.

Generated clip music is not treated as the final soundtrack. Every clip remains a separate audio source; room tone, score, loudness, J/L cuts, and sound bridges are rebuilt as one film.

## Tested Failure Patterns

The workflow includes lessons from actual local experiments—not a claim that one unfinished sample is a successful film:

- a 36-clip short-block version had 20/36 (55.6%) severe or blocking physical/visual issues;
- four tested 30-second Wan 3 clips internally cut 2–4 times, showing that long blocks reduce external joins but still need timed internal beats;
- native audio across twenty short units varied by 8.9 LU, with some boundaries jumping over 30 dB;
- tail-frame chaining improved the next opening but did not prevent late-block wardrobe/anatomy drift;
- “storybook / soft fantasy / cartoon” prompt language caused animated or plastic-CG drift; live-action medium locks improved material realism;
- a technically approved edit still failed cold-viewer story comprehension, so narrative QA is now an independent P0 gate.

Full observations and limits are in [benchmarks/tested-observations.md](benchmarks/tested-observations.md).

## Workflow

1. Select standalone, anthology, or serial form.
2. Lock pet identity, wardrobe construction, voice, medium, and world state.
3. Plan 4–6 observable beats per long block.
4. Select provider-neutral capabilities and paid mode.
5. Choose native dialogue, audio reference, external dubbing, or hybrid.
6. Generate the highest-risk or hook block first.
7. Inspect real media, 12-frame contact sheet, motion contacts, and audio/ASR.
8. Accept/reject/repair, then export a verified tail state.
9. Unlock dependent blocks and edit with motivated picture and sound transitions.
10. Require a cold viewer to retell goal → obstacle → choice/action → result.

## Tools

```bash
# Validate a continuity ledger and dynamic cost plan
python3 scripts/validate_plan.py \
  --continuity skills/pawdirector/assets/templates/continuity-ledger.csv \
  --cost skills/pawdirector/assets/templates/cost-plan.csv

# Estimate current provider costs after filling unit_price
python3 scripts/estimate_cost.py skills/pawdirector/assets/templates/cost-plan.csv

# Inspect a 30-second candidate
bash scripts/make_contact_sheet.sh candidate.mp4 candidate_contact_12.jpg
bash scripts/extract_tail_frame.sh candidate.mp4 candidate_tail.png
```

## Examples

- [Standalone 90-second pet short](examples/standalone-90s/README.md)
- [Anthology/unit episode](examples/anthology-episode/README.md)
- [Serialized episode](examples/serialized-episode/README.md)

Examples are fictional, use no private pet media, and focus on manifests rather than claiming unreviewed generations are finished films.

## FAQ

### How do I keep the same cat across AI video shots?

Use a canonical identity/material master plus the accepted previous state frame and a continuity ledger. Re-anchor after location changes, detected drift, or every two long blocks. A tail frame alone can carry existing errors forward.

### Which model is best for a 30-second AI pet short?

There is no permanent winner. Start with a model that currently supports the required duration, aspect ratio, reference type, and audio mode. Wan 3-class long generation is a practical hypothesis for fewer joins; Seedance 2.5-class generation is useful when richer audio/reference/edit control matters.

### How do I stop AI cat videos from looking like anime or plastic CGI?

Lock the medium as live-action cinema, real fur, practical fabric, and a real-scale environment. Put cuteness in feline timing and behavior—not “cartoon style” rendering words. Reject blocks when sampled frames drift materially.

### How do I maintain dialogue voice and lip sync across clips?

Create an approved voice bible and sample. Use model-native dialogue or reference audio where supported; otherwise use external dubbing with a lip-sync pass, reaction shots, profiles, inserts, or off-screen delivery. Validate exact words and speaker with ASR plus listening.

### How do I connect multiple generated clips without random jump cuts?

Pass accepted state, preserve screen direction and action phase, overlap action, and bridge with motion, occlusion, gaze, matched shape, or sound. Never change location, action, scale, and direction all at once.

## Independent Project

PawDirector is an independent community project and is not affiliated with ByteDance, Alibaba, MiniMax, Atlas Cloud, or other model/provider owners. Model and product names belong to their respective owners.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for research acknowledgements and licensing boundaries.

## Contributing

Provider adapters, dated model observations, failure cases, new pet formats, and reproducible QA improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
