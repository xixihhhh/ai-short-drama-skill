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

## Dialogue capacity

Fast social pacing does not mean nonstop words. Fit text to believable speaking duration and leave time for reactions and actions. For a 10–12 second dialogue unit, use 2–3 visual beats and enough lines to fill the performance without turning it into a monologue or a freeze.

Every line prompt should include:

1. speaker;
2. exact line;
3. concurrent physical action;
4. listener reaction;
5. next state after the line.

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

## External dubbing

Use a locked voice sample or consistent TTS/actor session. If exact lip sync is unavailable:

- keep lines off-screen or over reaction/cutaway shots;
- use profile, wide, back-of-head, phone, or masked-mouth framing;
- cut to paws, props, listener, environment, or consequence;
- use a dedicated lip-sync pass where appropriate.

## Final mix

Never concatenate generated audio as a finished mix by default. Put clips on separate tracks. Preserve useful dialogue/Foley, reduce or replace random BGM, and build:

- one continuous ambience per scene;
- one intentional music cue or connected score bed;
- J-cuts of roughly 4–6 frames for incoming dialogue/room tone;
- L-cuts for outgoing dialogue/action tails;
- dialogue matching within about ±1 LU for the same voice and ±1.5 LU across voices;
- a platform-appropriate final loudness target, commonly near -16 LUFS with true peak at or below -1 dBTP, adjusted to delivery specs.

Do a blind audio pass: eyes closed, listen for room changes, sudden silence, BGM restarts, clipped first syllables, and duplicated tails.
