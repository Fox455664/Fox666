import asyncio
import os
import logging
from pyrogram import Client, idle
from pyrogram.enums import ParseMode

# إعدادات اللوج
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

# استيراد التوكن والايدي
try:
    from casery import bot_token, bot_token2, caserid
    from config import API_ID, API_HASH
except ImportError:
    bot_token = os.getenv("BOT_TOKEN")
    bot_token2 = os.getenv("SESSION_STRING")
    caserid = int(os.getenv("OWNER_ID", "7669264153"))
    API_ID = int(os.getenv("API_ID", "24722068"))
    API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# تعريف الكلاينتات (خارج الدالة عشان الملفات التانية تشوفهم)
bot = Client(
    "CASERr_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr"),
    in_memory=True
)

assistant = Client(
    "CASERr_Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2,
    in_memory=True
)

# هذه هي الدالة التي يبحث عنها main.py
async def start_zombiebot():
    print("🚀 جاري تشغيل نظام القيصر...")

    # 1. تشغيل البوت
    try:
        await bot.start()
        me = await bot.get_me()
        print(f"✅ تم تشغيل البوت: @{me.username}")
    except Exception as e:
        print(f"❌ فشل تشغيل البوت: {e}")
        return

    # 2. تشغيل المساعد
    if bot_token2:
        try:
            await assistant.start()
            ass_me = await assistant.get_me()
            print(f"✅ تم تشغيل المساعد: @{ass_me.username}")
        except Exception as e:
            print(f"⚠️ فشل تشغيل المساعد: {e}")

    # 3. إشعار المطور
    try:
        await bot.send_message(
            chat_id=caserid,
            text=f"✅ **تم تشغيل السورس بنجاح!**\n\n🤖 **البوت:** @{me.username}\n📡 **النظام:** متصل مع main.py"
        )
    except:
        pass

    print("✅ السورس يعمل الآن بكفاءة...")
    
    # 4. وضع الخمول (مهم جداً عشان main.py ما يقفلش)
    await idle()
    
    # 5. الإغلاق عند التوقف
    await bot.stop()
    if bot_token2:
        await assistant.stop()
