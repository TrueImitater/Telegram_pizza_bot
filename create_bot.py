from os import getenv
from aiogram import Bot, Dispatcher


bot = Bot(token=getenv("API_TOKEN"))
dp = Dispatcher(bot)
