from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup

from loader import dp
from filters.group_filters import IsGroup
from keyboards.default.boshlanish import kinolar
from keyboards.inline.musiqa import music_btn

@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n Guruxga xush kelibsiz!")


@dp.message_handler(IsGroup(), text="/kino")
async def bot_kinolar(message: types.Message):
    await message.answer("Botimizdan Topishingiz mumkin bo'lgan filmlar!",reply_markup=kinolar)

@dp.message_handler(IsGroup(), commands="endfilm")
async def bot_end(message: types.Message):
    await message.answer(f"{message.from_user.full_name}! kinolar bo'limidan chiqdi",StopAsyncIteration())

@dp.message_handler(IsGroup(), commands="music")
async def bot_music(message: types.Message):
    photo="AgACAgIAAxkBAAIBvmbMZCgSf3bwPtuDhuq0rXyK3S51AAKL2zEbYE5hSmaUjsgoSKeaAQADAgADeAADNQQ"
    await message.answer_photo(photo=photo,caption="Eng zo'r musiqalarni faqat shu kanallardan topishingiz mumkin!",reply_markup=music_btn)