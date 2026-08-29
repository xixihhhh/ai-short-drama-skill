# 生成任务、候选谱系与恢复

创意状态与执行状态必须分离。故事、角色、空间和连续性是可迁移的创意真相；服务商字段、任务 ID、轮询状态和临时地址只是运行记录。使用 [generation-jobs.csv](../assets/templates/generation-jobs.csv) 保存后者。

## 请求身份

每次正式提交前生成：

- `request_fingerprint`：规范化后的完整提示词、参数版本、精确模型、模式、参考摘要和输出规格；
- `idempotency_key`：同一逻辑提交的稳定键；
- `authorization_scope_id`：本次请求落在哪个费用、平台、上传和重试授权内；
- `context_path`：能返回对应剧情段、镜头、参考和 QA 的项目内路径。

任何会改变像素、声音、时长或费用的字段变化都创建新候选，不覆盖旧请求。临时下载 URL 不参与指纹，真实素材摘要参与。

## 状态机

`planned → previewed → confirmed → submitted → processing → completed → reviewed → accepted | repair | rejected`

旁路状态：`cancel_requested → cancelled`、`unknown → recovered | failed`。

- `confirmed` 只对完整请求指纹有效；请求变化后回到 `previewed`。
- 超时、断网或客户端退出只产生 `unknown`，不能直接重提。
- 先按任务 ID、幂等键或服务商任务历史恢复；确认不存在后才允许新提交。
- 已取消任务若后来返回结果，保留为未验收候选，不自动进入正式状态。
- `completed` 只代表拿到输出；只有 `accepted` 才能解锁依赖段。

## 候选谱系

每个重试记录 `parent_job_id`、`changed_variable`、失败类别和拒绝理由。一次只改一个高层变量：种子、提示词条款、参考、模式或时长。需要同时改多项时视为重新设计，创建新的谱系根。

候选不能只按“最好看”挑选。先过 MUST-HIT 二元门，再用 [candidate-scorecard.csv](../assets/templates/candidate-scorecard.csv) 比较剧情任务、身份、空间、物理、表演、声音、可剪辑性和意外价值。关键候选尽量隐藏模型/种子信息做 A/B，评分人不得先看成本或生成顺序。

## 失败分类与恢复动作

| 类别 | 先做什么 | 禁止 |
|---|---|---|
| `transport` | 轮询、查历史、恢复下载 | 盲目重提 |
| `schema` | 重新读取当前 schema，重编请求预览 | 沿用旧字段猜测 |
| `authorization` | 回到授权边界 | 偷换入口或模型 |
| `provider_rejected` | 保存原始错误，修合法输入 | 无限重试同一请求 |
| `generation_quality` | QA 定位最小失败单元 | 把任务失败当网络失败 |
| `asset_missing` | 找回或重建已批准依赖 | 用近似素材悄悄替换 |
| `human_edit_conflict` | 刷新项目状态并使下游失效 | 覆盖人工修改 |

## 并发与断点

- 只并发 DAG 中无状态依赖的节点；每个节点记录依赖任务和解锁条件。
- 同一节点同一指纹只允许一个有效租约，防止两个 Agent 重复付费。
- 检查点至少保存：最近已验收段、未决任务、费用余额、候选谱系、人工修改后的失效范围。
- 恢复时先刷新运行状态和项目文件，再继续；不得凭旧对话内存假设任务仍在运行。
- 自动重试受 `max_retries`、预算、授权、重复失败模式和时间窗共同限制。

## 适配器边界

模型适配器只负责能力发现、请求编译、提交、轮询、取消、结果解析与错误归一化。它不得修改故事、镜头意图或连续性真相。换服务商时重编运行请求，不重写创意文件。
