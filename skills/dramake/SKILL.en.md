---
name: dramake
description: For Codex, Claude Code, WorkBuddy, and other Agent Skills clients, turn an idea, story outline, manuscript, copy, screenplay, storyboard, or existing media into a coherent, publishable AI short drama or short film. Use for landscape or portrait content on Douyin, Hongguo Short Drama, WeChat Channels, Kuaishou, Bilibili, YouTube, and other channels; live action, standalone shorts, anthology episodes, serialized drama, pets, anthropomorphic fantasy, animation/motion comics, UGC, and branded narratives. Covers story diagnosis, scripting, storyboarding, character and recurring-prop consistency, Wan 3, Seedance 2.5/2.0/Fast, MiniMax H3, 15–30 second blocks, native dialogue, reference audio, dubbing, spend control, continuity editing, physical QA, and cold-viewer review. Especially useful for avoiding clip piles, random jumps, static talking heads, identity/wardrobe/prop drift, malformed text, wrong motion direction, penetration, flat observational camera, voice drift, music restarts, and confusing plots.
license: MIT
metadata:
  author: Dramake contributors
  version: 0.3.3
  category: video-production
  tags: ai-video, text-to-video, short-drama, codex, claude-code, workbuddy, douyin, hongguo-drama, wan-3, seedance, minimax-h3
---

# Dramake

Treat short-drama creation as one connected production line, not a prompt pile. A beginner can start with a paragraph and receive story, script, storyboard, generation, dubbing, editing, and QA guidance behind explicit gates. An expert can take control at any stage.

This skill does not require one execution platform, website, API, or MCP. Use models and channels the user can lawfully access and wants to use. Confirm current schemas, prices, upload rules, and retention terms at execution time.

Use [project-state.md](references/en/project-state.md) as the single production state machine. Provider payloads, model prompts, and timelines are derived from approved creative state and inspected media.

## Non-negotiable rules

1. Give every protagonist a causal role. A human, animal, creature, product, or object protagonist must change the outcome, not decorate coverage.
2. Make cause and effect understandable with the sound muted.
3. Prefer fewer, longer story blocks when the model supports them, but choreograph internal beats and cuts.
4. Never generate a downstream continuity block from an unreviewed parent clip.
5. Lock identity, material, wardrobe structure, screen direction, props, weather, wetness, light, and audio state.
6. Use real contact, force, weight, support, inertia, friction, and consequences. Reject penetration and impossible anatomy.
7. Keep rendered text, phone UI, letters, prices, and countdowns out of generated footage. Add them in post.
8. Native dialogue may solve lip sync; native music does not solve the final mix. Build a continuous, centrally managed post-production sound system with scene ambience, intentional cues/score, and motivated bridges.
9. A technically clean clip is not a publishable story. Require a cold-viewer comprehension pass.
10. Do not claim to have watched, heard, or approved media without actual inspection evidence.

## Start from what the user already has

Do not require beginners to know production vocabulary. Route by input depth:

- **one-line idea:** offer 2–3 filmable directions and supply protagonist, desire, obstacle, escalation, and outcome;
- **story/manuscript/copy:** extract characters, relationships, timeline, props, secrets, reversals, and visible actions;
- **screenplay:** check causality, setup, reversals, dialogue density, locations, and running time;
- **storyboard/prompts:** check beats, continuity, physics, rendered-text risk, and model feasibility;
- **existing media/rough cut:** inspect picture and sound, locate the smallest failing unit, and do not restart without cause.

Then choose task depth:

- **inspect/advice:** analyze without generation or spend;
- **quick repair:** fix the smallest script, prompt, shot, join, voice, or mix unit;
- **production package:** create briefs, bibles, manifests, prompts, costs, and edit guidance;
- **execute/resume:** continue only from current accepted state;
- **full production:** run from source text through final review.

Do not force a local repair through the complete workflow.

## Choose the production shape and aspect ratio

