# -*- coding:utf-8 -*-
from typing import Awaitable, Callable
# -*- coding:utf-8 -*-
from typing import Awaitable, Callable, List
import requests
import json
from openai.types.chat import ChatCompletionMessageParam
from def_error import AuthenticationError
import time


# 定义一个类 NewGenerate
class NewGenerate:
    def __init__(self):
        pass

    # 异步方法: 获取聊天完整性结果
    async def get_chat_completion(self, messages: List[ChatCompletionMessageParam],
                                  api_key: str,
                                  base_url: str | None,
                                  callback: Callable[[str], Awaitable[None]],
                                  ) -> str:
        # 如果没有提供基础URL，则使用默认的OpenAI API地址
        if not base_url:
            base_url = "https://api.openai.com"
        url = "{}/v1/chat/completions".format(base_url)
        print("请求的URL是 {}".format(base_url))
        # 准备POST请求的负载数据
        payload = json.dumps({
            "model": "gpt-4-vision-preview",  # 模型名称
            "messages": messages,  # 消息列表
            "stream": True,  # 是否流式传输
            "max_tokens": 4096,  # 最大令牌数
            "temperature": 0  # 温度参数，控制随机性
        })
        # 准备请求头部信息
        headers = {
            'Authorization': 'Bearer {}'.format(api_key),  # API授权信息
            'Content-Type': 'application/json'  # 指定发送的数据类型为JSON
        }
        full_response = ""
        # 打印当前时间
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "-----")
        try:
            # 发起POST请求，并开启流式传输
            response = requests.request("POST", url, headers=headers, data=payload, stream=True)
        except Exception as e:
            # 如果请求发生异常，打印异常信息并返回空字符串
            print(e)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "连接失败")
            return ""
        # 处理请求响应
        if response.status_code == 200:
            # 流式读取响应内容
            for chunk in response.iter_lines():
                chunk = str(chunk, encoding="utf-8")
                if chunk.startswith("data: [DONE]"):
                    continue
                elif chunk.startswith("data"):
                    # 解析JSON数据
                    res = json.loads(chunk[5:])
                    if "content" in res["choices"][0]["delta"]:
                        if res["choices"][0]["delta"]["content"]:
                            sub_res = res["choices"][0]["delta"]["content"]
                            await callback(sub_res)  # 执行回调函数
                            full_response += sub_res  # 添加到完整响应字符串
                else:
                    pass
        elif response.status_code == 401:
            # 处理授权错误
            res = json.loads(response.text)
            if "error" in res:
                if res["error"]["type"] == "one_api_error":
                    response.close()
                    raise AuthenticationError("无效令牌")  # 抛出授权错误异常
        # 打印完整响应内容
        print(full_response)
        response.close()
        return full_response

    # 方法: 生成图像
    def generate_image(self, prompt: str, api_key: str, base_url: str) -> str:
        # 如果没有提供基础URL，则使用默认的OpenAI API地址
        if not base_url:
            base_url = "https://api.openai.com"
        # 图片生成的API地址
        url = "{}/v1/images/generations".format(base_url)
        # 准备POST请求的负载数据
        image_params = json.dumps({
            "model": "dall-e-3",  # 使用的生成模型
            "quality": "standard",  # 图片质量标准
            "style": "natural",  # 图片风格
            "n": 1,  # 生成图片的数量
            "size": "1024x1024",  # 图片尺寸
            "prompt": prompt,  # 提示信息
        })
        # 准备请求头部信息
        headers = {
            'Authorization': 'Bearer {}'.format(api_key),  # API授权信息
            'Content-Type': 'application/json'  # 指定发送的数据类型为JSON
        }
        # 打印当前时间和提示信息
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "开始", prompt)
        try:
            # 发起图片生成的POST请求
            response = requests.request("POST", url, headers=headers, data=image_params)
        except Exception as e:
            # 如果请求发生异常，打印异常信息并返回空字符串
            print(e)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "连接失败", prompt)
            return ""
        # 解析响应结果
        if response.status_code == 200:
            # 成功响应，解析JSON数据
            res = json.loads(response.text)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "成功", prompt)
            response.close()
            return res["data"][0]["url"]  # 返回生成的图片URL
        elif response.status_code == 401:
            # 处理授权错误
            res = json.loads(response.text)
            if "error" in res:
                if res["error"]["type"] == "one_api_error":
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "无效令牌", prompt)
                    response.close()
            return ""
        else:
            # 其他错误情况
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "失败", prompt)
            response.close()
            return ""

