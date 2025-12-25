import os
import redis
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger

# البيانات الأساسية
API_ID = 25761783
API_HASH = "7770de22ee036afb30a99d449c51f4b8"

# ✅ الرابط المباشر لقاعدة Upstash (تم التعديل هنا)
# لاحظ: rediss:// بـ 2 s عشان الاتصال الآمن
UPSTASH_URL = "rediss://default:AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE@ultimate-ferret-48101.upstash.io:6379"

# محاولة جلب الرابط من النظام، لو مش موجود نستخدم الرابط المباشر اللي فوق
REDIS_URL = os.getenv("REDIS_URL", UPSTASH_URL)

try:
    # الاتصال بقاعدة البيانات
    r = redis.from_url(REDIS_URL, decode_responses=False)
    # تجربة الاتصال للتأكد
    r.ping()
    print(f"✅ تم الاتصال بـ Redis بنجاح: {REDIS_URL.split('@')[1]}")
except Exception as e:
    print(f"❌ فشل الاتصال الأول، جاري المحاولة بالطريقة اليدوية... الخطأ: {e}")
    try:
        # محاولة اتصال يدوية (احتياطي)
        r = redis.Redis(
            host="ultimate-ferret-48101.upstash.io",
            port=6379,
            password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
            ssl=True,
            decode_responses=False
        )
        r.ping()
        print("✅ تم الاتصال بـ Redis (الطريقة اليدوية)")
    except Exception as e2:
        print(f"❌ فشل الاتصال نهائياً بقاعدة البيانات: {e2}")
        # هنا بس لو كل حاجة باظت يرجع للمحلي
        r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=False)

def get_Bots():
    try:
        lst = []
        # جلب قائمة البوتات المخزنة
        for a in r.smembers("maker_bots"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except Exception as e:
        print(f"Error getting bots: {e}")
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
