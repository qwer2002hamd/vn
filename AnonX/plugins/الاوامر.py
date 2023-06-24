import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""مرحبا بك عزيزي {message.from_user.mention}\nهذا قسم اوامر تشغيل البوت  \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر القنوات ›", callback_data="gr"), 
                 ],[
                    InlineKeyboardButton(
                        "‹ اوامر المجموعات ›", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "‹ اوامر مشتركه ›", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def cr_usage(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""
♚ مرحبا بك في اومر التشغيل بالقنوات

››  تشغيل ↫ اسم الاغنيه .
››  فيديو ↫ اسم الفديو .
››  انهاء ↫ لانهاء التشغيل في القناه .
››  تخطي ↫ لتخطي تشغيل القناه .
›› وقف ↫ لايقاف التشغيل مؤقتا في القناة
›› ربط القناه ↫ ايدي  القناه لربطها بالمجموعه .
›› مـطور الـبوت ↫ @ah_2_v

•⎆: قـناة السورس @ah07v
        
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def cr_usage(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل العربيه

›› تشغيل ↫ لتشغيل اغنية
›› فيديو ↫ لتشغيل فيديو 
›› تخطي ↫ لتخطي التشغيل الحالي
›› ايقاف ↫ لانتهاء التشغيل الحالي
›› وقف ↫ لايقاف التشغيل الحالي مؤقتا
›› استئناف ↫ لاستمرار التشغيل المتوقف
›› قائمة التشغيل ↫ لمعرفة التشغيل الحالي 
›› اعدادات ↫ لضبط اعدادات البوت
›› يـوزر الـمطور ↫ @ah_2_v

•⎆: قـناه الـسورس @ah07v
      
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر المجموعات بالانجليزي ›", callback_data="ad"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )




@app.on_callback_query(filters.regex("ad"))
async def cr_usage(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل الانجليزيه

/play - لتشغيل اغنيه
/vplay - لتشغيل فيديو
/playlist - لمعرفة قائمة التشغيل 
/skip - لتخطي التشغيل الحالي
/stop - ايقاف التشغيل الحالي
/pause - لايقاف التشغيل الحالي مؤقتا
/resume - استئناف التشغيل الحالي
/reload - تحديث قائمة الادمنية

›› يـوزر الـمطور @ah_2_v

•⎆: قـناه الـسورس @ah07v

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )





@app.on_callback_query(filters.regex("adm"))
async def cr_usage(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""
♚ مرحبا بك في الاوامر المشتركه

•الاوامر المشتركه العربيه

›› تحميل ↫ لتحميل اغنية من اليوتيوب
›› تحميل فيديو ↫ لتحميل فيديو من اليوتيوب

•⎆: قـناه الـسورس @ah07v

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر مشتركه بالانجليزي ›", callback_data="dm"),
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )


@app.on_callback_query(filters.regex("dm"))
async def cr_usage(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""
♚ مرحبا بك في الاوامر المشتركه

•الاوامر المشتركه الانجليزيه

/song - تحميل اغنيه من يوتيوب
/video - تحميل فيديو من يوتيوب

•⎆: قـناه الـسورس @ah07v
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="adm"),
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )




    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""مرحبا بك عزيزي {message.from_user.mention}\n في قسم اوامر التشغيل \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر القنوات ›", callback_data="gr"),
                 ],[
                    InlineKeyboardButton(
                        "‹ اوامر المجموعات ›", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "‹ اوامر مشتركه ›", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],

            ]

        ),

    )
