import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from handlers.start_handler import *
from handlers.commands_handler import *

dp = Dispatcher()

dp.message.register(start_handler, CommandStart())
dp.message.register(process_destination)
dp.message.register(process_date)
dp.message.register(process_duration)

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())