# import requests
# import json
# from typing import Awaitable, Callable, List
# from openai.types.chat import ChatCompletionMessageParam
# from def_error import AuthenticationError
# import time
# class NewGenerate:
#     def __init__(self):
#         pass
#     async def get_chat_completion(self, messages: List[ChatCompletionMessageParam],
#                                     api_key: str,
#                                     base_url: str | None,
#                                     callback: Callable[[str], Awaitable[None]],
#                                 ) -> str:
#
#         if not base_url:
#             base_url = "https://api.openai.com"
#         url = "{}/v1/chat/completions".format(base_url)
#         print("requests url is {}".format(base_url))
#         payload = json.dumps({
#         "model": "gpt-4-vision-preview",
#         "messages": messages,
#         "stream": True,
#         "max_tokens": 4096,
#         "temperature": 0
#         })
#         headers = {
#         'Authorization': 'Bearer {}'.format(api_key),
#         'Content-Type': 'application/json'
#         }
#         full_response = ""
#         print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"-----")
#         try:
#             response = requests.request("POST", url, headers=headers, data=payload, stream=True)
#         except Exception as e :
#             print(e)
#             print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"connection failed")
#             return ""
#         if response.status_code == 200:
#             for chunk in response.iter_lines():
#                 chunk = str(chunk, encoding = "utf-8")
#                 if chunk.startswith("data: [DONE]"):
#                     continue
#                 elif chunk.startswith("data"):
#                     res = json.loads(chunk[5:])
#                     if "content" in res["choices"][0]["delta"]:
#                         if res["choices"][0]["delta"]["content"]:
#                             sub_res = res["choices"][0]["delta"]["content"]
#                             await callback(sub_res)
#                             full_response += sub_res
#                 else:
#                     pass
#         elif response.status_code == 401:
#             res = json.loads(response.text)
#             if "error" in res:
#                 if res["error"]["type"] == "one_api_error":
#                     response.close()
#                     raise AuthenticationError("Invalid token")
#         print(full_response)
#         response.close()
#         return full_response
#
#     def generate_image(self,prompt: str, api_key: str, base_url: str) -> str:
#         if not base_url:
#             base_url = "https://api.openai.com"
#         url = "{}/v1/images/generations".format(base_url)
#         image_params = json.dumps({
#             "model": "dall-e-3",
#             "quality": "standard",
#             "style": "natural",
#             "n": 1,
#             "size": "1024x1024",
#             "prompt": prompt,
#         })
#         headers = {
#         'Authorization': 'Bearer {}'.format(api_key),
#         'Content-Type': 'application/json'
#         }
#         print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"start",prompt)
#         try:
#             response = requests.request("POST", url, headers=headers, data=image_params)
#         except Exception as e :
#             print(e)
#             print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"connection failed",prompt)
#             return ""
#         if response.status_code == 200:
#
#             res = json.loads(response.text)
#             print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"success",prompt)
#             response.close()
#             return res["data"][0]["url"]
#
#
#         elif response.status_code == 401:
#             res = json.loads(response.text)
#             if "error" in res:
#                 if res["error"]["type"] == "one_api_error":
#                     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"Invalid token",prompt)
#                     response.close()
#             return ""
#         else:
#
#             print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"failed",prompt)
#             response.close()
#             return ""
