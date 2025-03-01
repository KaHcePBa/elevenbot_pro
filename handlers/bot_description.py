from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Create a separate Router for description
description_router = Router()

desc_message = """
<b>Voice-recognition technology?</b> In a lift? In Scotland?\nYou ever tried voice-recognition technology? 🤔\n
👇 Delivered functions: 👇
1️⃣✅ <b><code>/weather city</code></b> to get weather 🌤️ for now
2️⃣️✅ <b><code>/gpt your_question</code></b> ask DeepSeek a question. 🤖
✨ <i>More features coming soon!</i> ✨
"""


@description_router.message(Command("description"))
async def description_message(message: Message):
    await message.answer(desc_message, parse_mode="HTML")
    await message.delete()
