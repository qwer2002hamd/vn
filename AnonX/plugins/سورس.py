
import asyncio

import os
import config
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
    command(["سورسي","سورس","السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/550daebd925be5fd35342.jpg",
        caption=f"""𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑌.𝑂²¹ ͢͢➛ℍ𝗺!ِٰ𝗱♪", url=f"https://t.me/ah_2_v"), 
                
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/HAMD_MUSIC_BOT?startgroup=true"),
                ],

            ]

        ),

    )


