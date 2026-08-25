# ContinuityDirector — 通用 AI 短片与短剧生产 Skill

[English](README.md)

面向真人短剧、独立小短片、单元剧、连续剧、萌宠故事、拟人奇幻、漫剧、UGC 和品牌剧情的通用 Agent Skill。重点解决：剧情看不懂、很多无关小视频硬拼、人物与服装漂移、站桩对白、穿模与物理错误、口型/声线不一致、背景音乐每段重启、付费失控和供应商绑定。

它**不绑定 Atlas Cloud、MCP 或任何平台**。用户自己选择官方产品、API、聚合平台、本地工作流或网页端；Skill 只根据当前可用能力、价格、数据上传政策和用户偏好选路。

## 支持范围

- 15–45 秒强钩子小短片；
- 45–120 秒独立剧情短片；
- 1–4 分钟真人、动画、宠物、奇幻或品牌剧情；
- 固定角色和世界规则的单元剧；
- 有季线、关系和道具状态的连续短剧；
- 小说/长文改编、人物关系和时间线抽取；
- 原生对白、参考音频、外部配音/TTS、口型、混合后期；
- 多模型、多供应商、预算和批量付费控制。

宠物不再是核心限制，只是其中一个内容配置和实测案例。

## 核心创新

### 生成段和剪辑节拍分开

`generation_block` 是 8–30 秒模型请求和连续性容器；`edit_beat` 是 2–8 秒的信息、动作、反应、对白和切镜单位。这样既能利用 Wan 3/Seedance 2.5 等长段能力减少外部接缝，又不会变成“一句话站 10 秒”。

### 上游验收后才解锁下游

独立定妆、音乐、声线、备选开头、非依赖插镜可以并行；连续剧情必须先下载上游成片、抽帧、听音频、检查物理和尾部状态。只有 `accepted tail state + canonical master + continuity ledger` 才能生成下一段。

### 模型、平台、质量、付费授权四件事分开

- 模型按长段、首尾帧、参考音频、原生对白、编辑/续写、画质等能力路由；
- 平台/供应商由用户选，不把 Atlas 或任何 API 写死；
- 质量有 Sketch / Economy / Balanced / Premium / Hero Insert / Final Polish；
- 授权有 plan-only / single-test / approved-batch / autopilot-with-cap。

选择 Premium 不等于授权无限花钱。批量模式必须记录平台、可上传素材、请求数、重试数和硬预算；用户预先授权后，不需要每一条重复确认，但超过边界必须停。

### 配音单独成为一条生产线

- 模型原生对白：优先口型和表演；
- 参考音频：锁定同一角色声线、语速、口音和情绪；
- 外部配音/TTS：配合口型工具、反应镜头、侧脸、远景、插镜和画外音；
- 混合方案：保留好的原生台词和拟音，旁白、电话声、环境、BGM 后期统一；
- 无对白：单一连续音乐/环境底和精选拟音。

原生视频中的随机音乐不会直接裸拼成成片。

### 技术过关不代表剧情能发

终片分四个门：剧情可懂性、身份/画风、物理/连续性、声音。冷观众不看梗概，也必须能复述“谁想要什么 → 被什么阻挡 → 做了什么 → 为什么得到这个结果”。

## 2026 年 8 月模型路由

每次执行前仍要核实用户所选平台的当前参数和价格：

- **Wan 3 类：**优先测试 20–30 秒多节拍剧情段，减少外部拼接；重点查后半段身份、服装、骨骼和画风漂移；
- **Seedance 2.5 类：**高预算多模态、参考音频、对白、编辑/续写/修复；
- **Seedance 2.0：**较可控的 4–15 秒对白、动作和过渡；
- **Seedance 2.0 Fast：**预演、覆盖、备选、经济档，严格验收后才可进终片；
- **MiniMax H3 类：**4–15 秒首尾帧/多模态/原生音画、高运动、高规格英雄镜头。

这些是起始假设，不是永久排名，也不限制用户使用其他模型。

## 安装

```bash
npx skills add xixihhhh/ai-short-drama-skill --skill continuity-director
```

## 调用示例

```text
使用 ContinuityDirector，把这个故事做成90秒9:16真人家庭短剧。
平台由我选择；请给 Economy 和 Balanced 两套模型与费用方案。
对白优先保证口型和固定声线，上游片段通过剧情、连续性、物理和声音检查后再生成下游。
```

## 实测经验已经变成门禁

- 旧版 36 个碎片短视频中，20 个存在严重或阻断级问题；
- 实测 30 秒视频内部会产生 2–4 次变化，说明长段仍要写 4–6 个时间节拍；
- 20 个原生音频短段响度跨度达到 8.9 LU，部分接缝超过 30 dB；
- 尾帧能改善下一段开头，但不能保证后半段服装和骨骼不漂；
- 技术检查通过的版本，冷观众仍可能完全看不懂剧情。

因此 Skill 不把“单条画面好看”当作完成，而是按完整电影的因果、画面、声音和观众理解验收。

## 文档入口

- [主 Skill](skills/continuity-director/SKILL.md)
- [内容配置](skills/continuity-director/references/content-profiles.md)
- [生成段与剪辑节拍](skills/continuity-director/references/generation-blocks-and-edit-beats.md)
- [模型路由](skills/continuity-director/references/model-router.md)
- [批量付费与授权](skills/continuity-director/references/authorization-and-batch.md)
- [预算和质量档](skills/continuity-director/references/budget-and-quality.md)
- [对白、参考音频与配音](skills/continuity-director/references/audio-and-dubbing.md)
- [连续性和转场](skills/continuity-director/references/continuity-and-transitions.md)
- [物理与失败检查](skills/continuity-director/references/physics-and-failure-modes.md)
- [2026 年 8 月 GitHub 工作流调研](research/2026-08-workflow-landscape.md)

## 开源与独立声明

MIT 许可证。ContinuityDirector 是独立社区项目，与字节跳动、阿里巴巴、MiniMax、Atlas Cloud 及其他模型/平台方无隶属关系。参考项目和许可证边界见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
