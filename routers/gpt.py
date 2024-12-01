import asyncio
import os

import openai
from openai import AsyncOpenAI
from aiogram import F
from aiogram import Router
from aiogram.types import Message

# Создаем отдельный Router для описания
gpt_router = Router()

client = AsyncOpenAI()
# Устанавливаем API-ключ для OpenAI
openai.api_key = os.getenv('OPENAI_APIKEY')


async def get_gpt_response(user_question: str) -> str:
    """
    Обращается к OpenAI API и получает ответ от модели.
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при запросе к OpenAI API: {e}"


@gpt_router.message(F.text.startswith('/gpt'))
async def handle_gpt_command(message: Message):
    """
    Обрабатывает команду /gpt и отвечает пользователю.
    """
    # Извлекаем вопрос из команды
    user_question = message.text.lstrip('/gpt').strip()
    if not user_question:
        await message.answer("Пожалуйста, напишите вопрос после команды /gpt.")
        return

    await message.answer("Думаю над ответом...")
    gpt_response = await get_gpt_response(user_question)
    await message.answer(gpt_response)
