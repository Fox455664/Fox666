import os
import pyrogram
import redis
import re
import asyncio
import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

# استيراد البوت والمتغيرات
from bot import bot as app, lolo, DEVS, DEVSs
from CASERr.calls import Call
from CASERr.hossam import mutegdv2d
from CASERr.CASERr import photo_responses
from CASERr.azan import azan, azkar_chatt, nday_catt
from config import user as usr, dev, call, logger, appp
from casery import casery, group, source, photosource, caserid, ch, OWNER

r = redis.Redis(
    host="ultimate-ferret-48101.upstash.io",
    port=6379,
    password="AbvlAAIncDEzYTgwNjBhYTRjNzI0N2NiODZjZGEwY2ZmMmIxOGI2YnAxNDgxMDE",
    ssl=True,  # مهم جدا عشان الرابط بتاعك فيه --tls
    decode_responses=True
)

API_ID = int(os.getenv("API_ID", "25655555"))
API_HASH = os.getenv("API_HASH", "57b330d11c2e758e6e3514ffc586bad5")
Bots = []
Musi = []
CASER = [] 
off = True

@app.on_message(filters.private)
async def me(client, message):
   # تأكد من أن الرسالة ليست من البوت نفسه
   if message.from_user.id == client.me.id:
       return
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
             try:
                await lolo.send_message(chat_member_updated.chat.id, message_text)
             except Exception:
                pass

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
    try:
        photo = await client.download_media(user.photo.big_file_id)
        await message.reply_photo(photo=photo, caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=user_id)]]))
        os.remove(photo)
    except:
        await message.reply_text(f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=user_id)]]))

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


# ... (دوال إدارة البوتات Redis Helper Functions) ...

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

# باقي الدوال المساعدة في الملف الأصلي (get_users, get_groups, الخ) تبقى كما هي



