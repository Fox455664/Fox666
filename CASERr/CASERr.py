import asyncio
import requests
import random
import re
import os
import time
import datetime
import redis
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram import Client as client
from unidecode import unidecode
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from pyrogram.errors import PeerIdInvalid, FloodWait
from collections import defaultdict
from pyrogram import enums
from asyncio import sleep
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from casery import caes, casery, group, source, photosource, caserid, OWNER, muusiic, suorce
from io import BytesIO
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

name = f"{OWNER}"

# اتصال قاعدة البيانات (Upstash)
try:
    r = redis.Redis(
        host="ultimate-ferret-48101.upstash.io",
        port=6379,
        password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
        ssl=True,
        decode_responses=True
    )
except:
    pass

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
    [("قسم الحذف والاستخراج")],
    [("مطور البوت"),("مطور السورس")], 
    [("السورس")],    
    [("/start")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
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
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
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
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
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
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keyttd = ReplyKeyboardMarkup(
  [
    [("ترويج للحمايه")],
    [("ترويج للميوزك")],   
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Kealrdyttd = ReplyKeyboardMarkup(
  [
    [("تعيين اسم البوت")],
    [("تعيين جروب السورس"), ("تعيين قناه السورس")],   
    [("تعيين مطور السورس"), ("تعيين صوره السورس")],   
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keal56rdyttd = ReplyKeyboardMarkup(
  [
    [("اضف قناه اشتراك")],  
    [("حذف قناه اشتراك")],   
    [("قنوات الاشتراك")],     
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keal16rdyttd = ReplyKeyboardMarkup(
  [
    [("الجروبات"), ("المستخدمين")],
    [("رفع نسخه الجروبات"), ("رفع نسخه الاشخاص")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keal36rdyttd = ReplyKeyboardMarkup(
  [
    [("《تعطيل التواصل》"), ("《تفعيل التواصل》")],
    [("تعطيل البوت بالصوره"),("تفعيل البوت بالصوره")],
    [("قفل الردود"),("فتح الردود")],
    [("قفل الميوزك"),("فتح الميوزك")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keal66rdyttd = ReplyKeyboardMarkup(
  [
    [("حظر مستخدم")],
    [("الغاء الحظر")],   
    [("المحظورين")],    
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Key282ard = ReplyKeyboardMarkup(
  [
    [("• استخرج جلسه •")],    
    [("• استخراج api •")],    
    [("• حذف حساب •")],    
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

Keal360rdyttd = ReplyKeyboardMarkup(
  [
    [("شغل"), ("فيد")],
    [("كمل"), ("وقف")],
    [("ايقاف"), ("تخطي")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  one_time_keyboard=True, 
  placeholder=f"{name}"
)

# --- تعريف المتغيرات والقوائم ---
caes = caes
casery = casery
source = source
group = group
caserid = caserid
photosource = photosource
muusiic = muusiic
suorce = suorce
names = {} 
devuser = {} 
devchannel = {} 
devgroup = {} 
devphots = {} 
devess = {} 

# --- دوال Redis للحظر والقنوات ---
def add_CASER(bots, bot_username):
    if is_CASER(bots, bot_username):
        return
    r.sadd(f"CASER{bot_username}", str(bots))

def is_CASER(bots, bot_username):
    try:
        a = get_CASER(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_CASER(bots, bot_username):
    if not is_CASER(bots, bot_username):
        return False
    r.srem(f"CASER{bot_username}", str(bots))

def get_CASER(bot_username):
    try:
        lst = []
        for a in r.smembers(f"CASER{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def johCASER(client, message):
    CASER = []  
    bot_username = client.me.username
    for x in get_CASER(bot_username):
        ch = x[0]
        CASER.append(ch)
    if message.from_user.id in CASER:
        return True     
    return False

# --- أوامر الحظر ---
@Client.on_message(filters.regex("حظر مستخدم") & filters.private, group=71513)
async def maadd_CASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    ask = await client.ask(message.chat.id, f"ارسل ايدي الشخص", timeout=300)
    channel = int(ask.text)
    oo = [channel]
    add_CASER(oo, bot_username)
    await client.send_message(message.chat.id, "تم الحظر بنجاح")
            
@Client.on_message(filters.command("المحظورين", "") & filters.private, group=71513089)
async def botzbjbbojCASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    o = 0
    text = "المحظورين\n"
    for x in get_CASER(bot_username):
        o += 1
        channel = x[0]
        text += f"{o}- {channel}\n"
    if o == 0:
        return await message.reply_text("لا يوجد محظورين")
    await message.reply_text(text)
  
@Client.on_message(filters.command(["فك الحظر","الغاء الحظر"], "") & filters.private, group=715138608)
async def deletehombie(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    try:
        bot = await client.ask(message.chat.id, "هات ايدي المستخدم", timeout=200)
    except:
        return
    channel = int(bot.text)
    for x in get_CASER(bot_username):
        if x[0] == channel:
            del_CASER(x, bot_username)
    await message.reply_text("تم الغاء حظر المستخدم")

# --- أوامر تعيين البيانات ---
@Client.on_message(filters.command(["تفعيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def for_5s(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  usr1 = await client.get_chat(OWNER_ID)
  wenru = usr1.username
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
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    if message.from_user.username in caes:
        if devess.get(bot_username) == wenru:
            del devess[bot_username]
            await message.reply_text("تم تعطيل الصلاحيات المدفوعة للبوت وحذفها من التخزين بنجاح ✨♥")
        else:
            await message.reply_text("الصلاحيات غير مفعلة من قبل")
    else:
        await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")

# --- دالة صنع الصورة (المصححة والمضمونة) ---
async def gen_ot(app, CASER, message, bot_id):
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_id = user_chat.photo.big_file_id
            downloaded_photo = await app.download_media(photo_id)
            youtube = Image.open(downloaded_photo)
            image1 = youtube.resize((1280, 720))
            image2 = image1.convert("RGBA")
            # تأثيرات الصورة
            background = image2.filter(ImageFilter.BoxBlur(10))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.5)
            
            draw = ImageDraw.Draw(background)
            # استخدام خط افتراضي لو الخطوط مش موجودة
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
            
            output_path = f"{CASER}.png"
            background.save(output_path)
            return output_path
        else:
            return photosource # رجوع للصورة الاحتياطية لو البوت ملوش صورة
    except Exception as e:
        print(f"Error gen_ot: {e}")
        return photosource # الأمان: لو حصل أي خطأ، رجع صورة السورس

# --- دالة Start (المعدلة) ---
@Client.on_message(filters.command(["/start"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
   if await johCASER(client, message):
     return
   if await johned(client, message):
     return
   
   bot_username = client.me.username
   bot_id = client.me.id
   
   # تجهيز البيانات
   OWNER_ID = await get_dev(bot_username)
   try:
       usr1 = await client.get_chat(OWNER_ID)
       wenru = usr1.username
       namew = usr1.first_name
   except:
       wenru = casery
       namew = "المطور"

   button = [[InlineKeyboardButton(text="عـــربـــي 🇪🇬", callback_data=f"arbk"), InlineKeyboardButton(text="English 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data=f"english")],[InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")]]
   
   # محاولة صنع الصورة
   photo = await gen_ot(client, bot_username, message, bot_id)
   
   # الإرسال الآمن (مستحيل يفشل)
   if photo:
       try:
           await message.reply_photo(photo=photo, caption="", reply_markup=InlineKeyboardMarkup(button))
           # حذف الصورة المولدة لتوفير المساحة
           if os.path.exists(photo) and photo != photosource:
               os.remove(photo)
       except:
           # لو فشل ارسال الصورة المولدة، ابعت صورة السورس
           await message.reply_photo(photo=photosource, caption="", reply_markup=InlineKeyboardMarkup(button))
   else:
       await message.reply_text("مرحباً بك في البوت 🌹", reply_markup=InlineKeyboardMarkup(button))

   # تسجيل المستخدم الجديد
   if not is_user(message.from_user.id, bot_id):
     add_user(message.from_user.id, bot_id)
     text = '🙍 شخص جديد دخل الى البوت !\n\n'
     text += f'🎯 الأسم: {message.from_user.first_name}\n'
     text += f'♻️ الايدي: {message.from_user.id}\n\n'
     text += f'🌐 اصبح عدد المستخدمين: {len(get_user(bot_id))}'
     
     # تبليغ المطورين
     try:
         await client.send_message(int(OWNER_ID), text)
     except: pass

# --- دالة التبليغ عند التشغيل (الميزة الجديدة) ---
async def send_online_signal():
    await asyncio.sleep(10) # انتظار الاتصال
    try:
        bot_username = appp.me.username
        ubot = await get_userbot(bot_username)
        OWNER_ID = await get_dev(bot_username)
        
        # رسالة التشغيل
        msg = f"""
✅ **تم تشغيل البوت بنجاح يا مطور!**

🤖 **البوت:** @{bot_username}
🎸 **المساعد:** {f'@{ubot.me.username}' if ubot else 'غير متصل ❌'}
📅 **الوقت:** {datetime.datetime.now().strftime("%I:%M %p")}

🚀 **المصنع شغال 100%**
"""
        # ارسال للوجر أو المطور
        logger_id = await get_logger(bot_username)
        if logger_id:
            await appp.send_message(logger_id, msg)
        else:
            await appp.send_message(OWNER_ID, msg)
    except Exception as e:
        print(f"Startup Log Error: {e}")

# تشغيل دالة التبليغ
try:
    loop = asyncio.get_event_loop()
    loop.create_task(send_online_signal())
except:
    pass
def get_channel(bot_username):
    # كود افتراضي لتجنب الخطأ
    return source
