# -*- coding:utf-8 -*-
from typing import Awaitable, Callable
import requests
import json
from typing import Awaitable, Callable, List
from openai.types.chat import ChatCompletionMessageParam
from def_error import AuthenticationError
import time
class NewGenerate:
    def __init__(self):
        pass
    async def get_chat_completion(self, messages: List[ChatCompletionMessageParam],
                                    api_key: str,
                                    base_url: str | None,
                                    callback: Callable[[str], Awaitable[None]],
                                ) -> str:
        
        if not base_url:
            base_url = "https://api.openai.com"
        url = "{}/v1/chat/completions".format(base_url)
        print("requests url is {}".format(base_url))
        payload = json.dumps({
        "model": "gpt-4-vision-preview",
        "messages": messages,
        "stream": True,
        "max_tokens": 4096,
        "temperature": 0
        })
        headers = {
        'Authorization': 'Bearer {}'.format(api_key),
        'Content-Type': 'application/json'
        }
        full_response = ""
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"-----")
        try:
            response = requests.request("POST", url, headers=headers, data=payload, stream=True)
        except Exception as e :
            print(e)
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"connection failed")
            return ""
        if response.status_code == 200:
            for chunk in response.iter_lines():
                chunk = str(chunk, encoding = "utf-8")
                if chunk.startswith("data: [DONE]"):
                    continue
                elif chunk.startswith("data"):
                    res = json.loads(chunk[5:])
                    if "content" in res["choices"][0]["delta"]:
                        if res["choices"][0]["delta"]["content"]:
                            sub_res = res["choices"][0]["delta"]["content"]
                            await callback(sub_res)
                            full_response += sub_res
                else:
                    pass
        elif response.status_code == 401:
            res = json.loads(response.text)
            if "error" in res:
                if res["error"]["type"] == "one_api_error":
                    response.close()
                    raise AuthenticationError("Invalid token")
        print(full_response)
        response.close()
        return full_response

    def generate_image(self,prompt: str, api_key: str, base_url: str) -> str:
        if not base_url:
            base_url = "https://api.openai.com"
        url = "{}/v1/images/generations".format(base_url)
        image_params = json.dumps({
            "model": "dall-e-3",
            "quality": "standard",
            "style": "natural",
            "n": 1,
            "size": "1024x1024",
            "prompt": prompt,
        })
        headers = {
        'Authorization': 'Bearer {}'.format(api_key),
        'Content-Type': 'application/json'
        }
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"start",prompt)
        try:
            response = requests.request("POST", url, headers=headers, data=image_params)
        except Exception as e :
            print(e)
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"connection failed",prompt)
            return ""
        if response.status_code == 200:
            
            res = json.loads(response.text)
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"success",prompt)
            response.close()
            return res["data"][0]["url"]

                    
        elif response.status_code == 401:
            res = json.loads(response.text)
            if "error" in res:
                if res["error"]["type"] == "one_api_error":
                    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"Invalid token",prompt)
                    response.close()
            return ""
        else:

            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"failed",prompt)
            response.close()
            return ""
