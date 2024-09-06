import openai

openai.api_key = 'sk-TA1eIqqydtm1695499D7795bB64b4f0180B0B222A425E83e'
openai.base_url = "https://free.gpt.ge/v1/"
openai.default_headers = {"x-foo": "true"}

def chatgpt(user_prompt: str) -> str:
    system_prompt = f"Analyze the following GitHub project README" + \
        "and generate a professional summary and key features of the project."
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    llm_response = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        max_tokens=2048,
        temperature=0.0,
        stream=False
    )
    
    llm_outputs = llm_response.choices[0].message.content
    return llm_outputs

if __name__ == "__main__":
    readme_content = "Hi, I am a test project."

    generated_content = chatgpt(readme_content)
    print(generated_content)