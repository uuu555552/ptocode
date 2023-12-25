- ​                                                                                                                  [English](README.md)          [中文](CN.README.md)
- [**free-gpt4apikey**]   
- <a href="https://twitter.com/Stockqwe222" target="_blank" style="background-color: #1DA1F2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; cursor: pointer; font-size: 16px;">
        Follow me on Twitter!
    </a>
- <a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=gQtTFHCHgyXjsfcXgjKSPBPsNyCJrGDB&jump_from=webapi&authKey=1HpFhOgqS83goVf3Td009vpg09C31cCSRDQYvWeB7Gs5RpwVobiQDS0qAgEOtiq2">
    <img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="ptocode交流群" title="ptocode交流群">
    </a>群640541448

# PtoCode (Image to Code)

This is a simple application that can transform screenshots into HTML/Tailwind CSS code. It uses GPT-4 Vision to generate codes and DALL-E 3 to produce similar images. Now, you can also input a URL to clone an existing website!

🆕 [Try it here](https://dbbot.net) (use your own OpenAI key - **Your key must have access to GPT-4 Vision, see the [FAQs](#️-faqs) section below for details**). Or see the [Getting Started](#-getting-started) section below for a guide on local installation.

##  Getting Started

The application has a React/Vite frontend and a FastAPI backend. You will need an OpenAI API key with access to the GPT-4 Vision API.

To run the backend (I use Poetry for package management - if you haven't installed it, use the command `pip install poetry` to do so):

```
<TEXT>cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001
```

To run the frontend:

```
<TEXT>cd frontend
yarn
yarn dev
```

Open http://localhost:3000 to use the application.

If you wish to run the backend on a different port, you need to update the VITE_WS_BACKEND_URL in `frontend/.env.local`.

For debugging purposes, if you don't want to waste GPT4-Vision calls, you can run the backend in mock mode (this will play a pre-recorded response):

Use the tutorial: First set the configuration API key and address. The gpt4-v and dall-e-3 keys are required. If you don't sign up at https://api.ptocode.com get 100 code generation for free

![image-20231225090659658](C:\Users\49607\AppData\Roaming\Typora\typora-user-images\image-20231225090659658.png)

![image-20231225091018764](C:\Users\49607\AppData\Roaming\Typora\typora-user-images\image-20231225091018764.png)

## Frequently Asked Questions

- **How can I provide feedback?** For feedback, feature requests, and reporting bugs, you can open an issue or contact me in the qq group.

## Hosted Version

🆕 [Try it here](https://ptocode.com) (bring your own OpenAI key - **Your key must have access to GPT-4 Vision. See the [FAQ](#️-faqs) section for more details**).

感谢前辈 https://github.com/abi/screenshot-to-code