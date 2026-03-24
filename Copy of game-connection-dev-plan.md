# Game Connection Platform — 技术开发路线图
*为架构师准备的完整开发方案*

---

## 产品背景与核心逻辑

Game Connection 是一个服务游戏行业的 B2B 展会平台，目标是从"一次性线下展会"升级为"持续运营的行业交流平台"。

核心用户角色：
- **展会方（Organizer）**：创建和管理展会，配置模块，管理参会者
- **开发商/发行商（Developer/Publisher）**：展示游戏，寻找合作，参与 Let's Meet 配对
- **投资人/买家（Investor/Buyer）**：寻找项目，洽谈合作
- **媒体（Press）**：获取资讯，申请采访
- **普通参会者（Attendee）**：浏览展会，参与活动

商业模式：
- 展会方付费使用平台（SaaS订阅）
- 赞助商付费购买曝光（Market模块）
- 未来：交易佣金、数据服务、AI增值功能

技术原则：
- PWA优先（一套代码，PC+Mobile自适应）
- API-first架构（后端先行，前端可替换）
- 模块化设计（展会方按需开启功能模块）
- 数据主权在平台（所有行为数据沉淀到平台）

---

## Phase 1 — 地基层（预计10-14周）

### 目标
这是整个项目最重要的阶段。架构师需要在这里做出所有核心决策。地基决定上限，这阶段不能省时间。

### 1.1 技术选型与架构决策

**后端框架**
- 推荐：Node.js (NestJS) 或 Go
- 原因：NestJS模块化架构天然匹配平台的多租户需求；Go性能更好但招人难
- 数据库：PostgreSQL（主库）+ Redis（缓存/会话）+ Elasticsearch（搜索）
- 文件存储：AWS S3 或 Cloudflare R2
- CDN：Cloudflare

**前端框架**
- 推荐：Next.js（React）
- 原因：SSR支持SEO，PWA支持移动端，生态成熟
- UI组件库：自建设计系统（基于已有的HTML原型）
- 状态管理：Zustand 或 React Query

**基础设施**
- 部署：AWS（ECS/Fargate）或 Railway（早期省钱）
- CI/CD：GitHub Actions
- 监控：Sentry（错误监控）+ Datadog（性能）
- 邮件：Resend 或 SendGrid

### 1.2 数据模型设计（最关键）

这里需要架构师最深度介入。数据模型设计错了，后面重构代价极大。

**核心实体：**

```
User（用户）
- id, email, name, avatar
- role: organizer | developer | publisher | investor | press | attendee
- company_id（关联）
- created_at, updated_at

Organization（机构/公司）
- id, name, description, logo
- type: game_studio | publisher | investor | media | service_provider
- country, website, social_links
- verified: boolean

Event（展会）
- id, organizer_id, name, slug
- start_date, end_date, location（线下地址或线上）
- status: draft | published | live | ended
- modules: jsonb（开启了哪些功能模块）
- settings: jsonb（各模块配置参数）

Game（游戏）
- id, developer_id, title, description
- genre[], platform[], stage（开发阶段）
- media（图片/视频）
- seeking: investment | publisher | coop（寻求什么合作）

EventParticipant（参会者）
- id, event_id, user_id
- role: exhibitor | buyer | press | attendee | speaker
- badge_type, registration_status
- check_in_at

Match（Let's Meet 配对）
- id, event_id, requester_id, receiver_id
- status: pending | accepted | declined | completed
- scheduled_at, room, duration
- notes

Product（Market商品）
- id, event_id, seller_id
- type: sponsorship | booth | ticket | advertising
- name, description, price, currency
- inventory, sold_count
- status: active | sold_out | hidden

Order（订单）
- id, buyer_id, product_id, event_id
- amount, currency, status
- payment_intent_id（Stripe）
- created_at
```

### 1.3 Auth系统

