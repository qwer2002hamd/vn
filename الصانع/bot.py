from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=21468057,
    api_hash="f4a868976632fec2260eb7a7f9d88720",
    bot_token="6285659665:AAGZvJZmLPpPjFYav6W31poajqz-Sc-mAMw",#توكن المصنع
    plugins=dict(root="ah_2_v")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "ah_2_v"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
