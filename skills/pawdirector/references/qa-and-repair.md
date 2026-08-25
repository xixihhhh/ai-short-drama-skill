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

## Severity

- **P0:** story incomprehensible, wrong identity, severe anatomy/penetration, missing required action/dialogue, privacy/safety problem. Reject or regenerate.
- **P1:** visible continuity/style/audio failure that harms viewing. Repair or bridge before final.
- **P2:** polish issue. Fix in edit when possible.

## Repair decision

- wrong story cause/effect: rewrite/regenerate;
- bad identity/anatomy across much of clip: regenerate from canonical anchor;
- localized object/wardrobe defect: edit/inpaint if supported;
- abrupt external join: bridge shot, matched action, or extend parent/child;
- dialogue text wrong but mouth usable: regenerate/lip-sync; do not merely subtitle contradictory speech;
- random music or loudness jump: separate/replace/mix in post;
- late-block drift: shorten accepted region, re-anchor, and generate the remainder;
- static unused duration: add purposeful beats and regenerate; camera movement alone is not a fix.

## Final viewing passes

1. Silent: can a cold viewer follow the physical story?
2. Normal: are motivation and emotion clear without reading a synopsis?
3. Eyes closed: does audio feel like one film?
4. Frame-step: do contacts, phones, props, wardrobe, and identities hold?
5. Mobile speaker: are first words and quiet reactions audible?

Technical approval never overrides cold-viewer failure.
