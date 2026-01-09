import asyncio
import requests
import random
import re
import os
import time
from datetime import datetime
import redis
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import PeerIdInvalid, FloodWait, UserNotParticipant
from pyrogram import enums

# استيراد بعض الدوال من ملفات أخرى (مع تجاهل الأخطاء إذا لم توجد)
try:
    from config import user, dev, call, logger, logger_mode, botname, appp
    from CASERr.daty import get_call, get_userbot, get_dev, get_logger
except ImportError:
    pass

# =========================================================
# ⬇️⬇️⬇️ بياناتك وإعدادات السورس (Titanx) ⬇️⬇️⬇️
# =========================================================

# المطورين الاحتياطيين
caes = ["f_o_x_351", "zozooryy", "cyv0we"]

# البيانات الأساسية
casery = "f_o_x_351"
caserid = 7669264153
OWNER_NAME = "النسور"
OWNER = caserid
muusiic = "SOURCE Titanx"
suorce = "SOURCE Titanx"
source = "https://t.me/fox68899"
ch = "fox68899"  # يوزر القناة بدون @
group = "https://t.me/fox68899"
photosource = "https://envs.sh/ws4.webp"

# =========================================================
# ⬆️⬆️⬆️ نهاية بياناتك ⬆️⬆️⬆️
# =========================================================

# --- حل مشكلة الاستيراد (Mapping Variables) ---
devchannel = source      # قناة السورس
devgroup = group         # جروب الدعم
devuser = casery         # يوزر المطور
name = f"{OWNER_NAME}"   # الاسم المعروض
devphots = photosource   # ✅ حل مشكلة devphots

# --- الاتصال بقاعدة البيانات (Upstash Redis) ---
try:
    r = redis.Redis(
        host="ultimate-ferret-48101.upstash.io",
        port=6379,
        password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
        ssl=True,
        decode_responses=True
    )
    # r.ping()
except Exception as e:
    print(f"❌ خطأ في الاتصال بـ Redis: {e}")
    r = None

# --- الكيبوردات ---
Keyard = ReplyKeyboardMarkup(
    [
        [("• زخرفه •")],
        [("• صراحه •"),("• تويت •")],
        [("• انصحني •"),("• لو خيروك •")],
        [("• حروف •"),("• امثله •")],
        [("• نكته •"),("• احكام •")],
        [("• قران •"),("• ازكار •")],
        [("• صور •")],
        [("• صور شباب •"),("• صور بنات •")],
        [("• انمي •"),("• استوري •")],
        [("• اغاني •")],
        [("• ممثلين •"),("• مغنين •")],
        [("• مشاهير •"),("• لاعبين •")],
        [("• اعلام •"),("• افلام •")],
        [("• لغز •"),("• مختلف •")],
        [("مطور البوت"),("مطور السورس")],
        [("السورس")],
        [("/start")]
    ],
    resize_keyboard=True
)

Keyboard = ReplyKeyboardMarkup(
    [
        [("قسم البوت"), ("قسم المساعد")],
        [("قسم الاذاعه"), ("قسم الترويج")],
        [("قسم الاشتراك"), ("قسم الاحتياطي")],
        [("《الاحصائيات》")],
        [("قسم التشغيل")],
        [("قسم الحظر")],
        [("قسم التفعيل والتعطيل")],
        [("مطور السورس"), ("مطور البوت")],
        [("سورس")]
    ],
    resize_keyboard=True
)

# --- دوال إدارة المستخدمين ---
def add_user(user_id, bot_id):
    if r: 
        try: r.sadd(f"USERS{bot_id}", user_id)
        except: pass

def is_user(user_id, bot_id):
    if r:
        try: return r.sismember(f"USERS{bot_id}", user_id)
        except: return False
    return False

def get_user(bot_id):
    if r:
        try: return list(r.smembers(f"USERS{bot_id}"))
        except: return []
    return []

def get_groups(bot_id):
    if r:
        try: return list(r.smembers(f"GROUPS{bot_id}"))
        except: return []
    return []

# --- دالة الاشتراك الإجباري ---
async def johned(client, message):
    try:
        user_status = await client.get_chat_member(ch, message.from_user.id)
        if user_status.status in [enums.ChatMemberStatus.BANNED, enums.ChatMemberStatus.LEFT]:
            raise UserNotParticipant 
        return False 
    
    except UserNotParticipant:
        try:
            bot_username = client.me.username
            await message.reply(
                f"🚸 **عذراً عزيزي {message.from_user.mention}**\n\n⚠️ **عليك الاشتراك في قناة السورس أولاً لاستخدام البوت.**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("اشترك الآن 🔱", url=source)],
                    [InlineKeyboardButton(f"تحديث 🔄", url=f"https://t.me/{bot_username}?start=start")]
                ]),
                disable_web_page_preview=True
            )
        except:
            pass
        return True 
        
    except Exception:
        return False

