from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Создаем отдельный Router для описания
pravo_router = Router()


@pravo_router.message(Command("getpnn"))
async def pravonn_message(message: Message):
    user_id_firstname = message.from_user.first_name
    pnn_message = f"""
👑👑👑 <b>Внимание!</b> 👑👑👑\n
Для <b>{user_id_firstname}</b>
предоставлено <b>Правонанахуй</b>!
    """
    await message.answer(pnn_message, parse_mode="HTML")
    await message.delete()
