import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AnonX import app
from config import OWNER_ID
from AnonX.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX.misc import SUDOERS

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}ZAIDRD")[1].replace("\n",""))
    return False

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}ZAIDRD{rd}\n")
    return True

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return


'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
def get_rdod(chat_id):
   with open("getrdod.txt", "r+") as f:
       lines = f.readlines()
   text = "• الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("ZAIDRD")[0]
       text += f"{b}\n"
   if text == "• الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"
       
async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await app.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
    

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
@app.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    ask1 = await app.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ask1.text
    ask2 = await app.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id))
    copy = await ask2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح")
    else: return await ask2.reply("حدث خطأ")

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
@app.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ask = await app.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ask.text}ZAIDRD{a}"
   b = del_rd(x)
   await ask.reply("• تم مسح الرد")
   

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
@app.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
@app.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("• لا توجد ردود هنا")
    else: return await message.reply(a)

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
@app.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await app.copy_message(message.chat.id, LOG, a, reply_to_message_id=message.id)
   else: return 
   
   
app.start()
print("Lol")

'''
Programmed by : 🎖️ @ah_2_v
   Channel -› • @ah07v
'''
