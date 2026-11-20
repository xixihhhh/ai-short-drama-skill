# From reviewed takes to an edit timeline

[The media and three CSV files](../../skills/dramake/assets/examples/edit-handoff/) also ship in the skill. The FFmpeg-generated 36-second, 4 fps reference is blue until 30 seconds and red afterwards. E01 uses source seconds 0–6 at 2× for three timeline seconds. E02 uses seconds 30–35. Their 0.5-second dissolve gives a 7.5-second timeline.

From the repository root:

```sh
cd skills/dramake
d=assets/examples/edit-handoff
python3 scripts/validate_plan.py --delivery --jobs "$d/generation-jobs.csv" --candidates "$d/candidate-scorecard.csv" --timeline "$d/edit-timeline.csv"
python3 scripts/reference_frames.py sheets "$d/reference.mp4" review.jpg
python3 scripts/reference_frames.py tail "$d/reference.mp4" last.png
```

The second page shows the red ending. The last cell in the CSV reads **00:00:35.750**. In a working copy, change E02's source interval to 29–34 seconds. Its duration still matches but delivery validation fails because the cut starts before the accepted range.
