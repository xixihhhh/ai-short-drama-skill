# 从验收候选到剪辑时间线

[示例素材与三份 CSV](../../skills/dramake/assets/examples/edit-handoff/) 随安装包提供。参考片由 FFmpeg 生成，36 秒、4 fps，前 30 秒为蓝色，随后为红色。镜头 E01 将前 6 秒按 2 倍速剪为 3 秒，E02 取第 30 至 35 秒。两段以 0.5 秒溶解连接，成片时间线长 7.5 秒。

从仓库根目录运行：

```sh
cd skills/dramake
d=assets/examples/edit-handoff
python3 scripts/validate_plan.py --delivery --jobs "$d/generation-jobs.csv" --candidates "$d/candidate-scorecard.csv" --timeline "$d/edit-timeline.csv"
python3 scripts/reference_frames.py sheets "$d/reference.mp4" review.jpg
python3 scripts/reference_frames.py tail "$d/reference.mp4" last.png
```

检查第二页的红色画面与 CSV 的最后一格 **00:00:35.750**。尝试在工作副本中把 E02 的源入点改成 29 秒，同时把出点改成 34 秒。事件依然是 5 秒，但会因超出已批准区间而失败。
