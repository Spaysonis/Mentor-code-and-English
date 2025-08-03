from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def create_question(data,question=None, answer=None, ):

    prompt_reading = (
        "Прочитай следующий текст и задай мне 3–5 вопросов в зависимости от размера и полноты текста, "
        "чтобы проверить, как хорошо я его понял(а). Строго должны быть только вопросы!, "
        "но и не слишком сложными — ориентируйся на средний уровень понимания.\n\n"
        f"Текст:\n{data}"
    )

    prompt_chek_answer = (f"Проверь мои ответы по следующему тексту: {data}. Ниже — вопросы, которые ты задал по нему: {question}."
                          f"Оцени мои ответы в общем, укажи ошибки (если есть) не отвечай слишком развернуто вот мои ответы:\n {answer}")

    prompt = prompt_reading

    if answer is not None:
        prompt = prompt_chek_answer


    responses = client.models.generate_content(
        model="gemini-1.5-flash", contents=prompt
    )
    result = responses.text
    return result


