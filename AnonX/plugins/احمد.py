import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


REPLY_MESSAGE = "**اليك لـوحه بعض مميزات الـبوت**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("المبرمـج"),
        ("الـمطور")
    ],
    [
        ("افتار شباب"),
        ("افتار بنات")
    ],
    [
        ("ستوري"), 
        ("كت بالصوره")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("اغنيه"), 
        ("غنيلي")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه"), 
        ("ايدي")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("اسمي"), 
        ("بايو")
    ],
    [
        ("نكته"),
        ("كتبات") 
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب"), 
        ("تحويل الصوره") 
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("الالعاب"), 
        ("ميديا")
    ],
    [
        ("اخـفاء الكيبورد")
    ]
]

@app.on_message(filters.regex("/HMD"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخـفاء الكيبورد"))
async def down(client, message):
          m = await message.reply(" تم اخفاء الكيبورد بنجاح .**\n\n- لاظهار لـوحه بعض مميزات الـبوت اضغط  /HMD", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يـوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/6468b22dc90f83241f86f.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
            ]
         ]
     )
  )

    
  
