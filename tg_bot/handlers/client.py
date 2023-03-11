import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from domain.hero import Hero
from services.alias import NotFoundError, find_hero
from services.calculator import Calculator
from services.wr_parser import Parser, StatusCodeError
from settings import HEROES_PARSER

heroes: list[Hero] = HEROES_PARSER.get_heroes()
logging.warning(f"Heroes parsed: {len(heroes)} count")


class FSM(StatesGroup):
    hero = State()
    result = State()


class AnswerBuilder:
    @staticmethod
    def build_win_rates_answer(lst: list[tuple[str, list[float]]]) -> str:
        heroes_count = len(lst[0][1])
        if heroes_count == 1:
            answer = "\n".join(f"{hero_name}: *" + str(*win_rates) + "*" for hero_name, win_rates in lst)
        else:
            answer = "\n".join("*" + str(round(sum(win_rates) / len(win_rates), 2)) + "*" + f" {hero_name}: {win_rates}"
                               for hero_name, win_rates in lst)
        return answer


async def run_stat(message: types.Message):
    await FSM.hero.set()
    await message.answer("Напиши вражеских героев \n Вот так: \nSlark\nTiny")
    await FSM.next()


async def get_result(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["result"] = message.text
        my_heroes: list[Hero] = []

        for i in data["result"].split("\n"):
            try:
                my_heroes.append(find_hero(heroes=heroes, value=i))
            except NotFoundError as e:
                await message.reply(f"Incorrect input: {str(e)}")
                return
        if not 1 <= len(my_heroes) <= 5:
            await message.reply(f"Вы должны передать от 1 до 5 героев, получено {len(my_heroes)}")
            return

        result: list[dict[str, float]] = []
        for i in my_heroes:
            try:
                parser_result = Parser(hero=i).get_win_rate()
            except StatusCodeError:
                await message.reply("Service Error")
                await state.finish()
                return
            result.append(parser_result)
        win_rate: list[tuple[str, list[float]]] = Calculator.calculate(lst=result, top=10)
    answer: str = AnswerBuilder.build_win_rates_answer(lst=win_rate)
    await message.reply(answer, parse_mode="Markdown")
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(run_stat, commands=["stat"], state=None)
    dp.register_message_handler(get_result, state=FSM.result)
