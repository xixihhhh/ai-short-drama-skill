# AI Short-Film Workflow Landscape — 2026-08

Snapshot checked on 2026-08-25. Stars and model capabilities change; verify current sources before citing. This document summarizes research and does not copy third-party prompts, schemas, or implementation.

## Popular general Agent Skill patterns

| Project | Snapshot signal | Useful pattern | ContinuityDirector response |
|---|---:|---|---|
| [Anthropic Skills](https://github.com/anthropics/skills) | ~171K stars | thin SKILL.md, progressive disclosure, evals, packaged resources | core skill remains under 300 lines; details live one reference layer away; eval suite included |
| [Superpowers](https://github.com/obra/superpowers) | ~277K stars | risk-dependent paths, evidence before completion | plan/test/batch/capped modes plus inspection evidence before canon |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | ~236K stars | router plus small composable capabilities | one public director entry routes format/profile/model/audio/spend without forcing the full workflow for a local repair |
| [Agent Skills specification](https://agentskills.io/specification) | open standard | portable SKILL.md structure and progressive context | standard folder layout, provider-neutral instructions, installable package |

## Short-drama and filmmaking workflows

| Project | Snapshot | Strongest contribution | Gap this project targets |
|---|---:|---|---|
| [OpenMontage](https://github.com/calesthio/OpenMontage) | ~50K stars, AGPL-3.0 | provider registry, budget caps, TTS/music/mix, frame/audio QA | huge application; ContinuityDirector offers a lightweight provider-neutral skill and original templates |
| [Emily Seedance 2.0](https://github.com/Emily2040/seedance-2.0) | ~6.9K stars, MIT | global plan, compile next segment only, observed media state, one-variable repair | single model family; this skill adds Wan 3/H3/Seedance routing and broad formats |
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) | ~2K stars, Apache-2.0 | stage ownership, novel extraction, deterministic gates | limited final video/audio/cost control and shorter default clips |
| [ZenStory Drama Skills](https://github.com/zenstory-ai/drama-skills) | ~1.1K stars, MIT | lightweight source files, provider adapters, paid approval, independent review | no cross-model long-block router or physical/contact media gate |
| [0xsline/short-drama](https://github.com/0xsline/short-drama) | ~1K stars, MIT | topics, hooks, paid-story beats, compliance and localization | screenplay-focused; no generation/audio/continuity pipeline |
| [AI Shortfilm Prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) | ~374 stars, mixed notice | prompt presentation, genre examples, eval/SEO packaging | prompt generator rather than inspected production state machine |
| [OnlyShot](https://github.com/A-cat-with-carrots/OnlyShot) | ~248 stars, MIT | static references/storyboard before expensive video | fixed short-fragment workflow conflicted with local continuity/audio results |
| [DramaClaw](https://github.com/dramaclaw/dramaclaw) | ~4K search snapshot, Elastic-2.0 | story graph, asset/voice library, resumable tasks, candidate sandbox | application platform; this skill keeps creative truth in portable files |

## August 2026 model workflow changes

- [Wan 3 official repository](https://github.com/AlibabaCloud-Official/Wan3.0) describes native 30-second generation, multimodal references, integrated sound, and editing. This makes long story blocks practical, but local evidence still requires internal timed beats and whole-block QA.
- [MiniMax H3 official repository](https://github.com/MiniMax-AI/MiniMax-H3) documents audiovisual generation, first/last/reference routes, native stereo sound, and up-to-15-second/2K workflows. This supports selective hero/action/dialogue inserts and explicit soundscape compilation.
- Seedance 2.5 community skills describe 4–30-second multimodal, audio-reference, edit, and extend workflows across surfaces. The active provider remains the parameter truth.
- Seedance 2.0/Fast remains useful for controlled shorter units and economy iterations; native audio still needs cross-clip post mixing.

## Combined design decisions

1. **Cross-format:** live action, pet, fantasy, animation, brand, UGC, standalone, anthology, and serial.
2. **Cross-provider:** capability manifest first; user-selected execution surface second.
3. **Dual timescale:** long generation blocks, fast internal edit beats.
4. **Observed-state continuation:** only inspected accepted footage may unlock dependent blocks.
5. **Separate audio router:** native dialogue, reference audio, dubbing/lip sync, VO, no-dialogue, and hybrid.
6. **Separate spend authorization:** quality tier never implies payment permission; capped batch/autopilot is explicit.
7. **Physical causality:** approach → contact → force → response → outcome, with human/animal/object-specific overlays.
8. **Narrative gate:** cold-viewer comprehension remains P0 even after technical QA passes.
9. **Repair economics:** keep / post-fix / local edit / reroll / rewrite, one variable at a time, systematic-failure stop rule.

## Licensing boundary

ContinuityDirector is independently written under MIT. OpenMontage AGPL code, unlicensed short-drama-agent/Seedance prompt text, mixed-license prompt packs, private media, and community example prompts are not redistributed. See [third-party notices](../THIRD_PARTY_NOTICES.md).
