from aiogram import Dispatcher, types


async def cmd_handler(message: types.Message):
    await message.answer(f"Hello {message.chat.first_name}! \n"
                         f"This bot help to pick up good hero \n "
                         f"against your enemy team!\n"
                         f"List of commands: \n"
                         f"/start - Refresh bot\n"
                         f"/stat - Run picking up\n"
                         f"/hero - Pick up hero")


async def help_handler(message: types.Message):
    await message.answer("List of commands: \n"
                         "/start - Refresh bot\n"
                         "/stat - Run picking up\n"
                         "/hero - Pick up hero")


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cmd_handler, commands=["start", "welcome", "about"])
    dp.register_message_handler(help_handler, commands=["help"])