# --- دالة جلب قناة السورس ---
def get_channel(bot_username):
    return source

# --- دوال الحظر ---
def add_CASER(bots, bot_username):
    if r: 
        try: r.sadd(f"CASER{bot_username}", str(bots))
        except: pass

async def johCASER(client, message):
    if not r: return False
    try:
        bot_username = client.me.username
        res = r.smembers(f"CASER{bot_username}")
        for x in res:
            if str(message.from_user.id) in x: return True
    except:
        pass
    return False

# --- دالة صناعة صورة البداية ---
async def gen_ot(app, bot_username, bot_id):
    output_path = f"start_{bot_id}.png"
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_path = await app.download_media(user_chat.photo.big_file_id)
            img = Image.open(photo_path).resize((1280, 720)).convert("RGBA")
            
            # فلتر وتعتيم الخلفية
            bg = img.filter(ImageFilter.BoxBlur(10))
            bg = ImageEnhance.Brightness(bg).enhance(0.5)
            
            draw = ImageDraw.Draw(bg)
            
            # محاولة تحميل الخطوط
            try:
                font_lg = ImageFont.truetype("font2.ttf", 80)
                font_sm = ImageFont.truetype("font.ttf", 45)
            except:
                font_lg = ImageFont.load_default()
                font_sm = ImageFont.load_default()

            # الكتابة على الصورة
            draw.text((580, 120), f"{suorce}", fill="white", font=font_lg)
            draw.text((580, 230), f"USER: @{bot_username}", fill="white", font=font_sm)
            draw.text((580, 300), f"ID: {bot_id}", fill="white", font=font_sm)
            draw.text((580, 370), f"DEV: @{casery}", fill="white", font=font_sm)
            
            bg.save(output_path)
            if os.path.exists(photo_path): os.remove(photo_path)
            return output_path
    except Exception as e:
        print(f"Error Gen Image: {e}")
    
    # في حالة الفشل، نرجع صورة السورس الافتراضية
    return photosource

# ================= كود Start =================

@Client.on_message(filters.command(["/start", "رجوع"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
    # 1. التحقق من الحظر
    if await johCASER(client, message): return
    
    # 2. التحقق من الاشتراك الإجباري
    if await johned(client, message): return

    bot_username = client.me.username
    bot_id = client.me.id
    
    # تحديد ايدي المطور
    OWNER_ID = caserid
    try:
        dev_chk = await get_dev(bot_username)
        if dev_chk: OWNER_ID = dev_chk
    except: pass

    # محاولة جلب معلومات المطور للعرض
    try:
        dev_info = await client.get_chat(OWNER_ID)
        dev_name = dev_info.first_name
        dev_user_link = dev_info.username
    except:
        dev_name = OWNER_NAME
        dev_user_link = casery

    # تسجيل المستخدم
    if not is_user(message.from_user.id, bot_id):
        add_user(message.from_user.id, bot_id)
        try:
            msg = f"🙍 **مستخدم جديد دخل للبوت:**\n\n🎯 الاسم: {message.from_user.mention}\n🆔 الايدي: `{message.from_user.id}`"
            await client.send_message(OWNER_ID, msg)
        except: pass

    # تجهيز الأزرار
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"), InlineKeyboardButton("English 🏴", callback_data="english")],
        [InlineKeyboardButton(dev_name, url=f"https://t.me/{dev_user_link}")]
    ])

    # تجهيز الصورة
    photo = await gen_ot(client, bot_username, bot_id)
    caption = f"╮⦿ اهـلا بڪ عزيـزي {message.from_user.mention}\n│⎋ اليـكـ كيبورد الاعضاء للاستمتاع"
    
    try:
        await message.reply_photo(
            photo=photo, 
            caption=caption, 
            reply_markup=Keyard
        )
        if photo != photosource and os.path.exists(photo): 
            os.remove(photo)
    except Exception as e:
        await message.reply_text("مرحباً بك في البوت 🌹", reply_markup=Keyard)
        print(f"Start Error: {e}")

# ================= إشعار التشغيل =================
async def send_online_signal():
    await asyncio.sleep(15)
    try:
        from bot import bot as main_bot 
        me = await main_bot.get_me()
        
        TARGET_ID = caserid 
        
        msg = f"""
✅ **تم تشغيل سورس {suorce} بنجاح**

🤖 البوت: @{me.username}
🆔 المطور: `{TARGET_ID}`
📢 قناة الاشتراك: @{ch}

🚀 السورس يعمل الآن بكفاءة!
✅ تم الاتصال بقاعدة البيانات Redis
"""
        await main_bot.send_message(TARGET_ID, msg)
        print("✅ Startup Signal Sent.")
    except Exception as e:
        print(f"Startup Signal Note: {e}")

asyncio.create_task(send_online_signal())
