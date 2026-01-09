import os
import logging
from pyrogram import Client, idle, filters
from pyromod import listen
from casery import bot_token, bot_token2

# إعدادات السجلات
logging.basicConfig(level=logging.INFO, format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s")
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", "24722068"))
API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# البوت الأساسي - قمنا بإضافة المجلدين في الـ plugins
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr"), # هنا مجلد الميوزك والأوامر
    in_memory=True
)

# الحساب المساعد
lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2,
    in_memory=True
)

async def start_zombiebot():
    print("🚀 جاري تشغيل المصنع والبوت...")
    await bot.start()
    if bot_token2:
        try:
            await lolo.start()
            print("✅ المساعد يعمل!")
        except:
            print("⚠️ فشل تشغيل المساعد")
    
    # تحميل أوامر المصنع يدوياً لو كانت في مجلد مختلف
    # @bot.on_message... (الخ)
    
    print("🚀 النظام يعمل الآن! اذهب للبوت وجرب.")
    await idle()
