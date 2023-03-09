import logging
from parser import Parser, StatusCodeError

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import hero
from alias import NotFoundError, find_hero
from calculator import Calculator, Answer
from settings import heroes_parser

heroes: list[hero.Hero] = heroes_parser.get_heroes()
logging.warning(f"Heroes parsed: {len(heroes)} count")


class FSM(StatesGroup):
    hero = State()
    result = State()


async def run_stat(message: types.Message):
    await FSM.hero.set()
    await message.answer("Напиши вражеских героев \n Вот так: \nSlark\nTiny")
    await FSM.next()


async def get_result(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["result"] = message.text
        result: list[dict[str, float]] = []
        my_heroes: list[hero.Hero] = []
        for i in data["result"].split("\n"):
            try:
                my_heroes.append(find_hero(heroes=heroes, value=i))
            except NotFoundError as e:
                await message.reply(f"Incorrect input: {str(e)}")
                return
        for i in my_heroes:
            try:
                parser_result = Parser(hero=i).get_win_rate()
            except StatusCodeError:
                await message.reply("Service Error")
                await state.finish()
                return
            result.append(parser_result)
        win_rate: list[tuple[str, list[float]]] = Calculator.calculate(result)
    answer: str = Answer.make_answers(win_rate, len(data["result"].split()))
    await message.reply(answer, parse_mode="Markdown")
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(run_stat, commands=["stat"], state=None)
    dp.register_message_handler(get_result, state=FSM.result)
