import os
import logging
from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, bot_token, bot_token2

# إعداد السجلات لرؤية الأخطاء في Koyeb
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# جلب البيانات
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if not API_ID or not API_HASH:
    logger.error("❌ API_ID or API_HASH is missing!")
    exit(1)

try:
    API_ID = int(API_ID)
except ValueError:
    logger.error("❌ API_ID must be an integer!")
    exit(1)

# تعريف الكلاينت (بدون تحميل البلاغنز هنا لتجنب التداخل الدائري)
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASER") # سيتم تحميل البلاغنز عند عمل start
)

lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2
)

DEVS = caes
DEVSs = []

async def start_zombiebot():
    logger.info("جاري تشغيل البوت الأساسي...")
    try:
        await bot.start()
        me = await bot.get_me()
        logger.info(f"✅ تم تشغيل البوت: @{me.username}")
    except Exception as e:
        logger.error(f"❌ فشل تشغيل البوت: {e}")
        return

    logger.info("جاري تشغيل الحساب المساعد...")
    try:
        await lolo.start()
        user = await lolo.get_me()
        logger.info(f"✅ تم تشغيل المساعد: {user.first_name}")
    except Exception as e:
        logger.error(f"⚠️ فشل تشغيل الحساب المساعد (تأكد من كود الجلسة): {e}")

    try:
        if casery:
            await bot.send_message(casery, "**✅ تم تشغيل الصانع بنجاح في السيرفر!**")
    except Exception as e:
        logger.warning(f"⚠️ لم أستطع إرسال رسالة للمطور: {e}")

    logger.info("🚀 النظام يعمل الآن بالكامل. في انتظار الأوامر...")
    await idle()
