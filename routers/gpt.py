import logging
import os
import openai
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Создаем отдельный Router для описания
gpt_router = Router()

# Устанавливаем API-ключ для OpenAI
openai.api_key = os.getenv('OPENAI_APIKEY')

@gpt_router.message(Command("gpt"))
async def gpt_response(message: Message):
    try:
        # Извлекаем вопрос пользователя
        question = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.answer("Вы забыли указать вопрос.")
        return

    try:
        # Асинхронный вызов ChatCompletion
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",  # Убедитесь, что используете доступную модель
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            max_tokens=500,
            temperature=0.7
        )

        # Извлекаем текст ответа
        answer = response["choices"][0]["message"]["content"]
        await message.answer(answer)

    except openai.OpenAIError as e:
        logging.error(f"Ошибка OpenAI: {e}")
        await message.answer("Произошла ошибка при обработке вашего запроса.")
