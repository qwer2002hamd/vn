

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
    command(["مميزات","المميزات"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس الميوزك
  
  
◉︙المبرمج ↫ لعمل نداء لمبرمج السورس
◉︙المالك↫لعمل نداء لممالك المجموعه
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
◉︙تلغراف او ميديا↫ لانشاء رابط بالرد ع الصوره
◉︙الكروب ↫ لعرض معلومات المجموعه
◉︙الرابط ↫يقوم بإنشاء رابط الكروب
◉︙تاك ↫لعمل تاك لكل الاعضاء
◉︙منو موجود ↫لمعرفة الموجودين في الاتصال
◉︙بحث+اسم الاغنيه ↫يبحث ما تريده
◉︙المغادره ↫النزول من الاتصال لعدم وجود احد
◉︙‹ قران 𐇡 الشيخ 𐇡 سوره 𐇡 اذكار  ›
◉︙‹ افتار شباب 𐇡 افتار بنات 𐇡 انمي ›
◉︙‹ هيدرات 𐇡 كتيبات 𐇡 ستوري ›
◉︙‹ كت 𐇡 يوزري 𐇡 اسالني ›
◉︙‹ صوره 𐇡 اقتباس 𐇡 جمالي ›
◉︙‹ صراحه 𐇡 لو خيروك 𐇡 اسمي ›
◉︙‹ نكته 𐇡 انصحني 𐇡 حروف ›

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
