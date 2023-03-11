from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import TOKEN
from tg_bot.handlers import client, other

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())
client.register_handlers_client(dp)
other.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
