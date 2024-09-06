from openai import OpenAI

client = OpenAI(
    api_key="sk-0738f7176f0a44e8ae8bc1569c2b6032",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def qianwen(user_prompt: str) -> str:
    system_prompt = f"分析以下 GitHub 项目 README，并生成项目的专业摘要和关键特性。"
        
    response = client.chat.completions.create(
        model="qwen1.5-14b-chat",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt
            },
        ],
    )
    
    message = response.choices[0].message.content
    return message

if __name__ == "__main__":
    readme_content = "你好，我是一个测试项目。"

    generated_content = qianwen(readme_content)
    print(generated_content)