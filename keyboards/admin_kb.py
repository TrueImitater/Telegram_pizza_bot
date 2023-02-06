from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

edit_kb = ReplyKeyboardMarkup(resize_keyboard=True)
edit_kb.add(KeyboardButton(text="/Загрузить"),
            KeyboardButton(text="/Удалить"))
