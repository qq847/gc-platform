# Game Connection 平台详情

## 基本信息
- GitHub: https://github.com/qq847/gc-platform（公开）
- GitHub Pages: https://qq847.github.io/gc-platform/
- 设计规范：#e8e4da背景，DM Sans字体，主色#d95f2b
- 文件命名：功能名_v版本_端（PC/Mobile）.html

## 页面数量
- 2026-03-24 完成：**94个HTML文件**
- 7个Phase：Discovery / Identity / Connection / Meetup / Events / Sponsorship / Commerce
- Phase 5 B2B Organizer（12模块）+ B2C Attendee 一一对应

## 关键文件
- index.html：汇总导航，Roadmap View（7Phase）+ Module View，左右双栏+右侧可编辑设计说明
- DesignRationale_v1.html：7步骤产品设计说明文档（给总框架设计师用）
- GC_Platform_Structure.html：旧版汇总导航

## Google Drive
- 根目录 ID: 10000WlzNJtr1m4_3DTZ1wgEUIo1Rij88（Game Connection New - Platform）
- workspace已通过Google Drive桌面客户端同步（计算机→我的Mac→workspace）

## 技术要点
- Live v40（Qiang原版）：225条真实GDC 2026数据，JS/数据不动只改CSS
- index备注用localStorage存储，note-id永远不能改（否则用户备注丢失）
- 新增页面后更新index.html的Roadmap View和Module View两个视图

## Token节省规则（2026-03-24确立）
- 改现有文件：用edit工具精准插入，不整体重写
- 派Agent做页面：每Agent做3-4个类似页面，不一个一个派
- 超时警惕：任务太大先拆分再派
