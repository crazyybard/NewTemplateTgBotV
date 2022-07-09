from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from tgbot.keyboards.inline import menu


async def user_start(message: Message):
    await message.reply("Приветикикикикик!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")


async def user_menu(message: Message):
    await message.answer('меню', reply_markup=menu)



def register_menu(dp: Dispatcher):
    dp.register_message_handler(user_menu, commands=["menu"], state="*")