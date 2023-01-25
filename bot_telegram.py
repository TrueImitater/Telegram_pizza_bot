import string
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from os import getenv
from helper_info import HELP_TEXT, DESCRIPTION_TEXT, TIME_WORKING_TEXT

bot = Bot(token=getenv('API_TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot has been started!")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text="Приветствую Вас! Какую информацию вы бы хотели спросить?")
    await message.delete()


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text=HELP_TEXT, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["description"])
async def description(message: types.Message):
    await bot.send_message(chat_id=message.from_id, text=DESCRIPTION_TEXT, parse_mode="HTML")
    await message.delete()


@dp.message_handler(Text(equals="Время работы"))
async def timeWorking(message: types.Message):
    await message.reply(text=TIME_WORKING_TEXT, parse_mode="HTML")


@dp.message_handler()
async def word_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('bad_words.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True, on_startup=on_startup)
