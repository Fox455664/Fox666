from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
import time 
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
import asyncio
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from pyrogram import Client
from youtubesearchpython import SearchVideos
from CASERr.CASERr import get_channel, devchannel, source, caes, devgroup, devuser, group, casery, johned
from io import BytesIO
import aiofiles
import wget
from pyrogram.types import *
import os, json, requests

yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
    
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل"], "") & filters.private, group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل صوت ⚡", callback_data=f"hidhkdhj"),InlineKeyboardButton("تحميل فديو ⚡", callback_data=f"voic5854e1")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]])
    chat_idd = message.chat.id
    await message.reply_text(f"اختر الان بالاسفل ماذا تريد تحميله ✨♥", reply_markup=keybord)
    
@Client.on_callback_query(filters.regex("voic5854e1"))
async def h24dgfgbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    name = await client.ask(CallbackQuery.message.chat.id, text="ارسل الان ما تريد تحميله ✨♥", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
        return await CallbackQuery.message.reply_text("لا يمكن تنزيل هذا")  
    else:
        print("احم")
    h = await CallbackQuery.message.reply_text(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "username": "oauth2",
        "password": "",
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"{e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await h.delete()
    try:
        await client.send_video(CallbackQuery.message.chat.id, video=video_file, duration=int(ytdl_data["duration"]), file_name=str(ytdl_data["title"]), thumb=sedlyf, supports_streaming=True, caption=capy)
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f"\n{e}")

@Client.on_callback_query(filters.regex("hidhkdhj"))
async def h24dg54hfbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    name = await client.ask(CallbackQuery.message.chat.id, text="**ارسل الان ما تريد تحميله ✨♥**", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
      return await CallbackQuery.message.reply_text("**لا يمكن تنزيل هذا**")  
    else:      
     print("احم")    
    h = await CallbackQuery.message.reply_text(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {'format': 'bestaudio[ext=m4a]', 'keepvideo': False, 'prefer_ffmpeg': False, 'geo_bypass': True, 'outtmpl': '%(title)s.%(ext)s', 'quite': True, "username": "oauth2", "password" : ""}
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"   : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await h.delete()
    try:
        await client.send_audio(CallbackQuery.message.chat.id, audio=audio_file, duration=int(ytdl_data["duration"]), title=str(ytdl_data["title"]), performer=str(ytdl_data["uploader"]), file_name=str(ytdl_data["title"]), thumb=sedlyf,caption=capy)
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f" \n{e}")

@Client.on_message(filters.text & filters.group, group=87543456773463275645433475)
async def handle_tiktok(c: Client, m: Message):
    bot_username = c.me.username
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    text = m.text
    if "tiktok.com" in text or "vm.tiktok.com" in text or "vt.tiktok.com" in text:
        url = text
        response = requests.get(f"https://tikwm.com/api/?url={url}")
        TikTok = response.json()
        if TikTok['msg'] == "success":
            tiktok_data = TikTok['data']
            author_nickname = tiktok_data['author']['nickname']
            author_unique_id = tiktok_data['author']['unique_id']
            author_id = tiktok_data['author']['id']
            play_count = tiktok_data['play_count']
            digg_count = tiktok_data['digg_count']
            comment_count = tiktok_data['comment_count']
            share_count = tiktok_data['share_count']
            title = tiktok_data['title']
            play_url = tiktok_data['play']
            music_url = tiktok_data['music']
            await m.reply_video(
                video=play_url,
                caption=f"- تم التحميل بنجاح\n\n"
                        f" - معلومات الحساب ↫ ⤈\n"
                        f"**- الاسم: {author_nickname}**\n"
                        f"**- المستخدم: {author_unique_id}**\n"
                        f"**- المعرف: {author_id}**\n\n"
                        f" - معلومات الموسيقى ↫ ⤈**\n"
                        f"**- الاسم: {tiktok_data['music_info']['author']}**\n\n"
                        f" - وصف الفيديو ↫ ⤈**\n"
                        f"**{title}**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("「 قناة السورس 」", url=f"{soesh}")],
                        [InlineKeyboardButton("「 مبرمج السورس 」", url=f"https://t.me/{devus}")]
                    ]
                )
            )
        else:
            await m.reply_text("❌ حدث خطأ أثناء التحميل.")