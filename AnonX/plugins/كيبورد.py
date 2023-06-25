import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from config import OWNER_ID
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
        ("تفعيل التواصل"),
        ("تعطيل التواصل"), 
        ("حاله التواصل") 
    ],
    [
        ("ضع قناة الاشتراك"),
        ("حذف قناه الاشتراك")
    ],
    [
        ("تفعيل الاشتراك"), 
        ("تعطيل الاشتراك"), 
        ("قناه الاشتراك") 
    ],
    [
        ("حاله الاشتراك"),
        ("الاحصائيات")
    ],
    [
        ("تفعيل اليوتيوب"), 
        ("تعطيل اليوتيوب"), 
        ("حاله اليوتيوب") 
    ],
    [
        ("تحديث السورس"),
        ("سرعه السيرفر")
    ],
    [
        ("اذاعه للمستخدمين"),
        ("اذاعه للكروبات")
    ],
    [
        ("اذاعه للمطورين"),
        ("اذاعه للاساسيين"), 
        ("اذاعه للقنوات") 
    ],
    [
        ("اذاعه للكل"), 
        ("توجيه للكل")
    ],
    [
        ("توجيه للمستخدمين"),
        ("توجيه للكروبات") 
    ],
    [
        ("توجيه للقنوات")
    ],
    [
        ("توجيه للاساسيين"), 
        ("توجيه للمطورين") 
        
    ],
    [
        ("رفع مطور"),
        ("تنزيل مطور"), 
        ("عرض المطورين") 
    ],
    [
        ("تفعيل البوت"), 
        ("تعطيل البوت")
    ],
    [
        ("اخـفاء الكيبورد")
    ]
]

@app.on_message(filters.regex("/AHMAD"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخـفاء الكيبورد"))
async def down(client, message):
          m = await message.reply(" تم اخفاء الكيبورد بنجاح", reply_markup= ReplyKeyboardRemove(selective=True))
