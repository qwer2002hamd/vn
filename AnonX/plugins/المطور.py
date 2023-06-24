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
    command(["مبرمج","المبرمج","المبرمـج"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cbb97494ade83d71605ed.jpg",
        caption=f"""مرحبا بك عزيزي {message.from_user.mention} في قسم مطور سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑌.𝑂²¹ ͢͢➛ℍ𝗺!ِٰ𝗱♪", url=f"https://t.me/ah_2_v"), 
                 ],[
                   InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],

            ]

        ),

    )



    