Choose one primary format for the current deliverable so its pacing can be validated. This does not lock the user into one series strategy, provider, model, or distribution channel; leave those choices open unless the user decides them. Read [format-routing.md](references/en/format-routing.md) when format is unclear.

- **Standalone microshort, 15–45s:** one hook, one escalating gag/problem, one payoff.
- **Standalone short, 45–120s:** 2–4 story blocks, complete emotional or comic arc.
- **Anthology/unit episode, 1–4 min:** stable characters and world rules; each episode resolves its own problem.
- **Serialized drama, 1–4 min per episode:** episode objective plus season question; continuity persists across episodes.

For social video, default to the shortest duration that supports setup, escalation, and payoff. Do not inflate a simple premise into 3–4 minutes.

Support `9:16`, `16:9`, `1:1`, and custom ratios. Record release channel, subject-safe area, caption area, cover crop, and delivery codec. For landscape and portrait versions, share story, cast, voices, props, and continuity canon but design and review composition, shot size, motion path, and safe areas separately. Do not default to center-cropping or mechanical padding.

## Gather the production brief

Use [production-brief.md](assets/templates/en/production-brief.md). Infer safe defaults from supplied assets and conversation. Ask only for choices that materially change output.

Minimum inputs:

- source text and adaptation boundaries;
- platform, aspect ratio, target duration, audience, and language;
- character, creature, product, location, or style reference assets and permission to use them;
- format and desired emotional flavor;
- available models/providers and approximate budget ceiling;
- dialogue policy: none, model-native, reference-audio, external dubbing, or hybrid;
- content profile and visual medium; do not default every project to live action or animation.

Never expose API keys, private media URLs, prediction IDs, faces, reference photos, voices, or local paths in a public example.

## Choose quality and spend mode

Open [budget-and-quality.md](references/en/budget-and-quality.md). Build a cost plan before paid generation. Prices are configuration, never permanent facts.

- **Sketch:** cheapest capable model, low resolution, one candidate; validates story and motion only.
- **Economy:** long blocks to reduce joins, usually 720p, one candidate plus targeted repairs.
- **Balanced:** stronger continuity/audio model for dialogue and transitions; two candidates only for hook, climax, or fragile action.
- **Premium:** richest multimodal references, audio reference/edit/extend where available, selective 1080p or higher output.
- **Hero insert:** spend on a 4–15s high-motion, transformation, emotional close-up, product reveal, creature detail, or climax shot; keep ordinary coverage economical.
- **Final polish:** upscale and repair accepted takes only. Never pay to upscale rejected footage.

Report estimated request count, expected retries, resolution, duration, and cost range. Separate provider price from creative recommendation.

Separately choose a spend-authorization mode from [authorization-and-batch.md](references/en/authorization-and-batch.md): `plan-only`, `single-test`, `approved-batch`, or `autopilot-with-cap`. A quality tier never implies permission to spend. If the user has pre-authorized a provider, upload policy, budget cap, and retry cap, do not ask for confirmation on every request; stop only at the defined boundary.

## Build the story before prompts

Read [story-and-pacing.md](references/en/story-and-pacing.md) and [directing-camera-and-pacing.md](references/en/directing-camera-and-pacing.md). Deliver:

1. one-sentence promise;
2. 0–3s visual hook;
3. protagonist-specific motivation;
4. visible goal and obstacle;
5. escalation every 4–8 seconds;
6. relationship/state change;
7. payoff or reversal;
8. a final emotional, comic, suspense, visual, or character-specific button.

For every scene, define one `directorial_intention`, a visible `value_before → value_after` turn, POV, power shift, subtext, and a filmable carrier. Camera, light, blocking, performance, sound, and cut must serve that same intention. “Cinematic” is not an intention.

