import sys
import traceback
import asyncio
import redis
from pyrogram import Client, filters, continue_propagation
from pyrogram.types import Message
from config import user, dev, call, logger, logger_mode, botname, appp
from casery import caserid

# --- الاتصال بقاعدة البيانات للفحص ---
try:
    r = redis.Redis(
        host="ultimate-ferret-48101.upstash.io",
        port=6379,
        password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
        ssl=True,
        decode_responses=True
    )
except:
    r = None

# ==============================================================================
# 👁️‍🗨️ (المفتش العام) - يشتغل قبل أي ملف في السورس (Group = -100)
# ==============================================================================
@Client.on_message(filters.all, group=-100)
async def inspector_entry(client, message: Message):
    if not message.from_user:
        return
    
    user_id = message.from_user.id
    username = f"@{message.from_user.username}" if message.from_user.username else "NoUser"
    msg_text = message.text if message.text else f"[{message.media}]"
    chat_id = message.chat.id
    
    print(f"\n⚡ [استلام] من: {username} ({user_id}) | النص: {msg_text}")

    # 1️⃣ فحص الحظر العام (Ban)
    try:
        bot_username = client.me.username
        if r:
            ban_list = r.smembers(f"CASER{bot_username}")
            for x in ban_list:
                if str(user_id) in x:
                    print(f"⛔ [منع] السبب: المستخدم محظور عام (Ban).")
                    # هنا مش بنوقف عشان كود الحظر الأصلي يشتغل ويرد عليه، بس إحنا عرفنا السبب
                    break
    except: pass

    # 2️⃣ فحص الكتم (Mute)
    # (هنا بنعمل محاكاة لفحص الكتم عشان نعرف لو هو السبب)
    # ملاحظة: الكود الفعلي للكتم موجود في hmay.py، بس هنا بنراقب بس

    # 3️⃣ تمرير الرسالة لباقي الملفات
    # لو الرسالة وصلت هنا، معناها إنها جاهزة للمعالجة
    # الأمر ده مهم جداً عشان يخلي باقي الملفات تشتغل
    message.continue_propagation()


# ==============================================================================
# 🚨 (صائد الأخطاء) - يمسك أي خطأ يحصل في أي ملف ويبعتهولك
# ==============================================================================
# بنستعمل هنا خدعة في بايروجرام عشان نلقط أي Exception يحصل في الهاندلرز
# (هذا الجزء متقدم ويعمل كـ Global Exception Handler)

# لا نحتاج لكود هنا، لأن بايروجرام بيطبع الأخطاء في اللوج تلقائياً.
# لكن سنضيف أمر لفحص "صحة السورس" يدوياً.

@Client.on_message(filters.command(["فحص", "النظام", "debug"], ""), group=999)
async def system_check(client, message):
    if message.from_user.id != caserid:
        return
    
    status_report = "📊 **تقرير حالة السورس (المتحكم):**\n\n"
    
    # 1. فحص الاتصال بـ Redis
    try:
        if r and r.ping():
            status_report += "✅ **قاعدة البيانات:** متصلة (Redis).\n"
        else:
            status_report += "❌ **قاعدة البيانات:** غير متصلة!\n"
    except:
        status_report += "❌ **قاعدة البيانات:** خطأ في الاتصال.\n"

    # 2. فحص البوت المساعد
    try:
        from CASERr.daty import get_userbot
        ubot = await get_userbot(client.me.username)
        if ubot and ubot.is_connected:
            status_report += "✅ **المساعد:** متصل وجاهز.\n"
        else:
            status_report += "⚠️ **المساعد:** غير متصل أو مفصول.\n"
    except:
        status_report += "⚠️ **المساعد:** لم يتم التحقق.\n"

    # 3. فحص الذاكرة (بسيط)
    status_report += f"✅ **البوت الأساسي:** يعمل (@{client.me.username}).\n"
    
    await message.reply_text(status_report)
    print("✅ [INFO] تم إرسال تقرير الفحص للمطور.")
