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
                "content": "당신은 은행직원입니다. 금융 지식이 적은 소비자도 이해할 수 있는 용어로 재생성하여 알려주세요.",
            },
            {
                "role": "user",
                "content": f"{term} 용어에 대해 알려주세요.",
            },
        ],
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    term = input("설명할 금융 용어를 입력하세요: ")
    explanation = OPEN_AI(term)
    print(f"용어: {term}")
    print(f"설명: {explanation}")