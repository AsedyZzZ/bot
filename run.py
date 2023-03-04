from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers import client, other

token = "5882393088:AAHQfJ5_p7hbuvMX-nmXOvmZGVoNOxtCVqQ"
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())
client.register_handlers_client(dp)
other.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
