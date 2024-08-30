from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

raqam=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Raqamni ulashish",request_contact=True)
        ]
    ]
)