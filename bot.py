import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message

# TOKENni Render platformasidagi muhitdan olamiz
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.answer(
        "Salom! Men video yuklab beruvchi botman.\n"
        "Instagram, TikTok va YouTube videolarini yuklay olaman.\n"
        "Iltimos, havolani yuboring!"
    )

# Hali yuklash funksiyasi qo‘shilmagan – bu bosqichma-bosqich qilinadi

if __name__ == "main":
    executor.start_polling(dp, skip_updates=True)
