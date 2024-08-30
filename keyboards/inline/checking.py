from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


chek_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obuna bo'lish",url="https://t.me/test_uchun7777")
        ],
        [
            InlineKeyboardButton(text="Obunani tekshirish ✅",callback_data="check_subs")
        ]
    ]
)