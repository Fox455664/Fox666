# --- START OF FILE bot.py ---
from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, group, source, photosource, caserid, ch, bot_token, bot_token2
import os

API_ID = int(os.getenv("API_ID", "25761783"))
API_HASH = os.getenv("API_HASH", "7770de22ee036afb30a99d449c51f4b8")

# Ensure bot_token and bot_token2 are not None or empty
if not bot_token:
    raise ValueError("BOT_TOKEN environment variable is not set!")
if not bot_token2:
    raise ValueError("SESSION_STRING environment variable is not set!")

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
