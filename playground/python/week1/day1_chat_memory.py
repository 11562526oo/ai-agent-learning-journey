import json
import os
from dotenv import load_dotenv
from openai import OpenAI
# 读取配置文件
load_dotenv()

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL")
# 创建openai通用客户端
client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)
# 定义系统角色
messages = [
    {"role": "system", "content": "你是一名专业、简洁、友好的 AI 助手。"}
]

print("输入 quit 退出程序。")
# 循环填充历史消息
while True:
    user_input = input("\n你:")

    if user_input.lower() == "quit":
        print("聊天结束")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )

    assistant_response = response.choices[0].message.content
    print("\nAI: ", assistant_response)

    messages.append({"role": "assistant", "content": assistant_response})
    print(json.dumps(messages, ensure_ascii=False, indent=2))

