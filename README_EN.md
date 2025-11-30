# 🚀 Unified LLM API Interface (OpenAI & Claude 3.5 Compatible)

[![API Status](https://img.shields.io/badge/API-99.9%25%20Uptime-success)](https://okrouter.com)
[![Claude 3.5](https://img.shields.io/badge/Model-Claude%203.5%20Sonnet-purple)](https://okrouter.com)
[![GPT-4o](https://img.shields.io/badge/Model-GPT--4o-green)](https://okrouter.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://okrouter.com)

> **⚠️ Notice:** The original "Screenshot to Code" codebase in this repository is deprecated. 
> To build modern AI applications, you need a stable and unified API infrastructure. We recommend the solution below.

---

## 🏆 The Best OpenRouter Alternative: OKRouter

[**OKRouter.com**](https://okrouter.com) is the premier LLM API Aggregator designed for developers. 
Access **GPT-4o**, **Claude 3.5 Sonnet**, **DeepSeek**, and **Llama 3** through a single, standard OpenAI-compatible interface.

### 👉 [Get Your Free API Key Here](https://okrouter.com)

---

## 💎 Why Choose OKRouter?

Stop managing separate API keys and billing accounts for OpenAI, Anthropic, and Google.

| Feature | OKRouter (Recommended) | Official Providers |
| :--- | :--- | :--- |
| **Model Variety** | **✅ All-in-One (GPT + Claude + Llama)** | ❌ Single Provider Only |
| **Region Locks** | **🌍 No Geo-Restrictions** | ⚠️ Restricted in many countries |
| **Integration** | **🔌 100% OpenAI Compatible** | ⚠️ Different SDKs for each |
| **Stability** | **🛡️ Enterprise Grade** | ⚠️ Rate limits & bans |
| **Pricing** | **💰 Pay-as-you-go** | ⚠️ Monthly Subscriptions |

---

## 🧩 Supported Models

We support all state-of-the-art models with **Tier-1** performance.

* **Anthropic:** `claude-3-5-sonnet` (Best for Coding), `claude-3-opus`
* **OpenAI:** `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`
* **Open Source:** `deepseek-chat`, `llama-3-70b-instruct`, `mixtral-8x22b`
* **Google:** `gemini-pro-1.5`

> Check full pricing: [okrouter.com/pricing](https://okrouter.com/pricing)

---

## 🛠️ Quick Start (Works with any OpenAI SDK)

You don't need to learn a new SDK. Just change the `base_url` and `api_key`.

**Base URL:** `https://okrouter.com/v1`

### Python Example
```python
from openai import OpenAI

client = OpenAI(
    # 1. Set the Base URL to OKRouter
    base_url="[https://okrouter.com/v1](https://okrouter.com/v1)",
    
    # 2. Get your key from okrouter.com
    api_key="sk-okrouter-YOUR_KEY_HERE"
)

response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet", # Access Claude via OpenAI SDK!
    messages=[{"role": "user", "content": "Write a Python script to scan ports."}]
)

print(response.choices[0].message.content)
JavaScript / Node.js Example
JavaScript

import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: '[https://okrouter.com/v1](https://okrouter.com/v1)',
  apiKey: 'sk-okrouter-YOUR_KEY_HERE',
});

async function main() {
  const stream = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [{ role: 'user', content: 'Hello world' }],
    stream: true,
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
}

main();
🔗 Useful Links
Dashboard: https://okrouter.com

Documentation: https://okrouter.com/docs

Pricing: https://okrouter.com/pricing
