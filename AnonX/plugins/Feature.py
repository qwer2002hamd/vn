

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint


@app.on_message(
    command(["مميزات","الاوامر"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس الميوزك
  
  
◉︙المطور ↫لعمل نداء لمطور البوت
◉︙ايدي ↫لعرض معلومات حسابك مع الصوره
◉︙كول.. ↫ لنطق البوت ما تقوله
◉︙الالعاب ↫يرسل لك اللعاب البوت
◉︙غنيلي او غغ ↫يرسل لك اغنيه 
◉︙بايو ↫يرسل البايو الخاص بيك
◉︙حكمه ↫يرسل حكمه 
◉︙انصحني ↫يرسل نصيحه
◉︙ابراج ↫يعرض لك معلومات عن برجك
◉︙حساب العمر+عمرك ↫يحسب عمرك
◉︙زخرفه+الاسم ↫يزخرف اسمك
◉︙تلغراف ↫ لانشاء رابط بالرد ع الصوره
◉︙الرابط ↫يقوم بإنشاء رابط الكروب
◉︙اذاعه ↫يعمل اذاعه خاص او عام وبالتثبيت
◉︙تاك ↫لعمل تاك لكل الاعضاء
◉︙منو موجود ↫لمعرفة الموجودين في الاتصال
◉︙التنبيه ↫بفتح وقفل المكالمه الصوتيه
◉︙بحث+اسم الاغنيه ↫يبحث ما تريده
◉︙الترحيب ↫يرحيب بالاعضاء عند. الدخول والمغادره
◉︙المغادره ↫النزول من الاتصال لعدم وجود احد
◉︙ستوري، صوره، قران، الشيخ، افتار شباب، افتار بنات، انمي، اقتباس، متحركه، افلام، جمالي، اسمي، جمالي، هيدرات، لو خيروك، كت،صراحه،اسالني
    

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),                        
                 ],[
                InlineKeyboardButton(
                        "‹ حذف ›", callback_data="close"),
               ],
          ]
        ),
    )
