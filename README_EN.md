<div align="right">

[**🇺🇸 English**](./README_EN.md) | [**🇨🇳 中文说明**](./README.md)

</div>

# 🚀 Next-Gen AI Aggregator: GPT-5, o4, Claude 4.5 & Gemini 3

[![API Status](https://img.shields.io/badge/API-99.9%25%20Uptime-success)](https://okrouter.com)
[![Models](https://img.shields.io/badge/Models-GPT--5%20%7C%20o4%20%7C%20Claude%204.5-purple)](https://okrouter.com)
[![Payment](https://img.shields.io/badge/Payment-Credit%20Card%20%7C%20Crypto-blue)](https://okrouter.com)

> **⚠️ Notice:** The legacy "screenshot-to-code" tool is deprecated.
> We recommend [**OKRouter**](https://okrouter.com) for accessing state-of-the-art AI models (**GPT-5, o4, Claude 4.5**) via a single, unified interface.

---

## 🏆 The Ultimate AI Gateway for Developers

[**OKRouter.com**](https://okrouter.com) simplifies AI integration. Stop managing separate API keys and billing accounts for OpenAI, Anthropic, and Google. 

Access all top-tier models through **one unified, OpenAI-compatible endpoint**.

### 👉 [Get Your Free API Key (No Credit Card Required)](https://okrouter.com)

---

## 💎 Why Global Developers Choose OKRouter?

We solve the fragmentation and restriction issues of official providers.

| Feature | OKRouter | Official Providers |
| :--- | :--- | :--- |
| **🌍 Region Locks** | **No Restrictions** (Access Claude 4.5 from EU/Asia) | ⚠️ Restricted in many countries |
| **💳 Payment** | **Crypto (USDT) & Credit Cards** | ⚠️ Strict Banking Requirements |
| **⚡ Integration** | **One SDK for All Models** | ❌ Different SDKs for each provider |
| **🧾 Billing** | **Unified Pay-As-You-Go** | ❌ Multiple Monthly Subscriptions |
| **🆔 Privacy** | **No Phone Verification / KYC** | ⚠️ Phone Number Required |

---

## 🚀 Supported Models (2025 Flagship)

Switch between models instantly by changing a single string in your code.

| Provider | Model ID | Best Use Case |
| :--- | :--- | :--- |
| **OpenAI** | `gpt-5` / `openai-o4` | 🧠 **AGI-Level Reasoning**, Complex Logic |
| **Anthropic** | `anthropic/claude-4.5-sonnet` | 💻 **SOTA Coding**, System Architecture |
| **Google** | `google/gemini-3-pro` | 📚 **10M+ Context Window**, Multimodal Analysis |
| **xAI** | `grok-3` | ⚡ **Real-time Knowledge**, Uncensored |

> 📊 [View Full Pricing & Model List](https://okrouter.com/pricing)

---

## 🛠️ Quick Start

You can use the standard **OpenAI SDK** (Python/Node.js) to access **Claude** or **Gemini**. No need to learn new libraries.

**Base URL:** `https://api.okrouter.com/v1`

### Python Example

```python
from openai import OpenAI

client = OpenAI(
    # 1. Point to OKRouter API Gateway
    base_url="[https://api.okrouter.com/v1](https://api.okrouter.com/v1)",
    # 2. Use your OKRouter Key
    api_key="sk-okrouter-YOUR_KEY_HERE"
)

# ✨ Magic: Access Claude 4.5 using OpenAI Client!
response = client.chat.completions.create(
    model="anthropic/claude-4.5-sonnet", 
    messages=[
        {"role": "system", "content": "You are a senior software engineer."},
        {"role": "user", "content": "Explain Quantum Computing to a 5-year-old."}
    ]
)

print(response.choices[0].message.content)
🔗 Resources
Dashboard: https://okrouter.com

API Documentation: https://okrouter.com/docs

Pricing: https://okrouter.com/pricing
