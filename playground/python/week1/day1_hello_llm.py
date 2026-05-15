import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

response = client.chat.completions.create(
    model=model,
    # messages 是对话内容列表
    # system：给模型设定角色
    # user：用户真正提出的问题
    messages=[
        {"role": "system", "content": "你是一名严格的技术导师，说话直接，不要套话。"},
        {"role": "user", "content": "我的第一次调用大模型，HELLO WORLD LLM!!"}
    ],
    # 热度 temperature 越高，回答越发散；越低，回答越稳定
    temperature=0.9
)

print("===模型输出===")
print(response.choices[0].message.content)
