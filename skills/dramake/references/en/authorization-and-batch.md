# Spend Authorization and Batch Execution

Quality mode answers “what should we buy?” Authorization mode answers “what has the user permitted us to buy?” Keep them separate.

## Plan-only

No paid generation, uploads, or external media mutations. Produce briefs, prompts, manifests, estimates, and dry runs.

## Single-test

The user authorizes one representative paid request within a named provider/model/mode and amount. Inspect it before requesting more.

## Approved batch

The user approves a defined batch:

- provider(s) and account/channel;
- allowed media uploads and retention/public-link implications;
- maximum requests and spend;
- resolution/duration/model routes;
- automatic retry count and eligible failure categories;
- stop conditions and reporting cadence.

Independent tasks may run in parallel. Continuity-dependent tasks remain gated by accepted parent state.

## Autopilot with cap

The user pre-authorizes execution inside a hard spend and retry cap. The agent may route models, regenerate failed units, and select candidates without asking after each request. It must stop before:

- exceeding cost/request/retry cap;
- changing provider or data-upload policy;
- using a voice/face/reference without rights;
- expanding scope or duration materially;
- accepting a P0 narrative, identity, physics, or audio failure.

## Selective premium escalation

Start economical. Upgrade only the hook, identity-critical dialogue, reveal, climax, contact-heavy action, or failed repair when expected value exceeds added cost. Never regenerate the entire project merely because one transition fails.

## Spend ledger

Record `request_id`, route, provider, model, duration, resolution, candidate purpose, quoted/actual cost, retry parent, status, accepted seconds, and reason. Track:

`cost_per_accepted_second = total_generation_cost / accepted_timeline_seconds`

This makes model decisions comparable across providers even when billing units differ.
