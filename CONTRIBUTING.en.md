# Contributing

[简体中文](CONTRIBUTING.md)

Contributions are welcome for provider-neutral workflows, dated model observations, reproducible failure cases, human/animal/object physics checks, format examples, dubbing strategies, and QA tooling.

## Rules

- Do not upload media or voices without rights and consent.
- Remove API keys, prediction IDs, signed URLs, private paths, faces, voices, and identifiable reference assets.
- Label claims as documented capability, dated observation, creative preference, or inference.
- Do not describe dynamic price or model limits as permanent facts.
- Include provider, model, date, settings, input category, inspection evidence, and failure/acceptance criteria for benchmark claims.
- Update the default Chinese document and its English mirror in the same pull request.
- Prefer one rule or variable per repair and add a corresponding test or evaluation case.

Run:

```bash
python3 scripts/validate_plan.py \
  --continuity skills/dramake/assets/templates/continuity-ledger.csv \
  --block-manifest skills/dramake/assets/templates/block-manifest.csv \
  --shot-plan skills/dramake/assets/templates/shot-plan.csv \
  --voice-bible skills/dramake/assets/templates/voice-bible.csv \
  --audio-continuity skills/dramake/assets/templates/audio-continuity.csv \
  --cost skills/dramake/assets/templates/cost-plan.csv
python3 -m unittest discover -s tests
python3 scripts/check_bilingual.py
```
