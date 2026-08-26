# Generation Blocks and Edit Beats

Dramake uses two timescales to avoid both extremes: hundreds of disconnected micro-clips and one vague full-scene prompt.

## Generation block

A provider request and continuity container, typically 8–30 seconds depending on model capability and scene risk. It owns:

- one location/time/axis envelope;
- accepted entry and exit state;
- canonical references and model route;
- audio-in/audio-out state;
- 3–6 internal edit beats;
- candidate, cost, and QA status.

## Edit beat

A 2–8 second unit in which the audience gains one thing: action, reaction, information, relationship change, joke, reveal, or transition. It owns:

- visible subject/action;
- camera size/angle/movement;
- dialogue or sound event;
- contact and resulting state;
- motivation for the next beat.

The model may produce internal cuts, or the editor may cut within an accepted long output. The beat plan gives those cuts meaning.

## When to use long blocks

Use 15–30 seconds when location, cast, style, and action can remain inside one continuity envelope and the model reliably supports time-coded multi-beat performance. Benefits: fewer paid requests and fewer external seams.

Risks: late identity/style drift, anatomy accumulation, uncontrolled internal cuts, repeated dialogue, and a weak tail. Inspect the whole block, not only start/end.

Enforce an event-load budget in long blocks: prefer one primary prop system, one high-risk physical chain, and one main comic/emotional payoff. A block may contain 4–6 internal beats, but should not combine several changing food identities, many speaker turns, precision tong work, a fall, a location change, and multiple prop-state mutations. When over budget, split setup, peak, and consequence blocks, using each accepted end state as the next entry state.

## When to shorten

Use 4–15 seconds for:

- exact dialogue or fragile lip sync;
- precision hand/object/animal contact;
- high-motion hero action;
- transformation or crowded interaction;
- scene/location changes;
- a block that repeatedly drifts after a known time.

## Editorial duration versus generation duration

The requested duration is not automatically the timeline duration. A 30-second output may contribute several accepted subranges; a 10-second generation may be cut to 4 seconds. Record `generated_duration`, `accepted_ranges`, and `edit_duration` separately.

Never fill extra model duration with frozen actors. Add purposeful micro-actions and reactions, or generate a shorter block.

For comedy, also record `macro_goal_id`, `macro_causal_contribution`, `event_load_budget`, `comedy_contract_ids`, and `performance_states`. Time-code the normal state, visible cause, protagonist eyeline, audience-visible information, partner/background reaction, reveal, and result hold. Do not rely on labels such as “funny” or “food flies onto the head.”
