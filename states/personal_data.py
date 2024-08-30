from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    fullName = State()  # ism
    email = State()  # email
    phoneNum = State()  # Tel raqami
    Text = State()
