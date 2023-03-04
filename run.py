from aiogram import executor, Dispatcher, Bot
from handlers import client, other
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = '5882393088:AAHQfJ5_p7hbuvMX-nmXOvmZGVoNOxtCVqQ'
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())
client.register_handlers_client(dp)
other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
