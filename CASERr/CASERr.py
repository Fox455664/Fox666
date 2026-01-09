import asyncio
import requests
import random
import re
import os
import time
import datetime
import redis
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup)
from pyrogram import filters, Client, enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import PeerIdInvalid, FloodWait, UserNotParticipant
from collections import defaultdict
from asyncio import sleep
from io import BytesIO
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

# ==========================================
# 1. استيراد الإعدادات والمتغيرات
# ==========================================
try:
    from config import user, dev, call, logger, logger_mode, botname, appp
    from CASERr.daty import get_call, get_userbot, get_dev, get_logger
except ImportError:
    # قيم افتراضية في حالة فشل الاستيراد
    botname = "CASERr"
    appp = None
    pass

# متغيرات السورس الأساسية
caserid = 7669264153
OWNER = caserid
OWNER_NAME = "النسور"
casery = "f_o_x_351"
suorce = "SOURCE Titanx"
source = "https://t.me/fox68899"
ch = "fox68899"
photosource = "https://envs.sh/ws4.webp"
muusiic = "M" 
caes = [casery, "fox68899"] # قائمة المطورين
name = f"{OWNER}"

# متغيرات تخزين مؤقت
names = {} 
devuser = {} 
devchannel = {} 
devgroup = {} 
devphots = {} 
devess = {} 

# ==========================================
# 2. اتصال Redis
# ==========================================
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

# ==========================================
# 3. الدوال الناقصة (الحل الجذري للمشاكل)
# ==========================================

# ✅ دالة get_channel (لحل مشكلة ملف التشغيل)
async def get_channel(message):
    try:
        if message.chat.type == enums.ChatType.CHANNEL:
            return message.chat
        if message.forward_from_chat and message.forward_from_chat.type == enums.ChatType.CHANNEL:
            return message.forward_from_chat
    except:
        pass
    return None

# ✅ دوال الاحصائيات والتخزين (عشان الكود ميفصلش في Start)
def get_user(bot_id):
    if not r: return []
    return r.smembers(f"users:{bot_id}")

def add_user(user_id, bot_id):
    if not r: return
    r.sadd(f"users:{bot_id}", user_id)

def is_user(user_id, bot_id):
    if not r: return False
    return r.sismember(f"users:{bot_id}", user_id)

def get_groups(bot_id):
    if not r: return []
    return r.smembers(f"groups:{bot_id}")

