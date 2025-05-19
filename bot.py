from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "Salom! Men video yuklab beruvchi Telegram botman.\n"
        "Instagram, TikTok yoki YouTube havolasini yuboring — men sizga videoni yuboraman."
    )
