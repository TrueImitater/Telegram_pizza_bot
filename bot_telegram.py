from aiogram import Bot, Dispatcher, executor, types
from os import getenv

bot = Bot(token=getenv('API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    await message.reply(text=message.text)


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True)
