import logging
# from loader import *
from config import *
from get_orders import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

result_message_buttons = InlineKeyboardMarkup()
result_message_buttons.add(InlineKeyboardButton(text='Next', callback_data="next"), InlineKeyboardButton(text='Back', callback_data="back"))
result_message_buttons.add(InlineKeyboardButton(text='Restart', callback_data="restart"))

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
    categories_ans = await message.answer("Now send me categories. Message must be like that: development, testing, admin, design")

@dp.message_handler(state=Order.categories)
async def categories(message: types.Message, state=FSMContext):
    global categories_ans
    await categories_ans.delete()
    await bot.delete_message(message.chat.id, message.message_id)
    async with state.proxy() as data:
        data['categories'] = (message.text).split(', ')
        global response
        response = get_orders(data['categories'], data['search'])
    global order_message_index
    order_message_index = 0
    global response_ans
    response_ans = await message.answer(response[order_message_index], reply_markup=result_message_buttons)
            
@dp.callback_query_handler()
async def on_next_callback(callback_query: types.CallbackQuery):
    if callback_query.data == 'next':
        global response_ans
        global order_message_index
        global response

        await response_ans.delete()  # удаляем предыдущее сообщение


        order_message_index += 1
        response_ans = await bot.send_message(
            callback_query.from_user.id,
            response[order_message_index],
            reply_markup=result_message_buttons,
        )
        await callback_query.answer(callback_query.from_user.id,
            response[order_message_index],
            reply_markup=result_message_buttons,)
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True,)