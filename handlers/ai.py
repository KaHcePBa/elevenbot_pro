from aiogram import F, Router
from aiogram.types import Message

from app import get_ai_response

# Create a separate Router for description
ai_router = Router()


@ai_router.message(F.text.startswith('/ai'))
async def handle_gpt_command(message: Message):
    # Extracting the question from the command
    user_question = message.text.lstrip('/ai').strip()
    if not user_question:
        await message.answer("Please write a question after the command /ai.")
        return

    await message.answer("Hold on, your request is being generated....")
    ai_response = await get_ai_response(user_question)
    await message.answer(ai_response)
