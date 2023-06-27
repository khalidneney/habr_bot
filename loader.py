from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

result_message_buttons = InlineKeyboardMarkup()
buttons_array = [
    InlineKeyboardButton(text='Next', callback_data="next"),
    InlineKeyboardButton(text='Back', callback_data="back"),
]
result_message_buttons.add(*buttons_array)
result_message_buttons.add(InlineKeyboardButton(text='Restart', callback_data="restart"))
