from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from helper_info import HELP_TEXT, DESCRIPTION_TEXT

bot = Bot(token=getenv('API_TOKEN'))
dp = Dispatcher(bot)


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

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
