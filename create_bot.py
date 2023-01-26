from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=getenv("API_TOKEN"))
dp = Dispatcher(bot, storage=storage)
