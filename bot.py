import asyncio
import os
import logging
from pyrogram import Client, idle, filters
from pyrogram.enums import ParseMode

# إعدادات اللوج
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

# استيراد التوكن والايدي
try:
    from casery import bot_token, bot_token2, caserid
    from config import API_ID, API_HASH
except ImportError:
    bot_token = os.getenv("BOT_TOKEN")
    bot_token2 = os.getenv("SESSION_STRING")
    caserid = int(os.getenv("OWNER_ID", "7669264153"))
    API_ID = int(os.getenv("API_ID", "24722068"))
    API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# تعريف الكلاينتات
bot = Client(
    "CASERr_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr"),
    in_memory=True
)

assistant = Client(
    "CASERr_Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2,
    in_memory=True
)

# ==========================================
# 🕵️ جاسوس النظام (لاختبار الاتصال فقط)
# ==========================================
@bot.on_message(filters.all, group=-1000)
async def system_spy(client, message):
    user_info = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.id}"
    print(f"🕵️ [SPY EVENT] وصلت رسالة من {user_info}: {message.text}")
    # لن نوقف الرسالة هنا، سنجعلها تمر لبقية الأوامر
    message.continue_propagation()

# ✅ الدالة الرئيسية للتشغيل
async def start_zombiebot():
    print("🚀 جاري بدء عملية تشغيل نظام القيصر...")

    # 1. تشغيل البوت
    try:
        await bot.start()
        
        # 🔥 مسح أي رابط قديم (الخطوة الأهم)
        await bot.delete_webhook()
        
        me = await bot.get_me()
        print(f"✅ تم الاتصال بنجاح!")
        print(f"🤖 يوزر البوت: @{me.username}")
        print(f"🆔 ايدي البوت: {me.id}")
    except Exception as e:
        print(f"❌ فشل تشغيل البوت: {e}")
        return

    # 2. تشغيل المساعد
    if bot_token2:
        try:
            await assistant.start()
            ass_me = await assistant.get_me()
            print(f"✅ تم تشغيل المساعد: @{ass_me.username}")
        except Exception as e:
            print(f"⚠️ فشل تشغيل المساعد: {e}")

    # 3. إشعار المطور
    try:
        await bot.send_message(
            chat_id=caserid,
            text=f"✅ **نظام القيصر استيقظ الآن!**\n\n🤖 البوت: @{me.username}\n🛠 المطور: [اضغط هنا](tg://user?id={caserid})"
        )
        print(f"🔔 تم إرسال إشعار التشغيل للمطور ({caserid})")
    except Exception as e:
        print(f"⚠️ لم أتمكن من إرسال رسالة للمطور: {e}")

    print("📡 البوت الآن في وضع الاستماع للرسائل (Idle Mode)...")
    
    # 4. الحفاظ على البوت يعمل
    await idle()
    
    # 5. الإغلاق الآمن
    await bot.stop()
    if bot_token2:
        await assistant.stop()
