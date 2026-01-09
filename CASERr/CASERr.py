import asyncio
import requests
import random
import re
import os
import time
from datetime import datetime
import redis
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import PeerIdInvalid, FloodWait
from pyrogram import enums
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from casery import caes, casery, group, source, photosource, caserid, OWNER, muusiic, suorce
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

# إعدادات الاسم الافتراضية
name = f"{OWNER}"

# --- الاتصال بقاعدة البيانات ---
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

# --- الكيبوردات الأساسية ---
# (تم الإبقاء عليها كما هي لضمان توافق الأوامر)
Keyard = ReplyKeyboardMarkup(
    [[("• زخرفه •")],[("• صراحه •"),("• تويت •")],[("• انصحني •"),("• لو خيروك •")],[("• حروف •"),("• امثله •")],[("• نكته •"),("• احكام •")],[("• قران •"),("• ازكار •")],[("• صور •")],[("• صور شباب •"),("• صور بنات •")],[("• انمي •"),("• استوري •")],[("• اغاني •")],[("• ممثلين •"),("• مغنين •")],[("• مشاهير •"),("• لاعبين •")],[("• اعلام •"),("• افلام •")],[("• لغز •"),("• مختلف •")],[("مطور البوت"),("مطور السورس")],[("السورس")],[("/start")]],
    resize_keyboard=True
)

Keyboard = ReplyKeyboardMarkup(
    [[("قسم البوت"), ("قسم المساعد")],[("قسم الاذاعه"), ("قسم الترويج")],[("قسم الاشتراك"), ("قسم الاحتياطي")],[("《الاحصائيات》")],[("قسم التشغيل")],[("قسم الحظر")],[("قسم التفعيل والتعطيل")],[("مطور السورس"), ("مطور البوت")],[("سورس")]],
    resize_keyboard=True
)

# --- دوال المستخدمين ---
def add_user(user_id, bot_id):
    if r: r.sadd(f"USERS{bot_id}", user_id)

def is_user(user_id, bot_id):
    if r: return r.sismember(f"USERS{bot_id}", user_id)
    return False

def get_user(bot_id):
    if r: return list(r.smembers(f"USERS{bot_id}"))
    return []

def get_groups(bot_id):
    if r: return list(r.smembers(f"GROUPS{bot_id}"))
    return []

# --- دالة الاشتراك الإجباري ---
async def johned(client, message):
    try:
        # يمكنك تعديل هذا المنطق لجلب قناة الاشتراك من الداتا
        return False 
    except:
        return False

# --- دالة جلب قناة السورس (هذه التي كانت تسبب ImportError) ---
def get_channel(bot_username):
    return source

# --- دوال الحظر ---
def add_CASER(bots, bot_username):
    if r: r.sadd(f"CASER{bot_username}", str(bots))

async def johCASER(client, message):
    if not r: return False
    bot_username = client.me.username
    res = r.smembers(f"CASER{bot_username}")
    for x in res:
        if str(message.from_user.id) in x: return True
    return False

# --- دالة صنع الصورة (المحسنة) ---
async def gen_ot(app, bot_username, bot_id):
    output_path = f"start_{bot_id}.png"
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_path = await app.download_media(user_chat.photo.big_file_id)
            img = Image.open(photo_path).resize((1280, 720)).convert("RGBA")
            
            # فلتر الصورة الخلفية
            bg = img.filter(ImageFilter.BoxBlur(10))
            bg = ImageEnhance.Brightness(bg).enhance(0.5)
            
            draw = ImageDraw.Draw(bg)
            try:
                font_lg = ImageFont.truetype("font2.ttf", 80)
                font_sm = ImageFont.truetype("font.ttf", 45)
            except:
                font_lg = font_sm = ImageFont.load_default()

            # رسم البيانات على الصورة
            draw.text((580, 120), f"{suorce}", fill="white", font=font_lg)
            draw.text((580, 230), f"USER: @{bot_username}", fill="white", font=font_sm)
            draw.text((580, 300), f"ID: {bot_id}", fill="white", font=font_sm)
            draw.text((580, 370), f"DEV: @{casery}", fill="white", font=font_sm)
            
            bg.save(output_path)
            if os.path.exists(photo_path): os.remove(photo_path)
            return output_path
    except Exception as e:
        print(f"Error Gen Image: {e}")
    return photosource

# --- أمر Start ---
@Client.on_message(filters.command(["/start", "رجوع"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
    if await johCASER(client, message): return
    
    bot_username = client.me.username
    bot_id = client.me.id
    
    # جلب معلومات المطور
    OWNER_ID = await get_dev(bot_username)
    try:
        dev_info = await client.get_chat(OWNER_ID)
        dev_name = dev_info.first_name
        dev_user = dev_info.username
    except:
        dev_name = "المطور"
        dev_user = casery

    # تسجيل مستخدم جديد
    if not is_user(message.from_user.id, bot_id):
        add_user(message.from_user.id, bot_id)
        try:
            await client.send_message(OWNER_ID, f"🙍 **مستخدم جديد دخل للبوت:**\n\n🎯 الاسم: {message.from_user.mention}\n🆔 الايدي: `{message.from_user.id}`")
        except: pass

    # الكيبورد
    buttons = [
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"), InlineKeyboardButton("English 🏴", callback_data="english")],
        [InlineKeyboardButton(dev_name, url=f"https://t.me/{dev_user}")]
    ]

    photo = await gen_ot(client, bot_username, bot_id)
    try:
        await message.reply_photo(photo=photo, caption=f"╮⦿ اهـلا بڪ عزيـزي {message.from_user.mention}\n│⎋ اليـكـ كيبورد الاعضاء للاستمتاع", reply_markup=Keyard)
        if photo != photosource and os.path.exists(photo): os.remove(photo)
    except:
        await message.reply_text("مرحباً بك في البوت 🌹", reply_markup=Keyard)

# ================= Startup Log =================
# الكود المصلح لإرسال إشارة التشغيل للمطور عند فتح السورس
async def send_online_signal():
    from bot import bot as main_bot # استيراد البوت الأساسي
    await asyncio.sleep(15) # انتظار استقرار الاتصال
    try:
        me = await main_bot.get_me()
        OWNER_ID = await get_dev(me.username)
        
        msg = f"""
✅ **تم تشغيل المصنع بنجاح**

🤖 البوت: @{me.username}
🆔 المطور: `{OWNER_ID}`
🕒 الوقت: {datetime.now().strftime('%I:%M %p')}

🚀 السورس يعمل الآن بكفاءة!
"""
        await main_bot.send_message(OWNER_ID, msg)
        print("✅ Startup Signal Sent.")
    except Exception as e:
        print(f"❌ Startup Signal Failed: {e}")

# تشغيل المهمة في الخلفية
asyncio.create_task(send_online_signal())
