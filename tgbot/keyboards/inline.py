from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Котлетки')
        ],
        [
            KeyboardButton(text='Макарошки'),
            KeyboardButton(text='Пельмешки'),
        ],
    ],
    resize_keyboard=True
)