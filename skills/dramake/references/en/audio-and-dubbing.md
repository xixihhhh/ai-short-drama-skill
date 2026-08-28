# Audio, Dialogue, and Dubbing

Choose the voice route deliberately. Model-native speech, reference audio, external dubbing, and hybrid post each solve different problems.

## Voice bible

For every recurring speaker record:

- language/accent and pronunciation notes;
- perceived age and gender presentation;
- timbre, pitch range, pace, breathiness, intensity range;
- emotional baseline and allowed extremes;
- an approved 8–20 second clean reference when lawful;
- loudness target and microphone/space character.

Do not share one vague reference across multiple characters.

Assign one `reference_audio_owner` to every voice reference. Store voice identity separately from microphone/room character so a location change is not mistaken for a new character voice and references cannot silently cross-bind speakers.

## Dialogue capacity

Fast social pacing does not mean nonstop words. Fit text to believable speaking duration and leave time for reactions and actions. For a 10–12 second dialogue unit, use 2–3 visual beats and enough lines to fill the performance without turning it into a monologue or a freeze.

Every line prompt should include:

1. speaker;
2. exact line;
3. concurrent physical action;
4. listener reaction;
5. next state after the line.

## Speaker and mouth binding

For every line in a multi-character scene, record `speaker_id`, `source_type` (`visible`, `offscreen`, or `PA`), `visible_mouth_owner`, `non_speaker_mouth_state`, and `turn_order`. Visible dialogue has exactly one mouth owner. Other characters stay closed-mouth, in profile, back-facing, occluded, or out of focus while giving listener reactions. When staff explain a promotion, show that staff member speaking or bind the voice to an explicit visible PA/off-screen source; never let a cat mouth the staff line.

Stage turns as `speaker action → line → closed-mouth listener reaction → next turn`, avoiding simultaneous mouth motion. Wrong-mouth speech, cross-bound voices, an unsourced announcement, or synchronized non-speaker mouths is P0. Regenerate or use a verifiable off-screen/reaction design; captions cannot repair it.

## Model-native speech

Best when native performance and lip sync are reliable. Validate with listening and ASR:

- exact wording and order;
- correct speaker;
- no missing or duplicated tail phrase;
- intended pace/emotion;
- no random generated song covering the voice.

Failed dialogue may be regenerated, shortened, or split into motivated reverse angles.

## Reference audio

Use only when the model/provider supports it and the user has rights. Reference audio should control voice/timing—not accidentally import unrelated BGM or noise. Trim silence and normalize the reference before upload.

## Multi-character reference audio plus native long dialogue

When a reference-driven video model accepts multiple audio references and produces native audio:

- Give every character a separate Voice ID, voice master, and upload cutdown. Never combine two speakers into one reference.
- Bind `Audio 1 → Character A`, `Audio 2 → Character B` in both prompt and asset table, alongside the matching character images.
- Choreograph several dialogue turns in one 20–30-second performance scene rather than one video request per line. Maintain listening, eyelines, prop action, movement, interruption, and reaction between lines.
- Request native audio containing dialogue, Foley, and scene ambience only, with no non-diegetic BGM, singing, or automatic score.
- After generation, verify speaker assignment, voice identity, lip sync, pace, facial performance, action, wording, and repeated tails. A voice reference strengthens control but never replaces acceptance.
- Keep accepted dialogue/Foley, then rebuild one continuous ambience and one coherent score in post instead of concatenating random clip mixes.

If the active endpoint caps total reference-audio duration, retain the longer voice masters and derive short, non-overlapping, information-dense upload samples per character. Treat the current schema as authoritative.

## External dubbing

Use a locked voice sample or consistent TTS/actor session. If exact lip sync is unavailable:

- keep lines off-screen or over reaction/cutaway shots;
- use profile, wide, back-of-head, phone, or masked-mouth framing;
- cut to hands/paws, props, listener, environment, or consequence;
- use a dedicated lip-sync pass where appropriate.

## Voice-over over B-roll

Use when exact narration, localization, or speed matters more than visible lip sync. Keep the speaker off-screen or visually silent and let action, evidence, product use, reactions, or environment carry the image. Do not show a speaking mouth with unrelated narration.

## Audio boundary state

For every block record active speaker, unfinished phrase, room tone, ambience phase, BGM bar/phrase, reverb tail, and the sound or silence that motivates the next cut. Audio continuity is state transfer just like picture continuity.

## Score arc, not per-clip music

Write one film-level functional curve—`hook → build → pressure → turn → release/callback`—before choosing one theme, several stems, or intentional silence. A continuous story normally carries one post-production music bed across visual cuts; retain model-random music only when it is an accepted diegetic source.

For every block record `music_cue_id`, incoming/outgoing bar, energy, density, BPM/key, planned dropouts, dialogue ducking, and J/L behavior. A climax needs contrast rather than maximum loudness throughout. A warm callback may reprise the opening motif with changed orchestration or harmony. A visual cut must not restart music, and background speech needs a locatable source.

## Voice consistency QA

Use ASR first for wording, speaker, order, omissions, and duplicated tails. Then run a human adjacent-clip blind A/B comparison for pace, pitch center/range, timbre, breath, intensity, pronunciation, and emotion. Automated metrics are warnings, not a standalone identity verdict.

## Final mix

Never concatenate generated audio as a finished mix by default. Put clips on separate tracks. Preserve useful dialogue/Foley, reduce or replace random BGM, and build:

- one continuous ambience per scene;
- one intentional music cue or connected score bed;
- J-cuts of roughly 4–6 frames for incoming dialogue/room tone;
- L-cuts for outgoing dialogue/action tails;
- dialogue matching within about ±1 LU for the same voice and ±1.5 LU across voices;
- a platform-appropriate final loudness target, commonly near -16 LUFS with true peak at or below -1 dBTP, adjusted to delivery specs.

Do a blind audio pass: eyes closed, listen for room changes, sudden silence, BGM restarts, clipped first syllables, and duplicated tails.
