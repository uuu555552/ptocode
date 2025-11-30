<div align="right">

[**🇺🇸 English**](./README_EN.md) | [**🇨🇳 中文说明**](./README.md)

</div>

# 🚀 Next-Gen AI API: GPT-5, o4, Claude 4.5 & Gemini 3

[![API Status](https://img.shields.io/badge/API-Online-success)](https://okrouter.com)
[![Models](https://img.shields.io/badge/Models-GPT--5%20%7C%20o4%20%7C%20Claude%204.5-purple)](https://okrouter.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://okrouter.com)

> **⚠️ Notice:** The legacy code is deprecated.
> We recommend [**OKRouter**](https://okrouter.com) for accessing the state-of-the-art AI models of 2025 (**GPT-5, o4, Claude 4.5**) via a single interface.

---

## 🏆 The Ultimate Model Aggregator

[**OKRouter.com**](https://okrouter.com) allows developers to access **OpenAI (GPT-5, o4)**, **Anthropic (Claude 4.5)**, and **Google (Gemini 3)** through one unified, OpenAI-compatible API endpoint.

### 👉 [Get Your Free API Key](https://okrouter.com)

---

## 💎 Supported Providers & Models (2025)

Switch between the world's most powerful models instantly.

| Provider | Top Models | Best For |
| :--- | :--- | :--- |
| **OpenAI** | **GPT-5** / **o4** | 🚀 **AGI-level Intelligence**, Superior Reasoning |
| **Anthropic** | **Claude 4.5 Sonnet** | 💻 **Ultimate Coding**, Complex Systems |
| **Google** | **Gemini 3 Pro** | 📚 **Massive Context**, Multimodal Analysis |
| **xAI** | **Grok-3** | ⚡ **Real-time**, Uncensored |

---

## 🛠️ Quick Start

Access **Gemini 3** or **Claude 4.5** using the standard OpenAI SDK.

**Base URL:** `https://api.okrouter.com/v1`

### Python Example
```python
from openai import OpenAI

client = OpenAI(
    # Use the dedicated API endpoint
    base_url="[https://api.okrouter.com/v1](https://api.okrouter.com/v1)",
    api_key="sk-okrouter-YOUR_KEY"
)

# Access Claude 4.5 via OpenAI Client!
response = client.chat.completions.create(
    model="anthropic/claude-4.5-sonnet", 
    messages=[{"role": "user", "content": "Refactor this code using modern patterns."}]
)

print(response.choices[0].message.content)
🔗 Links
Dashboard: https://okrouter.com

Pricing: https://okrouter.com/pricing

🔍 Keywords
