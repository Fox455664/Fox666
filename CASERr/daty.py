import os
import redis
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger

# البيانات الأساسية
API_ID = 25761783
API_HASH = "7770de22ee036afb30a99d449c51f4b8"

# جلب رابط Redis من إعدادات Koyeb
# ملاحظة: الرابط لازم يبدأ بـ rediss:// (بـ 2 s) عشان Upstash بيستخدم TLS
REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")

try:
    # الربط بقاعدة البيانات (التلقائي بيشغل SSL لو الرابط فيه rediss)
    r = redis.from_url(REDIS_URL, decode_responses=False)
    print("✅ تم الاتصال بقاعدة بيانات Redis بنجاح")
except Exception as e:
    print(f"❌ خطأ في الاتصال بـ Redis: {e}")
    # خيار احتياطي لو الرابط باظ
    r = redis.Redis(host="127.0.0.1", port=6379)

def get_Bots():
    try:
        lst = []
        # جلب قائمة البوتات المخزنة
        for a in r.smembers("maker_bots"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def get_dev(bot_username):
    # جلب ايدي المطور من الإعدادات أو الداتا
    owner = os.getenv("OWNER_ID")
    if owner:
        return int(owner)
    for x in get_Bots():
        if x[0] == bot_username:
            return x[1]
    return 7669264153

async def get_userbot(bot_username):
    if bot_username in user:
        return user[bot_username]
    for x in get_Bots():
        if x[0] == bot_username:
            SESSION = x[3]
            ubot = Client("CASER_ASSISTANT", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
            await ubot.start()
            user[bot_username] = ubot
            return ubot
    return None

async def get_call(bot_username):
    if bot_username in call:
        return call[bot_username]
    ubot = await get_userbot(bot_username)
    if ubot:
        # تشغيل نظام المكالمات
        calo = PyTgCalls(ubot, cache_duration=100)
        await calo.start()
        call[bot_username] = calo
        return calo
    return None

async def get_logger(bot_username):
    log_id = os.getenv("LOGGER_ID")
    if log_id:
        return int(log_id)
    for x in get_Bots():
        if x[0] == bot_username:
            return x[4]
    return None

async def del_userbot(bot_username):
    if bot_username in user:
        del user[bot_username]

async def del_call(bot_username):
    if bot_username in call:
        del call[bot_username]
