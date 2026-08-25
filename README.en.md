# Dramake — Turn Text into Director-Level AI Short Drama

[简体中文](README.md)

![Even a beginner can create director-level short drama by connecting text, script, storyboard, generation, dubbing, editing, and QA](assets/dramake-cover.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skill v0.3.0](https://img.shields.io/badge/Skill-v0.3.0-blue)
![Landscape and portrait](https://img.shields.io/badge/aspect-landscape%20%7C%20portrait-orange)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.en.md)

Dramake is a text-to-drama Skill for everyday creators. Even without screenwriting, storyboarding, dubbing, or editing experience, a beginner can start from an idea, copy, fiction, or a screenplay and use one Skill to connect story, storyboard, generation, dubbing, editing, and QA into a coherent, publishable, director-level AI short drama or short film.

Dramake is built for Douyin, Hongguo Short Drama, WeChat Channels, Kuaishou, Bilibili, YouTube, and other channels. It supports live action, standalone shorts, anthology episodes, serialized drama, pet stories, anthropomorphic fantasy, motion comics, UGC, and branded narratives. It addresses confusing plots, clip piles, random jumps, identity and wardrobe drift, static dialogue, broken physics, lip-sync and voice drift, music restarts, uncontrolled spend, and cuts that are not publishable.

Users choose their execution platform, interface, and generation tools. The Skill routes from current capability, price, privacy, and upload policy without locking the workflow to one website, API, MCP, or service.

## From Text to Final Cut

`source text → story diagnosis → story contract → script/beats → character/world canon → storyboard/generation blocks → model and cost route → video candidates → evidence QA → continuity edit → dubbing/mix → cold-viewer gate → release`

Input may be one idea, marketing copy, a novel chapter, a full script, a storyboard, reference assets, or existing video. The task may stop after diagnosis, script repair, or a production package, or continue into execution and repair.

## Supported Scope

- 15–45s hook-driven microshorts, ads, and account-growth content;
- 45–120s complete standalone shorts;
- 1–4 minute live-action, animated, pet, fantasy, UGC, or branded narratives;
- anthology/unit episodes with stable characters and world rules;
- serialized drama with season, relationship, knowledge, and prop state;
- adaptation from fiction, long-form text, outlines, and existing scripts;
- native dialogue, reference audio, external dubbing/TTS, lip sync, and hybrid post;
- `9:16`, `16:9`, `1:1`, and custom aspect ratios.

## Five Core Designs

### 1. Separate generation blocks from edit beats

A `generation_block` is the 8–30s model request and continuity container. An `edit_beat` is the 2–8s unit of information, action, reaction, dialogue, and cutting. Long outputs reduce external seams, but each still needs 3–6 meaningful changes instead of one line stretched across ten seconds.

### 2. Unlock downstream work only after parent acceptance

Independent character looks, voice anchors, music exploration, alternate hooks, and non-dependent inserts may run in parallel. A dependent scene starts only after the parent file is downloaded, frame-sampled, listened to, and checked for story, identity, physics, and exit state. Accepted tail state + canonical identity/material anchor + continuity ledger unlocks the child.

### 3. Separate model, execution platform, quality, and spend authorization

- Route models by long duration, first/last frame, reference audio, native dialogue, edit/extend, and resolution capability.
- Let the user choose the execution platform.
- Quality tiers are Sketch / Economy / Balanced / Premium / Hero Insert / Final Polish.
- Authorization modes are plan-only / single-test / approved-batch / autopilot-with-cap.

Choosing Premium never authorizes unlimited spend. Batch mode records allowed uploads, requests, retries, hard budget, and stop conditions.

### 4. Treat dubbing as its own production line

- Model-native dialogue prioritizes lip sync and performance.
- Reference audio locks voice, pace, accent, and emotion.
- External dubbing/TTS combines lip-sync tools, reactions, profiles, wide shots, inserts, and voice-over.
- Hybrid keeps good native lines and Foley while rebuilding narration, phone voices, ambience, and music in post.
- No-dialogue work uses a continuous ambience bed, one music structure, and selected Foley.

Random generated music is never concatenated straight into the final mix.

### 5. Technical success does not make a story publishable

The final cut passes four independent gates: narrative comprehension, identity/style, physics/continuity, and audio. A cold viewer who never read the synopsis must be able to retell: who wanted what → what stopped them → what they did → why the result happened.

## Landscape and Portrait

At project start, lock release channel, aspect ratio, safe area, subject scale, caption area, and cover crop. When one project needs landscape and portrait versions, share the story, character, scene, prop, voice, and continuity canon, but design and review composition, shot size, movement path, and caption-safe area separately.

Do not default to center-cropping 16:9 into 9:16 or padding 9:16 into 16:9.

## Model Router

Before execution, verify the active surface's parameters, duration, reference limits, audio capability, queue, storage rules, and price. The table is a starting hypothesis, not a permanent ranking, and does not exclude other models.

| Model family | First task to test | Main risk |
|---|---|---|
| Wan 3 long generation | 20–30s multi-beat story blocks, fewer external seams, 720p economy/balanced work | late identity, wardrobe, anatomy, and style drift |
| Seedance 2.5 multimodal | high-value dialogue, reference audio, rich image/video refs, edit, extend, and repair | cost and reference overload |
| Seedance 2.0 | 4–15s dialogue, action, transition, and balanced shots | more external seams in long films |
| Seedance 2.0 Fast | previews, coverage, alternates, and economy tests | final use still requires strict QA |
| MiniMax H3 audiovisual | 4–15s high-motion hero shots, first/last-frame control, and key audiovisual beats | uneconomical for every ordinary shot |

## Content Profiles

| Profile | Required locks |
|---|---|
| Live-action drama | face, hands, age, hair, wardrobe structure, eyelines, axis, performance, relationship knowledge |
| Pet/animal | species anatomy, coat map, eyes, proportions, behavior, contact, and human-animal bond |
| Anthropomorphic/fantasy | body plan, degree of anthropomorphism, power trigger, limit, cost, and consequence |
| Animation/motion comic | design grammar, line, shading, proportions, motion rhythm, and background depth |
| Brand/product narrative | geometry, materials, scale, label-safe plates, compliant claims, and plot function |
| UGC/talking head/interview | speaker, lens grammar, information density, authentic imperfection, movement, and room tone |

## Install

```bash
npx skills add xixihhhh/ai-short-drama-skill --skill dramake
```

Manual install:

```bash
git clone https://github.com/xixihhhh/ai-short-drama-skill.git
cp -R ai-short-drama-skill/skills/dramake ~/.codex/skills/dramake
```

## Example Request

```text
Use Dramake to turn this story into a 90-second live-action family short drama.
Make sure a cold viewer can understand the protagonist's goal, obstacle, choice, and result before storyboarding.
The Douyin version is 9:16 and the landscape version is 16:9. Share characters and voices,
but compose and review each version separately. Offer Economy and Balanced cost routes.
Generate no dependent block until its parent passes narrative, continuity, physics, and audio review.
```

## Quality and Paid Modes

1. **Sketch** — lowest useful preview; validates story and blocking.
2. **Economy** — commonly 720p; prefer long blocks and repair only failed units.
3. **Balanced** — use stronger models, references, and audio where they improve acceptance.
4. **Premium** — rich multimodal control, reference audio, edit/extend, selective higher resolution.
5. **Hero Insert** — focus spend on hook, fragile dialogue, transformation, action, reveal, or climax.
6. **Final Polish** — upscale, repair, grade, and mix accepted media only.

Authorization modes are `plan-only`, `single-test`, `approved-batch`, and `autopilot-with-cap`. The spend ledger tracks quoted cost, actual cost, and `cost_per_accepted_second`.

## Physics, Continuity, and Text Gates

Every contact action must show: `approach → contact → force → object/body response → stable outcome`.

Reject body/object penetration, animal-count changes, extra limbs, impossible support, teleporting props, reversed phone orientation, wardrobe topology changes, unexplained space/time jumps, and unexplained wetness or damage resets.

Video models are unreliable at stable rendered text, phone screens, letters, prices, and countdowns. Default to clean plates or visual evidence and add exact text in post.

## Documentation and Tools

- [Main Chinese Skill](skills/dramake/SKILL.md)
- [English Skill](skills/dramake/SKILL.en.md)
- [Content profiles](skills/dramake/references/en/content-profiles.md)
- [Generation blocks and edit beats](skills/dramake/references/en/generation-blocks-and-edit-beats.md)
- [Directing, camera, movement, and pacing](skills/dramake/references/en/directing-camera-and-pacing.md)
- [Identity, voice, and reference locks](skills/dramake/references/en/identity-voice-and-reference-locks.md)
- [Model router](skills/dramake/references/en/model-router.md)
- [Authorization and batch](skills/dramake/references/en/authorization-and-batch.md)
- [Audio and dubbing](skills/dramake/references/en/audio-and-dubbing.md)
- [Continuity and transitions](skills/dramake/references/en/continuity-and-transitions.md)
- [Physics and failure modes](skills/dramake/references/en/physics-and-failure-modes.md)
- [Anonymized tested observations](benchmarks/tested-observations.en.md)

```bash
python3 scripts/validate_plan.py \
  --continuity skills/dramake/assets/templates/continuity-ledger.csv \
  --block-manifest skills/dramake/assets/templates/block-manifest.csv \
  --shot-plan skills/dramake/assets/templates/shot-plan.csv \
  --voice-bible skills/dramake/assets/templates/voice-bible.csv \
  --audio-continuity skills/dramake/assets/templates/audio-continuity.csv \
  --cost skills/dramake/assets/templates/cost-plan.csv
python3 -m unittest discover -s tests
python3 scripts/check_bilingual.py
```

## Examples

- [Live-action family short drama](examples/live-action-90s/README.en.md)
- [Pet-led standalone short](examples/standalone-90s/README.en.md)
- [Anthology/unit episode](examples/anthology-episode/README.en.md)
- [Serialized short drama](examples/serialized-episode/README.en.md)

Examples are production manifests, not claims that unreviewed generations are finished films.

## License

MIT. See [LICENSE](LICENSE). Dramake is an independent community project.
