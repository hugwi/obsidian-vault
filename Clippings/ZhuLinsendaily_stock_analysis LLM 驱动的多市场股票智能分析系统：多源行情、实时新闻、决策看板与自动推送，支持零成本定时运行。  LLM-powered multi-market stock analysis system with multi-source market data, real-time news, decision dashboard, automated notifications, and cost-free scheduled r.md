---
title: "ZhuLinsen/daily_stock_analysis: LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs."
source: "https://github.com/ZhuLinsen/daily_stock_analysis"
author:
published:
created: 2026-06-21
description: "LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. - ZhuLinsen/daily_stock_analysis"
tags:
  - "clippings"
---
## 📈 股票智能分析系统

[![#1 Python Repository Of The Day | Trendshift](https://camo.githubusercontent.com/05f2c5e747dd59940b46c31e31a5bd326353f9b1fde8969d05da4f1f3bc73cae/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7472656e6473686966742f7265706f7369746f726965732f31383532372f6461696c793f6c616e67756167653d507974686f6e)](https://camo.githubusercontent.com/05f2c5e747dd59940b46c31e31a5bd326353f9b1fde8969d05da4f1f3bc73cae/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7472656e6473686966742f7265706f7369746f726965732f31383532372f6461696c793f6c616e67756167653d507974686f6e) [![Featured｜HelloGitHub](https://camo.githubusercontent.com/7b89842eed75bf05b853e87034ef0f07e723922d3f636a1a779f26547c6b242a/68747470733a2f2f6170692e68656c6c6f6769746875622e636f6d2f76312f776964676574732f7265636f6d6d656e642e7376673f7269643d366461613136653430356365343665643937623461353737303661656232396626636c61696d5f7569643d7066694a4d71685239757644476c54267468656d653d6e65757472616c)](https://hellogithub.com/repository/ZhuLinsen/daily_stock_analysis)

> 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱

[**产品预览**](#-%E4%BA%A7%E5%93%81%E9%A2%84%E8%A7%88) · [**功能特性**](#-%E5%8A%9F%E8%83%BD%E7%89%B9%E6%80%A7) · [**快速开始**](#-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B) · [**推送效果**](#-%E6%8E%A8%E9%80%81%E6%95%88%E6%9E%9C) · [**文档中心**](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/INDEX.md) · [**完整指南**](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md)

简体中文 | [English](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/README_EN.md) | [繁體中文](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/README_CHT.md)

## 💖 赞助商 (Sponsors)

[![Anspire Open 一站式模型和搜索服务](https://github.com/ZhuLinsen/daily_stock_analysis/raw/main/docs/assets/anspire.png)](https://open.anspire.cn/?share_code=QFBC0FYC) [![轻松抓取搜索引擎上的实时金融新闻数据 - SerpApi](https://github.com/ZhuLinsen/daily_stock_analysis/raw/main/docs/assets/serpapi_banner_zh.png)](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis)

## 🖥️ 产品预览

[![DSA Web 工作台演示](https://github.com/ZhuLinsen/daily_stock_analysis/raw/main/docs/assets/readme_workspace_tour_20260510.gif)](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/assets/readme_workspace_tour_20260510.gif)

## ✨ 功能特性

| 能力 | 覆盖内容 |
| --- | --- |
| AI 决策报告 | 核心结论、评分、趋势、买卖点位、风险警报、催化因素、操作检查清单 |
| 多市场数据聚合 | A股、港股、美股、ETF：行情、K 线、技术指标、资金流、筹码、新闻、公告和基本面；日股/韩股（`.T` / `.KS` / `.KQ` ）：YFinance 日线与基础行情、技术指标可用， `capital_flow` 、 `dragon_tiger` 、 `boards` 与部分高阶区块会按市场边界降级为 `not_supported` （见 [市场支持边界](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/market-support.md) ） |
| Web / 桌面工作台 | 手动分析、任务进度、历史报告、完整 Markdown、回测、持仓、配置管理、浅色 / 深色主题 |
| Agent 策略问股 | 多轮追问，支持均线、缠论、波浪、趋势、热点、事件、成长、预期等 15 种内置策略，覆盖 Web/Bot/API |
| 智能导入与补全 | 图片、CSV/Excel、剪贴板导入；股票代码/名称/拼音/别名补全 |
| 自动化与推送 | GitHub Actions、Docker、本地定时任务、FastAPI 服务和企业微信/飞书/Telegram/Discord/Slack/邮件推送 |

> 功能细节、字段契约、基本面 P0 超时语义、交易纪律、数据源优先级、Web/API 行为请看 [完整配置与部署指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md) 。

### 技术栈与数据来源

| 类型 | 支持 |
| --- | --- |
| AI 模型 | [Anspire](https://open.anspire.cn/?share_code=QFBC0FYC) 、 [AIHubMix](https://aihubmix.com/?aff=CfMq) 、Gemini、OpenAI 兼容、DeepSeek、通义千问、Claude、Ollama 本地模型等 |
| 行情数据 | [TickFlow](https://tickflow.org/auth/register?ref=WDSGSPS5XC) 、AkShare、Tushare、Pytdx、Baostock、YFinance、Longbridge |
| 新闻搜索 | [Anspire](https://open.anspire.cn/?share_code=QFBC0FYC) 、 [SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis) 、 [Tavily](https://tavily.com/) 、 [Bocha](https://open.bocha.cn/) 、 [Brave](https://brave.com/search/api/) 、 [MiniMax](https://platform.minimaxi.com/) 、SearXNG |
| 社交舆情 | [Stock Sentiment API](https://api.adanos.org/docs) （Reddit / X / Polymarket，仅美股，可选） |

> 完整规则见 [数据源配置](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E6%95%B0%E6%8D%AE%E6%BA%90%E9%85%8D%E7%BD%AE) 。

## 🚀 快速开始

### 方式一：GitHub Actions（推荐）

> 5 分钟完成部署，零成本，无需服务器。

#### 1\. Fork 本仓库

点击右上角 `Fork` 按钮（顺便点个 Star⭐ 支持一下）

#### 2\. 配置 Secrets

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**AI 模型配置（至少配置一个）**

默认先选一个模型服务商并填写 API Key；需要多模型、图片识别、本地模型或高级路由时，再参考 [LLM 配置指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/LLM_CONFIG_GUIDE.md) 。

| Secret 名称 | 说明 | 必填 |
| --- | --- | --- |
| `ANSPIRE_API_KEYS` | [Anspire](https://open.anspire.cn/?share_code=QFBC0FYC) API Key，一Key同时启用全球热门大模型和联网搜索，无需科学上网，含免费额度 | **推荐** |
| `AIHUBMIX_KEY` | [AIHubMix](https://aihubmix.com/?aff=CfMq) API Key，一Key切换使用全系模型，无需科学上网，本项目可享 10% 优惠 | **推荐** |
| `GEMINI_API_KEY` | Google Gemini API Key | 可选 |
| `ANTHROPIC_API_KEY` | Anthropic Claude API Key | 可选 |
| `OPENAI_API_KEY` | OpenAI 兼容 API Key（支持 DeepSeek、通义千问等） | 可选 |
| `OPENAI_BASE_URL` / `OPENAI_MODEL` | 使用 OpenAI 兼容服务时填写 | 可选 |

> Ollama 更适合本地 / Docker 部署，GitHub Actions 推荐使用云端 API。

**通知渠道配置（至少配置一个）**

| Secret 名称 | 说明 |
| --- | --- |
| `WECHAT_WEBHOOK_URL` | 企业微信机器人 |
| `FEISHU_WEBHOOK_URL` | 飞书机器人 |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Telegram |
| `DISCORD_WEBHOOK_URL` | Discord Webhook |
| `SLACK_BOT_TOKEN` + `SLACK_CHANNEL_ID` | Slack Bot |
| `EMAIL_SENDER` + `EMAIL_PASSWORD` | 邮件推送 |

更多渠道、签名校验、分组邮件、Markdown 转图片等配置见 [通知渠道详细配置](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E9%80%9A%E7%9F%A5%E6%B8%A0%E9%81%93%E8%AF%A6%E7%BB%86%E9%85%8D%E7%BD%AE) 。

**自选股配置（必填）**

| Secret 名称 | 说明 | 必填 |
| --- | --- | --- |
| `STOCK_LIST` | 自选股代码，如 `600519,hk00700,AAPL,7203.T,005930.KS` | ✅ |

**新闻源配置（推荐）**

新闻源会显著影响舆情、公告、事件和催化因素质量，建议至少配置一个搜索服务。

| Secret 名称 | 说明 | 必填 |
| --- | --- | --- |
| `ANSPIRE_API_KEYS` | [Anspire AI Search](https://aisearch.anspire.cn/) ：中文内容特别优化，适合 A 股新闻和舆情检索；同一 Key 可复用为 Anspire 大模型 | **推荐** |
| `SERPAPI_API_KEYS` | [SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis) ：搜索引擎结果补强，适合实时金融新闻 | **推荐** |
| `TAVILY_API_KEYS` | [Tavily](https://tavily.com/) ：通用新闻搜索 API | 可选 |
| `BOCHA_API_KEYS` | [博查搜索](https://open.bocha.cn/) ：中文搜索优化，支持 AI 摘要 | 可选 |
| `BRAVE_API_KEYS` | [Brave Search](https://brave.com/search/api/) ：隐私优先，美股资讯补强 | 可选 |
| `MINIMAX_API_KEYS` | [MiniMax](https://platform.minimaxi.com/) ：结构化搜索结果 | 可选 |
| `SEARXNG_BASE_URLS` | SearXNG 自建实例：无配额兜底，适合私有部署 | 可选 |

更多搜索源、社交舆情和降级规则见 [搜索服务配置](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E6%90%9C%E7%B4%A2%E6%9C%8D%E5%8A%A1%E9%85%8D%E7%BD%AE) 。

#### 3\. 启用 Actions

`Actions` 标签 → `I understand my workflows, go ahead and enable them`

#### 4\. 手动测试

`Actions` → `每日股票分析` → `Run workflow` → `Run workflow`

#### 完成

默认每个\*\*工作日 18:00（北京时间）\*\*自动执行，也可手动触发。默认非交易日（含 A/H/US 节假日）不执行；强制运行、交易日检查、断点续传等规则见 [完整指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E9%85%8D%E7%BD%AE) 。

### 方式二：客户端配置教程 / 本地运行 / Docker 部署

```
# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env && vim .env

# 运行分析
python main.py
```

常用命令：

```
python main.py --debug
python main.py --dry-run
python main.py --stocks 600519,hk00700,AAPL
python main.py --market-review
python main.py --schedule
python main.py --serve-only
```

> Docker 部署、定时任务、云服务器访问请参考 [完整指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md) ；桌面客户端打包请参考 [桌面端打包说明](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/desktop-package.md) 。

## 📱 推送效果

### 决策仪表盘

```
🎯 2026-02-08 决策仪表盘
共分析3只股票 | 🟢买入:0 🟡观望:2 🔴卖出:1

📊 分析结果摘要
⚪ 中钨高新(000657): 观望 | 评分 65 | 看多
⚪ 永鼎股份(600105): 观望 | 评分 48 | 震荡
🟡 新莱应材(300260): 卖出 | 评分 35 | 看空

⚪ 中钨高新 (000657)
📰 重要信息速览
💭 舆情情绪: 市场关注其AI属性与业绩高增长，情绪偏积极，但需消化短期获利盘和主力流出压力。
📊 业绩预期: 基于舆情信息，公司2025年前三季度业绩同比大幅增长，基本面强劲，为股价提供支撑。

🚨 风险警报:

风险点1：2月5日主力资金大幅净卖出3.63亿元，需警惕短期抛压。
风险点2：筹码集中度高达35.15%，表明筹码分散，拉升阻力可能较大。
风险点3：舆情中提及公司历史违规记录及重组相关风险提示，需保持关注。
✨ 利好催化:

利好1：公司被市场定位为AI服务器HDI核心供应商，受益于AI产业发展。
利好2：2025年前三季度扣非净利润同比暴涨407.52%，业绩表现强劲。
📢 最新动态: 【最新消息】舆情显示公司是AI PCB微钻领域龙头，深度绑定全球头部PCB/载板厂。2月5日主力资金净卖出3.63亿元，需关注后续资金流向。

---
生成时间: 18:00
```

### 大盘复盘

```
🎯 2026-01-10 大盘复盘

📊 主要指数
- 上证指数: 3250.12 (🟢+0.85%)
- 深证成指: 10521.36 (🟢+1.02%)
- 创业板指: 2156.78 (🟢+1.35%)

📈 市场概况
上涨: 3920 | 下跌: 1349 | 涨停: 155 | 跌停: 3

🔥 板块表现
领涨: 互联网服务、文化传媒、小金属
领跌: 保险、航空机场、光伏设备
```

## ⚙️ 配置说明

完整环境变量、模型渠道、通知渠道、数据源优先级、交易纪律、基本面 P0 语义和部署说明请参考 [完整配置指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md) 。

## 🖥️ Web 界面

Web 工作台提供配置管理、任务监控、手动分析、历史报告、完整 Markdown 报告、Agent 问股、回测、持仓管理、智能导入和浅色 / 深色主题。启动方式：

```
python main.py --webui
python main.py --webui-only
```

访问 `http://127.0.0.1:8000` 即可使用。认证、智能导入、搜索补全、历史报告复制、云服务器访问等细节见 [本地 WebUI 管理界面](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E6%9C%AC%E5%9C%B0-webui-%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2) 。

## 🤖 Agent 策略问股

配置任意可用 AI API Key 后，Web `/chat` 页面即可使用策略问股；如需显式关闭可设置 `AGENT_MODE=false` 。

- 支持均线金叉、缠论、波浪理论、多头趋势、热点题材、事件驱动、成长质量、预期重估等内置策略
- 支持实时行情、K 线、技术指标、新闻和风险信息调用
- 支持多轮追问、会话导出、发送到通知渠道和后台执行
- 支持自定义策略文件与多 Agent 编排（实验性）

> Agent 具体参数、 `skill` 命名兼容、多 Agent 模式和预算护栏见 [完整指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/full-guide.md#%E6%9C%AC%E5%9C%B0-webui-%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2) 与 [LLM 配置指南](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/LLM_CONFIG_GUIDE.md) 。

> DSA 聚焦日常分析报告；下面两个同系列项目分别覆盖选股、策略验证与策略进化，适合按需延伸使用。它们当前独立维护，后续会优先探索与 DSA 的候选股导入、回测验证和报告联动。

| 项目 | 定位 |
| --- | --- |
| [AlphaSift](https://github.com/ZhuLinsen/alphasift) | 多因子选股与全市场扫描，用于从股票池中提取候选标的 |
| [AlphaEvo](https://github.com/ZhuLinsen/alphaevo) | 策略回测与自我进化，用于验证策略规则，并通过迭代探索策略参数与组合 |

## 📬 联系与合作

<table><tbody><tr><td width="92"><strong>合作邮箱</strong></td><td><a href="mailto:zhuls345@gmail.com">zhuls345@gmail.com</a><br>项目咨询、部署支持与功能扩展</td><td align="center" rowspan="3" width="148"><a href="http://xhslink.com/m/tU520DWCKT"><img src="https://github.com/ZhuLinsen/daily_stock_analysis/raw/main/docs/assets/xiaohongshu_tick.jpg" width="112"></a><br><sub>扫码关注小红书</sub></td></tr><tr><td width="92"><strong>小红书</strong></td><td><a href="http://xhslink.com/m/tU520DWCKT">欢迎关注小红书</a></td></tr><tr><td width="92"><strong>问题反馈</strong></td><td><a href="https://github.com/ZhuLinsen/daily_stock_analysis/issues">提交 Issue</a></td></tr></tbody></table>

## 📄 License

[MIT License](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/LICENSE) © 2026 ZhuLinsen

欢迎在二次开发或引用时注明本仓库来源，感谢支持项目持续维护。

## ⚠️ 免责声明

本项目仅供学习和研究使用，不构成任何投资建议。股市有风险，投资需谨慎。作者不对使用本项目产生的任何损失负责。