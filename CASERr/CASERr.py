import asyncio
import requests
import random
import re
import os
import time
import datetime
import redis
from pyrogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup,
    CallbackQuery, ChatPrivileges, ReplyKeyboardMarkup
)
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

# ================= Redis =================
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

# ================= Keyboards =================
Keyard = ReplyKeyboardMarkup(
    [
        [("• زخرفه •")],
        [("• صراحه •"), ("• تويت •")],
        [("• انصحني •"), ("• لو خيروك •")],
        [("• حروف •"), ("• امثله •")],
        [("• نكته •"), ("• احكام •")],
        [("• قران •"), ("• ازكار •")],
        [("• صور •")],
        [("• صور شباب •"), ("• صور بنات •")],
        [("• انمي •"), ("• استوري •")],
        [("• اغاني •")],
        [("• ممثلين •"), ("• مغنين •")],
        [("• مشاهير •"), ("• لاعبين •")],
        [("• اعلام •"), ("• افلام •")],
        [("• لغز •"), ("• مختلف •")],
        [("قسم الحذف والاستخراج")],
        [("مطور البوت"), ("مطور السورس")],
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
        [("تفعيل الصلاحيات المدفوعه"), ("تعطيل الصلاحيات المدفوعه")],
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

# ================= Variables =================
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

# ================= Users =================
def add_user(user_id, bot_id):
    try:
        r.sadd(f"USERS{bot_id}", user_id)
    except:
        pass

def is_user(user_id, bot_id):
    try:
        return r.sismember(f"USERS{bot_id}", user_id)
    except:
        return False

def get_user(bot_id):
    try:
        return list(r.smembers(f"USERS{bot_id}"))
    except:
        return []

def get_groups(bot_id):
    try:
        return list(r.smembers(f"GROUPS{bot_id}"))
    except:
        return []

# ================= Subscription =================
async def johned(client, message):
    try:
        bot_username = client.me.username
        channel = devchannel.get(bot_username)
        if not channel:
            return False

        user = await client.get_chat_member(channel, message.from_user.id)
        if user.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            return False

        await message.reply_text(
            "🚫 لازم تشترك في قناة البوت",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📢 اشترك", url=f"https://t.me/{channel.replace('@','')}")]]
            )
        )
        return True
    except:
        return False

# ================= Bans =================
def add_CASER(bots, bot_username):
    try:
        r.sadd(f"CASER{bot_username}", str(bots))
    except:
        pass

def get_CASER(bot_username):
    try:
        return [eval(x) for x in r.smembers(f"CASER{bot_username}")]
    except:
        return []

async def johCASER(client, message):
    CASER = []
    bot_username = client.me.username
    for x in get_CASER(bot_username):
        CASER.append(x[0])
    return message.from_user.id in CASER

# ================= Image =================
async def gen_ot(app, CASER, message, bot_id):
    try:
        user_chat = await app.get_chat(bot_id)
        if not user_chat.photo:
            return photosource

        photo_id = user_chat.photo.big_file_id
        downloaded_photo = await app.download_media(photo_id)
        image = Image.open(downloaded_photo).resize((1280, 720)).convert("RGBA")

        bg = image.filter(ImageFilter.BoxBlur(10))
        bg = ImageEnhance.Brightness(bg).enhance(0.5)

        draw = ImageDraw.Draw(bg)
        try:
            arial = ImageFont.truetype("font2.ttf", 80)
            caesa = ImageFont.truetype("font.ttf", 50)
        except:
            arial = caesa = ImageFont.load_default()

        draw.text((580, 120), suorce, fill="white", font=arial)
        draw.text((580, 220), f"USER: @{CASER}", fill="white", font=caesa)
        draw.text((580, 290), f"ID: {bot_id}", fill="white", font=caesa)
        draw.text((580, 360), f"DeV: {casery}", fill="white", font=caesa)
        draw.text((580, 430), f"users: {len(get_user(bot_id))}", fill="white", font=caesa)
        draw.text((580, 500), f"groups: {len(get_groups(bot_id))}", fill="white", font=caesa)

        out = f"{CASER}.png"
        bg.save(out)
        return out
    except:
        return photosource

# ================= START =================
@Client.on_message(filters.command(["/start"], "") & filters.private, group=1267686)
async def for_us65ers(client, message):
    if await johCASER(client, message):
        return
    if await johned(client, message):
        return

    bot_username = client.me.username
    bot_id = client.me.id

    OWNER_ID = await get_dev(bot_username)
    try:
        usr = await client.get_chat(OWNER_ID)
        wenru = usr.username
        namew = usr.first_name
    except:
        wenru = casery
        namew = "المطور"

    buttons = [
        [
            InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"),
            InlineKeyboardButton("English 🏴", callback_data="english")
        ],
        [InlineKeyboardButton(namew, url=f"https://t.me/{wenru}")]
    ]

    photo = await gen_ot(client, bot_username, message, bot_id)

    try:
        await message.reply_photo(photo, reply_markup=InlineKeyboardMarkup(buttons))
        if os.path.exists(photo) and photo != photosource:
            os.remove(photo)
    except:
        await message.reply_text("مرحباً بك 🌹", reply_markup=InlineKeyboardMarkup(buttons))

    if not is_user(message.from_user.id, bot_id):
        add_user(message.from_user.id, bot_id)

# ================= Startup Log =================
# استيراد البوت الأساسي من ملف bot (تأكد من اسم الملف والكائن)
from bot import bot as main_bot

async def send_online_signal():
    # ننتظر قليلاً للتأكد من اتصال البوت بالخادم
    await asyncio.sleep(15)
    try:
        # الحصول على معلومات البوت الأساسي
        me = await main_bot.get_me()
        bot_username = me.username
        
        # جلب أيدي المطور
        OWNER_ID = await get_dev(bot_username)
        
        msg = f"""
✅ **تم تشغيل البوت بنجاح**

🤖 **يوزر البوت:** @{bot_username}
🆔 **أيدي المطور:** `{OWNER_ID}`
🕒 **الوقت:** {datetime.now().strftime('%I:%M %p')}

🚀 السورس يعمل الآن بالكامل!
"""
        # الإرسال باستخدام main_bot وليس appp
        await main_bot.send_message(OWNER_ID, msg)
        print(f"✅ Startup message sent to {OWNER_ID}")
        
    except Exception as e:
        # طباعة الخطأ لمعرفة السبب في حال فشل الإرسال
        print(f"❌ Error in send_online_signal: {e}")

# تشغيل المهمة في الخلفية
asyncio.create_task(send_online_signal())

