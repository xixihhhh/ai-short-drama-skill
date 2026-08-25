# Project State and Canon Promotion

Keep a small set of human-readable source-of-truth files. Adapters and provider payloads are derived outputs, not creative truth.

Recommended core:

1. `brief.md` — audience, format, story promise, rights, medium, budget and authorization;
2. `story.md` — causal chain, character knowledge, emotional curve, episode/season state;
3. `bibles.md` — characters, voices, world, locations, props, style and forbidden changes;
4. `blocks.md` — generation blocks, internal edit beats, dependencies, model capability needs;
5. `review.md` — candidate evidence, accepted ranges, observed exit states, repairs and cold-viewer results.

Optional machine-readable ledgers mirror these files for validation. They may not silently override approved creative state.

## Status machine

`planned → blocked_by_assets → ready → submitted → candidate → accepted | repair | rejected → canon`

- `candidate` means generated, not approved.
- `accepted` means the usable ranges and exit state passed required gates.
- `canon` means future work may inherit that asset or state.
- A rejected asset remains evidence but cannot anchor future generation.

## Adapter boundary

Provider-specific IDs, URLs, request schemas, and keys live in adapter/runtime files excluded from public examples. Creative manifests express capabilities and approved state. This lets the user change providers without rewriting the story.

## Planned state versus observed state

After media inspection, observed state wins. Update the next block from what actually appears in accepted footage, or regenerate the parent. Never pretend the plan is visible when the output contradicts it.
