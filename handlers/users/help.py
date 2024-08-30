from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Yordam kerak bo'lsa admin bilan bog'laning!",
            "https://t.me/bexajaan_04",)
    
    await message.answer("\n".join(text))
