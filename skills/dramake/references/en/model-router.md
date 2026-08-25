# Model Router

Route from required capability first, then compare providers, price, queue time, and user preference. Names below describe tested model families; always inspect the current endpoint schema.

| Need | First route to test | Why | Watch for |
|---|---|---|---|
| 20–30s narrative block | Wan 3-class long I2V/R2V | Fewer external joins; native audio options | Late-block identity, anatomy, wardrobe, and style drift |
| Rich image/video/audio referencing | Seedance 2.5-class R2V | Broad multimodal control; edit/extend options | Higher cost and over-constrained references |
| Reference-audio or dialogue repair | Seedance 2.5-class audio-aware route | Voice/timing can be part of generation | Confirm audio-only/mixed-reference rules per provider |
| 4–15s balanced dialogue or transition | Seedance 2.0-class | Shorter controlled multimodal shots | More external joins in long films |
| Cheap tests and alternates | Seedance 2.0 Fast-class | Lower-cost iteration | Do not waive final QA |
| 4–15s hero action or first/last lock | MiniMax H3-class I2V/R2V | Selective high-motion/high-resolution insert | Not economical for every ordinary shot |

As of the 2026-08 documented capability snapshot: Wan 3 supports native 30-second generation plus multimodal/editing routes; Seedance 2.5 supports up to 30 seconds per pass, extension, multimodal references, and timestamp editing; Seedance 2.0 supports 4–15 second native audiovisual generation and a Fast variant; MiniMax H3 supports up to 15 seconds, native stereo sound, and up to 2K. An execution surface may expose only part of the family capability, so the runtime schema remains authoritative.

## Routing questions

1. What duration is natively supported?
2. Can it accept canonical image plus accepted state frame?
3. Is first/last-frame mode mutually exclusive with references?
4. Are image, video, and audio reference roles explicit?
5. Does it generate dialogue/audio, and can music be disabled?
6. Can it return a last frame, edit, extend, or lip-sync?
7. Which resolutions are native versus upscaled?
8. What are current price, queue time, retry policy, and storage terms?

Create one editable [model-card.yaml](../../assets/templates/model-card.yaml) for every available route. Treat the active API/UI as the parameter truth. If duration, resolution, reference limits, pricing, or prompt dialect are unknown, use a conservative profile and do not guess.

## Provider neutrality

The same model may be available through official products, aggregators, APIs, web apps, or MCP servers. Store provider adapters outside the creative manifest. The manifest should request capabilities such as:

```yaml
needs:
  duration_seconds: 30
  aspect_ratio: 9:16
  native_audio: true
  reference_images: 2
  reference_audio: 1
  first_frame: true
  last_frame: false
  edit_or_extend: preferred
```

Then select a currently available endpoint that satisfies it. Never require one vendor in the core skill.

## Tested observations, not guarantees

- In a 2026-08 local project, Wan 3 regular 30-second outputs contained 2–4 internal scene changes and reduced the number of external joins. Prompts still required 4–6 timed beats.
- In the same project, tail-frame chaining improved the next opening but did not prevent later wardrobe or anatomy drift.
- Seedance 2.0-family short clips with native audio still required post-production sound continuity.

For native audiovisual models such as current MiniMax H3 routes, explicitly compile visual timeline, synchronized dialogue/diegetic sound, overall soundscape, and non-diegetic music policy. A reference asset must have one primary controller role such as identity, action, camera, environment, timing, or audio.

Record new evidence in a dated benchmark entry and update routing only after repeated results.
