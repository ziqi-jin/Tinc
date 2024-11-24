'''
@copyright ziqi-jin
'''

import requests
import json
from abc import ABC, abstractmethod

class ModelRequestBase(ABC):
    def __init__(self, model: str):
        self.model = model
        self.conversation_history = [dict(role="system", content="你是一个python代码生成器，你只可以输出可直接运行的代码及注释，不要加markdown格式，其他任何不能执行的内容均不可以出现，生成普通代码时，你的代码逻辑用类或函数封装，生成测试代码时，增加可以直接运行的主函数调用逻辑")]

    @abstractmethod
    def make_request(self, message: str):
        pass

    def add_message_to_history(self, message, role="user"):
        self.conversation_history.append({"role": role, "content": message})

class TheBAIModelRequest(ModelRequestBase):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        super().__init__(model)
        self.api_key = api_key
        self.url = "https://api.theb.ai/v1/chat/completions"
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def make_request(self, message: str):
        self.add_message_to_history(message)
        payload = json.dumps({
            "model": self.model,
            "messages": self.conversation_history,
            "stream": False,
            "model_params": {
                "temperature": 0
            }
        })
        response = requests.post(self.url, headers=self.headers, data=payload)
        
        if response.status_code == 200:
            data = response.json()
            self._handle_response(data)
            return data['choices'][0]['message']['content']
        else:
            response.raise_for_status()

    def _handle_response(self, data):
        if "choices" in data:
            choice = data["choices"][0]
            assistant_message = choice["message"]["content"]
            self.add_message_to_history(assistant_message, role="assistant")


if __name__ == "__main__":
    # Example usage
    api_key = ""
    model_request = TheBAIModelRequest(api_key=api_key)
    result = model_request.make_request("How are you?")
    print(result)

