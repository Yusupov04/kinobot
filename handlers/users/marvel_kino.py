from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.gallaktika_qoriqchilari import gallaktika_btn
from keyboards.inline.gallaktika_qoriqchilari import chumoli_btn
from keyboards.inline.gallaktika_qoriqchilari import qasos_btn


@dp.message_handler(text="🎬💎𝐆𝐀𝐋𝐀𝐊𝐓𝐈𝐊𝐀🪐𝐐𝐎'𝐑𝐈𝐐𝐂𝐇𝐈𝐋𝐀𝐑𝐈🌪🍿")
async def kino1(msg: types.Message):
    rasm = "AgACAgIAAxkBAAPBZswSflS6StSPPwABweRkSC4w-moqAAJ72TEbYE5hSku-k_gbjENFAQADAgADeQADNQQ"
    await msg.answer_photo(photo=rasm,reply_markup=gallaktika_btn)

@dp.message_handler( text="🎬ᑕHᑌᗰOᒪƖ🐜Oᗪᗩᗰ🍿")
async def kino2(msg: types.Message):
    rasm = "AgACAgIAAxkBAAIBMGbMLz7q7SqJUI5Uc1rxgeQYhvqQAAJk3jEbdx9oSovNhF1hUzOlAQADAgADeAADNQQ"
    await msg.answer_photo(photo=rasm, caption="""👇 Qismlardan tanlang 👇""",reply_markup=chumoli_btn)

@dp.callback_query_handler(text="🐜 1-qism 🐜")
async def chumoli1(call:CallbackQuery):
    kino="BAACAgIAAxkBAAIBNWbMNa-Iyat26CKQYvkf40rzmNVpAAJsIAACu_9JS_DJoz8X2EvNNQQ"
    await call.message.answer_video(video=kino,caption="""🎬 Chumoli 🐜 Odam (2015)
🇺🇿 O‘zbek tilida | 💽480p hd

Bizdan🍿 uzoqlashmang✅""")

@dp.callback_query_handler(text="🐜 2-qism 🐜")
async def chumoli2(call:CallbackQuery):
    kino="BAACAgIAAxkBAAIBN2bMNgXrxd1mDmW_IUKYFwgSMkabAAJ0IAACu_9JS7IjhJ9CE5r_NQQ"
    await call.message.answer_video(video=kino,caption="""🎬 Chumoli 🐜 Odam va Ari (2018)
🇺🇿 O‘zbek tilida | 💽480p hd

Bizdan🍿 uzoqlashmang✅""")

@dp.callback_query_handler(text="🐜 3-qism 🐜")
async def chumoli3(call:CallbackQuery):
    kino="BAACAgUAAxkBAAIBOWbMNnzYI46O1LoqucNz8RFcqNHkAALACgACL8pwVvAuteUsgAmoNQQ"
    await call.message.answer_video(video=kino,caption="""🎬 ➺ Chumoli Odam: Kvant olami 🔥 (2023)
🇺🇿 ➺ O'zbek Tilida
⚔️ ➺ Jangari, Fantastik""")


@dp.callback_query_handler(text="🪐 1-qism 🪐")
async def vgnbvf(call:CallbackQuery):
    video="BAACAgIAAxkBAAIBH2bMKqQ1JiDtu8vVO5GZfZwRP-5xAAJnGwAC-0BJSzC16Xi9DWdYNQQ"
    await call.message.answer_video(video=video,caption="""🎬 Galaktika Qoʻriqchilari (2014)
🇺🇿 O‘zbek tilida | 💽480p hd

Bizdan🍿 uzoqlashmang✅""")

@dp.callback_query_handler(text="🪐 2-qism 🪐")
async def adf(call:CallbackQuery):
    await call.message.answer_video(video="BAACAgIAAxkBAAIBIWbMK_u1FWn62li5PpEmyb1NKkGtAAJsGwAC-0BJS_H8P83StauyNQQ",caption="""🎬 Galaktika Qoʻriqchilari 2 (2017)
🇺🇿 O‘zbek tilida | 💽480p hd

Bizdan🍿 uzoqlashmang✅""")

@dp.callback_query_handler(text="🪐 3-qism 🪐")
async def wqe(call:CallbackQuery):
    kino3="BAACAgUAAxkBAAICCWbMbbfTvDc3Ed1Rp3Rv1qW9tGsIAAK3DQAC7VgwVueznKTW0cRUNQQ"
    await call.message.answer_video(video=kino3,caption=""""🎬 "GALAKTIKA QO'RIQCHILARI 3"
🇺🇿 O'zbek tilida (TV dublyaj)
📆 2023-yil 5-may
💿 HD FORMATDA (480p)""")

@dp.message_handler(text="🎬ℚ𝕆ℝ𝔸💫ℙ𝔸ℕ𝕋𝔼ℝ𝔸🍿")
async def qora(msg:types.Message):
    kino4="BAACAgIAAxkBAAIC1mbReW_OyzcCAu0FlWID9E5gwGAPAAKWGwAC-0BJS7mstVYAAZJ-DTUE"
    await msg.answer_video(video=kino4, caption="""🎬 Qora Pantera (2018)
🇺🇿 O‘zbek tilida | 💽480p hd

Bizdan🍿 uzoqlashmang✅""")

@dp.message_handler(text="🎬𝑫𝑶𝑪𝑻𝑶𝑹🎩𝑺𝑻𝑹𝑨𝑵𝑮𝑬🍿")
async def strange(msg:types.Message):
    kino5="BAACAgIAAxkBAAIC2GbReyFKRlPGwplhW6TnRBW1OBvcAAJaGwAC-0BJS2Hx8VbMylG2NQQ"
    await msg.answer_video(video=kino5,caption="""🎬 Doctor Strange 🎩
📀 Sifati: 480p HD
📆 Yil: 2016
🎞 Janr: Fantastika,  Sarguzasht. 
🇺🇿 O'zbek tilida""")

