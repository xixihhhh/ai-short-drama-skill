# Project State

Keep a small set of human-readable source-of-truth files. Adapters and provider payloads are derived outputs, not creative truth.

## Recommended files

- `production-brief.md`: source text, channel, aspect, duration, audience, budget, and rights;
- `story-contract.md`: audience promise, goal, obstacle, choice, result, plant/payoff;
- `character-world-bible.md`: character, voice, location, prop, and style canon;
- `prop-bible.md`: geometry, material, text layers, and state machine for recurring/cross-scene/text props;
- `block-manifest.csv`: scenes, generation blocks, edit beats, model and audio routes;
- `spatial-plan.csv`: location anchors, connectivity, blocking, mirrors, and scale state;
- `story-memory.csv`: series facts, character knowledge, timeline, reveals, and adaptation decisions;
- `continuity-ledger.csv`: accepted visual, audio, and physical state;
- `cost-plan.csv` and `spend-ledger.csv`: dynamic price, authorization, and actual spend;
- `generation-jobs.csv`: request identity, idempotency, polling, recovery, cancellation, and candidate lineage;
- `candidate-scorecard.csv`: hard gates, blind review, usable ranges, and decisions;
- `edit-timeline.csv`: final ranges, tracks, transforms, caption/title layers, and lineage;
- `qa/`: contact sheets, transcripts, timestamped defects, and decisions;
- `accepted/`: canonical shots, tails, stems, and final timeline.

Optional machine-readable ledgers mirror these files for validation. They may not silently override approved creative state.

## Status machine

`planned → ready → generated → reviewed → accepted | repair | rejected`

- `generated` never means approved.
- Only `accepted` or explicit `accepted_with_deviation` media may parent future work.

`ready` means creative and asset prerequisites are satisfied; it is not payment authorization. Track the request separately as `previewed → confirmed → submitted → recovered/completed`. Any material prompt, parameter, reference, or schema change returns `confirmed` to `previewed`. After a submission timeout, recover by request ID or task history before retrying.

Use the separate runtime state machine in [production-operations-and-recovery.md](production-operations-and-recovery.md) for recovery, idempotency, cancellation, and candidate lineage. Creative block state, request state, and timeline-use state cannot substitute for one another.

## Dependency graph and concurrency

Treat blocks as a DAG. Masters, music exploration, voice anchors, continuity-independent inserts, and coverage auditions may run in parallel; a child that needs its parent's observed exit state stays serial. Parallelism follows absence of state edges, not block numbering. Each node records dependencies, unlock condition, spend cap, and failure stop condition.

## Parent-child dependency

A dependent block records `scene_id`, `parent_block_id`, parent `observed_exit_state`, its own `entry_state`, unfinished motion, and transition. Do not replay completed beats or leak future beats.

Continue from accepted state inside one scene. At a location/time boundary, re-anchor from character and scene canon and make the change a motivated transition. Default output-sourced chain depth to 2 and hard-cap it at 3; restart at the cap, at scene boundaries, or on drift.

Complex scenes also maintain spatial anchors and blocking state; serialized work maintains series facts and character knowledge. When a human replaces, trims, or reinterprets a parent, invalidate confirmations, downstream jobs, and timeline events along dependency edges, then resume from the latest still-valid checkpoint.

## Adapter boundary

Provider-specific IDs, URLs, request schemas, and keys live in adapter/runtime files excluded from public examples. Creative manifests express capabilities and approved state. This lets the user change providers without rewriting the story.

## Planned state versus observed state

After media inspection, observed state wins. Update the next block from what actually appears in accepted footage, or regenerate the parent. Never pretend the plan is visible when the output contradicts it.
