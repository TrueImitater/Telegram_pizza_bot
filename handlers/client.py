from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from create_bot import bot
from helper_info import HELP_TEXT, DESCRIPTION_TEXT, TIME_WORKING_TEXT


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text="Приветствую Вас! Какую информацию вы бы хотели спросить?")
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
    await message.reply(text=TIME_WORKING_TEXT, parse_mode="HTML")


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(description, commands=['description'])
    dp.register_message_handler(get_time_work, Text(equals='Время работы'))