@dp.message_handler(text="🎬🪓𝕋𝕆ℝ⚡️🍿")
async def tor(msg:types.Message):
    kino6="BAACAgUAAxkBAAIC32bRfBGPdpPQdt1sQeEMTr9zWEByAAK6CgACL8pwVlkDRlc8IRjKNQQ"
    await msg.answer_video(video=kino6,caption="""🎬 "Tor: Sevgi va chaqmoq"
🇺🇿 O'zbek tilida
📆 2022-yil 7-iyul
🎞 Janri: Fantastika,  Jangari, Komediya.""")

@dp.message_handler(text="🌪𝚂𝙷𝙰𝙽𝙶 - 𝙲𝙷𝙸🔥")
async def shang(msg:types.Message):
    kino7="BAACAgIAAxkBAAIC4mbRfKhhnLDznZRzw4cjFOPeLe7FAAKRGwAC-0BJS86YvhWZs5e6NQQ"
    await msg.answer_video(video=kino7,caption="""🎬 Shang-Chi: O'nta Uzuk Afsonasi"
🇺🇿 O'zbek tilida 
📆 2021-yil 
🎞 Janri: Sarguzasht, Fantastika, Jangari""")

@dp.message_handler(text="🎬𝐀𝐁𝐀𝐃𝐈𝐘𝐋𝐀𝐑🌎🍿")
async def abad(msg:types.Message):
    kino8="BAACAgIAAxkBAAIC5WbRfU4TkTCloWn71rD2RJut8wABQgACUyAAAiVqSEvnV7z43j6odDUE"
    await msg.answer_video(video=kino8, caption="""🎬ABADIYLAR
🇺🇿O‘zbek tilida
📆2021-yil | 💿480p hd
🎞Janri : Jangari, Fantastika""")

@dp.message_handler(text="🎬𝚀𝙾𝚁𝙰🖤𝙱𝙴𝚅𝙰🍿")
async def qora(msg:types.Message):
    kino9="BAACAgIAAxkBAAIC7mbRfha0_2eQiSjVqCjAoUa8laVrAAJ5IAACu_9JSz6cDzDHpsUsNQQ"
    await msg.answer_video(video=kino9,caption="""🎬"QORA BEVA"  (2021)
🇺🇿 O‘zbek tilida
🎞 Janri: Jangari, Fantastika, Triller.

Bizdan🍿 uzoqlashmang✅""")

@dp.message_handler(text="🎬🟢𝗫𝗔𝗟𝗞🟢🍿")
async def hulk(msg:types.Message):
    kino10="BAACAgIAAxkBAAIC82bRfo9iK4ZnhOHs7F8i82lMW1-AAAIPHAAC-0BJS7DHTFsVlwTMNQQ"
    await msg.answer_video(video=kino10,caption="""🎥 Film nomi: 🟢Halk 2
📆Yili : 2008
🇺🇿Tili : O'zbek""")

@dp.message_handler(text="🎬𝐐𝐀𝐒𝐎𝐒𝐊𝐎𝐑𝐋𝐀𝐑")
async def qasos(msg:types.Message):
    rasm="AgACAgIAAxkBAAIC9mbRf2HkjdIYTWoHr4hDttx27Z2bAAKJ2DEbxr6QSsIMYZi3E7C5AQADAgADeAADNQQ"
    await msg.answer_photo(photo=rasm,caption="👇 Qismlardan tanlang 👇",reply_markup=qasos_btn)

@dp.callback_query_handler(text="1-qism")
async def qism1(call:CallbackQuery):
    kino11="BAACAgIAAxkBAAIC-GbRgXaZH7inUlvdK8zLQkZbk6A8AAIvGwAC-0BJS4aZGs-5rfV0NQQ"
    await call.message.answer_video(video=kino11,caption="""🎬Qasoskorlar
📆Yili : 2012
💽Sifati: 480p
🇺🇿Tili : O'zbek""")

@dp.callback_query_handler(text="2-qism")
async def qism2(call:CallbackQuery):
    kino12="BAACAgIAAxkBAAIC_mbRgfgl7lIlE1kGutCAcFKQz_tHAAI2GwAC-0BJS4oJ3og096ixNQQ"
    await call.message.answer_video(video=kino12,caption="""🎬Qasoskorlar | Altron Davri
📆Yili : 2015
💽Sifati: 480p
🇺🇿Tili : O'zbek""")

@dp.callback_query_handler(text="3-qism")
async def qism3(call:CallbackQuery):
    kino13="BAACAgIAAxkBAAIDAAFm0YJPsz7G31I5C0iBHyZaRdMKXQACPhsAAvtASUsFJCVLPrnEHDUE"
    await call.message.answer_video(video=kino13,caption="""🎬Qasoskorlar | Abadiyat Jangi
📆Yili : 2018
💽Sifati: 480p
🇺🇿Tili : O'zbek
""")

@dp.callback_query_handler(text="4-qism")
async def qism4(call:CallbackQuery):
    kino14="BAACAgIAAxkBAAIDAmbRgpBCLNb-tB-yNAEeLdaZTCRoAAJGGwAC-0BJSxZPkgKFilBrNQQ"
    await call.message.answer_video(video=kino14,caption="""🎬Qasoskorlar | Intiho
📆Yili : 2019
💽Sifati: 480p
🇺🇿Tili : O'zbek""")