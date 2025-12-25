from pyrogram import filters, Client
import asyncio
from typing import Optional
from pyrogram import Client, enums
from random import randint
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import AudioPiped
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from pyrogram.raw.base import GroupCallParticipant
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from CASERr.daty import get_call, get_userbot

@Client.on_message(filters.command(["مين في الكول","م ف ك","مين ف الكول"], ""))
async def ghsdh_user(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    
    # 🟢 الحماية: لو المساعد مش موجود
    if hoss is None:
        return await message.reply("⚠️ **عذراً، الحساب المساعد غير متصل حالياً!**\nتأكد من تشغيله في المصنع.")

    hh = await message.reply("استنا اطلع اشوف مين في الكول✨♥") 
    try:
        # محاولة انضمام وهمية لتحديث القائمة (بدون كراش)
        try:
            await hoss.join_group_call(message.chat.id, AudioPiped("./Hossam/CASER.mp3"), stream_type=StreamType().pulse_stream)
        except:
            pass
            
        text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
        participants = await hoss.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            mut = "يتحدث 🗣" if info.muted == False else "ساكت 🔕"
            try:
                user = await client.get_users(participant.user_id)
                name_u = user.mention
            except:
                name_u = "مستخدم"
            k +=1
            text +=f"{k}➤{name_u}➤{mut}\n"
        
        await hh.edit_text(f"{text}")
        try:
            await hoss.leave_group_call(message.chat.id)
        except: pass

    except Exception as e:
        await message.reply(f"حبيبي الكول مش مفتوح اصلااا\n😜")

# --- دالة جلب المكالمة (الآمنة) ---
async def get_group_call(client: Client, message: Message, err_message: str = "") -> Optional[InputGroupCall]:
    if not client:
        return None
        
    try:
        chat_peer = await client.resolve_peer(message.chat.id)
        if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
            if isinstance(chat_peer, InputPeerChannel):
                full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
            elif isinstance(chat_peer, InputPeerChat):
                full_chat = (await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
            
            if full_chat is not None:
                return full_chat.call
    except:
        pass
    
    if err_message:
        await message.reply_text(f"{err_message}")
    return None

@Client.on_message(filters.command(["فتح الكول","ف ك","ف الكول"], ""))
async def vc(c, message):
    bot_username = c.me.username
    user = await get_userbot(bot_username)
    
    if not user:
        return await message.reply_text("⚠️ **الحساب المساعد غير متصل!**")

    hh = await message.reply_text("جاري فتح الكول")   
    
    group_call = await get_group_call(user, message, err_message="")
    if group_call:
        await hh.edit_text("الكول مفتوح اصلا يليفه")
        return        
    try:
        await user.invoke(CreateGroupCall(peer=(await user.resolve_peer(message.chat.id)), random_id=randint(10000, 999999999)))
        await hh.edit_text("تم فتح الكول بنجاح.")           
    except Exception as e:
        await hh.edit_text(f"قم برفع الحساب المساعد مشرف في الجروب\nأو تأكد من صلاحياته.")
  
@Client.on_message(filters.command(["قفل الكول","ق الكول","ق ك"], ""))
async def end_vc(c, message):
    bot_username = c.me.username
    user = await get_userbot(bot_username)

    if not user:
        return await message.reply_text("⚠️ **الحساب المساعد غير متصل!**")

    hh = await message.reply_text("جاري قفل الكول")   
    
    group_call = await get_group_call(user, message, err_message="الكول مقفول اصلا يليفه")
    if not group_call:
        return        
    try:
        await user.invoke(DiscardGroupCall(call=group_call))
        await hh.edit_text("تم قفل الكول بنجاح.")           
    except Exception as e:
        await hh.edit_text(f"حدث خطأ أثناء القفل.")

@Client.on_message(filters.command(["استك"], ""))
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply or not reply.sticker:
        return await message.reply("**رد علي الملصق لجلب الكود 🤗⚡**")
    await message.reply_text(f"<b>تفضل عزيزي المطور هذا هو id الاستيكر الحالي </b> \n`{reply.sticker.file_id}`")
     
@Client.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma, _ = divmod(da, 60)
    ho, _ = divmod(ma, 60)
    
    msg_text = f"**- تم انهاء مكالمة الفيديو مدتها {da} ثواني**"
    if 60 < da < 3600:
        msg_text = f"**- تم انهاء مكالمة الفيديو مدتها {ma} دقيقه**"
    elif da >= 3600:
        msg_text = f"**- تم انهاء مكالمة الفيديو مدتها {ho} ساعة**"
        
    await message.reply(msg_text)