- 登录方式：Google OAuth（主要）+ 邮箱密码（备用）
- JWT + Refresh Token 机制
- 多角色权限系统（RBAC）
- 多租户隔离：每个展会是独立的数据空间
- SSO预留接口（未来企业客户需要）

**权限层级：**
```
Platform Admin（平台管理员）
  └── Organizer Admin（展会方管理员）
        └── Event Manager（活动管理员）
              └── Exhibitor（参展商）
              └── Participant（普通参会者）
```

### 1.4 API设计规范

- RESTful API，版本化（/api/v1/）
- OpenAPI/Swagger自动生成文档
- Rate limiting（防滥用）
- Webhook支持（展会方系统集成）
- GraphQL预留（未来移动端可能需要）

### 1.5 多租户架构

这是平台业务的核心：每个展会是独立的，但共用同一套基础设施。

方案：Schema-based 多租户（PostgreSQL row-level security）
- 每个Event有独立的数据隔离
- 展会方只能看到自己的数据
- 平台管理员可以跨展会查看

### Phase 1 交付物
- 完整数据库Schema
- Auth系统上线
- API文档
- 开发环境 + Staging环境搭建完毕
- CI/CD流水线配置完毕
- 基础Admin后台（用于平台管理）

### Phase 1 资源需求
- 架构师：全职，这阶段主导
- 后端工程师：2人
- 前端工程师：1人（负责搭设计系统）
- DevOps：兼职或外包
- 预算参考：人力成本为主，基础设施费用极低（<$500/月）

---

## Phase 2 — 核心产品层（预计12-16周）

### 目标
做出能在真实展会中跑起来的最小可用产品（MVP）。这阶段结束后要能找一个真实展会做灰度测试。

### 2.1 用户侧核心功能

**Onboarding流程**
- Google登录后进入4步引导
- 步骤1：选择角色（我是开发商/发行商/投资人/媒体/参会者）
- 步骤2：填写基本资料 + 公司信息
- 步骤3：选择兴趣标签（游戏类型、平台、地区）
- 步骤4：完善Profile（可跳过，后续补充）
- Profile完成度评分系统（激励用户完善信息）

**Profile页**
- 个人/公司双Profile（可切换）
- 游戏作品展示（开发商专属）
- 参会历史
- 社交链接
- 联系方式（需对方接受才可见，保护隐私）

**Live展会主页**
- 展会选择器（支持多展会切换）
- 活动日程（日历视图 + 列表视图）
- 地图（线下展会支持场馆地图）
- 搜索与筛选（按类型、时间、地点）
- 收藏/Going功能
- 冲突检测（同时段活动提醒）
- Google Calendar/.ics导出
- 分享功能（Canvas生成分享图）

**Organizations页**
- 公司目录（参展商列表）
- 搜索+筛选（按类型、国家、游戏类型）
- 公司详情页（游戏列表、团队成员、联系方式）

**Projects/Games页**
- 游戏展示目录
- 筛选：开发阶段、平台、类型、寻求合作类型
- 游戏详情页：媒体展示、开发团队、合作需求

**Messages消息系统**
- 一对一私信
- 消息请求（陌生人需先发申请）
- 已读/未读状态
- 通知系统（邮件 + 站内）

### 2.2 展会方后台（B2B Events）

**EventHQ Dashboard**
- 展会数据概览（注册人数、签到率、活跃度）
- 快捷操作入口
- 任务提醒

**EventSetupWizard（展会创建向导）**
- Step 1：基本信息（名称、时间、地点、封面图）
- Step 2：选择功能模块（Live/Let's Meet/Market/Awards等）
- Step 3：配置参会者类型和注册方式
- Step 4：发布设置（公开/私密/邀请制）

**EventModuleSetup（模块配置）**
- 每个模块独立开关
- 模块参数配置（如Let's Meet的时间槽设置）
- 模块预览

**BuyerInvitation（买家邀请）**
- 批量导入邮件列表
- 定制邀请邮件模板
- 邀请状态追踪

