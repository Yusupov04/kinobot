from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.personal_data import PersonalData
from keyboards.default.boshlanish import kinolar


@dp.message_handler(text="Fikr bildirish✍️", state=None)
async def enter_test(message: types.Message):
    await message.answer("Izohlar yozib qoldirish uchun ma'lumotlaringizni kiritish talab qilinadi!\n\nTo'liq ismingizni kiriting")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzil kiriting")

    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqam kiriting")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )

    await message.answer("Fikringizni yozib qoldiring")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.Text)
async def answer_text(message: types.Message, state:FSMContext):
    text = message.text

    await state.update_data(
        {"Izoh": text}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    text = data.get("Izoh")

    msg = f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon: - {phone}\n"
    msg += f"Izoh: {text}\n\n"
    msg += "Fikringiz uchun raxmat!"
    await message.answer(msg,reply_markup=kinolar)

    await state.finish()

    # await state.reset_state(with_data=False)