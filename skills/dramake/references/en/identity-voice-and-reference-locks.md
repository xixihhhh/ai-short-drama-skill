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
