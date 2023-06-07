import logging
from config import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

class Order(StatesGroup):
    search = State()
    categories = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message, state=FSMContext):
    global search_ans
    search_ans =  await  message.answer(text="Hi user! I am a bot which can send you habr freelance orders.\nSend me your search!")
    await Order.search.set()
@dp.message_handler(state=Order.search)
async def search(message: types.Message, state=FSMContext):
    global search_ans
    await bot.delete_message(message.chat.id, message.message_id)
    await search_ans.delete()
    async with state.proxy() as data:
        data['search'] = message.text
    await Order.categories.set()
    global categories_ans
    categories_ans = await message.answer("Now send me categories")

@dp.message_handler(state=Order.categories)
def categories(message: types.Message, state=FSMContext):

@dp.message_handler(content_types=types.ContentType.STICKER)
async def process_sticker(message: types.Message):
    await message.answer("you are fucking slave!!!!")


if __name__ == "__main__":
    executor.start_polling(dp)