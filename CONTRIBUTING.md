# Contributing

Contributions are welcome for provider-neutral workflows, dated model observations, reproducible failure cases, human/animal/object physics checks, format examples, dubbing strategies, and QA tooling.

## Rules

- Do not upload media or voices without rights and consent.
- Remove API keys, prediction IDs, signed URLs, private paths, faces, voices, and identifiable reference assets.
- Label claims as documented capability, dated observation, creative preference, or inference.
- Do not describe dynamic price or model limits as permanent facts.
- Include provider, model, date, settings, input category, inspection evidence, and failure/acceptance criteria for benchmark claims.
- Preserve relevant third-party notices when adapting licensed material.

Run:

```bash
python3 scripts/validate_plan.py \
  --continuity skills/continuity-director/assets/templates/continuity-ledger.csv \
  --cost skills/continuity-director/assets/templates/cost-plan.csv
python3 -m unittest discover -s tests
```
