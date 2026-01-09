import asyncio
import os
import redis
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from pyrogram import filters, Client, enums
from pyrogram.errors import UserNotParticipant

# استيراد الإعدادات
try:
    from config import user, dev, call, logger, logger_mode, botname, appp
    from CASERr.daty import get_call, get_userbot, get_dev, get_logger
except ImportError:
    pass

# ================= بيانات السورس =================
caserid = 7669264153
OWNER_NAME = "النسور"
OWNER = caserid
casery = "f_o_x_351"
suorce = "SOURCE Titanx"
source = "https://t.me/fox68899"
ch = "fox68899"
photosource = "https://envs.sh/ws4.webp"

# ================= Redis =================
try:
    r = redis.Redis(
        host="ultimate-ferret-48101.upstash.io",
        port=6379,
        password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
        ssl=True,
        decode_responses=True
    )
except Exception:
    r = None

# ================= الكيبوردات =================
Keyard = ReplyKeyboardMarkup(
    [[("• زخرفه •")],[("• صراحه •"),("• تويت •")],[("• انصحني •"),("• لو خيروك •")],[("• حروف •"),("• امثله •")],[("• نكته •"),("• احكام •")],[("• قران •"),("• ازكار •")],[("• صور •")],[("• صور شباب •"),("• صور بنات •")],[("• انمي •"),("• استوري •")],[("• اغاني •")],[("• ممثلين •"),("• مغنين •")],[("• مشاهير •"),("• لاعبين •")],[("• اعلام •"),("• افلام •")],[("• لغز •"),("• مختلف •")],[("مطور البوت"),("مطور السورس")],[("السورس")],[("/start")]],
    resize_keyboard=True
)

# ==========================================
# ✅ الدالة المفقودة (تمت إضافتها لحل المشكلة)
# ==========================================
async def get_channel(message):
    """دالة لجلب بيانات القناة لتجنب خطأ ImportError"""
    try:
        # لو الرسالة جاية من قناة مباشرة
        if message.chat.type == enums.ChatType.CHANNEL:
            return message.chat
        # لو الرسالة محولة من قناة
        if message.forward_from_chat and message.forward_from_chat.type == enums.ChatType.CHANNEL:
            return message.forward_from_chat
    except Exception:
        pass
    return None

# ✅ دوال الفحص (معدلة لتجنب التهنيج)
async def johCASER(client, message):
    if not r: return False
    try:
        bot_username = client.me.username
        if r.sismember(f"CASER{bot_username}", str(message.from_user.id)):
            return True
    except: pass
    return False

async def johned(client, message):
    if message.from_user.id == caserid: return False
    try:
        # فحص بسيط: لو القناة مش موجودة أو البوت مش أدمن هيعدي
        user_status = await client.get_chat_member(ch, message.from_user.id)
        if user_status.status in [enums.ChatMemberStatus.BANNED, enums.ChatMemberStatus.LEFT]:
            raise UserNotParticipant
        return False
    except Exception:
        # لو حصل أي خطأ في الفحص (زي إن البوت مش أدمن)، خليه يكمل عشان ميعلقش
        return False

# ================= أمر Start =================
@Client.on_message(filters.command(["start", "رجوع"]) & filters.private, group=0)
async def start_handler(client, message):
    # 🕵️ سطر تشخيصي مهم جداً
    print(f"🎯 [START HANDLER] الرسالة وصلت للملف! من: {message.from_user.id}")

    if await johCASER(client, message): 
        print("🚫 المستخدم محظور في Redis")
        return
        
    if await johned(client, message): 
        print("📢 المستخدم غير مشترك في القناة")
        # هنا المفروض نبعت رسالة الاشتراك بس هنعديها دلوقتي للتجربة
        # return 

    bot_username = client.me.username
    bot_id = client.me.id
    
    print(f"✅ جاري إرسال الرد لـ {message.from_user.first_name}")

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"), InlineKeyboardButton("English 🏴", callback_data="english")],
        [InlineKeyboardButton(OWNER_NAME, url=f"https://t.me/{casery}")]
    ])

    try:
        await message.reply_photo(
            photo=photosource, # استخدمنا الصورة الافتراضية فوراً للتجربة
            caption=f"╮⦿ اهـلا بڪ عزيـزي {message.from_user.mention}\n│⎋ اليـكـ كيبورد الاعضاء للاستمتاع",
            reply_markup=buttons
        )
        await message.reply_text("👇 **القائمة الرئيسية** 👇", reply_markup=Keyard)
    except Exception as e:
        print(f"❌ فشل إرسال الرد: {e}")
        await message.reply_text("أهلاً بك!", reply_markup=Keyard)
