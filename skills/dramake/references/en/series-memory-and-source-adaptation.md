# Long-source adaptation and series memory

Long fiction, serialized drama, and multi-episode IP cannot resend the entire source for every request or rely on conversational memory. Use [story-memory.csv](../../assets/templates/story-memory.csv) for cross-episode facts, character knowledge, timeline, and reveal state.

## Layered retrieval

1. **Series:** world rules, identities, long relationships, irreversible events, central secrets.
2. **Episode:** current objective, entry/exit state, prior dependencies, season thread to advance.
3. **Scene:** what each character knows, holds, has suffered, and where they are.
4. **Shot:** only the identity, space, props, and action state needed now.

Each fact retains `source_span` and validity interval, while a production prompt receives only the relevant slice. When sources conflict, record the conflict and make the adaptation decision canonical instead of silently merging incompatible versions.

## Character knowledge and reveals

Track when the audience, narrator, and each character learn a fact. A character cannot act on unrevealed knowledge; storyboards, inserts, and prompts cannot leak suspense early. A reveal must change choice, relationship, or risk rather than merely explain.

## Timeline and irreversible state

Injury, lost objects, broken relationships, death, exposed secrets, damaged props, and destroyed locations need `valid_from/valid_to`. Recovery requires a visible cause. When reusing wardrobe or locations across episodes, apply current timeline overrides before the long-term master.

## Splitting a long source

- Index by causal and scene boundaries, not fixed character count alone.
- Store summary, entities, open questions, prerequisites, and consequences per span.
- Choose the episode promise and closed task before retrieving source spans.
- Distinguish source fact, explicit rewrite, compression, merge, deletion, and invention.
- Resume from `resume_cursor`, latest canonical state, and current episode—not a full-season reinference.

## Memory gate

Before scripting or storyboarding, reject unresolved identity conflict, timeline paradox, knowledge violation, unexplained reset, duplicate reveal, reopened closed setup, or an episode that advances no relationship or season thread.