**ScheduleBuilder（日程管理）**
- 创建/编辑活动
- 时间冲突检测
- 发言人管理
- 多轨道日程

**EventPublicPage（公开展会详情页）**
- 对外展示页（SEO友好）
- 报名/购票入口
- 展会亮点展示

### 2.3 ConferenceCalendar（行业日历）

- 全行业展会日历（独立于单一展会）
- 数据来源：手工录入 + 合作方API
- 筛选：年份/月份/类型/地区
- Google Calendar/.ics导出
- 这是平台的SEO入口，引流作用极大

### Phase 2 交付物
- 用户完整注册+登录+Profile流程
- Live展会核心功能上线
- Organizations + Projects目录
- Messages基础版
- 展会方后台基础版
- 可支撑一个真实展会运营

### Phase 2 资源需求
- 后端工程师：2-3人
- 前端工程师：2人
- 设计师：1人（基于已有原型执行）
- QA：兼职
- 运营：1人（准备第一个测试展会）

---

## Phase 3 — B2B商业化层（预计10-14周）

### 目标
在有真实用户的基础上，搭建平台的核心商业化功能。这阶段的前提是Phase 2已经跑过至少一个真实展会，有真实数据验证基础功能。

### 3.1 Let's Meet（智能配对系统）

这是平台最有差异化的功能，也是技术复杂度最高的模块。

**参会者端：**
- Browse页：浏览其他参会者（按角色、兴趣、公司过滤）
- 发送配对请求（附留言）
- 接受/拒绝请求
- 我的会议日程（时间表视图）
- 会前提醒（邮件+站内通知）

**展会方配置端（LetsMeet_Setup）：**
- 开启时间：配对窗口开放时间
- 会议时长：15/20/30分钟可选
- 时间槽配置：每天几个时段、每时段几间会议室
- 房间管理：物理房间 or 线上视频间
- AI配对开关：是否启用智能推荐

**展会方管理端（LetsMeet_Organizer）：**
- 全局配对情况总览
- 房间分配管理
- 冲突检测与手动调整
- 导出配对报告

**AI配对算法（分阶段实现）：**
- V1：基于标签匹配（游戏类型、合作需求、地区）
- V2：加入历史行为数据（谁看了谁的Profile、谁收藏了哪些游戏）
- V3：机器学习模型（基于历史成功配对的训练数据）

### 3.2 Market（B2B交易模块）

**核心原则：平台不收佣金（初期），先跑量**

**SponsorExplore（赞助商浏览）：**
- 展示本展会可购买的赞助产品
- 分类：品牌曝光、场地冠名、数字广告、特色活动
- 价格、库存、已售情况实时展示

**SponsorBuilder（展会方配置赞助产品）：**
- 矩阵视图（Excel式，批量编辑）
- 导购流程视图（分步引导）
- 产品模板库（常见赞助类型快速添加）
- 自定义赞助包（组合多个产品）

**CheckoutCart（购物车+结账）：**
- 多产品同时购买
- 优惠码支持
- 开具发票（重要：B2B客户强需求）

**OrderConfirm（订单确认）：**
- 支付成功页
- 自动触发赞助权益交付流程
- 邮件确认

**BuyerDashboard（买家中心）：**
- 我的订单历史
- 权益使用进度
- 续购/升级入口

**支付集成：**
- Stripe（国际卡，主要）
- 银行转账（大额B2B订单）
- 发票管理系统

### 3.3 Awards（评奖模块）

- 展会方创建奖项类别
- 开发商提交参赛游戏
- 评委邀请与投票系统
- 结果公示
- 获奖徽章（可嵌入游戏页面/官网）

### 3.4 GameShowcase（游戏展示增强）

- 专属展示页（比普通游戏详情页更丰富）
- 预约试玩功能
- 媒体包下载（Press Kit）
- 与Let's Meet联动（展示页直接发起配对请求）

