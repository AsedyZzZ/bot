import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import find_dotenv, load_dotenv

from handlers import client, other

load_dotenv(find_dotenv())

bot = Bot(os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())
client.register_handlers_client(dp)
other.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
