from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Создаем отдельный Router для описания
description_router = Router()


@description_router.message(Command("description"))
async def description_message(message: Message):
    desc_message = """
<b>Voice-recognition technology?</b> In a lift? In Scotland? You ever tried voice-recognition technology?\n
👇 Delivered functions:
1️⃣✅ <b>''' /weather city '''</b> to get weather for now
2️⃣❌ (depreciated) checking birthdays of everyone and pin congrats with notification
3️⃣❌ <b>''' /gpt your question '''</b> to get info from ChatGPT
    """
    await message.answer(desc_message, parse_mode="HTML")
    await message.delete()