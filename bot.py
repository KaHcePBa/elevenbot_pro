import asyncio
import datetime
import logging

# import aioschedule
from aiogram import Bot, Dispatcher, Router
from dynaconf import LazySettings

# Импорт Routers
from routers.description import description_router  # Импорт роутера с командой дескрипшн
from routers.pnn import pravo_router
from routers.promo import promo_router
from routers.reaction import react_router
from routers.weather_router import weather_router

# from routers.gpt import gpt_router  # Импорт роутера gpt

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename='bot.log'
)
logging.info('Start running...')

settings = LazySettings(
    settings_files=["settings.yaml", ".secrets.yaml"],  # Указываем YAML-файлы
    environments=True,  # Активируем поддержку окружений
    env="development"  # Устанавливаем окружение по умолчанию
)

# Инициализация бота и основного роутера
bot = Bot(token=settings.BOT_TOKEN)
router = Router()


# Периодические задачи
# async def eleven_message():
#     await bot.send_message(
#         chat_id=settings.CHAT_ID,
#         text="<b>11:11, ёпта! Время ЭЛЭВЕН!</b>",
#         parse_mode="HTML"
#     )


# async def pin_birthday():
#     today = datetime.datetime.now()
#     yesterday = today - datetime.timedelta(days=1)
#     today_key = today.strftime("%d%m")
#     yesterday_key = yesterday.strftime("%d%m")
#
#     if today_key == '0103' and yesterday_key == '2802':
#         false_today_key = '2902'
#         user_name = settings.BIRTHDAYS.get(false_today_key, "Именинник")
#         message = await bot.send_message(
#             chat_id=settings.CHAT_ID,
#             text=f"🥳🥳🥳 С днем рождения, {user_name}! 🥳🥳🥳"
#         )
#         await bot.pin_chat_message(
#             chat_id=settings.CHAT_ID,
#             message_id=message.message_id,
#             disable_notification=False
#         )
#     elif today_key in settings.BIRTHDAYS:
#         user_name = settings.BIRTHDAYS[today_key]
#         message = await bot.send_message(
#             chat_id=settings.CHAT_ID,
#             text=f"🥳🥳🥳 С днем рождения, {user_name}! 🥳🥳🥳"
#         )
#         await bot.pin_chat_message(
#             chat_id=settings.CHAT_ID,
#             message_id=message.message_id,
#             disable_notification=False
#         )


# async def scheduler():
#     aioschedule.every().day.at("08:11").do(eleven_message)
#     aioschedule.every().day.at("06:00").do(pin_birthday)
#
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


# Запуск

async def main():
    dp = Dispatcher()
    # Подключаем Router. Если создаю новый Router, то добавляю его сюда. Могу и отключать их здесь.
    dp.include_router(description_router)  # Роутер для /description
    # dp.include_router(gpt_router)
    dp.include_router(pravo_router)
    dp.include_router(weather_router)
    dp.include_router(promo_router)
    dp.include_router(react_router)
    dp.include_router(router)

    # asyncio.create_task(scheduler())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем (Ctrl+C).")
    except asyncio.CancelledError:
        print("\nАсинхронная задача была отменена.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
    finally:
        print("Завершение работы.")
