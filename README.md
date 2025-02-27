[![Python](https://img.shields.io/badge/Python-3.13.0-blue.svg)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-v3.15-orange.svg)](https://docs.aiogram.dev)
[![Requests](https://img.shields.io/badge/Requests-2.x-olive.svg)](https://docs.python-requests.org/en/latest/)
[![Generic badge](https://img.shields.io/badge/deployed%20to-Heroku-darkviolet.svg)](https://www.heroku.com/)

# 📌 Telegram Bot

A simple Telegram bot with multiple features, including weather updates and message responses.

---

## 🚀 Active Features

### 🌦 Weather Forecast

Get the current weather conditions using the [OpenWeatherMap](https://openweathermap.org/) API.

- **Command:** `/weather 'city'`
- **Example:** `/weather tokyo`
- **Successful result:**
  ```
  TOKYO
  ☀️ Clear
  🌡 Temperature: 6°C
  🌡 Feels like: 5°C
  🚿 Humidity: 55%
  🌬 Wind: 1.54 m/s
  🧭 Direction: Southwest 🌬
  ```
- **Error handling:** If an incorrect city is provided, the bot will respond with a random message, e.g.:
  > *"It's pretty clear that one of us made a mistake and wasted someone else's valuable time."*

  Additionally, a sticker will be sent: `id: CAACAgIAAxkBAAEHZBljzZYeCnL_jRZDkG8KvkDAA1G1EAACggIAAi8P8AZ2H-Y5MFDEQS0E`

### 💬 Smart Replies

The bot listens to user messages and responds to certain keywords or phrases.

### 🤖 DeepSeek Integration

- Command: `/gpt 'question'` to communicate with ChatGPT (without context for now).

⚠️ *More features will be added later.*

---

## ❌ Deprecated Features

### 🎉 Birthday Reminders

- Used to check birthdays and pin congratulatory messages in groups.
- *Reason for removal:* Conflict with asynchronous jobs.

### 🤖 ChatGPT Integration

- Command: `/gpt 'question'` to communicate with ChatGPT.
- *Reason for removal:* Requires a payment method to be added to the ChatGPT profile.

---

Stay tuned for updates! 🚀
