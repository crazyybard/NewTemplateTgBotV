from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Меню')
        ]
    ],
    resize_keyboard=True
)

