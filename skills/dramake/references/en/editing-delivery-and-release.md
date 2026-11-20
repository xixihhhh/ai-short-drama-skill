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

Run this command from the installed Dramake folder with Python 3 and FFmpeg’s `ffprobe` on PATH.

```bash
python3 scripts/check_export.py final.mp4 --layout portrait --require-audio --srt final.srt
```

Supply the options required for your delivery. The command accounts for rotation and sample aspect ratio when checking display orientation, checks for an audio track, and checks that each UTF-8 SRT cue has a valid interval within the video duration. A failed check prints the reason and exits with a nonzero status. Review the audio content, burned-in captions and lip sync during playback.

## Reviewable edit handoff

Run the commands from the installed Dramake directory. The example includes encoded media and its review records:

```sh
d=assets/examples/edit-handoff
python3 scripts/validate_plan.py --delivery --timeline "$d/edit-timeline.csv" --jobs "$d/generation-jobs.csv" --candidates "$d/candidate-scorecard.csv"
python3 scripts/reference_frames.py sheets "$d/reference.mp4" review.jpg
python3 scripts/reference_frames.py tail "$d/reference.mp4" last.png
```

Use normal plan validation for draft paths before generation. Delivery mode resolves local files relative to the timeline directory or an explicit `--media-root`. A video event must cite the same block, job and media as its completed source job, and a passed MUST-HIT and accepted candidate decision. External dialogue, music, ambience and sound effects can cite a local audio stream directly. Events citing generated assets also need their approval. Archive remote outputs locally and point both manifests at the same file. The validator measures the relevant video or audio stream. Set the optional job column `output_sha256` to the checksum taken at review to detect replacement of a file under the same name.

Enter candidate `accepted_ranges` as `opening=0-6;ending=30-35.75` in seconds, using half-open intervals. A timeline event cites `R01:opening` in `accepted_range_id`. For legacy unnamed ranges `0-6;30-35.75`, use `R01:1` and `R01:2`. Source cuts must lie inside the selected range. Source duration divided by speed must equal timeline duration within 1 ms of rounding.

Events of the same `track_type` default to track `main`. Add a `track_id` column for parallel layers. Primary video covers the timeline from zero without gaps. For cuts, leave transition fields empty or use `cut`. For dissolves or crossfades, the outgoing and incoming events must name the same transition, such as `dissolve:0.5` or `crossfade:0.5`, with exactly that overlap in seconds. Triple overlaps and wholly nested events cannot be paired transitions.

Reference sheets contain up to 12 cells per page. The default samples a decoded frame every 2.5 seconds plus the first and final frame, retaining a short clip’s middle frame when it falls before the first interval; use `--interval 1` for denser sampling. Each cell displays its time relative to the first frame. The matching CSV lists the source file, page, cell and time. Page one uses the requested filename and subsequent pages use names such as `review-002.jpg`. Use a fresh output name for each run. A shot shorter than the interval can fall between samples; confirm exact cuts frame by frame.
