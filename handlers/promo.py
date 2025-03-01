from collections import defaultdict

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

promo_router = Router()

TRANSLATIONS = {
    'ru': {
        'promo_title': '🏎 Промокод <b>ELEVEN</b>',
        'promo_description': 'для каршеринговых услуг <b>(Anytime, HELLO, Multimotors)</b>.',
        'promo_instruction': 'Вводить промокод нужно <b>единоразово, при регистрации</b>.',
    },
    'en': {
        'promo_title': '🏎 Promo code <b>ELEVEN</b>',
        'promo_description': 'for car-sharing features <b>(Anytime, HELLO, Multimotors)</b>.',
        'promo_instruction': 'The promo code must be entered <b>once, during registration</b>.',
    }
}

TRANSLATIONS = defaultdict(lambda: TRANSLATIONS['en'], TRANSLATIONS)


@promo_router.message(Command("promocodes"))
async def promo_message(message: Message):
    language_code = message.from_user.language_code or 'en'
    texts = TRANSLATIONS[language_code]

    prm_message = f"{texts['promo_title']}\n{texts['promo_description']}\n{texts['promo_instruction']}"

    await message.answer(prm_message, parse_mode="HTML")
    await message.delete()
