import os

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv('DEEPSEEK_APIKEY'), base_url="https://api.deepseek.com")


# client = AsyncOpenAI(api_key=os.getenv('OPENAI_APIKEY'))


async def get_ai_response(user_question: str) -> str:
    """
    Accesses the OpenAI API and receives a response from the model.
    """
    try:
        response = await client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": "You are a friendly and helpful assistant. Your task is to answer users' questions in a "
                            "short, clear, polite and informative manner. If a user asks about something complicated, "
                            "try to explain it in simple words."},
                {"role": "user", "content": user_question}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during API request: {e}"
