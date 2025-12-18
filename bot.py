import os
import logging
from pyrogram import Client, idle, filters
from pyromod import listen
from casery import bot_token, bot_token2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", "24722068"))
API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# البوت الأساسي
bot = Client(
    "CAR",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr") # تأكد أن المجلد اسمه CASERr
)

# الحساب المساعد
lolo = Client(
    "hossam",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2
)

@bot.on_message(filters.command("تست", ""))
async def test_bot(client, message):
    await message.reply_text("✅ البوت يعمل بنجاح ومستعد للأوامر!")

async def start_zombiebot():
    await bot.start()
    await lolo.start()
    logger.info("🔥 البوت والحساب المساعد يعملان الآن!")
    await idle()
