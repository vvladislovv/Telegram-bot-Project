import asyncio
import logging
import os
import sys
from typing import Any

from SiteWork import login
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils import keyboard

load_dotenv()
Token = os.getenv('TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())     # /start
async def command_start_handler(message: Message) -> None:
    keyword = keyboard.InlineKeyboardBuilder()
    keyword.button(text="Start Train", callback_data="Start Train")
    keyword.adjust(1)

    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}. Нажми на кнопку", reply_markup=keyword.as_markup())


@dp.callback_query()    # Start Train CallBack
def callback_query(call: types.CallbackQuery) -> Any:
    print(call.data)
    if call.data == "Start Train":
        login.loginSite()


async def main() -> None:
    bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
