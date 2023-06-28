import os
import asyncio
import time
import shlex
import requests
from datetime import datetime
from pyrogram.errors import UserNotParticipant
from telegraph import upload_file
from typing import Callable, Coroutine, Dict, List, Tuple, Union
from json import JSONDecodeError
from pyrogram import Client, filters
from AnonX.config import BOT_USERNAME


@Client.on_message(command(["جراف", "تلجراف"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("- رد على صورة حتى احولها رابط تلجراف .")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("هاي شداز انت !!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(f"**- تم تحويل الصورة الى رابط تليجراف بنجاح :\n\nhttps://telegra.ph{response[0]}**", disable_web_page_preview=False)
    finally:
        os.remove(download_location)
