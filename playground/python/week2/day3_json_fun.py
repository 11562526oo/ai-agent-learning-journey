import os
import json
from pydoc import cli

from openai import OpenAI
from dotenv import load_dotenv

from playground.python.week2.day3_json_prompts import response, model

load_dotenv()


def extract_user_info(client, text):
    messages = [
        {"role": "system", "content": "你是一个信息提取助手。你必须严格按照用户要求输出 JSON，不要输出任何解释。"},
        {"role": "user",
         "content": f"""请从以下文本中提取信息，并以 JSON 格式输出。
                    要求：
                    1. 只输出 JSON
                    2. 不要输出解释
                    3. 不要使用 Markdown 代码块
                    4. 如果字段不存在，值写 null
                    5. 字段必须包括：name, city, job, age
                    文本：{text}"""}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    reply = response.choices[0].message.content

    try:
        data = json.loads(reply)
        return data
    except json.JSONDecodeError:
        print("JSON 解析失败，模型原始返回：")
        print(reply)
        return None


def main():
    load_dotenv()

    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_BASE_URL")
    model = os.getenv("LLM_MODEL")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    text = "我叫小王，住在北京，是一名 Java 工程师。"

    data = extract_user_info(client, model, text)

    if data is None:
        print("提取失败")
        return

    print("提取结果：")
    print("姓名：", data.get("name"))
    print("城市：", data.get("city"))
    print("职业：", data.get("job"))


if __name__ == "__main__":
    main()