For each block, define `entry_state`, observable beats, and `exit_state`. Use 4–6 beats for a 20–30 second long block, 2–3 beats for a 10–12 second dialogue block, and evidence-based density for other short blocks. A long request is a scene container, not one action stretched across its duration. Include continuous micro-acting: breathing, blinking, eye-lines, facial or species-appropriate reactions, prop interaction, and background life.

For a 60–120-second high-density Douyin narrative, enable the dedicated preset: visible conflict within 3 seconds, an immediate objective understood within 10 seconds, 18–24 effective beats per 90 seconds as a baseline, and one closed micro-task every 15–25 seconds. A roughly 30-second continuously voiced scene carries multiple advancing dialogue turns and 4–7 visible actions/reactions. Keep one macro goal across the film and causally bridge every scene change. Effective beats do not equal cuts or generation requests; never regress into a pile of fragments.

Reject the script before generation when:

- the stated protagonist could be removed without changing the plot;
- motivation appears only in exposition;
- a surprise has no planted setup;
- a character repeats the same point;
- location, time, or objective changes without an on-screen bridge;
- a cold viewer cannot state goal, obstacle, choice, and result.

## Select a content profile, then lock character, style, world, and state

Read [content-profiles.md](references/en/content-profiles.md). Select one primary profile and any necessary specialist overlay; profiles change constraints, not the core continuity workflow.

Create a canonical master and [character-bible.md](assets/templates/en/character-bible.md) for every recurring character or creature. Record identity, anatomy, face/body proportions, distinctive marks, wardrobe construction, allowed behaviors, forbidden mutations, and voice profile. Use [identity-voice-and-reference-locks.md](references/en/identity-voice-and-reference-locks.md) so each controlled dimension has exactly one authoritative reference and each recurring speaker has an independent voice anchor.

Before storyboarding, inventory every recurring, cross-scene, plot-critical, or text/logo-bearing prop and create a [prop-bible.md](assets/templates/en/prop-bible.md). First use a user-selected, validated high-fidelity image generation/editing route—including GPT Image-class models when chosen—to lock neutral-light multi-view geometry, scale, material, attachments, and states. Give exact copy a separate `text_plate_id` and track-composite it in post by default. Every shot references the same `prop_id + state_id + text_plate_id`; a scale, stamp, helmet, phone, or package cannot be redesigned across scenes.

For live-action work, anchor photography, real materials, practical wardrobe, real-scale environments, motivated lighting, and physically integrated VFX. For animation, explicitly lock the chosen design grammar, line/shading system, proportions, and motion language instead of applying live-action negatives.

For live-action/cute animal hybrids, put cuteness into performance and species behavior—not animated-render vocabulary. Read [style-and-medium-locks.md](references/en/style-and-medium-locks.md).

Maintain [continuity-ledger.csv](assets/templates/continuity-ledger.csv) as the source of truth. Every accepted block updates it.

## Design blocks and motivated joins

Use 15–30s blocks when the selected model reliably supports them; use shorter blocks for complex dialogue, precision contact, or fragile identity. Never choose duration by habit.

Use the dual-timescale plan in [generation-blocks-and-edit-beats.md](references/en/generation-blocks-and-edit-beats.md): a `generation_block` is the model request and continuity container, while an `edit_beat` is the 2–8 second unit of story information, performance, camera, and final cutting. Do not confuse “fewer model requests” with “fewer story beats.”

Each long block needs:

- 4–6 time-coded beats;
- one main action per beat;
- 2–5 motivated internal cuts or camera changes when needed;
- stable location/time/axis within the block;
- recurring-prop `prop_id/state_id/text_plate_id` plus the one allowed change;
- precise physical-event start, control input, world/screen vectors, phase sequence, and end state;
- one `impact_role` and visible consequence when a hook/collision/reveal/climax needs a sensory peak;
- an active 0.5–0.8s edit handle at the end;
- a clear exit action that the next block can catch.

