from aiogram import executor
from create_bot import dp
from handlers import admin, client, other
from data_base import sqlite_db


async def on_startup(_):
    sqlite_db.sql_start()
    print("Bot has been started!")

client.register_client_handlers(dp)
admin.register_handlers_admin(dp)
other.register_other_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp, skip_updates=True, on_startup=on_startup)
