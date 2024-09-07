from http import HTTPStatus
import dashscope
dashscope.api_key = 'sk-978a327d56f9435facb229110240472e'

def bailian(user_prompt: str) -> str:
    system_prompt = f"分析以下项目，并生成项目的专业摘要和关键特性。"
    
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ]

    response = dashscope.Generation.call(
        model='qwen-vl-max-0809',
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

if __name__ == "__main__":
    readme_content = "你好，我是一个测试项目。"

    generated_content = bailian(readme_content)
    print(generated_content)