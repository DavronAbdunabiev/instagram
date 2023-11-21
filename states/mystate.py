from aiogram.dispatcher.filters.state import State,StatesGroup


class ReklamaState(StatesGroup):
    add = State()
    check = State()
class KanalState(StatesGroup):
    check = State()