# --- START OF FILE CASER/CASER.py ---

import os
import pyrogram
import redis
import re
import asyncio
import json
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
    UserNotParticipant,
    FloodWait
)
from pyromod import listen
from bot import bot as app, DEVS, DEVSs, lolo # استيراد الـ app من ملف البوت الرئيسي
from CASERr.play import Call
from CASERr.hossam import mutegdv2d
from CASERr.CASERr import photo_responses
from CASERr.azan import azan, azkar, azkar_chatt, nday_catt
from config import user as usr, dev, call, logger, appp
from casery import caes, casery, group, source, photosource, caserid, ch, OWNER

r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)

API_ID = int(os.getenv("API_ID", "8186557"))
API_HASH = os.getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
Bots = []
Musi = []
CASER = [] 
off = True

@app.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
     return await message.reply_text(f"الصانع معطل تواصل مع المطور السورس {OWNER} \n  @{casery}")
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except UserNotParticipant:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
   message.continue_propagation()

welcome_enabled = True

@Client.on_chat_member_updated()
async def welcome(client, chat_member_updated):
     if not welcome_enabled:
         return
     if chat_member_updated.new_chat_member and chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
         kicked_by = chat_member_updated.new_chat_member.restricted_by
         user = chat_member_updated.new_chat_member.user
         if kicked_by and kicked_by.is_self:
             pass
         else:
             if kicked_by:
                 message_text = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                 try:
                     await lolo.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                 except Exception:
                     message_text += f"\n\nعذرًا، لم استطع حظر الإداري."
             else:
                 message_text = f"• المستخدم {user.mention} تم طرده من الدردشة."
             await lolo.send_message(chat_member_updated.chat.id, message_text)

@app.on_message(filters.command(["《السورس》"], ""))
async def alivehi(client: Client, message):
    if message.from_user.username in CASER:
        return
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس ⚡", url=f"{source}")]])
    await message.reply_photo(photo=photosource, caption="", reply_markup=keyboard)
    
@app.on_message(filters.command(["《مطور السورس》"], ""))
async def caesar(client: Client, message):
    if message.from_user.username in CASER:
        return
    user = await client.get_chat(chat_id=casery)
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = await client.download_media(user.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=user_id)]]))
    os.remove(photo)

@app.on_message(filters.command(["《صنع بوت》"], ""))
async def cae5465sar(client: Client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        if message.from_user.username in CASER:
            return        
        for x in get_Bots():
            if x.get('owner_id') == message.from_user.id:
                return await message.reply_text("لقد قمت بصنع بوت من قبل.")
        if len(get_Bots()) >= 100:
            return await message.reply_text("الصانع مكتمل يحبيبي 😂♥")
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("لدي جلسة", callback_data="session_ready")]])
    h = await message.reply_text("اهلا بك في صانع بوتات الميوزك ⚡🎵\nهل لديك جلسه حساب مساعد؟\nاختر بالازرار بالاسفل", reply_markup=keyboard)
    await asyncio.sleep(120)
    try:
        await h.delete()
    except:
        pass

@app.on_callback_query(filters.regex(pattern=r"^(session_ready)$"))
async def admin_risghts(client: Client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    try:
        session_msg = await client.ask(chat_id, "حسنًا، أرسل الجلسة الآن (String Session) المستخرجة من @StringSessionGen_Bot أو أي بوت آخر.", timeout=300)
        SESSION = session_msg.text.strip()
    except asyncio.TimeoutError:
        return await client.send_message(chat_id, "انتهى الوقت، حاول مرة أخرى.")

    try:
        token_msg = await client.ask(chat_id, "أرسل توكن البوت الآن. إذا لم يكن لديك توكن، استخرجه من @BotFather", timeout=300)
        TOKEN = token_msg.text.strip()
    except asyncio.TimeoutError:
        return await client.send_message(chat_id, "انتهى الوقت، حاول مرة أخرى.")

    Dev = CallbackQuery.from_user.id
    if CallbackQuery.from_user.username in DEVS:
        try:
            ahjusk = await client.ask(chat_id, "أرسل آيدي المطور", timeout=300)
            Dev = int(ahjusk.text)
        except (ValueError, asyncio.TimeoutError):
            await client.send_message(chat_id, "آيدي غير صالح أو انتهى الوقت. سيتم تعيينك كمالك.")
            Dev = CallbackQuery.from_user.id
    
    bot_client = Client("temp_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
    user_client = Client("temp_user", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)
    
    try:
        await bot_client.start()
        bot_info = await bot_client.get_me()
        bot_username = bot_info.username
        await bot_client.stop()
    except Exception as e:
        return await CallbackQuery.message.reply_text(f"**التوكن غير صالح 🚦**\n`{e}`")

    try:
        await user_client.start()
        await user_client.stop()
    except Exception as e:
        return await CallbackQuery.message.reply_text(f"**كود الجلسة غير صالح ⚠️**\n`{e}`")

    if is_Bots(bot_username):
        return await CallbackQuery.message.reply_text("لقد قمت بصنع هذا البوت من قبل.")
    
    bot_data = {
        'bot_username': bot_username,
        'owner_id': Dev,
        'bot_token': TOKEN,
        'session_string': SESSION,
        'creator_id': CallbackQuery.from_user.id
    }
    add_Bots(bot_data)

    await CallbackQuery.message.reply_text(
        f"✨ تم تنصيب بوت بنجاح\n"
        f"يوزر البوت: @{bot_username}\n"
        f"بواسطة: {CallbackQuery.from_user.mention}\n"
        f"توكن البوت: `{TOKEN}`\n"
        f"جلسة الحساب: `{SESSION}`"
    )
    await client.send_message(
        chat_id=caserid,
        text=f"✨ **بوت جديد تم صنعه** ✨\n\n"
             f"🤖 **البوت:** @{bot_username}\n"
             f"👑 **المالك:** ID `{Dev}`\n"
             f"🔧 **الصانع:** {CallbackQuery.from_user.mention}\n"
    )
    # This function is not defined, you might need to implement it.
    # await start_bot(client, CallbackQuery.message)


def add_Bots(bot_data):
    bot_username = bot_data.get('bot_username')
    if not bot_username or is_Bots(bot_username):
        return
    r.hset(f"maker:{caserid}:bots", bot_username, json.dumps(bot_data))

def is_Bots(bot_username):
    return r.hexists(f"maker:{caserid}:bots", bot_username)

def del_Bots(bot_username):
    if not is_Bots(bot_username):
        return False
    r.hdel(f"maker:{caserid}:bots", bot_username)
    return True

def get_Bots():
    try:
        bots_data = r.hgetall(f"maker:{caserid}:bots")
        return [json.loads(data) for data in bots_data.values()]
    except Exception as e:
        print(f"Error getting bots from Redis: {e}")
        return []

def get_Bots_backup():
    bots = get_Bots()
    text = '\n'.join([json.dumps(bot) for bot in bots])
    filename = 'Bots.txt'
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(text)
    return filename

def get_users(bot_id):
    try:
        user_ids = r.smembers(f"botusers{bot_id}")
        return [int(uid) for uid in user_ids]
    except:
        return []

def get_groups(bot_id):
    try:
        group_ids = r.smembers(f"botgroups{bot_id}")
        return [int(gid) for gid in group_ids]
    except:
        return []