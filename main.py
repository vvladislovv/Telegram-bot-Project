import asyncio
import logging
import os
import sys
#import config
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import  keyboard

load_dotenv()
Token = os.getenv('TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyword = keyboard.InlineKeyboardBuilder()
    keyword.button(text="Start Train", url="https://www.rail-nation.com/")
    keyword.button(text="Stop Train", url="https://www.rail-nation.com/")
    keyword.adjust(2)

    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}. Выбери одну из кнопок:", reply_markup=keyword.as_markup())


async def main() -> None:
    bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
