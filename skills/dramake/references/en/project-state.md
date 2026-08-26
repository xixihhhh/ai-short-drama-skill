# Project State

Keep a small set of human-readable source-of-truth files. Adapters and provider payloads are derived outputs, not creative truth.

## Recommended files

- `production-brief.md`: source text, channel, aspect, duration, audience, budget, and rights;
- `story-contract.md`: audience promise, goal, obstacle, choice, result, plant/payoff;
- `character-world-bible.md`: character, voice, location, prop, and style canon;
- `prop-bible.md`: geometry, material, text layers, and state machine for recurring/cross-scene/text props;
- `block-manifest.csv`: scenes, generation blocks, edit beats, model and audio routes;
- `continuity-ledger.csv`: accepted visual, audio, and physical state;
- `cost-plan.csv` and `spend-ledger.csv`: dynamic price, authorization, and actual spend;
- `qa/`: contact sheets, transcripts, timestamped defects, and decisions;
- `accepted/`: canonical shots, tails, stems, and final timeline.

Optional machine-readable ledgers mirror these files for validation. They may not silently override approved creative state.

## Status machine

`planned → ready → generated → reviewed → accepted | repair | rejected`

- `generated` never means approved.
- Only `accepted` or explicit `accepted_with_deviation` media may parent future work.

## Parent-child dependency

A dependent block records `scene_id`, `parent_block_id`, parent `observed_exit_state`, its own `entry_state`, unfinished motion, and transition. Do not replay completed beats or leak future beats.

Continue from accepted state inside one scene. At a location/time boundary, re-anchor from character and scene canon and make the change a motivated transition. Default output-sourced chain depth to 2 and hard-cap it at 3; restart at the cap, at scene boundaries, or on drift.

## Adapter boundary

Provider-specific IDs, URLs, request schemas, and keys live in adapter/runtime files excluded from public examples. Creative manifests express capabilities and approved state. This lets the user change providers without rewriting the story.

## Planned state versus observed state

After media inspection, observed state wins. Update the next block from what actually appears in accepted footage, or regenerate the parent. Never pretend the plan is visible when the output contradicts it.
