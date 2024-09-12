from openai import OpenAI

client = OpenAI(
    api_key = "sk-P3FtrVIy70fhrUNJzIzHPhNiAFW5XbV1goCaAIq2Q2oFBWNN",
    base_url = "https://api.moonshot.cn/v1",
)


def moonshot(user_prompt: str) -> str:
    system_prompt = f"分析以下项目，并生成项目的专业摘要和关键特性。"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    llm_response = client.chat.completions.create(
        messages=messages,
        model="moonshot-v1-128k",
        temperature=0.3,
        stream=False
    )
    
    llm_outputs = llm_response.choices[0].message.content
    return llm_outputs

if __name__ == "__main__":
    readme_content = "你好，我是一个测试项目。"

    generated_content = moonshot(readme_content)
    print(generated_content)