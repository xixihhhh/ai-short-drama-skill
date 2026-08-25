---
name: pawdirector
description: Create coherent AI pet short videos, cat films, standalone shorts, anthology episodes, or serialized dramas. Use when planning, prompting, generating, reviewing, repairing, dubbing, budgeting, or editing pet-led AI video with models such as Wan 3, Seedance 2.5/2.0/Fast, or MiniMax H3. Especially useful for pet identity consistency, live-action hybrid realism, 15–30 second story blocks, native dialogue, reference audio, continuity, physical realism, cost routing, and avoiding anime drift, static talking heads, jump cuts, broken physics, or fragmented sound.
license: MIT
metadata:
  author: PawDirector contributors
  version: 0.1.0
  category: video-production
  tags: ai-video, pet-video, short-video, short-drama, wan-3, seedance, minimax-h3
---

# PawDirector

Direct AI pet films as productions, not prompt piles. Build a readable story, lock the pet and world, route each block to a suitable model and cost tier, approve real media evidence, then edit with continuous picture and sound.

This skill is provider-neutral. Do not require Atlas Cloud, a particular MCP, or any single website. Use the provider, API, app, or manual workflow available to the user. Confirm current model schemas and prices at execution time.

## Non-negotiable rules

1. Treat the pet as the story engine, not decorative coverage.
2. Make cause and effect understandable with the sound muted.
3. Prefer fewer, longer story blocks when the model supports them, but choreograph internal beats and cuts.
4. Never generate a downstream continuity block from an unreviewed parent clip.
5. Lock identity, material, wardrobe structure, screen direction, props, weather, wetness, light, and audio state.
6. Use real contact, force, weight, support, inertia, friction, and consequences. Reject penetration and impossible anatomy.
7. Keep rendered text, phone UI, letters, prices, and countdowns out of generated footage. Add them in post.
8. Native dialogue may solve lip sync; native music does not solve the final mix. Use one continuous post-production sound bed unless the narrative requires otherwise.
9. A technically clean clip is not a publishable story. Require a cold-viewer comprehension pass.
10. Do not claim to have watched, heard, or approved media without actual inspection evidence.

## Start by choosing the production shape

Choose one primary format for the current deliverable so its pacing can be validated. This does not lock the user into one series strategy, provider, model, or distribution channel; leave those choices open unless the user decides them. Read [format-routing.md](references/format-routing.md) when format is unclear.

- **Standalone microshort, 15–45s:** one hook, one escalating gag/problem, one payoff.
- **Standalone short, 45–120s:** 2–4 story blocks, complete emotional or comic arc.
- **Anthology/unit episode, 1–4 min:** stable pet characters and world rules; each episode resolves its own human or pet problem.
- **Serialized drama, 1–4 min per episode:** episode objective plus season question; continuity persists across episodes.

For pet-first social video, default to 45–120 seconds. Do not inflate a simple premise into 3–4 minutes.

## Gather the production brief

Use [production-brief.md](assets/templates/production-brief.md). Infer safe defaults from supplied assets and conversation. Ask only for choices that materially change output.

Minimum inputs:

- platform, aspect ratio, target duration, audience, and language;
- pet reference assets and permission to use them;
- format and desired emotional flavor;
- available models/providers and approximate budget ceiling;
- dialogue policy: none, model-native, reference-audio, external dubbing, or hybrid;
- visual medium: default `live-action hybrid realism` unless the user explicitly asks for animation.

Never expose API keys, private media URLs, prediction IDs, faces, pet photos, or local paths in a public example.

## Choose quality and spend mode

Open [budget-and-quality.md](references/budget-and-quality.md). Build a cost plan before paid generation. Prices are configuration, never permanent facts.

- **Sketch:** cheapest capable model, low resolution, one candidate; validates story and motion only.
- **Economy:** long blocks to reduce joins, usually 720p, one candidate plus targeted repairs.
- **Balanced:** stronger continuity/audio model for dialogue and transitions; two candidates only for hook, climax, or fragile action.
- **Premium:** richest multimodal references, audio reference/edit/extend where available, selective 1080p or higher output.
- **Hero insert:** spend on a 4–15s high-motion, transformation, macro-paw, or climax shot; keep ordinary coverage economical.
- **Final polish:** upscale and repair accepted takes only. Never pay to upscale rejected footage.

