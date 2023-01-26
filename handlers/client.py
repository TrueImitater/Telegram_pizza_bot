from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from create_bot import bot
from keyboards import client_kb
from helper_info import HELP_TEXT, DESCRIPTION_TEXT, TIME_WORKING_TEXT


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text="Приветствую Вас! Какую информацию вы бы хотели спросить?", reply_markup=client_kb.start_kb)
    await message.delete()


# @dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text=HELP_TEXT, parse_mode="HTML")
    await message.delete()


# @dp.message_handler(commands=["description"])
async def description(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text=DESCRIPTION_TEXT, parse_mode="HTML")
    await message.delete()


# @dp.message_handler(Text(equals="Время работы"))
async def get_time_work(message: types.Message):
    await message.reply(text=TIME_WORKING_TEXT, parse_mode="HTML", reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(Text(equals="Где находится?"))
async def get_adress_pizza(message: types.Message):
    await message.reply(text="Улица Победы\nДом 42", reply_markup=ReplyKeyboardRemove())


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(description, commands=['description'])
    dp.register_message_handler(get_time_work, Text(equals='Время работы'))
    dp.register_message_handler(
        get_adress_pizza, Text(equals='Где находится?'))
