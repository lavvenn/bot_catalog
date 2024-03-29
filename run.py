import asyncio

from aiogram import Dispatcher, Bot

from app.handlers import router

from config import TOKEN


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())