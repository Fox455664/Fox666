import os
import logging
from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, bot_token, bot_token2

# ======================
# Logging
# ======================
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger("bot")

# ======================
# ENV
# ======================
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

if not API_ID or not API_HASH:
    logger.error("❌ API_ID or API_HASH is missing!")
    exit(1)

API_ID = int(API_ID)

# ======================
# Clients
# ======================
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr")  # ✅ البلجنات هنا
)

lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2
)

# ======================
# Start Bot
# ======================
async def start_zombiebot():
    logger.info("جاري تشغيل البوت الأساسي...")
    await bot.start()

    me = await bot.get_me()
    logger.info(f"✅ تم تشغيل البوت: @{me.username} | ID: {me.id}")

    logger.info("جاري تشغيل الحساب المساعد...")
    try:
        await lolo.start()
    except Exception as e:
        logger.warning(f"⚠️ فشل تشغيل الحساب المساعد: {e}")

    if casery:
        await bot.send_message(casery, "✅ تم تشغيل البوت بنجاح")

    logger.info("🚀 النظام يعمل الآن بالكامل")
    await idle()
