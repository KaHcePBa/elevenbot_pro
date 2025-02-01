from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Создаем отдельный Router для описания
description_router = Router()

desc_message = """
🌟 <b>Voice-recognition technology?</b> In a lift? In Scotland? 🌟\n
You ever tried voice-recognition technology? 🤔\n\n
👇 <b>Delivered functions:</b> 👇\n\n
1️⃣✅ <b><code>/weather city</code></b> — Get the current weather in the specified city. 🌤️\n\n
2️⃣❌ <i>[depreciated]</i> — Check birthdays and pin congratulations with notifications. 🎉\n\n
3️⃣❌ <i>[need billing]</i> <b><code>/gpt your question</code></b> — Ask ChatGPT a question. 🤖\n\n
✨ <u>More features coming soon!</u> ✨
"""


@description_router.message(Command("description"))
async def description_message(message: Message):
    await message.answer(desc_message, parse_mode="HTML")
    await message.delete()
