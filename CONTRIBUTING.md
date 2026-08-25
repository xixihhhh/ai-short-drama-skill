# 贡献指南

[English](CONTRIBUTING.en.md)

欢迎贡献文字转短剧流程、带日期的模型观察、可复现失败案例、人/动物/物体物理检查、横竖屏示例、配音策略、连续性规则和 QA 工具。

## 规则

- 未经权利与同意，不上传媒体、脸或声音；
- 移除密钥、请求 ID、签名链接、私人路径与可识别参考素材；
- 把结论标为文档能力、带日期实测、创作偏好或推断；
- 不把动态价格、时长和模型限制写成永久事实；
- 实测结论记录模型、执行入口、日期、设置、输入类别、检查证据与通过/失败标准；
- 中文默认文档与对应英文文档必须在同一个 PR 中同步更新；
- 一次修复尽量只改变一个规则或变量，并添加对应测试/评估案例。

运行：

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
