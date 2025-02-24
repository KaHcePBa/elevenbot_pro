from aiogram import Router
from aiogram.types import Message
from services.year_service import get_random_year_message, year_message  # Импорт роутера с рандомным текстом

# Create a separate Router for description
react_router = Router()

# Handling arbitrary messages
@react_router.message()
async def react_message(message: Message):
    user_message = message.text.lower()
    user_id_firstname = message.from_user.first_name
    user_id_fullname = message.from_user.full_name

    if 'всем привет' in user_message:
        await message.answer(f'Привет всем!', parse_mode="HTML")
    elif '@elevenchat_bot' == user_message:
        await message.answer(f'Слушаю, мой господин...', parse_mode="HTML")
    elif 'белвэб' in user_message:
        await message.answer(f'БелВЭБ! Звонят колокола!', parse_mode="HTML")
    elif 'здарова' in user_message:
        await message.answer(f'И тебе здарова, {user_id_fullname}!', parse_mode="HTML")
    elif 'с новым годом' in user_message:
        await message.answer(f'{user_id_fullname}, {get_random_year_message(year_message)}', parse_mode="HTML")
    elif '@elevenchat_bot что ты умеешь?' in user_message:
        await message.answer(f'А ты что умеешь, кожаный ублюдок?', parse_mode="HTML")
    elif 'ждем' in user_message:
        await message.reply(f'А я жду выходных... но походу их у меня никогда не будет', parse_mode="HTML")
    elif 'стакан' in user_message:
        await message.answer(f'Стаканный звон, стаканный звон, как много дум наводит он!', parse_mode="HTML")
    elif 'картошки гэтаму хлопцу' == user_message:
        await message.answer(f'По просьбе {user_id_firstname} даю тебе картоху!', parse_mode="HTML")
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHHzhjtZjH2rDjxRheMMQM9aJBS0h-uQACcQADRA3PF9YqB3hPsRJeLQQ')
