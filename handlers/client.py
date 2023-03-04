from aiogram import types, Dispatcher
#from keyboards.inline_k import pick_h_ikb
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import hero


class FSM(StatesGroup):
    hero = State()
    result = State()


async def run_stat(message: types.Message):
    await FSM.hero.set()
    await message.answer('Напиши вражеских героев \n Вот так: \n Slark \n Tiny')
    await FSM.next()


async def get_result(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['result'] = message.text
        for i in data['result'].split():
            x = hero.Hero(i)
            x.get_win_rate()

    await message.reply()
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(run_stat, commands=['stat'], state=None)
    dp.register_message_handler(get_result, state=FSM.result)
    # dp.register_message_handler(give_result)
#     dp.register_callback_query_handler(answer_num)
#     dp.register_message_handler(get_hero, commands=['hero'])
