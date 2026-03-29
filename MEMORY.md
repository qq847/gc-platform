# MEMORY.md — 长期记忆（精华层）

> 详细内容见 memory/ 子文件。每2周更新一次。

---

## 关于 Qiang Qiang

- 全名：强强，里昂，法国（Europe/Paris）
- WhatsApp: +33642753673 | 邮箱: qq@connection-events.com
- emlyon EMBA在读（EMBAEC06，Team 1），压力大
- 决策风格：先轻量试跑，量起来再扩展；不喜欢废话，要直接结论
- 沟通语言：中文
- 车辆：Citroën GH-214-JM（已有居民停车证）

---

## 关于公司

- **公司：** Connection Events / 东品游戏（西品/互娱/北京/致远联游）
- **业务：** 中国独立游戏发行商，海外游戏引进中国（版号/渠道/本地化）
- **团队：**
  - 薛田田 — 财务（外汇/税务/结算）
  - 张元琦 — 制作/技术（版本/渠道/服务器/招聘）
  - 赵少东 — 市场/展会（CJGC/社媒/Newsletter）
  - 郭鹏 — 版号/客服/招聘筛选
  - 白耘赫 — 美术
- **工具：** Monday.com（board: 5093101454）、Gmail（qq@connection-events.com）

---

## 重要项目 & 截止日期

### 🔴 紧急（本周）
- **3/25（今天）**：MacBook Pro取货 — Fnac Lyon Bellecour，营业到19:30，需企业发票（薛田田提供SIRET）
- **3/25（今天）**：同舟共济 iOS CPU优化截止
- **3/26（明天）**：Newsletter西安GC+Deep Rock公告（赵少东）
- **3/27**：Ghostship第一笔款$30,000（薛田田）⚠️ Critical
- **3/27**：新签合同境外汇款（薛田田）

### 📋 近期重要
- **3/31**：王国保卫战5 DLC（张元琦）
- **3/31**：核算2月开发者销售报告（薛田田）
- **4/2**：百战天虫全渠道首发 🔴 最高优先级
- **4/10**：第一季度税务申报（薛田田）

### 项目状态
- **百战天虫**：4/2首发，iOS版权授权问题未解决，Android内购80%，12家渠道对接中
- **Deep Rock Galactic**：与Ghostship签约，代码交接 ⚠️超期未确认（3/24截止，张元琦），版号资料准备中
- **同舟共济**：版号申请中，iOS CPU优化截止3/25（今天）
- **财务**：Apple结汇$107,863.33、Ironhide付汇$172,663.85（Critical，薛田田）

### ✅ 近期完成
- Game Connection平台：94页面全部完成并推送 GitHub Pages
- MEMORY.md精简（600行→90行），memory/子文件归档
- Anthropic账单（6笔）已转发给tonbby

---

## 关键人物

- **李鑫**：大学校友，公司重要股东，杭州无端游戏创始人（Rust移动端，腾讯全球发行）
- **Jacob**：瑞典同学，Coffee Stain合作邮件已发（3/18），Satisfactory等移动端机会
- **tonbby**：tonbby@connection-events.com，报销联系人

---

## Game Connection 平台

→ 详见 memory/gc-platform.md

- GitHub Pages: https://qq847.github.io/gc-platform/
- GitHub 仓库: https://github.com/qq847/gc-platform
- 本地路径: /Users/qiang/.openclaw/workspace/gc-platform/
- 102个HTML原型（PC+Mobile），4个Tab（Roadmap/Module/Journey/VI待建）
- Drive根目录ID: 10000WlzNJtr1m4_3DTZ1wgEUIo1Rij88

**设计系统：**
- 背景 #e8e4da，橙色 #d95f2b，深字 #1c1a17，次字 #6b6660，边框 #e0dbd2，字体 DM Sans
- Premium区（Buyer/Sponsor/DealRoom）：背景 #1c1a17 黑色系
- 侧边栏4种：A.Dashboard白 B.Wizard白 C.Filter白 D.Premium黑
- 顶导2种：标准白60px / Premium黑60px

**平台架构12个Phase（飞机上重新梳理）：**
Phase1:Discovery Phase2:Identity Phase3:Messaging Phase4:EventPublishing+Showcase
Phase5:Conference Phase6:SponsorshipBasic Phase7:Ticketing Phase8:BuyerProgram
Phase9:Exhibition Phase10:Meetings Phase11:Awards Phase12:SponsorshipAdvanced

**9种用户角色：** Attendee/Developer/Buyer/ServiceProvider/Sponsor/Organizer/Speaker/Press/Jury

**待做优先级（P1最高）：**
- P1 🔴 Buyer Commerce 分叉（B3电商入口，ProjectBiz加按钮，进入Premium黑色UI）
- P2 🟡 Organizer模块动态导航（选模块后侧边栏菜单动态变化）
- P3 🟡 谈判Loop节点（条款未达成→返回循环）
- P4 🟢 Speaker_v1_PC.html 真实内容（提案表单+审核状态）
- P5 🟢 统一VI（7种侧边栏变体→4种标准，批量Agent处理）

**🚀 Journey tab（已完成）：** 10条角色流程，侧边栏跳转，分叉标记
**🎨 VI tab：** 待建

---

## AI自动化

→ 详见 memory/automation.md

- 3个Cron Jobs已配置（广告清理/日报/凌晨扫描）
- Token节省规则：用edit不重写；每Agent做3-4个页面；大任务先拆分

---

## 偏好 & 规则

- 回复简洁，直接结论，不要废话开头
- 金额必须仔细核对（教训：107,863误读成107万）
- 主动存档，不靠"心理记忆"
- 派Agent时：开始说干啥、结束说结果
- MEMORY.md只留每天用得到的信息，其余归档到memory/子文件

---

*最后更新：2026-03-25*
