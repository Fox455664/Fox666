# --- START OF FILE bot.py ---
from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, group, source, photosource, caserid, ch, bot_token, bot_token2
import os

# جلب البيانات من إعدادات السيرفر فقط لضمان عدم استخدام بيانات قديمة
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# التحقق من وجود البيانات قبل التشغيل
if not bot_token:
    raise ValueError("BOT_TOKEN is missing! Please add it to Koyeb Environment Variables.")
if not bot_token2:
    raise ValueError("SESSION_STRING is missing! Please add it to Koyeb Environment Variables.")
if not API_ID:
    raise ValueError("API_ID is missing! Please add it to Koyeb Environment Variables.")
if not API_HASH:
    raise ValueError("API_HASH is missing! Please add it to Koyeb Environment Variables.")

# تحويل الـ API_ID لرقم
try:
    API_ID = int(API_ID)
except ValueError:
    raise ValueError("API_ID must be an integer number!")

# تعريف الكلاينت
bot = Client("CAR", api_id=API_ID, api_hash=API_HASH, bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=API_ID, api_hash=API_HASH, session_string=bot_token2)    

DEVS = caes
DEVSs = []
bot_id = bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(casery, "**تم تشغيل الصانع بنجاح..💗**")
    except Exception as e:
      print(f"Could not send start message to owner: {e}")
    await idle()
# --- END OF FILE bot.py ---
