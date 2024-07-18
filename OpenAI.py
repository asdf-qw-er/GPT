from openai import OpenAI

def READ_API_KEY(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            return first_line
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."
    except Exception as e:
        return f"오류가 발생했습니다: {e}"
    
def OPEN_AI(term):
    client=OpenAI(
        api_key = READ_API_KEY('API_KEY.txt')
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": "",
            },
        ],
    )

    return completion.choices[0].message.content