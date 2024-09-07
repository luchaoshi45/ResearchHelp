from http import HTTPStatus
import dashscope
dashscope.api_key = 'sk-ff9595809dbd4f34bc83cb5eb69e76f6'

def qianwen(user_prompt: str) -> str:
    system_prompt = f"分析以下 GitHub 项目 README，并生成项目的专业摘要和关键特性。"
    
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ]

    response = dashscope.Generation.call(
        model='qwen-max',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    
    if response.status_code == HTTPStatus.OK:
        print(response)
        return response.output["choices"][0]["message"]['content']
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message)
        )
        return None
    
    # responses = dashscope.Generation.call(
    #     model='qwen-max',
    #     messages=messages,
    #     result_format='message',  # set the result to be "message" format.
    #     stream=True, # set streaming output
    #     incremental_output=True  # get streaming output incrementally
    # )

    # for response in responses:
    #     if response.status_code == HTTPStatus.OK:
    #         print(response.output.choices[0]['message']['content'],end='')
    #     else:
    #         print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
    #             response.request_id, response.status_code,
    #             response.code, response.message
    #         ))

    

# from openai import OpenAI

# client = OpenAI(
#     api_key="sk-ff9595809dbd4f34bc83cb5eb69e76f6",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )

# def qianwen(user_prompt: str) -> str:
#     system_prompt = f"分析以下 GitHub 项目 README，并生成项目的专业摘要和关键特性。"
        
#     response = client.chat.completions.create(
#         model="qwen-max",
#         messages=[
#             {
#                 "role": "system",
#                 "content": system_prompt,
#             },
#             {
#                 "role": "user",
#                 "content": user_prompt
#             },
#         ],
#     )
    
#     message = response.choices[0].message.content
#     return message

if __name__ == "__main__":
    readme_content = "你好，我是一个测试项目。"

    generated_content = qianwen(readme_content)
    print(generated_content)