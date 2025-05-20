from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men video yuklab beruvchi botman. Instagram, TikTok va YouTube’dan video link yuboring.")

if _name_ == 'main':
    from aiogram import
executor    
    executor.start_polling(dp, skip_updates=True)
