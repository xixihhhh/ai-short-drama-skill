# Generation jobs, candidate lineage, and recovery

Keep creative state separate from execution state. Story, identity, space, and continuity are portable creative truth; provider fields, task IDs, polling state, and temporary URLs are runtime records. Store the latter in [generation-jobs.csv](../../assets/templates/generation-jobs.csv).

## Request identity

Before submission, derive:

- `request_fingerprint` from the normalized full prompt, parameter version, exact model, mode, reference digest, and output specification;
- an `idempotency_key` stable for the same logical submission;
- an `authorization_scope_id` identifying the approved provider, upload, spend, and retry boundary;
- a project-relative `context_path` back to the block, shot, references, and QA.

Any pixel-, audio-, duration-, or cost-affecting change creates a new candidate instead of overwriting the previous request. Temporary download URLs do not affect the fingerprint; real asset digests do.

## State machine

`planned → previewed → confirmed → submitted → processing → completed → reviewed → accepted | repair | rejected`

Side paths are `cancel_requested → cancelled` and `unknown → recovered | failed`.

- Confirmation applies only to one complete fingerprint; a request change returns it to `previewed`.
- Timeout, disconnection, or client exit produces `unknown`, not permission to resubmit.
- Recover by task ID, idempotency key, or provider history before creating a new request.
- A cancelled task that later yields output remains an unreviewed candidate.
- `completed` means an output exists; only `accepted` unlocks dependent blocks.

## Candidate lineage

Every retry records `parent_job_id`, `changed_variable`, failure class, and rejection reason. Change one high-level variable at a time: seed, one prompt clause, one reference, mode, or duration. A multi-variable change is a redesign and starts a new lineage root.

Do not select a take merely because it looks attractive. Pass binary MUST-HIT gates first, then use [candidate-scorecard.csv](../../assets/templates/candidate-scorecard.csv) to compare narrative job, identity, space, physics, acting, audio, editability, and useful surprise. For hero candidates, hide model and seed metadata during A/B review when practical.

## Failure classes and recovery

| Class | First action | Never |
|---|---|---|
| `transport` | poll, inspect history, recover download | blindly resubmit |
| `schema` | reload the current schema and rebuild preview | guess with stale fields |
| `authorization` | return to the approved boundary | silently switch route |
| `provider_rejected` | retain the raw error and repair legal input | retry forever |
| `generation_quality` | locate the smallest failing QA unit | treat it as a network failure |
| `asset_missing` | recover or rebuild the approved dependency | silently substitute a lookalike |
| `human_edit_conflict` | refresh project state and invalidate downstream work | overwrite human edits |

## Concurrency and checkpoints

- Run only DAG nodes without state dependencies in parallel; record dependency jobs and unlock conditions.
- Permit one active lease for one node and fingerprint so two agents cannot duplicate spend.
- A checkpoint contains the latest accepted block, pending jobs, remaining budget, candidate lineage, and invalidation caused by human edits.
- On resume, refresh runtime and project state before proceeding; do not trust stale conversational memory.
- Auto-retry is bounded jointly by `max_retries`, spend, authorization, repeated failure pattern, and time window.

## Adapter boundary

A model adapter owns capability discovery, request compilation, submission, polling, cancellation, result parsing, and normalized errors. It cannot alter story, directorial intent, or continuity truth. Switching providers recompiles runtime requests, not creative files.
