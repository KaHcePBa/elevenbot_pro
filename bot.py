import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router

# Import Routers
from handlers import ai_router, description_router, pravo_router, promo_router, react_router, weather_router

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename='bot.log'
)
logging.info('Start running...')

# Initialization of the bot and the main router
bot = Bot(token=os.getenv('BOT_TOKEN'))


# bot = Bot(token=settings.BOT_TOKEN) # Dynaconf lazysettings
# router = Router()


async def main():
    dp = Dispatcher()
    # Connect Router. If I create a new Router, I add it here. I can also disable them here.
    dp.include_routers(description_router,
                      ai_router,
                      pravo_router,
                      weather_router,
                      promo_router,
                      react_router)
    # dp.include_router(ai_router)
    # dp.include_router(pravo_router)
    # dp.include_router(weather_router)
    # dp.include_router(promo_router)
    # dp.include_router(react_router)
    # dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nThe program was interrupted by the user (Ctrl+C).")
    except asyncio.CancelledError:
        print("\nThe asynchronous task was canceled.")
    except Exception as e:
        print(f"\nThere's been a mistake: {e}")
    finally:
        print("Job completion.")
