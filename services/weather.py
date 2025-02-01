import requests

from config.config import settings  # Импорт настроек из dynaconf

# Настройки
dynaconf_settings = settings


def get_weather(city_name: str) -> dict:
    # Получает данные о погоде для указанного города через OpenWeatherMap API.
    # api_key = os.getenv('WEATHER_APIKEY')
    api_key = dynaconf_settings.WEATHER_APIKEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={api_key}'
    response = requests.get(url)
    return response.json()


def get_wind_direction(degree: float) -> str:
    # Преобразует числовое значение направления ветра в текстовый формат.

    if 337.5 <= degree < 22.5:
        return "С⬇️"
    elif 22.5 <= degree < 67.5:
        return "СЗ↘️"
    elif 67.5 <= degree < 112.5:
        return "З➡️"
    elif 112.5 <= degree < 157.5:
        return "ЮЗ↗️"
    elif 157.5 <= degree < 202.5:
        return "Ю⬆️"
    elif 202.5 <= degree < 247.5:
        return "ЮВ↖️"
    elif 247.5 <= degree < 292.5:
        return "В⬅️"
    elif 292.5 <= degree < 337.5:
        return "СВ↙️"
    return "Неизвестное направление"
