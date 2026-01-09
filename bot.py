import os
import logging
from pyrogram import Client, idle, filters
# من المهم استيراد datetime و os إذا كنت ستستخدمهم في رسالة التشغيل
from datetime import datetime

# --- إعداد السجلات (هذا الجزء هو الذي كان ناقصاً أو به خطأ) ---
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

# استيراد الإعدادات من ملف casery
from casery import bot_token, bot_token2, caserid

API_ID = int(os.getenv("API_ID", "24722068"))
API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# تعريف البوت
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr")
)

# تعريف المساعد
lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2
)

async def start_zombiebot():
    logger.info("جاري تشغيل البوت...")
    await bot.start()
    
    # كود إرسال رسالة التشغيل للمطور
    try:
        me = await bot.get_me()
        msg = f"""
✅ **تم تشغيل البوت بنجاح**

🤖 **يوزر البوت:** @{me.username}
🆔 **أيدي المطور:** `{caserid}`
🕒 **الوقت:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🚀 النظام يعمل الآن بالكامل!
"""
        await bot.send_message(caserid, msg)
        logger.info(f"✅ Startup message sent to {caserid}")
    except Exception as e:
        logger.warning(f"⚠️ فشل إرسال رسالة التشغيل: {e}")

    if bot_token2:
        logger.info("جاري تشغيل المساعد...")
        try:
            await lolo.start()
        except Exception as e:
            logger.warning(f"⚠️ فشل تشغيل المساعد: {e}")
            
    logger.info("🚀 النظام يعمل الآن بالكامل!")
    await idle()
