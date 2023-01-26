from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# keyboards open on /start message
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton(text="Время работы"),
             KeyboardButton(text="Где находится?"))
