import asyncio
import datetime
import logging
from decimal import Decimal, ROUND_HALF_UP

import aioschedule
import dynaconf
import openai
from aiogram import Bot, Dispatcher, types, executor

from services import weather
from services.random_message import get_random_message  # Импорт функции возвращающей рандомное сообщение посыла
from services.random_message import nah_message  # Импорт списка сообщений из которых рандомно выбирается одно

##
openai.api_key = dynaconf.settings.OPENAI_APIKEY
# openai.api_key = os.getenv('OPENAI_APIKEY')

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')

# Set startlogging message
logging.info('Start running...')  # set startlogging message

# Initialize bot and dispatcher
bot = Bot(dynaconf.settings.BOT_TOKEN)
# bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


# Work with commands (needs registration in BotFather)
@dp.message_handler(commands=['description'])
async def description_message(message: types.Message):
    desc_message = """
<b>Voice-recognition technology?</b> In a lift? In Scotland? You ever tried voice-recognition technology?\n
👇 Delivered functions:
1️⃣ enter the command <b>''' /weather city '''</b> to get weather for now
2️⃣ checking birthdays of everyone and pin congrats with notification
3️⃣ enter the command <b>''' /gpt your question '''</b> to get info from ChatGPT (update: token is expired)
    """
    await message.answer(f'{desc_message}', parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['promocodes'])
async def promo_message(message: types.Message):
    prm_message = """
🏎 Промокод <b>ELEVEN</b>
для каршеринговых услуг <b>(Anytime, HELLO, Multimotors)</b>.
Вводить промокод нужно <b>единоразово, при регистрации</b>.
    """
    await message.answer(f'{prm_message}', parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['getpnn'])
async def pravonn_message(message: types.Message):
    user_id_firstname = message.from_user.first_name
    pnn_message = f"""
👑👑👑 <b>Внимание!</b> 👑👑👑\n
Для <b>{user_id_firstname}</b>
предоставлено <b>Правонанахуй</b>!
    """
    await message.answer(f'{pnn_message}', parse_mode="HTML")
    await message.delete()


# Work with commands (don`t needs registration in BotFather)
@dp.message_handler(commands=["gpt"])  # ChatGPT
async def gpt_response(message: types.Message):
    chat_id = message.chat.id

    question = message.text.split(" ", maxsplit=1)[1]
    prompt = (f"Answer the question : {question}")
    completions = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )

    message = completions.choices[0].text
    await bot.send_message(chat_id, text=message)


@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    # chat_id = message.chat.id
    city_name = message.text.split()[1]
    weather_data = weather.get_weather(city_name)
    code = weather_data['cod']  # код ошибки если не найден запрашиваемый город
    random_message = get_random_message(nah_message)  # рандомное сообщение, если не найден город

    if code != '404':
        temperature = Decimal(weather_data['main']['temp'])  # Текст превращаем в дробное число
        feels_like = Decimal(weather_data['main']['feels_like'])
        temperature = temperature.quantize(Decimal('1'), rounding=ROUND_HALF_UP)  # Округление по правилам математики
        feels_like = feels_like.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']

        wind_degree = weather_data['wind']['deg']
        wind_direction = weather.get_wind_direction(wind_degree)

        city = str.upper(weather_data['name'])

        # Get weather icon
        # icon = weather_data['weather'][0]['icon']
        # url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        # response = requests.get(url)
        # open("icon.png", "wb").write(response.content)

        reply_text = f'🌍 <b>{city}</b>\n' \
                     f'<i>{weather_description}</i>\n' \
                     f'\n' \
                     f'🌡 <b>Температура:</b> {temperature}°C\n' \
                     f'🌡 <b>Ощущается:</b> {feels_like}°C\n' \
                     f'🚿 <b>Влажность:</b> {humidity}%\n' \
                     f'🌬 <b>Ветер:</b> {wind_speed} m/s\n' \
                     f'🌬 <b>Направление:</b> {wind_direction}'

        await message.answer(reply_text, parse_mode="HTML")
        await message.delete()

        # Отправка иконки как картинку сразу за текстовым сообщением
        # with open("icon.png", "rb") as image:
        #     await bot.send_photo(chat_id=chat_id, photo=image)

    else:
        await message.reply(f'{random_message}')
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHZBljzZYeCnL_jRZDkG8KvkDAA1G1EAACggIAAi8P8AZ2H-Y5MFDEQS0E')


# Work with user message


