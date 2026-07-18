from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    first_name = State()
    age = State()
    gender = State()
    province = State()
    city = State()
    photo = State()
    bio = State()