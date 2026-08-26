# Identity, Voice, and Reference Locks

Consistency does not come from adding more references. Give each controlled dimension one authoritative source and update transient state only after acceptance.

## Two state layers

- **Canonical:** face/coat map, proportions, wardrobe construction, product geometry, persistent props, location layout, voice identity, directorial voice.
- **Transient:** pose, action phase, frame position, wetness/injury, prop orientation, emotion, audio phase, unfinished motion.

Canon controls who/what the subject is; accepted parent media controls its current state.

## Reference-authority matrix

Give every asset one primary role: identity, first frame, last frame, product, environment, motion, camera, timing, audio, or style. Every target dimension has one winning asset and explicit exclusions. Drop any asset that controls nothing.

Do not infer authority from upload order, filename, or media type. Resolve conflict by user must-have → identity/product canon → accepted transient state → scene/style reference → inference.

## Visual identity lock

Record identity ID and master media; face/eyes/hair/coat map/proportions/scale; wardrobe coverage, material, closures, seams, and accessory count; handedness or species-appropriate action; allowed folds/wetness/dirt/emotion; forbidden face, coat, limb-count, wardrobe-topology, or product-geometry changes.

Every block uses canon plus current accepted state. A tail frame alone propagates drift.

## Performance canon

For cute-animal, comedy, and animated-performance characters, also lock `performance_mode`, degree of anthropomorphism, signature stance, eyeline rules, ear/tail/eye/paw expression library, anticipation, overshoot/settle, permitted squash/stretch range, and forbidden human anatomy or prop capability. Create at least five pose/expression masters: `neutral → expectant/confident → surprised/out of control → embarrassed/covering → triumphant/callback`. Downstream shots may amplify performance but cannot randomly fall back to ordinary pet behavior or switch to fully animated materials.

For every featured gag, record what the protagonist can see, what occludes it, when the partner sees it, and who reacts first. Eyeline and information advantage are transient character state and must transfer across shots like wardrobe and props.

## Recurring props and text masters

Before storyboarding, inventory every prop that appears more than once, crosses scenes, drives a key action, or carries text/logo. Create a [prop-bible.md](../../assets/templates/en/prop-bible.md) and unique `prop_id`. Use a user-selected, validated high-fidelity image model—such as a GPT Image-class generation/editing route—to make neutral-light, low-distortion front/back/side/top/three-quarter masters. Lock scale, geometry, part count, material, color, attachments, and allowed states. A scale, stamp, phone, package, helmet, tool, or key must not be redesigned in each scene.

Give text-bearing props two authorities: prop geometry canon controls shape, motion, occlusion, and light; `text_plate_id` controls exact copy, numbers, logo, font, and layout. Save exact text as a transparent PNG/vector and track-composite it in post by default instead of asking the video model to redraw it every frame. Even when an image model renders text reliably, approve one static text master first and use it as a texture or post layer—never let downstream shots rewrite it freely.

At every appearance, record `prop_id + state_id + text_plate_id`, owner, orientation, open/attached state, intact/damaged state, wetness/dirt, and the only intended change from the previous state. Compare start, action peak, and end against authoritative views. A drifted prop cannot become the next reference.

## Voice lock

For each recurring speaker, separately store:

- `voice_id` and a rights-cleared 8–20s clean anchor;
- language, accent, pronunciation list, perceived age/gender presentation;
- timbre, pitch center/range, pace, breath, intensity range;
- emotional baseline and allowed variation;
- microphone/room character, separate from voice identity;
- other characters that must never share the reference.

Remove silence, noise, and music from reference audio and normalize it. If the model cannot reference voices, prefer one consistent external dubbing route over random native voices per clip.

## Voice consistency QA

Across clips, compare ASR words/speaker/order, words or syllables per second, pitch center/range, breath and intensity, loudness/reverb/mic distance, pronunciation of names, and human blind A/B identity. Automated metrics are warnings, not the final identity decision.

## Drift response

Locate the first drift timestamp and preserve only earlier accepted ranges. Edit a local defect; re-anchor from canon and shorten the block for systematic drift. Drifted media cannot become a child source.