Use one primary camera move per internal shot. Record `camera_start`, `camera_path`, `camera_motivation`, `camera_end`, and `subject_endpoint`. As a conservative starting budget, allow roughly 4–6 seconds per internal shot: about 2 shots in 10 seconds, 2–3 in 12–15 seconds, and 2–5 shots or one phased long take in 20–30 seconds. Validate and adjust for the active model/surface.

For every external join:

- use the accepted tail frame as a state anchor when supported;
- also provide the canonical identity/material anchor; tail frames alone propagate drift;
- preserve screen direction and action phase;
- overlap action by roughly 0.3–2s when useful;
- bridge with action, occlusion, whip, foreground pass, sound, glance, or matched shape;
- do not change location, action, scale, and direction simultaneously.

Read [continuity-and-transitions.md](references/en/continuity-and-transitions.md).

Treat a new location, time, or core spatial relationship as a scene boundary. Re-anchor from character/world canon rather than calling it seamless continuation. Default output-sourced chain depth to 2 and relax only after repeated active-route validation.

## Route by capability, not brand loyalty

Use [model-router.md](references/en/model-router.md). Re-check the provider's current documentation before submitting.

General routing:

- **Wan 3-class 30s generation:** long narrative blocks, reference-driven multi-character native dialogue, fewer external joins, and 720p economy/balanced work. Choose mixed R2V or strict frame locking—not both—and check character/voice binding plus late-block drift.
- **Seedance 2.5-class multimodal generation:** premium dialogue, multiple image/video/audio references, edit/extend, reference-audio continuity, last-frame workflows.
- **Seedance 2.0:** balanced 4–15s multimodal/dialogue/transition shots.
- **Seedance 2.0 Fast:** previews, coverage, alternate takes, and budget drafts; final use only after strict QA.
- **MiniMax H3-class generation:** short high-motion hero inserts, strong first/last-frame control, high-resolution selective shots.

These are default hypotheses, not permanent model rankings. If a provider exposes different capabilities, route from the actual schema.

## Choose the audio and dialogue route

Read [audio-and-dubbing.md](references/en/audio-and-dubbing.md). Choose per scene, not globally by fashion.

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
2. Approve canonical character/style/world/prop references.
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

Read [physics-and-failure-modes.md](references/en/physics-and-failure-modes.md).

Before generation, list visible `physical_contact_points`. Use anatomy-appropriate action primitives for the subject. Human hands, animal paws, machines, liquids, fabric, vehicles, and magical effects need different contact and motion rules. Rewrite actions that exceed the subject's anatomy or the shot's complexity budget.

Required visible order:

`approach → contact → force → object/body response → stable outcome`

Compile “reverse, turn, detach, collide” into `physical_start_state → control_input → world/screen motion vectors → phase_sequence → physical_end_state`. Give one generation block only one high-risk precision event; split complex events into setup, peak, and consequence shots. A correct written intention with wrong observed movement is still a rejection.

Reject any clip with body/object penetration, extra or missing animals, impossible support, teleporting props, reversed phone orientation, clothing topology changes, unexplained resets, or unreadable physical cause.

## QA, repair, and edit

Use [qa-report.md](assets/templates/en/qa-report.md) and [qa-and-repair.md](references/en/qa-and-repair.md).

Run four separate gates:

1. **Narrative:** cold viewer can retell goal → obstacle → choice/action → outcome.
2. **Identity/style:** characters, creatures, products, clothing, materials, and medium remain canonical.
3. **Physics/continuity:** contacts, direction, state, and joins are plausible.
4. **Audio:** dialogue, loudness, ambience, BGM, and bridges are continuous.

Repair the smallest failing unit. Use edit/extend when capable, bridge shots when the join is the problem, and regeneration when identity, anatomy, or story causality is broken. Do not hide a narrative failure with music.

## Required deliverables

Return or save:

- production brief and selected format;
- character/style/world bibles;
- recurring prop bibles, exact-text plates, and prop state machines;
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
