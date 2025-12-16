from pyrogram import filters, Client
import asyncio
from typing import Optional
from pyrogram import Client, enums
from random import randint
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.stream import AudioPiped, AudioVideoPiped
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from pyrogram.raw.base import GroupCallParticipant
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallParticipant
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat, InputUserSelf
from pyrogram.types import Message
from datetime import datetime
import requests
import pytz
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes

@Client.on_message(filters.command(["مين في الكول","م ف ك","مين ف الكول","مين ف كول "], ""))
async def ghsdh_user(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)    
    hh = await message.reply("استنا اطلع اشوف مين في الكول✨♥") 
    try:
     await hoss.join_group_call(message.chat.id, AudioPiped("./Hossam/CASER.mp3"), stream_type=StreamType().pulse_stream)
     text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
     participants = await hoss.get_participants(message.chat.id)
     k = 0
     for participant in participants:
      info = participant
      if info.muted == False:
       mut="يتحدث 🗣"
      else:
       mut="ساكت 🔕"
      user = await client.get_users(participant.user_id)
      k +=1
      text +=f"{k}➤{user.mention}➤{mut}\n"
     await hh.edit_text(f"{text}")
     await hoss.leave_group_call(message.chat.id)
    except Exception:
     # NoActiveGroupCall or others
     await message.reply(f"حبيبي الكول مش مفتوح اصلااا\n😜")
      
async def get_group_call(
    client: Client, message: Message, err_message: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply_text(f"{err_message}")
    return False

@Client.on_message(filters.command(["فتح الكول","ف ك","ف الكول"], ""))
async def vc(c, message):
    bot_username = c.me.username
    user = await get_userbot(bot_username)
    hh = await message.reply_text("جاري فتح الكول")   
    if (group_call := await get_group_call(user, message, err_message="الكول مفتوح")):
     await message.reply_text("الكول مفتوح اصلا يليفه")
     return        
    try:
     await user.invoke(CreateGroupCall(peer=(await user.resolve_peer(message.chat.id)), random_id=randint(10000, 999999999)))
     await hh.edit_text("تم فتح الكول بنجاح.")           
    except Exception as e:
     await hh.edit_text(f"قم برفع الحساب المساعد مشرف في الجروب")
  
@Client.on_message(filters.command(["قفل الكول","ق الكول","ق ك"], ""))
async def end_vc(c, message):
    bot_username = c.me.username
    user = await get_userbot(bot_username)
    hh = await message.reply_text("جاري قفل الكول")   
    if not (group_call := await get_group_call(user, message, err_message="الكول مقفول")):
     await hh.edit_text("الكول مقفول اصلا يليفه")
     return        
    try:
     await user.invoke(DiscardGroupCall(call=group_call))
     await hh.edit_text("تم قفل الكول بنجاح.")           
    except Exception as e:
     await hh.edit_text(f"قم برفع الحساب المساعد مشرف في الجروب")

@Client.on_message(filters.command(["استك"], ""))
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("**رد علي الملصق لجلب الكود 🤗⚡**")
    if not reply.sticker:
        return await message.reply("**رد علي الملصق لجلب الكود 🤗⚡**")
    await message.reply_text(f"<b>تفضل عزيزي المطور هذا هو id الاستيكر الحالي </b> \n`{reply.sticker.file_id}`")
     
@Client.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {da} ثواني**")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقه**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقتين**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعه**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعتين**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يوم**")
        elif 2 <= day[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يومين**")
        elif 3 <= day[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {day[0]} ايام**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {day[0]} يوم**")
