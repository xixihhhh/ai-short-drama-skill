# Budget and Quality Modes

Do not hardcode provider prices in the skill. Put current prices into a project cost file and label currency, billing unit, provider, model, date checked, and whether resolution/duration changes price.

## Modes

### Sketch

- Purpose: test hook, blocking, and premise.
- Resolution: lowest useful preview, normally 480p or 720p.
- Candidates: one per independent block.
- Audio: scratch only.
- Stop rule: do not polish a weak story.

### Economy

- Purpose: publishable simple short with controlled retries.
- Prefer long blocks when reliable to minimize paid joins.
- Default 720p; one candidate, plus selective rerender of failed blocks.
- Allocate extra retry budget to identity-critical shots, dialogue, contact-heavy action, the hook, reveal, and climax.

### Balanced

- Purpose: stronger performance, dialogue, and continuity.
- Use capable multimodal/reference models where they materially help.
- Two candidates only for hook, reveal, climax, or high-risk physics.
- Keep ordinary reaction/bridge coverage economical.

### Premium

- Purpose: dialogue-heavy, branded, or high-value episode.
- Use reference audio, edit/extend, last-frame return, richer references, and selective 1080p/higher output where available.
- Require audio stems or a deliberate replacement plan.

### Hero Insert

- Purpose: 4–15s transformation, high-speed action, fragile dialogue, creature/product detail, emotional close-up, or spectacular reveal.
- Route to the best short high-control model rather than upgrading the whole film.

### Final Polish

- Upscale, denoise, stabilize, color, mix, caption, and encode accepted media only.
- Fix a join with a bridge or local edit before regenerating unrelated blocks.

## Cost plan formula

For each route calculate:

`expected_cost = blocks × candidates × unit_price + expected_repairs × repair_price + post_cost`

Use a retry factor based on risk:

- simple reaction: 1.1–1.3;
- dialogue/performance: 1.3–1.8;
- contact-heavy action or transformation: 1.8–3.0.

Report best case, expected case, and capped case. Require user confirmation only when crossing their stated spend ceiling or causing a material external charge.
