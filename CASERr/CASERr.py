import asyncio
import redis
import os
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
import config  # تأكد أن ملف config.py بجانبه

# اتصال Redis (باستخدام الرابط الخارجي الذي أرسلته في config)
r = redis.from_url(config.REDIS_URL, decode_responses=True)

# --- الكيبوردات ---
Keyard = ReplyKeyboardMarkup([
    [("• زخرفه •")], [("• صراحه •"),("• تويت •")], [("• انصحني •"),("• لو خيروك •")],
    [("• حروف •"),("• امثله •")], [("• نكته •"),("• احكام •")], [("• قران •"),("• ازكار •")],
    [("• صور •")], [("• صور شباب •"),("• صور بنات •")], [("• انمي •"),("• استوري •")],
    [("• اغاني •")], [("• ممثلين •"),("• مغنين •")], [("• مشاهير •"),("• لاعبين •")],
    [("• اعلام •"),("• افلام •")], [("• لغز •"),("• مختلف •")], [("قسم الحذف والاستخراج")],
    [("مطور البوت"),("مطور السورس")], [("السورس")], [("/start")],
], resize_keyboard=True)

Keyboard = ReplyKeyboardMarkup([
    [("قسم البوت"), ("قسم المساعد")], [("قسم الاذاعه"), ("قسم الترويج")],
    [("قسم الاشتراك"), ("قسم الاحتياطي")], [("《الاحصائيات》")], [("قسم التشغيل")],
    [("قسم الحظر")], [("قسم التفعيل والتعطيل")], [("قسم الحذف والاستخراج")],
    [("كيب الاعضاء")], [("مطور السورس"), ("مطور البوت")], [("سورس")],
], resize_keyboard=True)

# --- البوت ---
app = Client(
    "TitanxBot",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

@app.on_message(filters.command(["start", "/start", "رجوع"]) & filters.private)
async def start_handler(client, message):
    bot_id = client.me.id
    # تسجيل المستخدم في رديس
    r.sadd(f"users:{bot_id}", message.from_user.id)
    
    buttons = [
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"), 
         InlineKeyboardButton("English 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="english")],
        [InlineKeyboardButton(config.OWNER_NAME, url=f"https://t.me/{config.casery}")]
    ]
    
    await message.reply_photo(
        photo=config.photosource,
        caption=f"👋 أهلاً بك في بوت {config.suorce}\n\nاستخدم الأزرار في الأسفل للتحكم.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    
    if message.from_user.id == config.caserid:
        await message.reply_text("مرحباً بك أيها المطور..", reply_markup=Keyboard)
    else:
        await message.reply_text("القائمة الرئيسية:", reply_markup=Keyard)

# --- دالة التشغيل ---
async def start_bot():
    print("--- جارٍ بدء تشغيل البوت ---")
    async with app:
        bot_info = await app.get_me()
        print(f"✅ تم تشغيل البوت بنجاح: @{bot_info.username}")
        try:
            await app.send_message(config.caserid, f"✅ تم تشغيل بوتك بنجاح!\n🤖 اليوزر: @{bot_info.username}")
        except Exception as e:
            print(f"لم يتم إرسال رسالة التشغيل للمطور: {e}")
        
        await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\nتم إيقاف البوت.")
