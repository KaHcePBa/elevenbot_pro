from aiogram import F, Router
from aiogram.types import Message

from app import get_ai_response

ai_router = Router()


@ai_router.message(F.text.startswith('/ai'))
async def handle_ai_command(message: Message):
    user_question = message.text.lstrip('/ai').strip()
    if not user_question:
        await message.answer("Напиши вопрос после команды: /ai Ваш вопрос")
        return

    await message.answer("Думаю что тебе ответить…")

    try:
        answer, provider = await get_ai_response(user_question)
        await message.answer(f"LLM: {provider}\n\n{answer}")
    except Exception as e:
        await message.answer(
            "Сейчас оба провайдера недоступны или возникла ошибка при запросе.\n"
            f"Техническая деталь: {e}"
        )
