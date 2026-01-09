import asyncio
import os
import redis
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from pyrogram import filters, Client
from pyrogram.errors import UserNotParticipant
from pyrogram import enums

# استيراد الإعدادات
try:
    from config import user, dev, call, logger, logger_mode, botname, appp
    from CASERr.daty import get_call, get_userbot, get_dev, get_logger
except ImportError:
    pass

# ================= بيانات السورس =================
caes = ["f_o_x_351", "zozooryy", "cyv0we"]
casery = "f_o_x_351"
caserid = 7669264153
OWNER_NAME = "النسور"
OWNER = caserid
muusiic = "SOURCE Titanx"
suorce = "SOURCE Titanx"
source = "https://t.me/fox68899"
ch = "fox68899"
group = "https://t.me/fox68899"
photosource = "https://envs.sh/ws4.webp"

# ================= متغيرات الربط =================
devchannel = source
devgroup = group
devuser = casery
name = f"{OWNER_NAME}"
devphots = photosource

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

# ================= دوال المساعدة =================
def add_user(user_id, bot_id):
    if r: r.sadd(f"USERS{bot_id}", user_id)

def is_user(user_id, bot_id):
    if r: return r.sismember(f"USERS{bot_id}", user_id)
    return False

# دالة الحظر
async def johCASER(client, message):
    if not r: return False
    try:
        bot_username = client.me.username
        res = r.smembers(f"CASER{bot_username}")
        for x in res:
            if str(message.from_user.id) in x: return True
    except: pass
    return False

# دالة الاشتراك الإجباري
async def johned(client, message):
    if message.from_user.id == caserid: return False # استثناء المطور
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
        except: pass
        return True
    except: return False

# دالة الصورة
async def gen_ot(app, bot_username, bot_id):
    output_path = f"start_{bot_id}.png"
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_path = await app.download_media(user_chat.photo.big_file_id)
            img = Image.open(photo_path).resize((1280, 720)).convert("RGBA")
            bg = img.filter(ImageFilter.BoxBlur(10))
            bg = ImageEnhance.Brightness(bg).enhance(0.5)
            draw = ImageDraw.Draw(bg)
            try:
                font_lg = ImageFont.truetype("font2.ttf", 80)
                font_sm = ImageFont.truetype("font.ttf", 45)
            except:
                font_lg = font_sm = ImageFont.load_default()

            draw.text((580, 120), f"{suorce}", fill="white", font=font_lg)
            draw.text((580, 230), f"USER: @{bot_username}", fill="white", font=font_sm)
            draw.text((580, 300), f"ID: {bot_id}", fill="white", font=font_sm)
            draw.text((580, 370), f"DEV: @{casery}", fill="white", font=font_sm)
            bg.save(output_path)
            if os.path.exists(photo_path): os.remove(photo_path)
            return output_path
    except: pass
    return photosource

# ================= أمر Start =================
# ✅ التعديل هنا: group=0 وفلتر صحيح
@Client.on_message(filters.command(["start", "رجوع"]) & filters.private, group=0)
async def start_handler(client, message):
    if await johCASER(client, message): return
    if await johned(client, message): return

    bot_username = client.me.username
    bot_id = client.me.id
    
    # حفظ المستخدم
    if not is_user(message.from_user.id, bot_id):
        add_user(message.from_user.id, bot_id)
        try:
            await client.send_message(caserid, f"🙍 **مستخدم جديد:** {message.from_user.mention}")
        except: pass

    # الأزرار
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"), InlineKeyboardButton("English 🏴", callback_data="english")],
        [InlineKeyboardButton(OWNER_NAME, url=f"https://t.me/{casery}")]
    ])

    # إرسال الصورة
    photo = await gen_ot(client, bot_username, bot_id)
    try:
        await message.reply_photo(
            photo=photo,
            caption=f"╮⦿ اهـلا بڪ عزيـزي {message.from_user.mention}\n│⎋ اليـكـ كيبورد الاعضاء للاستمتاع",
            reply_markup=buttons
        )
        await message.reply_text("👇 **القائمة الرئيسية** 👇", reply_markup=Keyard)
        
        if photo != photosource and os.path.exists(photo):
            os.remove(photo)
    except:
        await message.reply_text("أهلاً بك!", reply_markup=Keyard)
