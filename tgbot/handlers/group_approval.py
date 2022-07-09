# import asyncio
# import random
#
# from aiogram import Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
#
#
# async def process_chat_invite_request(chat_join_request: ChatJoinRequest, state: FSMContext):
#     approve_buttons = [
#                 InlineKeyboardButton(text='😺', callback_data='cat'),
#                 InlineKeyboardButton(text='🐶', callback_data='dog'),
#                 InlineKeyboardButton(text='🐬', callback_data='dolphin'),
#             ]
#     random.shuffle(approve_buttons)
#     await chat_join_request.bot.send_message(
#         chat_join_request.from_user.id, 'Нажмите на котика',
#         reply_markup=InlineKeyboardMarkup(inline_keyboard=[approve_buttons])
#     )
#     await state.update_data(chat_id=chat_join_request.chat.id)
#     await state.set_state('chat_join_request')
#
#
# async def approve_callback_group_captcha(call: CallbackQuery, state: FSMContext):
#     await call.message.answer('Вы были приняты в группу')
#     data = await state.get_data()
#     chat_id = data['chat_id']
#     await call.bot.approve_chat_join_request(chat_id, call.from_user.id)
#
#
# async def decline_callback_group_captcha(call: CallbackQuery, state: FSMContext):
#     await call.message.answer('Вы не приняты в группу')
#     data = await state.get_data()
#     chat_id = data['chat_id']
#     await call.bot.decline_chat_join_request(chat_id, call.from_user.id)
#     await state.reset_state()
#
#
#     # Тут через if можно выставлять условия принять или отклонить
#     #await asyncio.sleep()
#     #await chat_join_request.approve()
#     #await chat_join_request.decline()
#
#
# def register_group_approval(dp: Dispatcher) -> object:
#     dp.register_chat_join_request_handler(process_chat_invite_request)
#     dp.register_callback_query_handler(approve_callback_group_captcha, text='cat', state='chat_join_request')
#     dp.register_callback_query_handler(decline_callback_group_captcha, text='cat', state='chat_join_request')