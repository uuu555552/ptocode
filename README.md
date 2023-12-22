- ​                                                                                                                         [English](README.md) [中文](CN.README.md)
- [**free-gpt4apikey**]   
- <a href="https://twitter.com/Stockqwe222" target="_blank" style="background-color: #1DA1F2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; cursor: pointer; font-size: 16px;">
        Follow me on Twitter!
    </a>
- <a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=gQtTFHCHgyXjsfcXgjKSPBPsNyCJrGDB&jump_from=webapi&authKey=1HpFhOgqS83goVf3Td009vpg09C31cCSRDQYvWeB7Gs5RpwVobiQDS0qAgEOtiq2">
    <img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="ptocode交流群" title="ptocode交流群">
    </a>加群640541448领取免费gpt4,dall

# PtoCode（图片转代码）

这是一个简单的应用，能将屏幕截图转化为HTML/Tailwind CSS代码。它使用GPT-4 Vision生成代码，并使用DALL-E 3生成相似的图片。现在，你还可以输入一个URL来克隆一个现有的网站！

🆕 [在此试用](https://dbbot.net)（需要使用你自己的OpenAI密匙 - **你的密匙必须拥有访问GPT-4 Vision的权限，详情请查看下方的[常见问题](#️-faqs)部分**）。或者查看下方的[开始使用](#-getting-started)部分获取本地安装指南。

## 🛠 开始使用

该应用程序有一个React/Vite前端和一个FastAPI后端。你将需要一个有权访问GPT-4 Vision API的OpenAI API密钥。

运行后端（我使用Poetry进行包管理 - 如果你没有安装它，使用`pip install poetry`命令进行安装）：

```
cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001
```

运行前端:

```
cd frontend
yarn
yarn dev
```

打开 http://localhost:3000来使用应用程序。

如果你希望在不同的端口运行后端，需要更新`frontend/.env.local`中的VITE_WS_BACKEND_URL。

为了调试目的，如果你不想浪费GPT4-Vision的调用次数，你可以在模拟模式下运行后端（这将会播放一个预先录制的响应）：

## Docker

如果你的系统上已经安装了Docker，在根目录下，运行以下命令：

```
<BASH>echo "OPENAI_API_KEY=sk-your-key" > .env
docker-compose up -d --build
```

应用程序将在 http://localhost:3000上运行。注意，你不能使用这个设置来开发应用程序，因为文件的改变不会触发重建。

##  常见问题解答

- **我如何提供反馈?** 对于反馈、功能请求和报告错误，可以开一个问题反馈或在 qq群 上联系我。

##  托管版本

🆕 [在此处尝试](https://dbbot.net) (自带你的OpenAI密钥 - **你的密钥必须具有对GPT-4 Vision的访问权限。查看 [FAQ](#️-faqs) 部分获取详细信息**). 
