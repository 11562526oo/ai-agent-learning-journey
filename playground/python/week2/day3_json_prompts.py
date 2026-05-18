import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL")

client = OpenAI(api_key=api_key, base_url=base_url)

messages = [
    {"role": "system", "content": "你是一个信息提取助手。你必须严格按照用户要求输出 JSON，不要输出任何解释。"},
    {"role": "user",
     "content": """请从以下文本中提取信息，并以 JSON 格式输出。
                要求：
                1. 只输出 JSON
                2. 不要输出解释
                3. 不要使用 Markdown 代码块
                4. 如果字段不存在，值写 null
                5. 字段必须包括：name, city, job, age
                文本：我叫王敏，今年 28 岁，在成都做 UI 设计师。"""}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.9
)

reply = response.choices[0].message.content

print("模型原始返回：")
print(reply)

# data字典
try:
    data = json.loads(reply)
except json.JSONDecodeError:
    print("解析失败：模型返回的不是合法 JSON")
# json.dumps()  把 Python 对象 转成 JSON 字符串。

# job = data.get("job", "未知职业")
# print(job)

print("\n解析后的 Python 字典：")
print(data)

print("\n字段读取结果：")
print("姓名：", data["name"])
print("城市：", data["city"])
print("职业：", data["job"])
print("年龄：", data["age"])