Report estimated request count, expected retries, resolution, duration, and cost range. Separate provider price from creative recommendation.

## Build the story before prompts

Read [story-and-pacing.md](references/story-and-pacing.md). Deliver:

1. one-sentence promise;
2. 0–3s visual hook;
3. pet-specific motivation;
4. visible goal and obstacle;
5. escalation every 4–8 seconds;
6. relationship/state change;
7. payoff or reversal;
8. final pet-instinct button.

For each block, define `entry_state`, 4–6 observable beats, and `exit_state`. A 30-second request is a scene container, not one action stretched for 30 seconds. Include continuous micro-acting: breathing, blinking, eye-lines, paw/ear/tail reactions, prop interaction, and background life.

Reject the script before generation when:

- the cat could be removed without changing the plot;
- motivation appears only in exposition;
- a surprise has no planted setup;
- a character repeats the same point;
- location, time, or objective changes without an on-screen bridge;
- a cold viewer cannot state goal, obstacle, choice, and result.

## Lock pet, style, world, and state

Create a canonical master and [character-bible.md](assets/templates/character-bible.md) for every recurring pet. Record species, sex, coat map, eyes, body proportions, distinctive marks, wardrobe construction, allowed behaviors, forbidden mutations, and voice profile.

For live-action/cute hybrid work:

- write `real photographed cat`, `real fur strands`, `practical fabric`, `real-scale environment`, `live-action full-frame cinema`, and `cinematic practical/VFX integration`;
- express cuteness through timing, paws, ears, tail, scale contrast, curiosity, embarrassment, and real feline behavior;
- prohibit illustration, anime, storybook rendering, children's animation, plastic CGI fur, game assets, dolls, plush toys, chibi bodies, and miniature sets.

Do not use “cartoon style” to request cute acting. It changes the medium. Read [live-action-hybrid-style.md](references/live-action-hybrid-style.md).

Maintain [continuity-ledger.csv](assets/templates/continuity-ledger.csv) as the source of truth. Every accepted block updates it.

## Design blocks and motivated joins

Use 15–30s blocks when the selected model reliably supports them; use shorter blocks for complex dialogue, precision contact, or fragile identity. Never choose duration by habit.

Each long block needs:

- 4–6 time-coded beats;
- one main action per beat;
- 2–5 motivated internal cuts or camera changes when needed;
- stable location/time/axis within the block;
- an active 0.5–0.8s edit handle at the end;
- a clear exit action that the next block can catch.

For every external join:

- use the accepted tail frame as a state anchor when supported;
- also provide the canonical identity/material anchor; tail frames alone propagate drift;
- preserve screen direction and action phase;
- overlap action by roughly 0.3–2s when useful;
- bridge with action, occlusion, whip, foreground pass, sound, glance, or matched shape;
- do not change location, action, scale, and direction simultaneously.

Read [continuity-and-transitions.md](references/continuity-and-transitions.md).

## Route by capability, not brand loyalty

Use [model-router.md](references/model-router.md). Re-check the provider's current documentation before submitting.

General routing:

- **Wan 3-class 30s generation:** long narrative blocks, fewer external joins, 720p economy/balanced work, native audio when useful.
- **Seedance 2.5-class multimodal generation:** premium dialogue, multiple image/video/audio references, edit/extend, reference-audio continuity, last-frame workflows.
- **Seedance 2.0:** balanced 4–15s multimodal/dialogue/transition shots.
- **Seedance 2.0 Fast:** previews, coverage, alternate takes, and budget drafts; final use only after strict QA.
- **MiniMax H3-class generation:** short high-motion hero inserts, strong first/last-frame control, high-resolution selective shots.

These are default hypotheses, not permanent model rankings. If a provider exposes different capabilities, route from the actual schema.

## Choose the audio and dialogue route

Read [audio-and-dubbing.md](references/audio-and-dubbing.md). Choose per scene, not globally by fashion.

### No dialogue

