from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    mail = State()
    id = State()
    phone = State()