### Phase 3 交付物
- Let's Meet全流程上线
- Market基础版（赞助商购买流程）
- 支付系统接入
- Awards模块
- 第一笔真实交易完成

### Phase 3 资源需求
- 后端工程师：3人（配对算法需要专人）
- 前端工程师：2人
- 设计师：1人
- 运营/BD：2人（开始主动销售赞助商品）
- 支付合规：法务配合

---

## Phase 4 — 数据与智能层（持续进行）

### 目标
将平台积累的数据转化为竞争壁垒。这是平台从"工具"变成"生态"的关键。

### 4.1 数据基础设施

**事件追踪系统：**
- 用户行为全量埋点（页面浏览、点击、停留时长）
- 展会数据（签到率、配对成功率、交易转化率）
- 工具：Mixpanel 或自建（ClickHouse）

**数据仓库：**
- 原始数据：S3/R2
- 分析层：ClickHouse 或 BigQuery
- BI工具：Metabase（内部）+ 定制报表（给展会方）

### 4.2 展会方数据报表

这是展会方续费的核心驱动力。

- 参会者画像报告（行业分布、国家分布、职位分布）
- 配对效果报告（请求数、接受率、会议完成率）
- 赞助商ROI报告（曝光量、点击量、线索数）
- 对比历届数据（年同比、环比）
- 可导出PDF（给展会方用于向赞助商汇报）

### 4.3 AI功能路线图

**V1（基于规则）：**
- AI Pick（基于标签的游戏推荐）
- 智能日程建议（基于兴趣的活动推荐）

**V2（基于协同过滤）：**
- "你可能感兴趣的公司"
- "与你相似的用户还关注了"

**V3（大模型集成）：**
- AI助手（展会导览、问题解答）
- 智能配对解释（"为什么推荐你们见面"）
- 自动生成展会报告摘要

### 4.4 开放平台

- 公开API（让展会方系统集成）
- Webhook（实时事件推送）
- 数据导出工具（参会者名单、配对记录等）
- 第三方集成：Salesforce、HubSpot、Eventbrite

### 4.5 移动端增强

- PWA推送通知（替代App内通知）
- 离线模式（展会现场可能网络差）
- 二维码扫描（现场签到、名片交换）
- NFC支持（高端展会场景）

---

## 技术债务管理原则

1. **每个Phase结束做一次技术审查**，评估哪些临时方案需要重构
2. **20%时间留给技术债务**，不能全力冲功能
3. **测试覆盖率要求**：核心业务逻辑>80%，API>60%
4. **文档同步更新**：API文档、数据库Schema、部署文档

---

## 关键架构决策摘要（给架构师）

| 决策点 | 推荐方案 | 原因 |
|--------|----------|------|
| 前端 | Next.js PWA | SSR+SEO+移动端一体 |
| 后端 | NestJS | 模块化，适合多租户 |
| 数据库 | PostgreSQL | 关系型，支持复杂查询 |
| 搜索 | Elasticsearch | 全文搜索+筛选 |
| 缓存 | Redis | 会话+高频数据 |
| 文件 | Cloudflare R2 | 便宜，CDN集成 |
| 部署 | AWS ECS | 弹性扩容 |
| 支付 | Stripe | 国际化支持好 |
| 邮件 | Resend | 开发体验好 |
| 监控 | Sentry+Datadog | 标配 |

---

## 时间与成本估算

| 阶段 | 时间 | 团队规模 | 备注 |
|------|------|----------|------|
| Phase 1 | 10-14周 | 4-5人 | 架构师主导 |
| Phase 2 | 12-16周 | 5-6人 | 前端加重 |
| Phase 3 | 10-14周 | 6-8人 | BD开始招人 |
| Phase 4 | 持续 | 8-10人 | 数据工程师加入 |

**总计：约18-24个月到达Phase 4初期**

---

*最后更新：2026-03-23*
