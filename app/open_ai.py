import os

from openai import AsyncOpenAI

# Ключ берём из переменной окружения
client = AsyncOpenAI(
    api_key=os.getenv('OPENAI_APIKEY')
)

# Системные инструкции (если не заданы – используем дефолтные)
instructions = os.getenv('INSTRUCTIONS')
model = os.getenv("MODEL_NAME", "gpt-4.1")


async def get_ai_response(user_question: str) -> str:
    """
    Делает запрос к OpenAI ChatGPT API и возвращает ответ.
    """
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": user_question}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:

        return f"Ошибка во время запроса: {e}"
