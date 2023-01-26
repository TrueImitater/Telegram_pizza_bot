import string
import json
from aiogram import Dispatcher, types


# @dp.message_handler()
async def word_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('bad_words.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(word_filter)
