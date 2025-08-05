[![Python](https://img.shields.io/badge/Python-3.13.0-blue.svg)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-v3.15-orange.svg)](https://docs.aiogram.dev)
[![Requests](https://img.shields.io/badge/Requests-2.x-olive.svg)](https://docs.python-requests.org/en/latest/)
[![Generic badge](https://img.shields.io/badge/deployed%20to-Heroku-darkviolet.svg)](https://www.heroku.com/)

# Telegram Bot

A professional Telegram bot offering various functionalities, including weather updates and intelligent message responses.

## Features

### 🌦 Weather Forecast
Retrieve current weather conditions via the OpenWeatherMap API.

- **Command**: `/weather <city>`
- **Example**: `/weather tokyo`
- **Output**:

```plaintext 
TOKYO
Condition: Clear ☀️
Temperature: 6°C 🌡
Feels like: 5°C 🌡
Humidity: 55% 🚿
Wind: 1.54 m/s 🌬
Direction: Southwest 🧭
```

- **Error Handling**: If an invalid city is entered, the bot responds with a random message, e.g.:
> "It's pretty clear that one of us made a mistake and wasted someone else's valuable time."
Additionally, a sticker is sent (ID: CAACAgIAAxkBAAEHZBljzZYeCnL_jRZDkG8KvkDAA1G1EAACggIAAi8P8AZ2H-Y5MFDEQS0E).

### Smart Replies
The bot detects specific keywords or phrases in user messages and provides tailored responses.

### AI Integration
- **Command**: `/ai <question>`
Interact with AI (context-free for now).

Stay tuned for further enhancements!