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

messages = [
    {"role": "system", "content": "你是一名专业、简洁、友好的 AI 助手。"}
]

MAX_HISTORY = 4

print("输入exit退出")

while True:
    user_input = input("\n你：")

    if user_input == "exit":
        print("BYE BYE")
        break

    if user_input.lower() == "messages":
        for i, msg in enumerate(messages):
            print(f"{i}: role={msg['role']},content={msg['content']}")
        continue

    messages.append({"role": "user", "content": user_input})
    # print("目前消息是这样的", messages)
    # 裁剪历史消息
    messages = [messages[0]] + messages[1:][-MAX_HISTORY:]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    print("\nAI：", assistant_reply)

    messages.append({"role": "assistant", "content": assistant_reply})
    # print("最后裁剪之前消息是这样的", messages)

    # 再裁剪一次，避免 assistant 回复加入后历史继续变长
    messages = [messages[0]] + messages[1:][-MAX_HISTORY:]
