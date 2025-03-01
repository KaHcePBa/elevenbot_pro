import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router

# Import Routers
from handlers import description_router
from handlers import gpt_router
from handlers import pravo_router
from handlers import promo_router
from handlers import react_router
from handlers import weather_router
# from handlers.bot_description import description_router
# from handlers.gpt_router import gpt_router  # gpt router import
# from handlers.pravo_router import pravo_router
# from handlers.promo_router import promo_router
# from handlers.reaction_router import react_router
# from handlers.weather_router import weather_router

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
router = Router()


async def main():
    dp = Dispatcher()
    # Connect Router. If I create a new Router, I add it here. I can also disable them here.
    dp.include_router(description_router)  # A router for /description
    dp.include_router(gpt_router)
    dp.include_router(pravo_router)
    dp.include_router(weather_router)
    dp.include_router(promo_router)
    dp.include_router(react_router)
    dp.include_router(router)

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
