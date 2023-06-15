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
    command(["مطور","المطور"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/550a336110068bf81b891.jpg",
        caption=f"""**★⊷⧼𝑠𝑜𝑢𝑟𝑐𝑒 𝑎𝑟𝑛𝑜𝑝 ‌ㇱ⧽⊶★**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطور سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇\n**★⊷⧼𝑠𝑜𝑢𝑟𝑐𝑒 𝑎𝑟𝑛𝑜𝑝 ‌ㇱ⧽⊶★**""",
        def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="مطور البوت", user_id=OWNER
            ), 
            InlineKeyboardButton(
                text="𝑠𝑜𝑢𝑟𝑐𝑒 𝑎𝑟𝑛𝑜𝑝 ‌ㇱ", url=f"https://t.me/N_G_122"
            )
        ],
     ]
    return buttons
