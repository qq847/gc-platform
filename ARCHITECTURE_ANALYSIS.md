# Game Connection 平台架构分析与优化方案

## 一、现有平台结构

### 1.1 EventHub（B2C 端）

**顶部导航 Tab：**
- 🏠 Home（信息流）
- 📅 Calendar（日历视图）
- 🔴 Live（直播视图）
- 🎮 Projects（游戏项目浏览）
- 🏢 Companies（公司目录：Publisher/Developer/Investor/Service/Distributor）
- 👤 Profile（个人资料）

**现有用户角色：**
- 参会者（Attendee）
- 游戏开发者（Developer）
- 买家/发行商（Buyer/Publisher）
- 投资人（Investor）

### 1.2 EventHQ（B2B 端 - 主办方后台）

**8 个功能模块：**
1. Event Setup（活动创建）
2. Products（票务/展位/赞助包）
3. Attendees（参会者 + Buyer Invitations）
4. Conference（议程管理）
5. Awards（奖项评选）
6. GameShowcase（游戏项目审核）
7. LetsMeet（1对1商务会议）
8. Settings（账户设置）

---

## 二、新增角色需求分析

### 2.1 Sponsor（赞助商）

**核心需求：**
- 浏览可购买的赞助包（Gold/Silver/Bronze）
- 在线支付购买赞助包
- 查看赞助权益履行状态（Logo 展示、社交媒体宣传、展位位置等）
- 下载赞助合同和发票

**现有覆盖情况：**
- EventHQ 的 `Products_v1_PC.html` 已有 Sponsorship Tab，展示了赞助包和已确认赞助商列表
- **但这是主办方视角**，缺少赞助商自助购买和管理界面

**建议方案：**
- 在 EventHub 顶部导航新增 `💼 Sponsor` Tab
- 创建 `Sponsor_Portal_v1_PC.html`，包含：
  - **Browse Packages**：浏览可购买的赞助包
  - **My Sponsorship**：已购买的赞助权益和履行状态
  - **Invoices & Contracts**：合同和发票下载

---

### 2.2 Media（媒体/记者）

**核心需求：**
- 申请媒体票（Press Pass）
- 查看活动议程，标记感兴趣的 Session
- 预约采访开发者/发行商
- 下载媒体资料包（Press Kit）

**现有覆盖情况：**
- Attendees 页面的 Buyer Invitations Tab 中有 "Press / Media" 分类
- 但媒体没有独立的工作台

**建议方案：**
- 在 EventHub 顶部导航新增 `📰 Media` Tab
- 创建 `Media_Portal_v1_PC.html`，包含：
  - **Press Pass Application**：媒体票申请
  - **My Schedule**：个人议程安排（从 Conference 筛选）
  - **Interview Requests**：预约采访（连接 LetsMeet 系统）
  - **Press Kit**：媒体资料下载

---

### 2.3 Association（协会/展团管理者）

**核心需求：**
- 管理旗下所有参展成员（子公司、会员单位）
- 批量购买展位和门票
- 查看成员的参与状态（报名、提交项目、预约会议）
- 统一开具发票

**现有覆盖情况：**
- 完全缺失

**建议方案：**
- 在 EventHub 顶部导航新增 `🏛️ Association` Tab
- 创建 `Association_Portal_v1_PC.html`，包含：
  - **Members Management**：成员列表和批量邀请
  - **Group Purchases**：批量购买展位/门票
  - **Participation Overview**：成员参与状态仪表盘
  - **Billing & Invoices**：统一财务管理

---

### 2.4 Investor/Publisher Deal Flow（投资人/发行商签约流程）

**核心需求：**
- 浏览游戏项目库（已在 Projects Tab）
- 标记感兴趣的项目（Shortlist）
- 预约 1对1 会议（已在 LetsMeet）
- 签署 NDA
- 提交 Term Sheet / LOI
- 跟踪签约进度

**现有覆盖情况：**
- Projects Tab 已有游戏浏览功能
- LetsMeet 已有会议预约功能
- **缺少签约流程管理**

**建议方案（复杂，可后续实现）：**
- 在 Projects 页面右侧边栏增加 **Deal Pipeline** 模块
- 或在 Profile 中增加 **My Deals** Tab
- 包含：Shortlist / NDA Signed / Term Sheet Sent / In Negotiation / Closed

---

## 三、顶部导航栏重组方案

