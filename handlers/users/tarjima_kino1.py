from aiogram import types

from loader import dp

@dp.message_handler(text="🖥 Inferno")
async def kino1(msg: types.Message):
    kino="BAACAgQAAxkBAANgZsm0mcIzYDvcMjE5qD_PYhBQtU0AAgQUAAKXxvhR5On_X22ZQpQ1BA"
    await msg.answer_video(video=kino,caption="""🖥 Inferno

⭐️ IMDb: — 6.2

📆 2016
📹 720p
🇺🇿 O‘zbek tilida
🌍 Vengriya
🎭 #detektiv, #triller""")
    
@dp.message_handler(text="🖥 Yer qarida")
async def kino2(msg: types.Message):
    kino="BAACAgQAAxkBAANrZsm1lj6R9PMrhQPHm_dCrNTwIZIAApAXAALYuDlSR_Y-gcQEkAk1BA"
    await msg.answer_video(video=kino,caption="""🖥 Yer qarida

📆 2003
📹 1080p
🇺🇿 O‘zbek tilida 
🌍 AQSh
🎭 #ilmiy_fantastik""")
    
@dp.message_handler(text="🖥 Sobotaj")
async def kino3(msg: types.Message):
    kino="BAACAgQAAxkBAAOTZsm6_HJF-Tjw5oe9osEiow5HY_MAAhcIAAJYnohR5GXTo66Gcgs1BA"
    await msg.answer_video(video=kino,caption="""🖥 Sobotaj

📆 2013
📹 480p
🇺🇿 O‘zbek tilida 
🌍 AQSh
🎭 #kriminal, #jangari, #triller""")
    
@dp.message_handler(text="🖥 Samaritan")
async def kino4(msg: types.Message):
    kino="BAACAgUAAxkBAAN1Zsm220E2Jh1hdZuXN60DDZYd1N4AAjsKAAJzj8hWIZbf1TLtySE1BA"
    await msg.answer_video(video=kino,caption="""🖥 Samaritan 

📆 2022
🇺🇿 O‘zbek tilida 
📹 720p 
⭐️ IMDb: – 5.7
🇺🇸 AQSh
🎭 #jangari, #fantastika""")
    
@dp.message_handler(text="⚡️sᴏɴɪᴄ🌪 (2022)🔥")
async def kino5(msg: types.Message):
    kino="BAACAgQAAxkBAAN3Zsm3IEqFQ9nHfanRCbDmQ0Z9d_oAAnoPAAKIDNhTuYB2CtUneYk1BA"
    await msg.answer_video(video=kino,caption="""🎬 Sonic 2 ⚡️ (2022)
🇺🇿 O‘zbek tilida (My5) dublyaji
📀Sifati 720p """)

@dp.message_handler(text="🎩ғᴏᴋᴜs🎭")
async def kino6(msg: types.Message):
    kino="BAACAgEAAxkBAAN7Zsm4LGbYcHHzBYz7bnng4d3hqOYAAmMAA_MH-UcKKkGuzwjtyTUE"
    await msg.answer_video(video=kino,caption="""🎬 ➺ Fokus 
🇺🇿 ➺ O'zbek Tilida [480p/HD]
🌍 ➺ Davlati: AQSH
⚔️ ➺ Janri: Melodrama, Kriminal""")
    
@dp.message_handler(text="🎬🦍ʀᴇᴍᴘᴇʏᴊ🦍🍿")
async def kino7(msg: types.Message):
    kino="BAACAgQAAxkBAAN_Zsm5FO9VVcgkfJF8a-8NwyXTJdwAAqsJAAJnnvlTA_M1Atp91RI1BA"
    await msg.answer_video(video=kino,caption="""🎬 ➺ Rempeyj [2018]
🇺🇿Tili ➺ O'zbek Tilida 
💽 Sifati ➺ 480p | hd
🎭Janri ➺ Fantastik, Jangari""")

@dp.message_handler(text="ɴᴀғᴀs💨 ᴏʟᴍᴀ🔫")
async def kino8(msg: types.Message):
    kino="BAACAgQAAxkBAAOCZsm5v6xdEcKN6M0HAycGMM5J4y4AAh8KAAICtXFQ29MRYXvWvPg1BA"
    await msg.answer_video(video=kino,caption="""🎥 Nafas olma
📹 Sifati: HD 480p
📆 Yil: 2016
🎞 Janr: Jinoyatchilik, Triller
🇺🇿 O'zbek tilida""")
    