# ==========================================
# 4. الكيبوردات (كما طلبتها)
# ==========================================
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
    [("قسم الحذف والاستخراج")],
    [("مطور البوت"),("مطور السورس")], 
    [("السورس")],    
    [("/start")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
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
    [("قسم الحذف والاستخراج")],
    [("كيب الاعضاء")],
    [("مطور السورس"), ("مطور البوت")],
    [("سورس")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keybcasoard = ReplyKeyboardMarkup(
  [
    [("قسم البوت"), ("قسم المساعد")],   
    [("قسم الاذاعه"), ("قسم الترويج")],   
    [("قسم الاشتراك"), ("قسم الاحتياطي")],     
    [("《الاحصائيات》")],
    [("قسم التشغيل")],    
    [("قسم الحظر")],    
    [("قسم التفعيل والتعطيل")],
    [("قسم الحذف والاستخراج")],
    [("كيب الاعضاء")],
    [("تفعيل الصلاحيات المدفوعه"),("تعطيل الصلاحيات المدفوعه")],
    [("مطور السورس"), ("مطور البوت")],
    [("سورس")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keyboazard = ReplyKeyboardMarkup(
  [
    [("《اذاعة》")],
    [("《اذاعة بالمجموعات》")], 
    [("《اذاعة بالتوجيه》")], 
    [("《اذاعة بالتثبيت》")],  
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keyttd = ReplyKeyboardMarkup(
  [
    [("ترويج للحمايه")],
    [("ترويج للميوزك")],   
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Kealrdyttd = ReplyKeyboardMarkup(
  [
    [("تعيين اسم البوت")],
    [("تعيين جروب السورس"), ("تعيين قناه السورس")],   
    [("تعيين مطور السورس"), ("تعيين صوره السورس")],   
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keal56rdyttd = ReplyKeyboardMarkup(
  [
    [("اضف قناه اشتراك")],  
    [("حذف قناه اشتراك")],   
    [("قنوات الاشتراك")],     
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keal16rdyttd = ReplyKeyboardMarkup(
  [
    [("الجروبات"), ("المستخدمين")],
    [("رفع نسخه الجروبات"), ("رفع نسخه الاشخاص")],
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keal36rdyttd = ReplyKeyboardMarkup(
  [
    [("《تعطيل التواصل》"), ("《تفعيل التواصل》")],
    [("تعطيل البوت بالصوره"),("تفعيل البوت بالصوره")],
    [("قفل الردود"),("فتح الردود")],
    [("قفل الميوزك"),("فتح الميوزك")],
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keal66rdyttd = ReplyKeyboardMarkup(
  [
    [("حظر مستخدم")],
    [("الغاء الحظر")],   
    [("المحظورين")],    
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Key282ard = ReplyKeyboardMarkup(
  [
    [("• استخرج جلسه •")],    
    [("• استخراج api •")],    
    [("• حذف حساب •")],    
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

Keal360rdyttd = ReplyKeyboardMarkup(
  [
    [("شغل"), ("فيد")],
    [("كمل"), ("وقف")],
    [("ايقاف"), ("تخطي")],
    [("رجوع")],
  ],
  resize_keyboard=True, one_time_keyboard=True, placeholder=f"{name}"
)

# ==========================================
# 5. دوال الحظر (Ban Logic)
# ==========================================
def add_CASER(bots, bot_username):
    if is_CASER(bots, bot_username):
        return
    if r: r.sadd(f"CASER{bot_username}", str(bots))

def is_CASER(bots, bot_username):
    try:
        a = get_CASER(bot_username)
        # تعديل لضمان التوافق مع أنواع البيانات
        if str(bots) in [str(x) for x in a] or bots in a:
            return True
        return False
    except:
        return False

def del_CASER(bots, bot_username):
    if r: r.srem(f"CASER{bot_username}", str(bots))

def get_CASER(bot_username):
    try:
        if not r: return []
        lst = []
        for a in r.smembers(f"CASER{bot_username}"):
            try: lst.append(eval(a))
            except: lst.append(a)
        return lst
    except:
        return []

async def johCASER(client, message):
    if not r: return False
    bot_username = client.me.username
    # التحقق من قائمة المحظورين
    if is_CASER([message.from_user.id], bot_username):
        return True
    return False

# ==========================================
# 6. دالة فحص الاشتراك (Join Check)
# ==========================================
async def johned(client, message):
    if message.from_user.id == caserid: return False
    try:
        user_status = await client.get_chat_member(ch, message.from_user.id)
        if user_status.status in [enums.ChatMemberStatus.BANNED, enums.ChatMemberStatus.LEFT]:
            raise UserNotParticipant
        return False
    except UserNotParticipant:
        return True # المستخدم غير مشترك
    except:
        return False

# ==========================================
# 7. أوامر الحظر (Handlers)
# ==========================================
@Client.on_message(filters.regex("حظر مستخدم") & filters.private, group=71513)
async def maadd_CASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    ask = await client.ask(message.chat.id, f"ارسل ايدي الشخص", timeout=300)
    try:
        channel = int(ask.text)
        oo = [channel]
        add_CASER(oo, bot_username)
        await client.send_message(message.chat.id, "تم الحظر بنجاح")
    except:
        await client.send_message(message.chat.id, "ايدي خطأ")
            
@Client.on_message(filters.command("المحظورين", "") & filters.private, group=71513089)
async def botzbjbbojCASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    o = 0
    text = "المحظورين\n"
    for x in get_CASER(bot_username):
        o += 1
        channel = x[0] if isinstance(x, list) else x
        text += f"{o}- {channel}\n"
    if o == 0:
        return await message.reply_text("لا يوجد محظورين")
    await message.reply_text(text)
  
@Client.on_message(filters.command(["فك الحظر","الغاء الحظر"], "") & filters.private, group=715138608)
async def deletehombie(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    try:
        bot = await client.ask(message.chat.id, "هات ايدي المستخدم", timeout=200)
        channel = int(bot.text)
        # مسح المستخدم
        del_CASER([channel], bot_username)
        await message.reply_text("تم الغاء حظر المستخدم")
    except:
        pass

# ==========================================
# 8. أوامر التفعيل والتعطيل
# ==========================================
@Client.on_message(filters.command(["تفعيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def for_5s(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
  try:
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
  except: wenru = casery
  
  if message.from_user.username in caes:
    try: 
     devess[bot_username] = wenru
     await message.reply_text(f"تم تفعيل الصلاحيات المدفوعة للبوت بنجاح، شكرا لك ✨♥")
    except:
     return await message.reply_text("تم التفعيل من قبل")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
     
@Client.on_message(filters.command(["تعطيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def disabl(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
    try:
        usr1 = await client.get_chat(OWNER_ID)
        wenru = usr1.username
    except: wenru = casery

    if message.from_user.username in caes:
        if devess.get(bot_username) == wenru:
            del devess[bot_username]
            await message.reply_text("تم تعطيل الصلاحيات المدفوعة للبوت وحذفها من التخزين بنجاح ✨♥")
        else:
            await message.reply_text("الصلاحيات غير مفعلة من قبل")
    else:
        await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")

# ==========================================
# 9. دالة صنع الصورة
# ==========================================
async def gen_ot(app, CASER, message, bot_id):
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_id = user_chat.photo.big_file_id
            downloaded_photo = await app.download_media(photo_id)
            youtube = Image.open(downloaded_photo)
            image1 = youtube.resize((1280, 720))
            image2 = image1.convert("RGBA")
            
            background = image2.filter(ImageFilter.BoxBlur(10))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.5)
            
            draw = ImageDraw.Draw(background)
            try:
                arial = ImageFont.truetype("font2.ttf", 80)
                caesa = ImageFont.truetype("font.ttf", 50)
            except:
                arial = ImageFont.load_default()
                caesa = ImageFont.load_default()

            box_size = (500, 500)
            box_position = (40, 100)
            box_image = Image.new("RGBA", box_size, (255, 255, 255, 0))
            box_draw = ImageDraw.Draw(box_image)
            box_draw.ellipse([(0, 0), box_size], outline="white", width=5)
            
            inner_image = Image.open(downloaded_photo)
            inner_image = inner_image.resize((480, 480))
            box_image.paste(inner_image, (10, 10))
            background.paste(box_image, box_position)
            
            draw.text((580, 220), f"USER: @{CASER}", (255, 255, 255), font=caesa)
            draw.text((580, 120), f"{suorce}", fill="white", stroke_width=2, stroke_fill="white", font=arial)
            draw.text((580, 290), f"ID: {bot_id}", (255, 255, 255), font=caesa)
            draw.text((580, 360), f"DeV: {casery}", (255, 255, 255), font=caesa)
            draw.text((580, 430), f"users: {len(get_user(bot_id))}", (255, 255, 255), font=caesa)
            draw.text((580, 500), f"groups: {len(get_groups(bot_id))}", (255, 255, 255), font=caesa)
            
            output_path = f"{CASER}_{message.from_user.id}.png"
            background.save(output_path)
            
            # تنظيف الصورة المحملة
            if os.path.exists(downloaded_photo):
                os.remove(downloaded_photo)
            return output_path
        else:
            return photosource 
    except Exception as e:
        print(f"Error gen_ot: {e}")
        return photosource 

# ==========================================
# 10. Start Handler (مصحح)
# ==========================================
@Client.on_message(filters.command(["start", "/start", "رجوع"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
   if await johCASER(client, message):
     return await message.reply_text("🚫 انت محظور من استخدام البوت.")
     
   if await johned(client, message):
     await message.reply_text(f"⚠️ **عذراً، يجب عليك الاشتراك في قناة البوت أولاً:**\n@{ch}")
     return
   
   bot_username = client.me.username
   bot_id = client.me.id
   
   OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
   try:
       usr1 = await client.get_chat(OWNER_ID)
       wenru = usr1.username
       namew = usr1.first_name
   except:
       wenru = casery
       namew = "المطور"

   button = [[InlineKeyboardButton(text="عـــربـــي 🇪🇬", callback_data=f"arbk"), InlineKeyboardButton(text="English 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data=f"english")],[InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")]]
   
   msg = await message.reply_text("⏳ جاري التحميل...")
   photo = await gen_ot(client, bot_username, message, bot_id)
   
   try:
       await msg.delete()
       await message.reply_photo(photo=photo, caption="👋 **أهلاً بك في البوت!**", reply_markup=InlineKeyboardMarkup(button))
       # حذف الصورة المولدة
       if photo != photosource and os.path.exists(photo):
           os.remove(photo)
   except:
       await message.reply_photo(photo=photosource, caption="", reply_markup=InlineKeyboardMarkup(button))

   # إظهار الكيبورد المناسب
   if message.from_user.id == caserid or message.from_user.username in caes:
       await message.reply_text("👇 **قائمة المطور** 👇", reply_markup=Keyboard)
   else:
       await message.reply_text("👇 **القائمة الرئيسية** 👇", reply_markup=Keyard)

   # تسجيل المستخدم الجديد
   if not is_user(message.from_user.id, bot_id):
     add_user(message.from_user.id, bot_id)
     text = '🙍 شخص جديد دخل الى البوت !\n\n'
     text += f'🎯 الأسم: {message.from_user.first_name}\n'
     text += f'♻️ الايدي: {message.from_user.id}\n\n'
     text += f'🌐 اصبح عدد المستخدمين: {len(get_user(bot_id))}'
     try:
         await client.send_message(int(OWNER_ID), text)
     except: pass

# ==========================================
# 11. إشعار التشغيل
# ==========================================
async def send_online_signal():
    await asyncio.sleep(10)
    try:
        # استخدام appp لو متوفر، أو client لو لا
        if 'appp' in globals() and appp:
            bot = appp
        else:
            return 
            
        bot_username = bot.me.username
        ubot = await get_userbot(bot_username) if 'get_userbot' in globals() else None
        OWNER_ID = await get_dev(bot_username) if 'get_dev' in globals() else caserid
        
        msg = f"""
✅ **تم تشغيل البوت بنجاح!**
🤖 **البوت:** @{bot_username}
🚀 **الحالة:** 100%
"""
        await bot.send_message(OWNER_ID, msg)
    except Exception as e:
        pass

try:
    loop = asyncio.get_event_loop()
    loop.create_task(send_online_signal())
except:
    pass
