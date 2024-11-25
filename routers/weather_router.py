from decimal import Decimal, ROUND_HALF_UP
from services.random_message import get_random_message, nah_message  # Импорт роутера с рандомным текстом
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.weather import get_weather, get_wind_direction

weather_router = Router()


@weather_router.message(Command("weather"))
async def weather_command(message: Message):
    try:
        city_name = message.text.split(maxsplit=1)[1]
    except IndexError:
        await message.answer("Укажите город после команды /weather.")
        return

    # Получаем данные о погоде
    weather_data = get_weather(city_name)
    code = weather_data.get('cod', '404')
    random_message = get_random_message(nah_message)

    if code != '404':
        # Извлечение и округление данных о погоде
        temperature = Decimal(weather_data['main']['temp']).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        feels_like = Decimal(weather_data['main']['feels_like']).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']
        wind_degree = weather_data['wind']['deg']
        wind_direction = get_wind_direction(wind_degree)
        city = weather_data['name'].upper()

        # Формирование ответа
        reply_text = (
            f'🌍 <b>{city}</b>\n'
            f'<i>{weather_description}</i>\n\n'
            f'🌡 <b>Температура:</b> {temperature}°C\n'
            f'🌡 <b>Ощущается:</b> {feels_like}°C\n'
            f'🚿 <b>Влажность:</b> {humidity}%\n'
            f'🌬 <b>Ветер:</b> {wind_speed} m/s\n'
            f'🌬 <b>Направление:</b> {wind_direction}'
        )
        await message.answer(reply_text, parse_mode="HTML")
        await message.delete()
    else:
        await message.answer(random_message)
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEHZBljzZYeCnL_jRZDkG8KvkDAA1G1EAACggIAAi8P8AZ2H-Y5MFDEQS0E')