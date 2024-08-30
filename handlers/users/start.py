import sqlite3

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.config import ADMINS
from keyboards.default.boshlanish import kinolar
from keyboards.default.tarjima import tarjima_kino
from keyboards.default.marvel import marvel_film
from filters.private_filter import IsPrivate

from loader import dp, db, bot


@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=kinolar)
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)



# @dp.message_handler(IsPrivate(),commands="start")
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!\nBotga xush kelibsiz!",reply_markup=kinolar)

@dp.message_handler(text="🇺🇿 Tarjima kinolar 🍿")
async def tarjima_kino_uchun(msg: types.Message):
    await msg.answer("Eng zo'r tarjima kinolar", reply_markup=tarjima_kino)

@dp.message_handler(text="Marvel Kinolari 🍿")
async def marvel_kino_uchun(msg: types.Message):
    await msg.answer("Marvel olamining barcha filmlari!",reply_markup=marvel_film)

@dp.message_handler(text="Back")
async def bosh_sahifa(msg: types.Message):
    await msg.answer("Bosh sahifa", reply_markup=kinolar)


@dp.message_handler(text="sadf")
async def sadf(msg: types.Message):
    await msg.answer("Sadf")