Prefer one continuous post BGM and continuous ambience, plus curated Foley. Generated clips should avoid random music.

### Model-native dialogue

Use when lip sync and performance are stronger than external dubbing. Keep lines short, specify speaker, action during speech, reaction after speech, and the next beat. Validate words, speaker assignment, emotion, repeated tails, and pacing with ASR plus human listening.

### Reference-audio dialogue

Create one approved voice anchor per recurring character. Use it only where the selected model supports audio reference. Lock language, pace, age impression, timbre, intensity range, and pronunciation. Do not cross-bind voices between characters.

### External dubbing

Use when dialogue accuracy, translation, casting, or editing flexibility dominates. Generate clean performances first, then use supported lip-sync/audio-driven tools or conceal mismatch with reaction shots, off-screen lines, profile angles, inserts, and motivated cutaways.

### Hybrid

Keep model-native lip-synced hero lines; replace narration, phone voices, off-screen dialogue, music, ambience, and Foley in post.

Across all modes, place each clip on separate tracks. Normalize speech, carry room tone/rain across same-scene cuts, use J/L cuts, duck BGM, and avoid hard audio restarts at every visual join.

## Generate in gated order

1. Approve story and block plan.
2. Approve canonical pet/style/world references.
3. Generate the hook block or highest-risk block first.
4. Download and inspect the real output.
5. Make a 12-frame contact sheet for a 30s block; inspect start, 25%, 50%, 75%, and end at minimum.
6. Inspect contact peaks and physics at slow speed.
7. Transcribe and listen when audio exists.
8. Mark candidate `accepted`, `repair`, or `rejected` with evidence.
9. Extract an accepted tail frame and update continuity state.
10. Only then unlock the dependent block.

Parallelize independent assets, music exploration, voice anchors, non-dependent inserts, and alternative hooks. Do not parallelize continuity-dependent story blocks before their parent state is accepted.

## Physics and anatomy gate

Read [physics-and-failure-modes.md](references/physics-and-failure-modes.md).

Before generation, list visible `physical_contact_points`. Use feline action primitives: walk, run, crouch, jump, paw, bat, bite, push with head/body, knead, balance with tail. Rewrite adult-like carrying, prolonged upright posture, or precision handwork.

Required visible order:

`approach → contact → force → object/body response → stable outcome`

Reject any clip with body/object penetration, extra or missing animals, impossible support, teleporting props, reversed phone orientation, clothing topology changes, unexplained resets, or unreadable physical cause.

## QA, repair, and edit

Use [qa-report.md](assets/templates/qa-report.md) and [qa-and-repair.md](references/qa-and-repair.md).

Run four separate gates:

1. **Narrative:** cold viewer can retell goal → obstacle → choice/action → outcome.
2. **Identity/style:** pet, clothing, materials, and medium remain canonical.
3. **Physics/continuity:** contacts, direction, state, and joins are plausible.
4. **Audio:** dialogue, loudness, ambience, BGM, and bridges are continuous.

Repair the smallest failing unit. Use edit/extend when capable, bridge shots when the join is the problem, and regeneration when identity, anatomy, or story causality is broken. Do not hide a narrative failure with music.

## Required deliverables

Return or save:

- production brief and selected format;
- character/style/world bibles;
- beat sheet and block manifest;
- provider-neutral model and audio route;
- budget/candidate plan;
- prompts with time-coded beats and negative constraints;
- continuity ledger;
- per-candidate evidence and QA status;
- accepted-takes list and tail frames;
- audio mix map;
- final cold-viewer report;
- publication metadata and cover plan, with text added in post unless a reliable image model is explicitly used.

Name outputs consistently: `BLOCK_ID_vN.mp4`, `_tail.png`, `_contact_12.jpg`, `_audio.wav`, and `_QA.md`.

## Evidence boundaries

In project documentation, distinguish:

- **documented capability:** verified from current official/provider schema;
- **observed result:** seen in a specific model/provider/date/config;
- **creative preference:** chosen for this story;
- **inference:** likely, but not directly verified.

Do not present dynamic pricing, duration limits, or comparative quality as timeless facts.
