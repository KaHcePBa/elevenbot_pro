import logging

import openai
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dynaconf import LazySettings
from openai import AsyncOpenAI

# Simply import AsyncOpenAI instead of OpenAI and use await with each API call. More info: https://github.com/openai/openai-python?tab=readme-ov-file#async-usage

settings = LazySettings(
    settings_files=["settings.yaml", ".secrets.yaml"],  # Указываем YAML-файлы
    environments=True,  # Активируем поддержку окружений
    env="development"  # Устанавливаем окружение по умолчанию
)

# Создаем отдельный Router для описания
gpt_router = Router()

# Устанавливаем API-ключи
client = AsyncOpenAI(
    api_key=settings.OPENAI_APIKEY,  # This is the default and can be omitted
)


# ToDo
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
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
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
