# 项目状态

保持少量可读的事实源。接口参数与运行 ID 是派生信息，不是创意真相。

## 建议文件

- `production-brief.md`：输入文字、渠道、画幅、时长、受众、预算、权利；
- `story-contract.md`：观众承诺、目标、阻碍、选择、结果、铺垫/回报；
- `character-world-bible.md`：角色、声线、场景、道具与风格母版；
- `prop-bible.md`：重复/跨场景/文字道具的几何、材质、图层和状态机；
- `block-manifest.csv`：场景、生成段、剪辑节拍、模型与声音路线；
- `spatial-plan.csv`：地点锚点、连通关系、角色走位、镜面与尺度状态；
- `story-memory.csv`：系列事实、人物知识、时间线、揭示与改编决定；
- `continuity-ledger.csv`：已验收视觉/声音/物理状态；
- `cost-plan.csv` 与 `spend-ledger.csv`：动态价格、授权、实际费用；
- `generation-jobs.csv`：请求身份、幂等、轮询、恢复、取消与候选谱系；
- `candidate-scorecard.csv`：候选硬门、盲评、可用区间和决定；
- `edit-timeline.csv`：正式剪辑区间、轨道、变换、字幕/标题和来源链；
- `qa/`：接触表、转写、时间点缺陷与决定；
- `accepted/`：正式镜头、尾帧、音轨和最终时间线。

## 状态

`planned → ready → generated → reviewed → accepted | repair | rejected`

`generated` 不等于 `accepted`。只有 `accepted` 或明确 `accepted_with_deviation` 的素材可成为父段。

`ready` 只表示创意与素材条件齐备，不代表已授权付费。正式请求另记录 `previewed → confirmed → submitted → recovered/completed`：prompt、参数、参考、模型 schema 的任一实质变化都会让 `confirmed` 回退为 `previewed`。提交超时先用请求 ID 或任务历史找回，不能把未知状态当失败后直接重提。

任务恢复、幂等、取消和候选谱系使用独立运行状态机，详见 [production-operations-and-recovery.md](production-operations-and-recovery.md)。创意段状态、请求状态和时间线使用状态不可互相冒充。

## 依赖图与并行

把生成段视为 DAG。母版、音乐探索、声线、无剧情依赖的插镜和覆盖方案可以并行；需要父段真实退出状态的子段保持串行。并行不是按段号平均分配，而是只并发没有状态边的工作。每个节点记录依赖、解锁条件、费用上限和失败停止条件。

## 父子依赖

依赖段记录 `scene_id`、`parent_block_id`、父段 `observed_exit_state`、自身 `entry_state`、未完成运动和转场方式。已完成节拍不得重演，未来节拍不得提前泄漏。

场景内允许从验收状态接续；换地点/时间时从人物与场景母版重新锚定，并把地点变化作为有动机的转场。

输出来源链默认最多连续 2 段，硬上限 3 段。到达上限、跨场景或发现漂移时，从长期母版与当前已验收状态重新锚定。

复杂空间同时维护地点锚点和走位状态；连续剧同时维护系列事实与人物知识状态。父段被人工替换、修剪或重解释后，按依赖边使旧确认、下游任务和时间线事件失效，再从最近仍有效的检查点恢复。

## 计划与实测冲突

验收素材的实际状态优先于计划。出现偏差时：记录偏差；选择接受为正式状态、修复、拒绝或下一段重新锚定；更新后续计划；移除意外提前完成的节拍；携带未完成节拍。不得假装计划结果已经发生。

## 执行入口隔离

执行入口的 ID、URL、字段、密钥和适配信息保存在不公开的运行文件。创意清单只表达能力与验收状态，因此可以更换入口而不重写故事。