### 方案 A：角色分组（推荐）

```
🏠 Home | 📅 Calendar | 🔴 Live | 🎮 Projects | 🏢 Companies | 👤 Profile
                                                                    ↓
                                                            [角色切换下拉菜单]
                                                            - Attendee（默认）
                                                            - ⚡ Organizer
                                                            - 💼 Sponsor
                                                            - 📰 Media
                                                            - 🏛️ Association
```

**优点：**
- 保持导航栏简洁
- 角色切换集中在 Profile 下拉菜单
- 不同角色看到不同的 Dashboard

**缺点：**
- 角色入口深度增加一层

---

### 方案 B：平铺导航（直观）

```
🏠 Home | 📅 Calendar | 🔴 Live | 🎮 Projects | 🏢 Companies | ⚡ Organizer | 💼 Sponsor | 📰 Media | 🏛️ Association | 👤 Profile
```

**优点：**
- 所有角色入口平铺，一目了然
- 快速切换，无需下拉

**缺点：**
- 导航栏拥挤（10 个 Tab）
- 对普通参会者造成信息过载

---

### 方案 C：分层导航（推荐）

**第一层（主导航）：**
```
🏠 Discover | 📅 Calendar | 🔴 Live | 🎮 Projects | 🏢 Companies | 👤 Profile
```

**第二层（角色入口，右上角独立区域）：**
```
[For Business ▾]
  - ⚡ Organizer Dashboard
  - 💼 Sponsor Portal
  - 📰 Media Center
  - 🏛️ Association Hub
```

**优点：**
- 主导航保持简洁（面向 C 端）
- B 端角色集中在 "For Business" 下拉菜单
- 清晰区分 C 端和 B 端功能

---

## 四、页面合并建议

### 4.1 不建议合并的页面

以下页面功能独立，应保持独立：
- EventHQ Dashboard（主办方总控）
- GameShowcase（游戏审核）
- LetsMeet（会议配置）
- Awards（奖项管理）

### 4.2 可以整合的功能

| 现有页面 | 可整合内容 | 整合方式 |
|---------|-----------|---------|
| **Products** | Sponsor Portal 的赞助包浏览 | 在 Products 的 Sponsorship Tab 增加"赞助商视角"切换 |
| **Attendees** | Media 的媒体票申请 | 在 Attendees 的 Buyer Invitations Tab 增加"媒体申请"入口 |
| **Conference** | Media 的议程安排 | Conference 增加"我的日程"个人视图 |
| **Settings** | Association 的成员管理 | Settings 的 Team Tab 增加"展团管理"模式 |

### 4.3 需要新建的独立页面

| 页面 | 功能 | 原因 |
|------|------|------|
| `Sponsor_Portal_v1_PC.html` | 赞助商自助购买和管理 | 业务流程独立，不适合嵌入 Products |
| `Media_Portal_v1_PC.html` | 媒体工作台 | 需要整合票务、议程、采访预约多个功能 |
| `Association_Portal_v1_PC.html` | 协会/展团管理 | 涉及批量操作和财务，需要独立界面 |

---

## 五、推荐实施路径

### 阶段 1：顶部导航优化（立即实施）
1. 在 EventHub 顶部导航 Live 和 Projects 之间插入 `⚡ Organizer`
2. 点击直接跳转到 `EventHQ_Dashboard_v1_PC.html`

### 阶段 2：新角色页面（分步实施）
1. 创建 `Sponsor_Portal_v1_PC.html`（赞助商门户）
2. 创建 `Media_Portal_v1_PC.html`（媒体中心）
3. 创建 `Association_Portal_v1_PC.html`（协会/展团管理）

### 阶段 3：导航栏重组（优化）
- 采用 **方案 C（分层导航）**
- 将 Organizer/Sponsor/Media/Association 整合到 "For Business" 下拉菜单
- 主导航保持简洁

### 阶段 4：Deal Flow（复杂功能，后续）
- 在 Projects 或 Profile 中增加签约流程管理

---

## 六、你的决策点

请确认以下问题：

1. **顶部导航方案**：选择方案 A / B / C？还是有其他想法？
2. **新角色页面优先级**：Sponsor / Media / Association 哪个先做？
3. **是否需要合并现有页面**：还是保持独立，只做导航优化？
4. **Deal Flow 功能**：现在暂时忽略，还是给出框架设计？
