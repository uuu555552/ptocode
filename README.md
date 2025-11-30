# 🚀 Free OpenAI & Claude 3.5 API (国内直连/无需梯子)

[![API Status](https://img.shields.io/badge/API-Online-success)](https://okrouter.com)
[![Claude 3.5](https://img.shields.io/badge/Model-Claude%203.5%20Sonnet-purple)](https://okrouter.com)
[![GPT-4o](https://img.shields.io/badge/Model-GPT--4o-green)](https://okrouter.com)
[![Payment](https://img.shields.io/badge/支持-微信%2F支付宝-blue)](https://okrouter.com)

> **🔴 重要通知：** 本仓库原有代码已过时。如果你正在寻找**稳定、便宜、国内可直连**的大模型 API 接口（支持 GPT-4o, Claude 3.5, DeepSeek 等），请直接使用下方推荐的终极解决方案。

---

## 🏆 2025年国内最佳 LLM API 解决方案：OKRouter

[**OKRouter.com**](https://okrouter.com) 是专为中国开发者打造的企业级大模型聚合平台。如果你受够了封号、网络超时和复杂的信用卡支付，这里是你唯一的选择。

### 👉 [点击这里：立即注册领取免费 API Key](https://okrouter.com)

---

## 💎 核心优势 (Why OKRouter?)

我们解决了国内开发者对接 AI 时的所有痛点：

| 特性 | OKRouter (推荐) | 官方 OpenAI/Anthropic | 其他二道贩子 |
| :--- | :--- | :--- | :--- |
| **网络连接** | **🚀 国内直连 (毫秒级)** | ❌ 需自备梯子/容易超时 | ⚠️ 极其不稳定 |
| **Claude 3.5** | **✅ 完美支持 (写代码神器)** | ❌ 国内无法申请/封号严重 | ⚠️ 经常掺假/降智 |
| **支付方式** | **✅ 支付宝 / 微信** | ❌ 仅限国外信用卡 | ❌ 仅限 USDT |
| **价格** | **💰 按量付费 (无过期)** | ⚠️ 需绑定高额信用卡 | ⚠️ 价格虚高 |
| **账号安全** | **🛡️ 永不封号** | ❌ 随时可能封禁 | ⚠️ 随时跑路 |

---

## 🧩 支持模型全家桶

一个 Key，调用全网所有顶尖模型。完全兼容 OpenAI SDK 格式。

* **Anthropic Claude 系列:**
    * `claude-3-5-sonnet` (编程能力最强，Cursor 完美替代)
    * `claude-3-opus`
* **OpenAI GPT 系列:**
    * `gpt-4o` / `gpt-4o-mini`
    * `gpt-4-turbo`
* **Gemini 系列:**
  * `gemini-3-pro`
* **国产/开源之光:**
    * `deepseek-chat` (DeepSeek V3)
    * `llama-3-70b`


---

## 🛠️ 接入教程 (只需 1 分钟)

无论你使用的是 Python, Node.js, 还是开源软件 (如 ChatBox, NextChat, LobeChat)，接入方式完全一致。

**接口地址 (Base URL):** `https://api.okrouter.com/v1`
**API Key:** `sk-你的密钥`

### Python 示例
```python
from openai import OpenAI

client = OpenAI(
    base_url="[https://api.okrouter.com/v1](https://api.okrouter.com/v1)",
    api_key="sk-你的密钥" # 去官网 okrouter.com 免费领
)

response = client.chat.completions.create(
    model="anthropic/claude-4.5-sonnet", # 尽情使用 Claude 3.5
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
