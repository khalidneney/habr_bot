from bs4 import BeautifulSoup
import logging
from config import *
import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(text="""
        Hi user! I am a bot which can send you habr freelance orders.
    """)


@dp.

if __name__ == "__main__":
    executor.start_polling(dp)