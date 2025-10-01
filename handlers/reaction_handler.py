from aiogram import Router
from aiogram.types import Message

from app import get_random_year_message, year_greeting

react_router = Router()
PARSE_MODE = "HTML"

RESPONSES = {
    "всем привет": "Привет всем!",
    "@elevenchat_bot": "Слушаю, мой господин...",
    "здарова": "И тебе здарова, {user_fullname}!",
    "с новым годом": "{user_fullname}, {year_greeting}",
    "@elevenchat_bot что ты умеешь?": "А ты что умеешь, кожаный ублюдок?",
    "ждем": "А я жду выходных... но походу их у меня никогда не будет",
    "стакан": "Стаканный звон, стаканный звон, как много дум наводит он!",
    "картошки гэтаму хлопцу": "По просьбе {user_firstname} даю тебе картоху!"
}


@react_router.message()
async def react_message(message: Message):
    user_text = message.text.lower().strip()
    user_data = {
        "user_firstname": message.from_user.first_name,
        "user_fullname": message.from_user.full_name,
        "year_greeting": get_random_year_message(year_greeting),
    }

    if user_text in RESPONSES:
        await message.answer(RESPONSES[user_text].format(**user_data), parse_mode=PARSE_MODE)
        if user_text == "картошки гэтаму хлопцу":
            await message.answer_sticker(
                sticker='CAACAgIAAxkBAAEHHzhjtZjH2rDjxRheMMQM9aJBS0h-uQACcQADRA3PF9YqB3hPsRJeLQQ')
        return
