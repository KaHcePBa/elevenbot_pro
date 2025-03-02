from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

about_router = Router()

info_message = """
Voice-recognition technology?\nIn a lift? In Scotland? 🤔\n
👇 <b>Delivered functions:</b> 👇
1️⃣ <code>/weather city</code> to get weather 🌤️ for now
2️⃣️ <code>/ai your_question</code> ask AI (Deepseek 🤖) a question
✨ <i>More app coming soon!</i> ✨
"""


@about_router.message(Command("about"))
async def about_message(message: Message):
    await message.answer(info_message, parse_mode="HTML")
    await message.delete()