@dp.message_handler()
async def react_message(message: types.Message):
    # Identificators
    user_message = str.lower(message.text)
    user_id = message.from_user.id
    user_id_firstname = message.from_user.first_name
    user_id_fullname = message.from_user.full_name

    if 'всем привет' in user_message:
        await message.answer(f'Привет всем!', parse_mode="HTML")
    elif '@elevenchat_bot' == user_message:
        await message.answer(f'Слушаю, мой господин...', parse_mode="HTML")
    elif 'белвэб' in user_message:
        await message.answer(f'БелВЭБ! Звонят колокола!', parse_mode="HTML")
    elif 'здарова' in user_message:
        await message.answer(f'И тебе здарова,{user_id_fullname}!', parse_mode="HTML")
    elif '@elevenchat_bot что ты умеешь?' in user_message:
        await message.answer(f'А ты что умеешь, кожаный ублюдок?', parse_mode="HTML")
    elif 'ждем' in user_message:
        await message.reply(f'А я жду выходных... но походу их у меня никогда не будет', parse_mode="HTML")
    elif 'стакан' in user_message:
        await message.answer(f'Стаканный звон, стаканный звон, как много дум наводит он!', parse_mode="HTML")
    elif set(dynaconf.settings.FORBIDDEN_WORDS) & set(
            # elif set(os.getenv('FORBIDDEN_WORDS')) & set(
            user_message.split()):  # search words from list 'forbidden_words' in user_message
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHHh9jtQ9Gds_m9MwvqWvtkP2fabQDuwACYAADTlzSKftFyO1xnR2cLQQ')
    elif 'картошки гэтаму хлопцу' == user_message:
        await message.answer(f'По просьбе {user_id_firstname} даю тебе картоху!', parse_mode="HTML")
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHHzhjtZjH2rDjxRheMMQM9aJBS0h-uQACcQADRA3PF9YqB3hPsRJeLQQ')


# -------- Send eleven message and check birthdays once per day

@dp.message_handler()
async def eleven_message():  # функция отправки сообщения в чат
    await bot.send_message(chat_id=dynaconf.settings.CHAT_ID,
                           # await bot.send_message(chat_id=os.getenv('CHAT_ID'),
                           text=f'<b>11:11, ёпта! Время ЭЛЭВЕН!</b>', parse_mode="HTML")


@dp.message_handler()
async def pin_birthday():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    today_key = today.strftime("%d%m")  # получаем сегодняшнюю дату в формате DDMM
    yesterday_key = yesterday.strftime("%d%m")  # получаем вчерашнюю дату в формате DDMM

    if today_key == '0103' and yesterday_key == '2802':  # пока костыльная обработка невисокосного года
        false_today_key = '2902'
        user_name = dynaconf.settings.BIRTHDAYS[false_today_key]  # парсим имя именинника из словаря по ключу даты
        # user_name = os.getenv('BIRTHDAYS')[false_today_key]  # парсим имя именинника из словаря по ключу даты
        message = await bot.send_message(chat_id=dynaconf.settings.CHAT_ID,
                                         # message = await bot.send_message(chat_id=os.getenv('CHAT_ID'),
                                         text=f"🥳🥳🥳 С днем рождения, {user_name}! 🥳🥳🥳")
        await bot.pin_chat_message(chat_id=dynaconf.settings.CHAT_ID, message_id=message.message_id,
                                   # await bot.pin_chat_message(chat_id=os.getenv('CHAT_ID'), message_id=message.message_id,
                                   disable_notification=False)  # пишем и закрепляем сообщение
    elif today_key in dynaconf.settings.BIRTHDAYS.keys():
        user_name = dynaconf.settings.BIRTHDAYS[today_key]  # парсим имя именинника из словаря по ключу даты
        # elif today_key in os.getenv('BIRTHDAYS').keys():
        #     user_name = os.getenv('BIRTHDAYS')[today_key]  # парсим имя именинника из словаря по ключу даты
        message = await bot.send_message(chat_id=dynaconf.settings.CHAT_ID,
                                         # message = await bot.send_message(chat_id=os.getenv('CHAT_ID'),
                                         text=f"🥳🥳🥳 С днем рождения, {user_name}! 🥳🥳🥳")
        await bot.pin_chat_message(chat_id=dynaconf.settings.CHAT_ID, message_id=message.message_id,
                                   # await bot.pin_chat_message(chat_id=os.getenv('CHAT_ID'), message_id=message.message_id,
                                   disable_notification=False)  # пишем и закрепляем сообщение


# Планирование джобов
async def scheduler_msg():  # функция планирования отправки сообщения в определенное время
    aioschedule.every().day.at("08:11").do(eleven_message)  # UTC отправка сообщения элевен
    aioschedule.every().day.at("06:00").do(pin_birthday)  # UTC отправка и закрепление поздравления с ДР
    while True:
        await aioschedule.run_pending()  # задача постоянно выполняется
        await asyncio.sleep(1)  # через сколько секунд переключиться на другую задачу (в секундах)


# Function at start
async def on_startup(_):  # создаем задачу на сервере сразу после запуска бота
    asyncio.create_task(scheduler_msg())  # конкурентный контроль выполнения функций


# --------- End eleven message once per day


# Always waiting for message or command
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)  # skip_updates чтобы бот не обращал внимания на старые сообщения
