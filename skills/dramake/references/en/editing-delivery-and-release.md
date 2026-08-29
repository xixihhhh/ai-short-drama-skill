# Edit timeline, normalization, and release delivery

“Clips generated” is not “film finished.” Use [edit-timeline.csv](../../assets/templates/edit-timeline.csv) to place actual accepted ranges on a timeline while preserving lineage back to story blocks, jobs, and QA.

## From candidate to timeline

Each event records source media, `source_in/source_out`, `timeline_in/timeline_out`, speed, framing transform, transition, audio routing, caption/title IDs, grade, and source job. Use accepted candidates or explicitly approved deviations only; never assume the entire generated clip belongs in the cut.

Retain handles, but remove broken heads/tails, prompt after-motion, repeated action, and dead freeze tails. Across events, inspect action phase, screen direction, eyeline, sound field, and repeated information. A transition must express a change in time, space, action, or emotion.

## Delivery normalization

Before formal assembly, normalize proxies or final sources to the project delivery profile:

- resolution, pixel aspect, color space/transfer, frame-rate policy, and audio sample rate;
- orientation metadata that agrees with visible pixels rather than relying on player rotation;
- an explicit keep-timebase or constant-frame-rate decision for VFR sources;
- approved reframing rather than mechanical center crops;
- separate editable layers for captions, art titles, logos, and UI;
- separate dialogue, ambience, music, and effects stems before final mix.

Normalization is not permission to downgrade every source to one poor format. Choose an edit working format and final release profile, then apply only necessary conversions.

## Editable delivery

In addition to the master, retain:

- relocatable project-relative media manifests;
- timeline-event to source mappings;
- caption text, timecode, speaker, and style IDs;
- audio stems, loudness target, and music rights state;
- cover, title layers, landscape/portrait versions, and safe areas;
- model/job/candidate/QA lineage without keys or temporary signed URLs.

Generate an import package for the user's editor when useful, but preserve a provider-neutral timeline manifest first so one proprietary format cannot lock the project.

## Pre-release technical gate

Automate checks for missing media, invalid duration/overlap, timeline gaps, inconsistent resolution/frame rate/color, silence or clipping, loudness violations, black frames, freeze frames, duplicate tails, caption bounds, and cover safe areas.

Human review covers cold-viewer comprehension, phone brightness, subtitle legibility, music dynamics and dialogue ducking, first-frame hook, final button, loop seam, landscape/portrait composition, and detail after platform compression. Successful upload does not equal accepted content.
