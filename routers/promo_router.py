# from aiogram import Router
# from aiogram.filters import Command
# from aiogram.types import Message
#
# # Create a separate Router for description
# promo_router = Router()
#
#
# # Connecting other handlers
# @promo_router.message(Command("promocodes"))
# async def promo_message(message: Message):
#     prm_message = """
# 🏎 Промокод <b>ELEVEN</b>
# для каршеринговых услуг <b>(Anytime, HELLO, Multimotors)</b>.
# Вводить промокод нужно <b>единоразово, при регистрации</b>.
#     """
#     await message.answer(prm_message, parse_mode="HTML")
#     await message.delete()


from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Create a separate Router for description
promo_router = Router()


# Function for retrieving text in the desired language
def get_localized_text(language_code, text_key):
    translations = {
        'ru': {
            'promo_title': '🏎 Промокод <b>ELEVEN</b>',
            'promo_description': 'для каршеринговых услуг <b>(Anytime, HELLO, Multimotors)</b>.',
            'promo_instruction': 'Вводить промокод нужно <b>единоразово, при регистрации</b>.',
        },
        'en': {
            'promo_title': '🏎 Promo code <b>ELEVEN</b>',
            'promo_description': 'for car-sharing services <b>(Anytime, HELLO, Multimotors)</b>.',
            'promo_instruction': 'The promo code must be entered <b>once, during registration</b>.',
        }
    }
    # Default is English, if the language is not supported
    return translations.get(language_code, translations['en']).get(text_key, '')


# Connecting other handlers
@promo_router.message(Command("promocodes"))
async def promo_message(message: Message):
    language_code = message.from_user.language_code or 'en'  # If the language is not specified, use English

    # Forming a message using localized text
    prm_message = (
        f"{get_localized_text(language_code, 'promo_title')}\n"
        f"{get_localized_text(language_code, 'promo_description')}\n"
        f"{get_localized_text(language_code, 'promo_instruction')}"
    )

    await message.answer(prm_message, parse_mode="HTML")
    await message.delete()
