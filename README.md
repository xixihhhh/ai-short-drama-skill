<div align="center">

# Dramake

### 把一段文字，拍成一部能看懂、能衔接、能发布的 AI 短剧

一个面向普通创作者的导演级 Agent Skill。不会编剧、分镜、配音或剪辑，也能从点子、文案、小说或剧本开始，串起完整的 AI 短剧生产线。

[English](README.en.md) · [快速开始](#quick-start) · [Agent 兼容](#agent-compatibility) · [工作流](#workflow) · [模型路由](#model-routing) · [文档](#docs)

<p>
  <a href="https://github.com/xixihhhh/ai-short-drama-skill/releases/latest"><img src="https://img.shields.io/github/v/release/xixihhhh/ai-short-drama-skill?style=flat-square&amp;color=7c3aed" alt="Release"></a>
  <a href="skills/dramake/SKILL.md"><img src="https://img.shields.io/badge/Skill-v0.6.0-2563eb?style=flat-square" alt="Skill v0.6.0"></a>
  <a href="tests/test_templates.py"><img src="https://img.shields.io/badge/tests-25%20passed-16a34a?style=flat-square" alt="25 tests passed"></a>
  <a href="README.en.md"><img src="https://img.shields.io/badge/docs-中文%20%7C%20English-0891b2?style=flat-square" alt="Chinese and English"></a>
  <a href="#agent-compatibility"><img src="https://img.shields.io/badge/agents-Codex%20%7C%20Claude_Code%20%7C%20WorkBuddy-f97316?style=flat-square" alt="Codex, Claude Code, and WorkBuddy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-111827?style=flat-square" alt="MIT License"></a>
</p>

<br>

<img src="assets/dramake-cover.png" alt="Dramake 从文字、剧本、分镜到 AI 短剧成片" width="100%">

</div>

> Dramake 不是提示词合集。它把故事、角色、镜头、模型、声音、预算和质检放进同一条可追踪的生产线，让生成结果更像一部影片，而不是一堆互不相干的小视频。

可用于 Codex、Claude Code、WorkBuddy 及其他支持 `SKILL.md` / Agent Skills 的智能体。面向抖音、红果短剧、视频号、快手、B站、TikTok、YouTube 等渠道；支持真人短剧、独立短片、单元剧、连续剧、萌宠、拟人奇幻、漫剧、UGC 与品牌剧情。执行平台、API、MCP 和模型入口始终由用户选择。

<a id="quick-start"></a>

## 1 分钟上手

安装：

```bash
npx skills add xixihhhh/ai-short-drama-skill --skill dramake
```

然后把故事直接交给 Agent：

```text
使用 Dramake，把下面的故事做成 90 秒真人家庭短剧。
先检查剧情是否让普通观众看得懂，再输出剧本、角色母版、分镜、
模型与费用路线、配音方案和质检标准。抖音版 9:16，交付 720p。
在父段通过剧情、身份、物理和声音检查前，不要生成依赖它的下一段。
```

你也可以只让它完成某一段工作：诊断故事、改剧本、做分镜、修站桩对白、统一声线、检查粗剪，或修复一个失败镜头。

<a id="agent-compatibility"></a>

## 在哪些 Agent 里使用

Dramake 采用标准 `SKILL.md + references + assets` 目录结构。核心指令不依赖某个聊天产品，但不同 Agent 的安装位置和工具权限不同。

| Agent / 客户端 | 兼容方式 | 建议安装 |
|---|---|---|
| **OpenAI Codex** | 当前版本已完成格式、引用、模板和安装包验证 | `npx skills add xixihhhh/ai-short-drama-skill --skill dramake` |
| **Claude Code** | 遵循 Agent Skills / `SKILL.md` 目录规范 | 使用 Skills 安装器，或复制到 `.claude/skills/dramake/` |
| **WorkBuddy** | 支持本地 Skill 的版本可手动导入完整 `dramake` 目录 | 复制到用户级 Skills 目录；以当前客户端导入入口为准 |
| **其他 Agent Skills 客户端** | 能读取 `SKILL.md` 并访问同目录 references/assets 即可 | 下载 [dramake.skill](https://github.com/xixihhhh/ai-short-drama-skill/releases/latest) 或复制目录 |

兼容 Skill 不等于自动拥有视频生成能力。Agent 仍需连接用户选择的网页、API、MCP、本地模型或其他生成工具；Dramake 负责导演、路由、状态、预算与验收。

## 它和同类方案有什么不同

Dramake 不是新的视频模型，也不是绑定某个网站的生成平台。它是一层“导演与制片系统”：把用户选择的模型、工具和素材组织成一条有状态、有预算、有验收标准的成片流程。

| 常见同类方案 | 常见结果 | Dramake 的区别 |
|---|---|---|
| **视频提示词库** | 能写单镜头，但不维护整片状态 | 同时维护剧情、人物知识、服装、道具、动作阶段、声线和声音边界 |
| **一键文生视频平台** | 生成快，但模型、费用与修复路径被平台决定 | 服务商中立；模型、入口、质量档和付费授权分别选择 |
| **逐镜头批量工作流** | 五六秒一段，最后像素材拼盘 | 区分长 `generation_block` 与短 `edit_beat`，减少外缝但保持段内节奏 |
| **只锁角色脸的连续性方案** | 脸相似，服装、手机、动作和声线仍漂移 | 长期母版 + 短期验收状态 + 每个维度唯一权威参考 |
| **所有镜头一次并行生成** | 上游已经错了，下游继续复制错误 | 独立任务可并行；依赖剧情必须等父段真实验收后解锁 |
| **只检查画面清晰度** | 技术漂亮，但剧情看不懂、声音像拼接 | 剧情、身份/画风、物理/连续性、声音四道独立门禁 |
| **“高级档”直接批量付费** | 重试和成本失控 | 质量档不等于消费许可；预算、上传、候选和停止条件单独授权 |

### 一个入口，内置十二类能力

目前只需要安装一个 `dramake` Skill。下面是它内部协同工作的能力模块，不是十二个需要分别安装的碎片 Skill。

| 内置能力 | 负责什么 | 主要产物 |
|---|---|---|
| **Story Doctor** | 从点子/小说/剧本中修因果、动机、铺垫、反转和节奏 | 剧情合同、节拍表、冷观众问题 |
| **Visual Director** | 把情绪目标变成景别、调度、表演、运镜和剪辑动机 | 导演合同、分镜与镜头计划 |
| **Continuity Keeper** | 维护父子段、轴线、动作阶段、道具、湿度、光线和场景边界 | 连续性账本、验收尾帧、转场方案 |
| **Spatial Director** | 锁地点锚点、走位、出入口、镜面拓扑、巨物尺度和异常空间规则 | 空间图、走位状态、反向空间检查 |
| **Series Memory** | 管理长篇来源、人物知识、时间线、揭示和跨集不可逆状态 | 系列事实账本、来源切片、恢复游标 |
| **Identity & Style Lock** | 锁人物/动物/产品、服装拓扑、重复道具、文字图层、材质和横竖屏视觉规则 | 角色/道具圣经、画风母版、参考权威矩阵 |
| **Voice & Audio Director** | 统一说话人、声线、口型路线、环境、音乐和 J/L cut | Voice Bible、音频连续性与混音图 |
| **Model Router** | 在 Wan 3、Seedance、MiniMax H3 或其他模型间按能力选路 | 可替换模型卡与逐段生成路线 |
| **Budget Guard** | 分离质量档与付费权限，计算候选、重试和上限 | 费用计划、授权模式、支出账本 |
| **Job Orchestrator** | 管理请求指纹、幂等、轮询、取消、断点恢复和候选谱系 | 任务账本、检查点、恢复决定 |
| **QA & Repair** | 抽帧、听音、检查剧情/物理/漂移，选择最小修复 | QA 报告、保留/后期修/编辑/重抽/重写决定 |
| **Edit & Release** | 把验收区间装入可编辑时间线，统一媒体并完成发布前技术门 | 时间线清单、分轨、交付母版与发布检查 |

<a id="workflow"></a>

## 从文字到成片

| 阶段 | Dramake 做什么 | 通过条件 |
|---|---|---|
| **01 故事** | 从文字提取主角、欲望、阻碍、升级、铺垫与回报 | 冷观众能说清目标、行动与结果 |
| **02 记忆与母版** | 锁角色、服装、材质、场景、道具、声线，并建立跨集事实/知识状态 | 每个维度一个权威参考；无时间线或知识冲突 |
| **03 空间与导演设计** | 编排地点锚点、走位、导演意图、价值变化、节拍、表演和运镜 | 每个动作有可达路径；每个镜头能回答“为什么这样拍” |
| **04 生成路由** | 按长段、对白、首尾帧、参考音频、编辑和预算选模型 | 质量档与付费授权明确分离 |
| **05 任务执行** | 用指纹和幂等键提交、轮询、恢复、取消并保留候选谱系 | 不重复付费；所有输出可回到请求上下文 |
| **06 证据验收** | 下载真实素材，抽帧、听音、慢放检查并盲评候选 | 父段验收后才解锁依赖段 |
| **07 成片交付** | 将验收区间装入时间线，连续性剪辑、分轨混音、标准化和发布检查 | 画面、剧情和声音像同一部影片；技术门全部通过 |

### 两个时间尺度

- `generation_block`：8–30 秒的模型请求与连续性容器，减少外部硬接缝；
- `edit_beat`：2–8 秒的信息、动作、反应、对白或切镜单位，保证段内节奏。

长视频不等于站桩长镜头。20–30 秒生成段通常包含 4–6 个可观察节拍，以及有动机的内部切镜或阶段变化。

## 它重点解决什么

| 常见失败 | Dramake 的处理方式 |
|---|---|
| 剧情突然跳地点、观众看不懂 | 剧情合同、人物知识状态、场景桥与冷观众门禁 |
| 一句话说完后站着不动 | 台词、并行动作、听者反应、微表演与退出动作共同编排 |
| 多段像随机素材硬拼 | 验收尾部状态、轴线、动作阶段、声音边界和有动机的转场 |
| 人脸、毛色、服装和道具漂移 | 长期母版 + 短期验收状态 + 参考权威矩阵 |
| 印章、秤、头盔或文字跨幕变形 | 中性光多视角道具圣经 + `prop/state/text_plate` ID + 精确文字后期合成 |
| 穿模、额外肢体、手机翻面 | `接近 → 接触 → 施力 → 响应 → 稳定结果` 物理门禁 |
| 倒车变前进、转向/脱落没发生 | 世界/屏幕运动向量 + 可见阶段 + 稳定终态，逐帧按实际画面验收 |
| 碰撞镜头像远处平看 | 预备、逼近、近镜头遮挡/尺度骤增、冲击落点、机位反应和可见后果 |
| 笑点靠台词解释、猫咪只会站桩 | 主线反转、笑点可读性合同、视线信息差、动画演员式表演和反应停顿 |
| 工作人员的台词却由猫咪开口 | 每句唯一说话者、可见嘴型主体、非说话者闭嘴状态与明确广播来源 |
| 每段声线、底噪和音乐都不同 | Voice ID、参考音频、人工 A/B、连续环境和统一终混 |
| 选了 Premium 就失控花钱 | 模型、执行入口、质量档、付费授权与重试上限分别记录 |

<a id="model-routing"></a>

## 模型路由，不绑定平台

每次执行前核实当前入口的时长、参考素材、音频、编辑、分辨率、价格与保存规则。下表是测试起点，不是永久排名。

| 模型系列 | 优先测试任务 | 主要风险 |
|---|---|---|
| **Wan 3** | 20–30 秒多节拍剧情段、减少外部接缝、720p 经济/均衡档 | 后半段身份、服装、骨骼和画风漂移 |
| **Seedance 2.5** | 高价值对白、音频/图像/视频参考、编辑、续写与修复 | 参考过载与成本 |
| **Seedance 2.0** | 4–15 秒对白、动作、过渡和均衡镜头 | 长片需要更多外部接缝 |
| **Seedance 2.0 Fast** | 预演、覆盖、备选与经济档测试 | 进入终片前仍需严格验收 |
| **MiniMax H3** | 4–15 秒高运动重点镜头、首尾帧和关键音画段 | 不必把普通镜头全部做成高成本段 |

其他模型也可以接入。Dramake 路由的是能力，不是品牌忠诚度。

## 横屏、竖屏与多种内容

| 成片形式 | 内容配置 | 发布画幅 |
|---|---|---|
| 15–45 秒强钩子小短片 | 真人、萌宠、品牌、UGC | `9:16` 抖音 / TikTok / Shorts |
| 45–120 秒独立短片 | 家庭、喜剧、奇幻、动作、动画 | `9:16`、`16:9`、`1:1` |
| 1–4 分钟单元剧 | 固定角色和世界规则，每集独立解决问题 | 竖屏或横屏独立设计 |
| 1–4 分钟连续短剧 | 维护关系、知识、伤势、道具和季线状态 | 抖音、红果短剧及其他渠道 |

横竖双版本共享剧情、角色、道具和声线母版，但分别设计构图、景别、运动路径、字幕与封面安全区；默认不把一个版本机械裁成另一个版本。

## 声音与配音

Dramake 可按场景选择原生对白、参考音频、外部配音/TTS、画外音或混合路线。原生对白优先解决口型和表演，角色声线用独立 Voice ID 与授权锚点维持；环境、音乐、电话声和问题音频在后期统一。

随机生成的音乐不会直接裸拼成终片。同场景保留连续环境底，使用 J/L cut、对白避让和响度匹配，让闭眼听也像同一部影片。

## 可靠性门禁

| 验证项 | 当前状态 |
|---|---:|
| 自动化仓库测试 | **25 项通过** |
| 中英文文档对应 | **38 组通过** |
| Skill 官方格式校验 | **通过** |
| 完整合法生产计划 | **可通过** |
| 错误父子依赖、稀疏长段、越界镜头、未知声线 | **会被拒绝** |

验证的是工作流、文件结构和计划约束，不是对任何视频模型结果的无条件保证。模型能力与价格在执行时复核，候选质量以真实视频、音频、抽帧和冷观众结果为准。

<a id="docs"></a>

## 文档与工具

| 入口 | 用途 |
|---|---|
| [主 Skill](skills/dramake/SKILL.md) · [English Skill](skills/dramake/SKILL.en.md) | 完整工作流与触发说明 |
| [导演、镜头与节奏](skills/dramake/references/directing-camera-and-pacing.md) | 导演意图、运镜合同、内部切镜和节奏曲线 |
| [喜剧可读性与动画化表演](skills/dramake/references/comedy-and-animated-performance.md) | 宏观反转、笑点信息差、反应停顿、拟人表演与物理边界 |
| [角色、声线与参考锁](skills/dramake/references/identity-voice-and-reference-locks.md) · [重复道具圣经](skills/dramake/assets/templates/prop-bible.md) | 人物、服装、重复/文字道具、材质、声音与参考权威 |
| [连续性与转场](skills/dramake/references/continuity-and-transitions.md) | 父子状态、尾帧、重新锚定与场景边界 |
| [空间地图与走位](skills/dramake/references/spatial-blocking-and-world-state.md) · [系列记忆](skills/dramake/references/series-memory-and-source-adaptation.md) | 复杂空间、镜面/巨物、长篇来源、人物知识和跨集状态 |
| [对白、配音与混音](skills/dramake/references/audio-and-dubbing.md) | 原生对白、参考音频、外部配音和声音连续性 |
| [模型路由](skills/dramake/references/model-router.md) · [费用授权](skills/dramake/references/authorization-and-batch.md) | 可替换模型、预算、批量和停止条件 |
| [物理与失败模式](skills/dramake/references/physics-and-failure-modes.md) · [QA 修复](skills/dramake/references/qa-and-repair.md) | 穿模、解剖、文字、手机方向与最小修复 |
| [任务恢复与候选谱系](skills/dramake/references/production-operations-and-recovery.md) · [剪辑与发布](skills/dramake/references/editing-delivery-and-release.md) | 幂等、断点恢复、候选盲评、正式时间线和技术交付 |
| [匿名实测记录](benchmarks/tested-observations.md) · [验证报告](evals/benchmark-report.md) | 已观察问题与验证边界 |

<details>
<summary><strong>本地校验命令</strong></summary>

```bash
python3 scripts/validate_plan.py \
  --continuity skills/dramake/assets/templates/continuity-ledger.csv \
  --block-manifest skills/dramake/assets/templates/block-manifest.csv \
  --shot-plan skills/dramake/assets/templates/shot-plan.csv \
  --voice-bible skills/dramake/assets/templates/voice-bible.csv \
  --audio-continuity skills/dramake/assets/templates/audio-continuity.csv \
  --cost skills/dramake/assets/templates/cost-plan.csv \
  --jobs skills/dramake/assets/templates/generation-jobs.csv \
  --spatial skills/dramake/assets/templates/spatial-plan.csv \
  --story-memory skills/dramake/assets/templates/story-memory.csv \
  --candidates skills/dramake/assets/templates/candidate-scorecard.csv \
  --timeline skills/dramake/assets/templates/edit-timeline.csv

python3 -m unittest discover -s tests
python3 scripts/check_bilingual.py
```

</details>

## 示例

| 项目 | 适合查看的能力 |
|---|---|
| [90 秒真人家庭短剧](examples/live-action-90s/README.md) | 真人表演、因果与对白 |
| [90 秒宠物独立短片](examples/standalone-90s/README.md) | 写实可爱、物种动作与接触 |
| [单元剧](examples/anthology-episode/README.md) | 固定角色与每集独立回报 |
| [连续短剧](examples/serialized-episode/README.md) | 跨集关系、知识和道具状态 |

这些示例是制作清单，不会把未验收的模型输出冒充成已完成影片。

## 安装、贡献与许可

- 下载最新安装包：[Dramake Releases](https://github.com/xixihhhh/ai-short-drama-skill/releases/latest)
- 提交失败案例或模型兼容信息：[Issues](https://github.com/xixihhhh/ai-short-drama-skill/issues)
- 参与改进：[贡献指南](CONTRIBUTING.md)
- 许可证：[MIT](LICENSE)

<div align="center">

**从文字开始。用证据验收。把片段变成作品。**

</div>
