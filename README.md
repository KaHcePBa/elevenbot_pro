[![Python](https://img.shields.io/badge/Python-3.13.0-blue.svg)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-v3.15-orange.svg)](https://docs.aiogram.dev)
[![Requests](https://img.shields.io/badge/Requests-2.x-olive.svg)](https://docs.python-requests.org/en/latest/)
[![Generic badge](https://img.shields.io/badge/deployed%20to-Heroku-darkviolet.svg)](https://www.heroku.com/)


[//]: # ([![Aioschedule]&#40;https://img.shields.io/badge/Aioschedule-0.5.2-olive.svg&#41;]&#40;https://aioschedule.readthedocs.io/en/latest/&#41;)


[//]: # ([![Dynaconf]&#40;https://img.shields.io/badge/Dynaconf-3.2.6-blue.svg&#41;]&#40;https://dynaconf.readthedocs.io/en/latest/&#41;)
[//]: # ([![PyCharm]&#40;https://img.shields.io/badge/PyCharm-Community%20Edition-black.svg&#41;]&#40;https://www.jetbrains.com/pycharm/&#41;)

# Telegram bot.

### Active features:
* type `/weather 'city'` to see the weather forecast through the [OpenWeatherMap](https://openweathermap.org/) API
  * successful result `/weather tokyo`:
 
        TOKYO
        clear
        🌡 Temperature: 6°C
        🌡 Feels: 5°C
        🚿 Humidity: 55%
        🌬 Wind: 1.54 m/s
        🌬 Direction: Southwest 🌬
  
  * epic fail result `/weather toookyo`:
    * random message example: 
    
    `It's pretty clear that one of us made a mistake and wasted someone else's valuable time.`
    * sticker to message [`id: CAACAgIAAxkBAAEHZBljzZYeCnL_jRZDkG8KvkDAA1G1EAACggIAAi8P8AZ2H-Y5MFDEQS0E`] 
* the bot listens to user messages and responds to some of them
* more information will be added later.

### Depreciated features:
* check birthdays and pin congrats with notify to users in groups
  * _[Reason: Some conflicts with asynchronous jobs]_
* `/gpt 'question'` communicate with ChatGPT 
  * _[Reason: It is necessary to add a payment card to your ChatGPT profile.]_
