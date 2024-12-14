from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Создаем отдельный Router для описания
description_router = Router()

desc_message = """
<b>Voice-recognition technology?</b> In a lift? In Scotland?\nYou ever tried voice-recognition technology?\n
👇 Delivered functions: 👇
1️⃣✅ <b>''' /weather city '''</b> to get weather for now
2️⃣❌ <i> [depreciated] </i> check birthdays and pin congrats with notify
3️⃣❌ <i> [need billing] </i> <b>''' /gpt your question '''</b> ChatGPT 
"""


@description_router.message(Command("description"))
async def description_message(message: Message):
    await message.answer(desc_message, parse_mode="HTML")
    await message.delete()
