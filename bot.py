import os
import logging
from pyrogram import Client, idle, filters
from pyromod import listen
from casery import bot_token, bot_token2

# إعدادات السجلات
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", "24722068"))
API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

if not bot_token:
    logger.error("❌ BOT_TOKEN missing!")
    exit(1)

# البوت الأساسي
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr") # تأكد أن ملفات الأوامر داخل مجلد CASERr
)

# الحساب المساعد
lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2
)

# أمر للتأكد من أن البوت يستجيب
@bot.on_message(filters.command("تست", ""))
async def test_msg(client, message):
    await message.reply_text("✅ البوت شغال وبيرد على الأوامر!")

async def start_zombiebot():
    logger.info("جاري تشغيل البوت...")
    await bot.start()
    
    if bot_token2:
        logger.info("جاري تشغيل المساعد...")
        try:
            await lolo.start()
        except Exception as e:
            logger.warning(f"⚠️ فشل تشغيل المساعد: {e}")
            
    logger.info("🚀 النظام يعمل الآن بالكامل!")
    await idle()
