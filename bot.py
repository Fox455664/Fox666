import asyncio
import os
import logging
from pyrogram import Client, idle
from pyrogram.enums import ParseMode

# استيراد التوكن والايدي من ملفات الإعدادات
try:
    from casery import bot_token, bot_token2, caserid
    from config import API_ID, API_HASH
except ImportError:
    # قيم افتراضية في حالة عدم وجود الملفات (للتجربة)
    bot_token = os.getenv("BOT_TOKEN")
    bot_token2 = os.getenv("SESSION_STRING")
    caserid = int(os.getenv("OWNER_ID", "7669264153"))
    API_ID = int(os.getenv("API_ID", "24722068"))
    API_HASH = os.getenv("API_HASH", "72feca3ed88891eeff3852e20817cdca")

# إعداد اللوج
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

# تعريف البوت الأساسي
bot = Client(
    "CASERr_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=bot_token,
    plugins=dict(root="CASERr"), # تحديد مكان ملفات الأوامر
    in_memory=True
)

# تعريف المساعد (Assistant)
assistant = Client(
    "CASERr_Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=bot_token2,
    in_memory=True
)

async def main():
    print("🚀 جاري تشغيل البوت والمساعد...")
    
    # تشغيل البوت
    try:
        await bot.start()
        me = await bot.get_me()
        print(f"✅ تم تشغيل البوت: @{me.username}")
    except Exception as e:
        print(f"❌ فشل تشغيل البوت: {e}")
        return

    # تشغيل المساعد
    if bot_token2:
        try:
            await assistant.start()
            ass_me = await assistant.get_me()
            print(f"✅ تم تشغيل المساعد: @{ass_me.username}")
        except Exception as e:
            print(f"⚠️ فشل تشغيل المساعد (تأكد من كود السيشن): {e}")

    # إرسال رسالة للمطور
    try:
        await bot.send_message(
            chat_id=caserid,
            text=f"✅ **تم إعادة تشغيل السورس بنجاح!**\n\n🤖 **البوت:** @{me.username}\n🚀 **النظام:** Pyrogram Native Idle"
        )
    except Exception:
        pass

    print("✅ السورس يعمل الآن بكفاءة عالية (Idle Mode)...")
    await idle() # وضع الخمول للحفاظ على البوت شغال
    
    # عند الإغلاق
    await bot.stop()
    if bot_token2:
        await assistant.stop()

if __name__ == "__main__":
    # تشغيل البوت مباشرة
    bot.run(main())
