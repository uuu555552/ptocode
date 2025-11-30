<div align="right">

[**🇺🇸 English**](./README_EN.md) | [**🇨🇳 中文说明**](./README.md)

</div>

# 🚀 全能大模型聚合 (GPT-5, o4, Claude 4.5, Gemini 3)

[![API Status](https://img.shields.io/badge/API-Online-success)](https://okrouter.com)
[![Models](https://img.shields.io/badge/Models-GPT--5%20%7C%20o4%20%7C%20Claude%204.5-blue)](https://okrouter.com)
[![Payment](https://img.shields.io/badge/支付-支付宝%2F微信-07c160.svg)](https://okrouter.com)

> ⚠️ **项目公告：** 原“截图转代码”代码已过时。
> 想要体验最新的 **GPT-5, OpenAI o4, Claude 4.5**？请使用下方的终极 API 解决方案。

---

## 🏆 OKRouter: 首发支持下一代 AI 模型

[**OKRouter.com**](https://okrouter.com) 是国内首家支持 **GPT-5** 和 **Claude 4.5** 的企业级聚合平台。
我们打破了账号封禁和地域限制，通过**统一的 OpenAI 格式接口**，让你抢先接入全球最强模型。

### 👉 [立即注册领取测试 Key (支持 GPT-5)](https://okrouter.com)

---

## 💎 2025 旗舰模型支持

无需等待官方排队，OKRouter 一个 Key 即可调用所有 T0 级模型：

| 厂商 (Provider) | 核心模型 (Latest Models) | 实力定位 |
| :--- | :--- | :--- |
| **OpenAI** | **GPT-5** <br> **OpenAI o4** (推理皇) | 🚀 **AGI 级智能**，逻辑推理天花板，碾压 o1。 |
| **Anthropic** | **Claude 4.5 Sonnet** <br> Claude 4.5 Opus | 🌟 **代码生成之神**，复杂工程能力远超 3.5。 |
| **Google** | **Gemini 3 Pro** <br> Gemini 3 Flash | 📚 **超长记忆 (10M Token)**，多模态理解新标杆。 |
| **xAI** | **Grok-3** | ⚡ 实时推特信息流，无审查，风格犀利。 |

> 📊 查看实时价格表：[okrouter.com/pricing](https://okrouter.com/pricing)

---

## 🚀 为什么选择 OKRouter？

1.  **国内首发 GPT-5/o4：** 当官方还在对国内封锁时，我们已经完成了企业级专线接入。
2.  **Claude 4.5 直连：** 完美解决 Anthropic 极其严格的封号问题。
3.  **独立 API 域名：** 采用 `api.okrouter.com` 专用线路，稳定性更高。
4.  **按量付费：** 支持 **支付宝 / 微信**，拒绝 200 美元的订阅费，用多少充多少。

---

## 🛠️ 接入示例 (Python)

演示如何通过 OKRouter 调用最新的 **OpenAI o4** 或 **Claude 4.5**。

**⚠️ 注意：API 请求地址已更新为 `api.okrouter.com`**

```python
from openai import OpenAI

client = OpenAI(
    # 关键配置：使用专用的 API 域名
    base_url="[https://api.okrouter.com/v1](https://api.okrouter.com/v1)",
    api_key="sk-你的密钥" # 去官网 okrouter.com 免费领
)

# ✨ 随意切换 2025 最新模型
# 选项: "gpt-5", "openai-o4", "anthropic/claude-4.5-sonnet", "google/gemini-3-pro"
model_id = "gpt-5" 

response = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "system", "content": "You are a helpful assistant from 2025."},
        {"role": "user", "content": "What is the difference between GPT-5 and o4?"}
    ]
)

print(f"Response from {model_id}:")
print(response.choices[0].message.content)
🔗 快速通道
⚡️ 官网注册: https://okrouter.com

📖 开发文档: https://okrouter.com/docs
