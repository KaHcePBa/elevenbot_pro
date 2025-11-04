from aiogram import F, Router
from aiogram.types import Message

from app import get_ai_response

# Create a separate Router for description
ai_router = Router()


@ai_router.message(F.text.startswith('/ai'))
async def handle_ai_command(message: Message):
    # Извлекаем вопрос после команды
    user_question = message.text.lstrip('/ai').strip()
    if not user_question:
        await message.answer("Напишите вопрос после команды: /ai Ваш вопрос")
        return

    await message.answer("Думаю над ответом…")

    try:
        answer, provider = await get_ai_response(user_question)
        await message.answer(f"Источник: {provider}\n\n{answer}")
    except Exception as e:
        await message.answer(
            "К сожалению, сейчас оба провайдера недоступны или возникла ошибка при запросе.\n"
            f"Техническая деталь: {e}"
        )
