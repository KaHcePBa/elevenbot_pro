from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Create a separate Router for description
promo_router = Router()


# Connecting other handlers
@promo_router.message(Command("promocodes"))
async def promo_message(message: Message):
    prm_message = """
🏎 Промокод <b>ELEVEN</b>
для каршеринговых услуг <b>(Anytime, HELLO, Multimotors)</b>.
Вводить промокод нужно <b>единоразово, при регистрации</b>.
    """
    await message.answer(prm_message, parse_mode="HTML")
    await message.delete()
