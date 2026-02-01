import os
import redis
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger

# البيانات الأساسية
API_ID = 25761783
API_HASH = "7770de22ee036afb30a99d449c51f4b8"

# --- إعدادات الاتصال بـ Redis ---
# الرابط المباشر مع rediss:// للاتصال المشفر
UPSTASH_URL = "rediss://default:AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE@ultimate-ferret-48101.upstash.io:6379"

# محاولة جلب الرابط من متغيرات النظام أولاً، وإلا استخدام الرابط المباشر
REDIS_URL = os.getenv("REDIS_URL", UPSTASH_URL)

try:
    # محاولة الاتصال الأولى عبر الرابط
    r = redis.from_url(REDIS_URL, decode_responses=False)
    r.ping() # فحص الاتصال
    print(f"✅ Connected to Redis successfully via URL.")
except Exception as e:
    print(f"⚠️ URL connection failed: {e}, trying manual parameters...")
    try:
        # محاولة الاتصال اليدوية (Fallback)
        r = redis.Redis(
            host="ultimate-ferret-48101.upstash.io",
            port=6379,
            password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
            ssl=True,
            decode_responses=False
        )
        r.ping()
        print("✅ Connected to Redis successfully via Manual Params.")
    except Exception as e2:
        print(f"❌ Failed to connect to Redis: {e2}")
        # الاتصال المحلي كحل أخير (لن يعمل على Koyeb بدون سيرفر محلي)
        r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=False)

# --- الدوال المساعدة ---

def get_Bots():
    try:
        lst = []
        # جلب البوتات من قاعدة البيانات (تأكد أن المفتاح maker_bots هو المستخدم في كودك)
        bots = r.smembers("maker_bots")
        for a in bots:
            try:
                lst.append(eval(a.decode('utf-8')))
            except Exception as inner_e:
                print(f"Error parsing bot data: {inner_e}")
        return lst
    except Exception as e:
        print(f"Error getting bots list: {e}")
        return []

async def get_dev(bot_username):
    # الأولوية لمتغير النظام، ثم البحث في الداتا، ثم الافتراضي
    owner = os.getenv("OWNER_ID")
    if owner:
        return int(owner)
    
    bots = get_Bots()
    for x in bots:
        if x[0] == bot_username:
            return int(x[1])
    
    return 7669264153 # الايدي الافتراضي

async def get_userbot(bot_username):
    if bot_username in user:
        return user[bot_username]
    
    bots = get_Bots()
    for x in bots:
        if x[0] == bot_username:
            SESSION = x[3]
            try:
                # تم إضافة in_memory=True لتجنب مشاكل الملفات على Koyeb
                # تم تغيير اسم الجلسة ليكون فريداً لكل بوت لتجنب التداخل
                ubot = Client(
                    name=f"helper_{bot_username}",
                    api_id=API_ID,
                    api_hash=API_HASH,
                    session_string=SESSION,
                    in_memory=True
                )
                await ubot.start()
                user[bot_username] = ubot
                return ubot
            except Exception as e:
                print(f"❌ Error starting userbot for {bot_username}: {e}")
                return None
    return None

async def get_call(bot_username):
    if bot_username in call:
        return call[bot_username]
    
    ubot = await get_userbot(bot_username)
    if ubot:
        try:
            # تشغيل PyTgCalls
            calo = PyTgCalls(ubot, cache_duration=100)
            await calo.start()
            call[bot_username] = calo
            return calo
        except Exception as e:
            print(f"❌ Error starting PyTgCalls for {bot_username}: {e}")
            return None
    return None

async def get_logger(bot_username):
    log_id = os.getenv("LOGGER_ID")
    if log_id:
        return int(log_id)
        
    bots = get_Bots()
    for x in bots:
        if x[0] == bot_username:
            return x[4]
    return None

async def del_userbot(bot_username):
    if bot_username in user:
        try:
            await user[bot_username].stop()
        except:
            pass
        del user[bot_username]

async def del_call(bot_username):
    if bot_username in call:
        try:
            await call[bot_username].leave_group_call()
        except:
            pass
        del call[bot_username]
