# QA and Repair

## Evidence pack per candidate

- original output file;
- metadata probe;
- 12-frame contact sheet for a 30s clip;
- start/25/50/75/end frames;
- slow-motion review notes for contact peaks;
- audio extraction and ASR when dialogue exists;
- QA report with timestamps;
- accepted tail frame only after approval.

## Four gates and severity

1. **Narrative:** a cold viewer can state goal, obstacle, action/choice, result, and protagonist role.
2. **Identity/style:** face, body, animal count, coat, product, wardrobe topology, material, and medium match canon.
3. **Physics/continuity:** contact, force, response, axis, direction, props, state, and joins are credible.
4. **Audio:** line, speaker, voice, lip sync, loudness, ambience, music, and bridges remain coherent.

Comedy, cute-animal, and animated-performance work adds two gates:

5. **Gag legibility:** muted viewing still exposes the normal state, visible cause, audience advantage, character misread, reaction hold, reveal, and macro consequence.
6. **Performance:** a 15–30 second block has at least three distinguishable states; action includes anticipation, peak, reaction, and settle; background reaction follows the cause.

Treat a gag that works only because dialogue says “where is my food,” because a crowd suddenly laughs, or because the viewer must guess the object path/occlusion as a P0 story/performance failure. Staff dialogue mouthed by a cat, simultaneous speaker mouths, or an announcement without a source is also P0.

- **P0:** story incomprehensible, wrong identity, severe anatomy/penetration, missing required action/dialogue, privacy/safety problem. Reject or regenerate.
- **P1:** visible continuity/style/audio failure that harms viewing. Repair or bridge before final.
- **P2:** polish issue. Fix in edit when possible.

Common mappings:

- closed-glass/body penetration: P0;
- extra finger or broken anatomy in a key contact/performance frame: normally P0;
- wardrobe topology change: P1, upgraded to P0 when identity becomes ambiguous;
- unexplained phone side/hand flip: normally P1;
- mutating generated label/text: P1, upgraded to P0 for brand, legal, safety, or story-critical information;
- malformed complex text that should have been a post overlay: reject that plate and rebuild it post-safe.

## Five decisions

Every take ends in exactly one production disposition:

1. keep;
2. fix in post;
3. local model edit/extend;
4. reroll with the same brief;
5. rewrite the brief, asset, or scene.

- wrong story cause/effect: rewrite/regenerate;
- bad identity/anatomy across much of clip: regenerate from canonical anchor;
- localized object/wardrobe defect: edit/inpaint if supported;
- abrupt external join: bridge shot, matched action, or extend parent/child;
- dialogue text wrong but mouth usable: regenerate/lip-sync; do not merely subtitle contradictory speech;
- random music or loudness jump: separate/replace/mix in post;
- late-block drift: shorten accepted region, re-anchor, and generate the remainder;
- static unused duration: add purposeful beats and regenerate; camera movement alone is not a fix.

## One variable and attempt budget

Change one causal variable per retry whenever possible. Define the maximum candidate/retry count and good-enough threshold before the first paid request. If the same defect appears twice under essentially the same route, treat it as systematic: switch mode/model, shorten the block, redesign the action, improve the anchor, or move the fix to post. Allow at most 2–3 same-brief rerolls before rewriting; do not burn the remaining cap on identical rerolls.

## Final viewing passes

1. Silent: can a cold viewer follow the physical story?
2. Normal: are motivation and emotion clear without reading a synopsis?
3. Eyes closed: does audio feel like one film?
4. Frame-step: do contacts, phones, props, wardrobe, and identities hold?
5. Mobile speaker: are first words and quiet reactions audible?

Technical approval never overrides cold-viewer failure.

For comedy also ask: what visible action caused the event, what does the audience know that the character does not, on which frame does the reveal land, and how does the gag advance the major reversal? If these cannot be answered, rewrite the gag contract before rerolling.
