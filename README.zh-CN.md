# PawDirector — AI 萌宠短片与猫咪短剧 Skill

[English](README.md)

把宠物照片做成连贯的 15–120 秒 AI 萌宠视频、独立猫咪短片、单元剧或连续短剧，重点解决：角色漂移、动漫化、塑料 CG、无关跳切、穿模、站桩对白、口型与声线不一致、背景音突然断掉。

PawDirector 是一个**不绑定平台**的 Agent Skill。用户可以自己选择官方产品、API、聚合平台、网页端或 MCP；核心流程只根据时长、首尾帧、图片/视频/音频参考、原生对白、编辑/续写、分辨率、价格和排队时间选型。

## 核心能力

- 独立 15–45 秒小短片、45–120 秒剧情短片；
- 固定猫咪角色的单元剧；
- 有季线和连续状态的系列短剧；
- MiniMax H3、Wan 3、Seedance 2.5、Seedance 2.0/Fast 能力路由；
- Sketch、Economy、Balanced、Premium、Hero Insert、Final Polish 六档付费模式；
- 无对白、模型原生对白、参考音频、外部配音/TTS、混合配音；
- 角色定妆、实拍轻卡通画风锁、物理接触、连续性状态、声音桥、冷观众测试；
- 30 秒长段内部 4–6 个节拍，减少外部拼接但避免“一句话站 10 秒”。

## 快速安装

```bash
npx skills add <OWNER>/ai-pet-short-video-skill --skill pawdirector
```

或把 `skills/pawdirector` 复制到你的 Agent skills 目录。

## 一句话调用

```text
使用 PawDirector，把我的两只猫做成90秒9:16写实轻卡通短片。
按我能用的平台和预算自动选择模型，不绑定供应商；有对白时优先保证口型和声线，
每个连续片段必须先下载、抽12帧、检查穿模与尾帧状态，再生成下一段。
```

## 为什么和普通提示词库不同

普通工作流常把很多 4–10 秒视频直接拼起来，画面像无关素材，声音也会每段重启。PawDirector 把长视频请求当成“剧情段落容器”：每 4–7 秒发生一次可见推进，内部切镜有动机，段尾提供可接力状态；下一段必须继承已验收的身份、位置、方向、动作、服装、道具、天气和声音。

同时，可爱只来自圆爪、耳朵、尾巴、猫咪习性、体型反差和表演节奏，不使用“动漫/童话/卡通渲染”把真实猫做成塑料 CG。

## 模型选型

- **Wan 3 类长视频能力：**优先尝试 20–30 秒剧情段，减少外部接缝；重点检查后半段毛发、服装、骨骼和穿模。
- **Seedance 2.5 类多模态能力：**适合高预算对白、参考音频、多图/视频参考、局部编辑、续写和修复。
- **Seedance 2.0：**适合 4–15 秒较可控的对白、动作和过渡镜头。
- **Seedance 2.0 Fast：**适合预演、备选镜头和低成本覆盖；通过严格质检后才能进终片。
- **MiniMax H3 类能力：**适合 4–15 秒高运动、高分辨率、首尾帧控制的英雄镜头和特效爆点。

以上是起始路由，不是永久排名。每次执行前应核实用户所选平台的最新能力和价格。

## 付费模式

- **Sketch：**低成本验证故事和动作；
- **Economy：**通常 720p，长段优先，失败局部重做；
- **Balanced：**对白/连续性用更强模型，只给开头和高潮多候选；
- **Premium：**参考音频、多模态、编辑/续写、选择性高分辨率；
- **Hero Insert：**把预算集中到猫爪特写、变身、追逐、奇观或情绪高潮；
- **Final Polish：**只放大和精修已验收镜头。

价格不写死，由用户选择的平台在当日提供。模板会计算请求数、重试系数、最好/预期/封顶成本。

## 配音与声音

- 原生对白适合解决口型，但必须验收台词、角色归属、语速、尾句重复；
- 同一角色建立固定声线说明和合法参考音频；
- 外部配音需要口型工具或反应镜头、侧脸、远景、猫爪/道具插镜、画外音等剪辑策略；
- 原生片段里的随机 BGM 不直接裸拼；每段分轨，统一铺环境底、主题音乐、对白响度和 J/L Cut 声音桥。

## 实测护栏

在本地实验中，旧版 36 个短片段有 20 个出现严重或阻断问题；30 秒长段会自行形成 2–4 次内部切镜，但仍需时间轴；短片段原生音频响度跨度达到 8.9 LU，部分边界跃变超过 30 dB；尾帧能改善下一段开头，却不能保证整段服装和骨骼稳定。这些结果被写成门禁，而不是宣传某个模型“最好”。

## 文档入口

- [主 Skill](skills/pawdirector/SKILL.md)
- [模型路由](skills/pawdirector/references/model-router.md)
- [预算模式](skills/pawdirector/references/budget-and-quality.md)
- [对白、参考音频与配音](skills/pawdirector/references/audio-and-dubbing.md)
- [连续性与转场](skills/pawdirector/references/continuity-and-transitions.md)
- [物理与穿模检查](skills/pawdirector/references/physics-and-failure-modes.md)
- [实测观察](benchmarks/tested-observations.md)

## 许可证与独立声明

本项目采用 MIT 许可证，是独立社区项目，与字节跳动、阿里巴巴、MiniMax、Atlas Cloud 及其他模型/平台方无隶属关系。研究来源和许可证边界见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
