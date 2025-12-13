import asyncio
import requests
import random
import re
import json
import pytz
import textwrap
import aiofiles
import aiohttp
import os
from pyrogram.types import Message, ChatPermissions
from collections import defaultdict, deque
import sqlite3
import time
import datetime
from pyrogram import Client as client
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from typing import List, Union
from pyrogram import *
import pyromod.listen
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import aiohttp
from datetime import datetime, timedelta
from random import choice
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from traceback import format_exc
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from telegraph import upload_file
from unidecode import unidecode
import sqlite3
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from asyncio import gather
from io import BytesIO
from pyrogram import Client, filters
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned, devphots
from casery import caes, casery, group, source, photosource, caserid, OWNER, muusiic, suorce 
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from pyrogram.errors import exceptions
from pyrogram.enums import ParseMode
from math import sqrt
from typing import Union
from CASERr.CASERr import caserid
#...........................................  زواج  ...........................................................................    
users_db = {}

@Client.on_message(filters.command(["طلاق"], ""), group=18005655435)
async def divorce(client, message: Message):
    if not message.reply_to_message:
        await message.reply("يرجى الرد على رسالة شخص آخر 'طلاق'.")
        return
    target_user = message.reply_to_message.from_user
    user_id = message.from_user.id
    target_user_id = target_user.id
    if user_id in users_db and users_db[user_id] == target_user_id:
        del users_db[user_id]
        del users_db[target_user_id]        
        await message.reply(
            f"لقد تم طلاقك من {message.from_user.mention}."
        )
    else:
        await message.reply("لا يمكنك الطلاق من شخص لم تكن متزوجًا منه.")
        

@Client.on_message(filters.command(["زوجني"], "") & filters.reply)
async def marriage_offer(client, message: Message):
    if not message.reply_to_message:
        await message.reply("يرجى الرد على رسالة شخص آخر 'زوجني'.")
        return    
    target_user = message.reply_to_message.from_user
    user_id = message.from_user.id
    target_user_id = target_user.id
    if user_id in users_db:
        return await message.reply("انت مجوز يعسل")
    if target_user_id in users_db:
        return await message.reply("الشخص مجوز يعسل")        
    await send_marriage_keyboard(message, user_id, target_user_id)

async def send_marriage_keyboard(message: Message, user_id: int, target_user_id: int):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("قبول", callback_data=f"accept_{user_id}_{target_user_id}"),
         InlineKeyboardButton("رفض", callback_data=f"reject_{user_id}_{target_user_id}")]
    ])
    await message.reply_to_message.reply_text(
        f"اقتراح زواج من {message.from_user.mention}، هل توافق؟", reply_markup=keyboard
    )

@Client.on_callback_query(filters.regex("^(accept_(\\d+)_(\\d+)|reject_(\\d+)_(\\d+))$"))
async def callbacy_handler(client, callback_query):
    data = callback_query.data
    action, user_id, target_user_id = data.split("_")
    if callback_query.from_user.id != int(target_user_id):
        await callback_query.answer("بطل لعب في حاجه مش بتعتك", show_alert=True)
        return
    if action == "accept":
        users_db[int(user_id)] = int(target_user_id)
        users_db[int(target_user_id)] = int(user_id)
        await callback_query.answer("تم قبول الزواج!")
        await callback_query.edit_message_text("تم قبول الزواج!")
    elif action == "reject":
        await callback_query.answer("تم رفض الزواج!")
        await callback_query.edit_message_text("تم رفض الزواج!")

@Client.on_message(filters.command("زوجتي", ""), group=18005054)
async def show_spouse(client, message: Message):
    user_id = message.from_user.id
    spouse_id = users_db.get(user_id)
    if spouse_id:
        us1r = await client.get_users(spouse_id)
        ho2ss = us1r.mention()    
        await message.reply(f"زوجتك هي: {ho2ss}")
    else:
        await message.reply("ليس لديك زوجة بعد.")

@Client.on_message(filters.command("زوجي", ""), group=180055764)
async def show_spouse_reverse(client, message: Message):
    user_id = message.from_user.id
    spouse_id = None
    for key, value in users_db.items():
        if value == user_id: 
            spouse_id = key
            break
    if spouse_id:
        us1r = await client.get_users(spouse_id)
        ho2ss = us1r.mention()    
        await message.reply(f"زوجك هو: {ho2ss}")
    else:
        await message.reply("ليس لديك زوج بعد.")
#...........................................  زواج  ...........................................................................    
#...........................................  الجاسوس  ...........................................................................    
plaayers = {}
game_staate = []
playe = [] 
amakenm = [
    "حضانه", "مطعم", "بلايستيشن", "البريد", "ملعب", "مول", 
    "حديقه", "متحف", "مطار", "البحر", "الصحراء", "الجيم", 
    "ملاهي", "البيت", "مستشفي", "مدرسة", "جامعة", "صالة أفراح", 
    "كنيسة", "مسجد", "محطة قطار", "حديقة حيوان", "سوق", 
    "مكتبة", "محل تجاري", "مركز تسوق", "مركز صحي", "مسرح"
]
foods = [
    "كوارع", "سمك", "فراخ", "مكرونه بشمل", "تفاح", "بطاطس", 
    "كشري", "رز", "حمام", "كفته", "مانجا", "بيتزا", "موز", 
    "كاكا", "بطيخ", "طاجن", "محشي", "شوربة", "فطير", "عصير", 
    "كعكة", "سلطة", "فواكه", "شاورما", "حمص", "بقوليات", 
    "برجر", "سندوتشات", "شيبس", "بيتزا كريسبي"
]
hawas = [
    "فيل", "اسد", "دب", "كلب", "نمر", "زرافه", "قرد", "ثعبان", 
    "حصان", "خروف", "قطه", "بقره", "سلحفه", "حربايه", "خنزير", "ديناصور",
    "جمل", "قطة فهد", "لقلق", "عصفور", "سمكة", "دلفين", "قرش",
    "بجعة", "بومة", "بستاني", "نسر", "عقاب", "غزال", "يحشوش", "ثور",
    "فأر", "لعبة", "سلحفاة كبيرة", "إوزة", "خروف عربي"
]

plaingrs = [
    "ميسي", "رونالدو", "نيمار", "بيليه", "مارادونا", "زيدان", 
    "كريستيانو", "هاري كين", "محمد صلاح", "ساني", "دي بروين", 
    "كافاني", "بوجبا", "لوكا مودريتش", "سيرجيو راموس", 
    "أليسون", "مانويل نوير", "تير شتيجن", "غريزمان", "إيكاردي", 
    "فاران", "مبابي", "أجويرو", "فرينكي دي يونغ", "رحيم ستيرلينغ", 
    "تيمو فيرنر", "ديمبلي", "أونانا", "محرز", "فجولي", 
    "كريم بنزيما", "فيرجيل فان دايك", "راشفورد", "كوبو", "لوكاتيلي", 
    "رودري", "هالاند", "كوكي", "بيدري", "بوسكيتس", 
    "شيزني", "ديفيد دي خيا", "ألفونسو ديفيز", "جو هارت", "أرثر", 
    "نغولو كانتي", "ماركوس ألونسو", "سمير هاندانوفيتش", "أندريا بيلوتي", "أوتافيو"
]

ama556kenm = [
    "حضانه", "مطعم", "بلايستيشن", "البريد", "ملعب", "مول", 
    "حديقه", "متحف", "مطار", "البحر", "الصحراء", "الجيم", 
    "ملاهي", "البيت", "مستشفي", "مدرسة", "جامعة", "صالة أفراح", 
    "كنيسة", "مسجد", "محطة قطار", "حديقة حيوان", "سوق", 
    "مكتبة", "محل تجاري", "مركز تسوق", "مركز صحي", "مسرح", 
    "كوارع", "سمك", "فراخ", "مكرونه بشمل", "تفاح", "بطاطس", 
    "كشري", "رز", "حمام", "كفته", "مانجا", "بيتزا", "موز", 
    "كاكا", "بطيخ", "طاجن", "محشي", "شوربة", "فطير", "عصير", 
    "كعكة", "سلطة", "فواكه", "شاورما", "حمص", "بقوليات", 
    "برجر", "سندوتشات", "شيبس", "بيتزا كريسبي",
    "فيل", "اسد", "دب", "كلب", "نمر", "زرافه", "قرد", "ثعبان", 
    "حصان", "خروف", "قطه", "بقره", "سلحفه", "حربايه", "خنزير", "ديناصور",
    "جمل", "قطة فهد", "لقلق", "عصفور", "سمكة", "دلفين", "قرش",
    "بجعة", "بومة", "بستاني", "نسر", "عقاب", "غزال", "يحشوش", "ثور",
    "فأر", "لعبة", "سلحفاة كبيرة", "إوزة", "خروف عربي",
    "ميسي", "رونالدو", "نيمار", "بيليه", "مارادونا", "زيدان", 
    "كريستيانو", "هاري كين", "محمد صلاح", "ساني", "دي بروين", 
    "كافاني", "بوجبا", "لوكا مودريتش", "سيرجيو راموس", 
    "أليسون", "مانويل نوير", "تير شتيجن", "غريزمان", "إيكاردي", 
    "فاران", "مبابي", "أجويرو", "فرينكي دي يونغ", "رحيم ستيرلينغ", 
    "تيمو فيرنر", "ديمبلي", "أونانا", "محرز", "فجولي", 
    "كريم بنزيما", "فيرجيل فان دايك", "راشفورد", "كوبو", "لوكاتيلي", 
    "رودري", "هالاند", "كوكي", "بيدري", "بوسكيتس", 
    "شيزني", "ديفيد دي خيا", "ألفونسو ديفيز", "جو هارت", "أرثر", 
    "نغولو كانتي", "ماركوس ألونسو", "سمير هاندانوفيتش", "أندريا بيلوتي", "أوتافيو"
]

@Client.on_message(filters.command(["الجاسوس"], ""), group=58513)
async def hdjf575888(client, message):
    global plaayers, game_staate
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []
    if chat_id not in game_staate:
     if user_id not in plaayers[chat_id]:
         plaayers[chat_id].append(user_id)  
         game_staate.append(chat_id)  
         playe.append(user_id)  
         player_count = len(plaayers[chat_id])
         await message.reply_text(f"تم انضمام {player_count} الي العبه اضغط أبدا عند اكتمال العابين", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("بدا اللعبه", callback_data="hossamkfd " + str(message.from_user.id))], [InlineKeyboardButton("انضمام", callback_data="joiname")]]))
     else:
         await message.reply_text("انت منضم بالفعل")
    else:
        await message.reply_text("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")
        
@Client.on_callback_query(filters.regex("joiname"))
async def hfjvmgvjdkfc(client, chrr: CallbackQuery):
    global plaayers, playe
    chat_id = chrr.message.chat.id
    user_id = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = [] 
    if user_id not in plaayers[chat_id]:
        try:
          await client.send_message(user_id, "اجهز ي رايق")    
          plaayers[chat_id].append(user_id)  
          await chrr.answer("تم تسجيلك في اللعبه بنجاح ✅", show_alert=True)
        except Exception as e:
          await chrr.answer(f"دوس بدا في البوت نفسه عشان تلعب", show_alert=True)
    else:
        await chrr.answer("انت منضم بالفعل", show_alert=True)
    player_count = len(plaayers[chat_id])
    for usr in playe: 
      await chrr.edit_message_text(f"تم انضمام {player_count} الي العبه اضغط أبدا عند اكتمال العابين", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("بدا اللعبه", callback_data="hossamkfd " + str(usr))], [InlineKeyboardButton("انضمام", callback_data="joiname")]]))

@Client.on_callback_query(filters.regex("^hossamkfd (\\d+)$"))
async def st58t_57game(client, chrr: CallbackQuery):
    global players
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []     
    user_id = int(chrr.matches[0].group(1))
    if len(plaayers[chat_id]) < 2:
        await chrr.answer("لا يمكن بدء اللعبة. يجب أن يكون هناك 2 على الأقل من اللاعبين.", show_alert=True)
        return
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        button = [
            [InlineKeyboardButton(text="امـاكـن", callback_data=f"amaken " + str(chrr.from_user.id)), 
             InlineKeyboardButton(text="الـطـعـام", callback_data=f"food " + str(chrr.from_user.id))],
            [InlineKeyboardButton(text="حـيـوانـات", callback_data=f"hawan " + str(chrr.from_user.id)),
             InlineKeyboardButton(text="لـعـيـبـه", callback_data=f"plaing " + str(chrr.from_user.id))],            
            [InlineKeyboardButton(text="عـشـوائـي", callback_data=f"ama556 " + str(chrr.from_user.id))],            
        ]
        await chrr.message.reply_text("اختار حاجه من دوله", reply_markup=InlineKeyboardMarkup(button))
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)

@Client.on_callback_query(filters.regex("^amaken (\\d+)$"))
async def a57en_g586ame(client, chrr: CallbackQuery):
    global plaayers
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []    
    user_names = []
    spy_user = random.choice(plaayers[chat_id])
    us1r = await client.get_users(spy_user)
    ho2ss = us1r.mention()    
    amak = random.choice(amakenm)
    user_id = int(chrr.matches[0].group(1))
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        for player in plaayers[chat_id]:
            if player == spy_user:
                await client.send_message(player, "أنت الجاسوس 🤫")
            else:
                await client.send_message(player, amak)
        for plyer in plaayers[chat_id]:                
            usr = await client.get_users(plyer)
            hoss = usr.mention()
            await client.send_message(chrr.message.chat.id, f"اتكلم يا {hoss}\nمعاك 25 ثانية.")
            await asyncio.sleep(25)
        for player_id in plaayers[chat_id]:
           user = await client.get_users(player_id)
           user_names.append(user.first_name)
        await client.send_poll(chrr.message.chat.id, "مين الجاسوس 😂♥", user_names, is_anonymous=False)
        await asyncio.sleep(20)
        plaayers[chat_id].clear()
        game_staate.clear()
        playe.clear()
        ask = await client.ask(chrr.message.chat.id, f"اي هي الكلمه يا جاسوس {ho2ss}\n معاك 30 ثانيه", filters=filters.user(spy_user), timeout=30)
        if ask.text == f"{amak}":
          return await ask.reply_text(f"**الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فعلا الواد دا**")
        await ask.reply_text(f"الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فاشل")        
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)

@Client.on_callback_query(filters.regex("^food (\\d+)$"))
async def d_g645ame(client, chrr: CallbackQuery):
    global plaayers
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []    
    user_names = []
    spy_user = random.choice(plaayers[chat_id])
    us1r = await client.get_users(spy_user)
    ho2ss = us1r.mention()    
    amak = random.choice(foods)
    user_id = int(chrr.matches[0].group(1))
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        for player in plaayers[chat_id]:
            if player == spy_user:
                await client.send_message(player, "أنت الجاسوس 🤫")
            else:
                await client.send_message(player, amak)
        for plyer in plaayers[chat_id]:                
            usr = await client.get_users(plyer)
            hoss = usr.mention()
            await client.send_message(chrr.message.chat.id, f"اتكلم يا {hoss}\nمعاك 25 ثانية.")
            await asyncio.sleep(25)
        for player_id in plaayers[chat_id]:
           user = await client.get_users(player_id)
           user_names.append(user.first_name)
        await client.send_poll(chrr.message.chat.id, "مين الجاسوس 😂♥", user_names, is_anonymous=False)
        await asyncio.sleep(20)
        plaayers[chat_id].clear()
        game_staate.clear()
        playe.clear()
        ask = await client.ask(chrr.message.chat.id, f"اي هي الكلمه يا جاسوس {ho2ss}\n معاك 30 ثانيه", filters=filters.user(spy_user), timeout=30)
        if ask.text == f"{amak}":
          return await ask.reply_text(f"**الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فعلا الواد دا**")
        await ask.reply_text(f"الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فاشل")        
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)

@Client.on_callback_query(filters.regex("^hawan (\\d+)$"))
async def hagfgan_g575ame(client, chrr: CallbackQuery):
    global plaayers
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []    
    user_names = []
    spy_user = random.choice(plaayers[chat_id])
    us1r = await client.get_users(spy_user)
    ho2ss = us1r.mention()    
    amak = random.choice(hawas)
    user_id = int(chrr.matches[0].group(1))
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        for player in plaayers[chat_id]:
            if player == spy_user:
                await client.send_message(player, "أنت الجاسوس 🤫")
            else:
                await client.send_message(player, amak)
        for plyer in plaayers[chat_id]:                
            usr = await client.get_users(plyer)
            hoss = usr.mention()
            await client.send_message(chrr.message.chat.id, f"اتكلم يا {hoss}\nمعاك 25 ثانية.")
            await asyncio.sleep(25)
        for player_id in plaayers[chat_id]:
           user = await client.get_users(player_id)
           user_names.append(user.first_name)
        await client.send_poll(chrr.message.chat.id, "مين الجاسوس 😂♥", user_names, is_anonymous=False)
        await asyncio.sleep(20)
        plaayers[chat_id].clear()
        game_staate.clear()
        playe.clear()
        ask = await client.ask(chrr.message.chat.id, f"اي هي الكلمه يا جاسوس {ho2ss}\n معاك 30 ثانيه", filters=filters.user(spy_user), timeout=30)
        if ask.text == f"{amak}":
          return await ask.reply_text(f"**الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فعلا الواد دا**")
        await ask.reply_text(f"الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فاشل")        
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)
        
@Client.on_callback_query(filters.regex("^plaing (\\d+)$"))
async def hawas5_g575ame(client, chrr: CallbackQuery):
    global plaayers
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []    
    user_names = []
    spy_user = random.choice(plaayers[chat_id])
    us1r = await client.get_users(spy_user)
    ho2ss = us1r.mention()    
    amak = random.choice(plaingrs)
    user_id = int(chrr.matches[0].group(1))
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        for player in plaayers[chat_id]:
            if player == spy_user:
                await client.send_message(player, "أنت الجاسوس 🤫")
            else:
                await client.send_message(player, amak)
        for plyer in plaayers[chat_id]:                
            usr = await client.get_users(plyer)
            hoss = usr.mention()
            await client.send_message(chrr.message.chat.id, f"اتكلم يا {hoss}\nمعاك 25 ثانية.")
            await asyncio.sleep(25)
        for player_id in plaayers[chat_id]:
           user = await client.get_users(player_id)
           user_names.append(user.first_name)
        await client.send_poll(chrr.message.chat.id, "مين الجاسوس 😂♥", user_names, is_anonymous=False)
        await asyncio.sleep(20)
        plaayers[chat_id].clear()
        game_staate.clear()
        playe.clear()
        ask = await client.ask(chrr.message.chat.id, f"اي هي الكلمه يا جاسوس {ho2ss}\n معاك 30 ثانيه", filters=filters.user(spy_user), timeout=30)
        if ask.text == f"{amak}":
          return await ask.reply_text(f"**الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فعلا الواد دا**")
        await ask.reply_text(f"الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فاشل")        
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)

@Client.on_callback_query(filters.regex("^ama556 (\\d+)$"))
async def ama556kenm_g575ame(client, chrr: CallbackQuery):
    global plaayers
    chat_id = chrr.message.chat.id
    hossam = chrr.from_user.id
    if chat_id not in plaayers:
        plaayers[chat_id] = []    
    user_names = []
    spy_user = random.choice(plaayers[chat_id])
    us1r = await client.get_users(spy_user)
    ho2ss = us1r.mention()    
    amak = random.choice(ama556kenm)
    user_id = int(chrr.matches[0].group(1))
    if user_id == chrr.from_user.id:
        await chrr.message.delete()
        for player in plaayers[chat_id]:
            if player == spy_user:
                await client.send_message(player, "أنت الجاسوس 🤫")
            else:
                await client.send_message(player, amak)
        for plyer in plaayers[chat_id]:                
            usr = await client.get_users(plyer)
            hoss = usr.mention()
            await client.send_message(chrr.message.chat.id, f"اتكلم يا {hoss}\nمعاك 25 ثانية.")
            await asyncio.sleep(25)
        for player_id in plaayers[chat_id]:
           user = await client.get_users(player_id)
           user_names.append(user.first_name)
        await client.send_poll(chrr.message.chat.id, "مين الجاسوس 😂♥", user_names, is_anonymous=False)
        await asyncio.sleep(20)
        plaayers[chat_id].clear()
        game_staate.clear()
        playe.clear()
        ask = await client.ask(chrr.message.chat.id, f"اي هي الكلمه يا جاسوس {ho2ss}\n معاك 30 ثانيه", filters=filters.user(spy_user), timeout=30)
        if ask.text == f"{amak}":
          return await ask.reply_text(f"**الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فعلا الواد دا**")
        await ask.reply_text(f"الجاسوس هو {ho2ss}\nاجابتو كانت :{ask.text}\nطلع جاسوس فاشل")        
    else:
        await chrr.answer("مينفعش تبدا اللعبه انت", show_alert=True)
#...........................................  الجاسوس  ...........................................................................    
#...........................................  معلومات الجروب  ...........................................................................
@Client.on_message(filters.command(["جروب", "رابط الجروب","الرابط","الجروب","ايدي الجروب"], ""), group=7053086584) 
async def mag1moatt(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
        return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in caes:     
        chat_idd = message.chat.id
        chat_name = message.chat.title
        # تحقق إذا كانت المجموعة عامة أو خاصة
        if message.chat.username:  # إذا كانت المجموعة عامة
            chat_username = f"@{message.chat.username}"   
            link_username = f"https://t.me/{message.chat.username}"  
        else:  # إذا كانت المجموعة خاصة
            invite_link = await client.export_chat_invite_link(message.chat.id)  # توليد رابط دعوة خاص
            chat_username = "الجروب خاص"
            link_username = invite_link
        await message.reply_text(f"**😎 ¦ اسم الجروب: {chat_name}\n❤ ¦ ايدي الجروب: `{chat_idd}`\n☠️ ¦ معرف الجروب: {chat_username}\n🌚 ¦ رابط المجموعه: {link_username} **")
    else:
        return await message.reply_text(f"عذرا عزيزي {message.from_user.mention}\n هذا الأمر لا يخصك ✨♥")
#...........................................  معلومات الجروب  ..........................................................................
#...........................................  معلومات القناه  ..........................................................................
@Client.on_message(filters.command(["قناه", "رابط القناه", "الرابط", "القناه","ايدي القناه","ايدي قناه","الايدي"], ""), group=7053084)
async def can1oat(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    # التحقق من أن الرسالة ليست من مستخدم فردي في القناة
    if message.sender_chat:  # تحقق من أن الرسالة تأتي من قناة
        chat_id = message.chat.id
        chat_name = message.chat.title
        chat_username = f"@{message.chat.username}" if message.chat.username else "القناه خاصه "
        # إذا كانت القناة خاصة، قم بإنشاء رابط دعوة
        if not message.chat.username:
            link_username = await client.export_chat_invite_link(chat_id)
        else:
            link_username = f"https://t.me/{message.chat.username}"
        await message.reply_text(f"**😎 ¦ اسم القناة: {chat_name}\n❤ ¦ ايدي القناة: `{chat_id}`\n☠️ ¦ معرف القناة: {chat_username}\n🌚 ¦ رابط القناة: {link_username} **")
#...........................................  معلومات القناه  ..........................................................................
#...........................................  الاله الحاسبه   .........................................................................
@Client.on_message(filters.command(["الاله", "الحاسبه"], ""), group=7053)
async def start(client, message: Message) -> None:
   user_id: int = message.from_user.id
   caption: str = "- ادخل عمليتك...\n|"
   info = await client.get_chat(caserid)
   markup: Keyboard = Keyboard([
       [Button("AC", "c"), Button("DEL", "DEL"), Button(info.first_name, url=f"{info.username}.t.me")], 
       [Button("√", "sqrt("), Button("^", "**"), Button("(", "("), Button(")", ")")],
       [Button("7", "7"), Button("8", "8"), Button("9", "9"), Button("÷", "/")],
       [Button("4", "4"), Button("5", "5"), Button("6", "6"), Button("×", "*")],
       [Button("1", "1"), Button("2", "2"), Button("3", "3"), Button("-", "-")],
       [Button(".", "."), Button("0", "0"), Button("=", "="), Button("+", "+")],
       [Button("- Hide Calculator -", f"d {user_id}")]
   ])
   await message.reply_text(caption, reply_markup=markup)

@Client.on_callback_query(filters.regex(r"^(0|1|2|3|4|5|6|7|8|9|=|[+\-*/^()])$"))
async def jvu5nput(client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    markup: Keyboard = callback.message.reply_markup.inline_keyboard
    if int(markup[-1][0].callback_data.split()[1]) != user_id: 
        return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)    
    if callback.data == "=": 
        return await callback.answer("- أدخل عمليه أولا...\n|", show_alert=True)    
    caption: str = f"{callback.message.text.replace('|', '')}{callback.data}"
    markup[-2][-2].callback_data = "result " + caption.split('\n', 1)[-1]
    await callback.edit_message_text(caption, reply_markup=Keyboard(markup), parse_mode=ParseMode.HTML)
    
@Client.on_callback_query(filters.regex(r"^(c)$"))
async def clear(client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id 
    caption: str = "- ادخل عمليتك...\n|"
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    try:await callback.edit_message_text(caption, reply_markup=markup)
    except exceptions.bad_request_400.MessageNotModified:await callback.answer("- لايوجد مدخلات لحذفها..\n|")

@Client.on_callback_query(filters.regex(r"^(DEL)$"))
async def rm(client, callback: CallbackQuery):
    user_id: int = callback.from_user.id 
    text: str = callback.message.text
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    elif text.endswith("|"): return await callback.answer("- لا شئ ليتم حذفه.")
    caption: str = text[:-1] if len(text.split("\n")[1]) > 1 else text[:-1] + "|"
    return await callback.edit_message_text(caption, reply_markup=markup)

@Client.on_callback_query(filters.regex(r"^(result)"))
async def _result(client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    data: str = callback.data
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    markup.inline_keyboard[-2][-2].callback_data = "="
    try:result: Union[int, float] = eval(data.split(maxsplit=1)[1])
    except ZeroDivisionError: return await callback.answer("- لا يمكنك القسمه على صفر", show_alert=True)
    except SyntaxError: return await callback.answer("- تأكد من كتابة العمليه بشكله صحيح", show_alert=True)
    caption: str = f"- ناتج العمليه...\n{result}"
    await callback.edit_message_text(caption, reply_markup=markup)


@Client.on_callback_query(filters.regex(r"^(d )"))
async def d(client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    await callback.message.delete()
#...........................................  الاله الحاسبه   .........................................................................
#...........................................   زكرني  ..........................................................................
reminders = {}

@Client.on_message(filters.command(["زكرني","فكرني","منبه"], ""), group=7005453)
async def set_reminder(client, message: Message):
    try:
        time_str = message.text.replace(["زكرني","فكرني","منبه"], "").strip()
        hour_minute = time_str.split(":")        
        if len(hour_minute) != 2:
            await message.reply_text("الرجاء إدخال الوقت بصيغة صحيحة, مثال: زكرني 8:30.")
            return                
        hour = int(hour_minute[0])
        minute = int(hour_minute[1])
        if not (1 <= hour <= 23) or not (0 <= minute < 60):
            await message.reply_text("الرجاء إدخال ساعة صحيحة بين 1 و 23 والدقائق بين 0 و 59.")
            return
        user_id = message.from_user.mention
        useid = message.from_user.id
        chat_id = message.chat.id
        if user_id not in reminders:
            reminders[user_id] = []
        reminders[user_id].append((hour, minute))
        await message.reply_text(f"تم إعداد التذكير لك في الساعة {hour}:{minute:02d} {'ص' if hour < 12 else 'م'}.")
        await hosscasar(client, message, user_id, chat_id, useid)
    except ValueError:
        await message.reply_text("الرجاء إدخال وقت صحيح.")
        
async def hosscasar(client, message, user_id, chat_id, useid):
        while True:
            now = datetime.now(pytz.timezone("Africa/Cairo"))
            for reminder in reminders.get(user_id, []):
                rem_hour, rem_minute = reminder
                if now.hour % 23 == (rem_hour % 23) and now.minute == rem_minute:
                    await client.send_message(chat_id, f"مرحبا عزيزي: {user_id}\n لقد امرتني بتزكيرك في هذا الوقت ✨♥")
                    try: 
                      await client.send_message(useid, f"مرحبا عزيزي: {user_id}\n لقد امرتني بتزكيرك في هذا الوقت ✨♥")
                    except Exception as e:
                      print(e)
                    reminders[user_id].remove(reminder)
                    break
            await asyncio.sleep(30)
#...........................................   زكرني  ..........................................................................
#...........................................  تقيد بوقت ...........................................................................    
@Client.on_message(filters.command(["تقيد مؤقت","تقييد مؤقت","تقيد موقت","تقييد موقت"], "") & filters.group, group=68688)
async def restriction(app: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id 
    reply_to = message.reply_to_message
    replied_id = reply_to.from_user.id
    admin = ChatMemberStatus.ADMINISTRATOR
    owner = ChatMemberStatus.OWNER
    memberA = await app.get_chat_member(chat_id, user_id)
    memberB = await app.get_chat_member(chat_id, replied_id)
    if memberA.status not in [admin, owner]: return await message.reply_text("- يجب أن تكون مشرف في المجموعه على الأقل لإستخدام هذا الأمر.")
    elif memberB.status in [admin, owner]: return await message.reply_text(f"- لا يمكنك تقييد {'المالك' if memberB.status == owner else 'المشرف'}.")
    text = message.text.split()
    timer = datetime.now() + timedelta(seconds=int(text[1])) if len(text) > 1 else datetime.now() + timedelta(seconds=30)
    try:await app.restrict_chat_member(chat_id=chat_id, user_id=replied_id, until_date=timer, permissions=ChatPermissions(can_send_messages=False))
    except TypeError: pass
    await message.reply_text(f"- تم تقييده حتى {timer.strftime('%H:%M:%S')}")
    asyncio.create_task(checker(chat_id, replied_id, timer, app))

async def checker(chat_id, user_id, until_date, app):
    current = datetime.now().strftime('%H:%M:%S')
    while current != until_date.strftime('%H:%M:%S'):
        current = datetime.now().strftime('%H:%M:%S')
    await app.restrict_chat_member(chat_id, user_id, permissions=ChatPermissions(can_send_messages=True))
    return   
#...........................................  تقيد بوقت ...........................................................................    
    #..........................................     مطور البوت انضم    ...............................................................
@Client.on_message(filters.new_chat_members)
async def welco857me(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    try:
        user = await client.get_chat(OWNER_ID)
        CASER = user.username 
        if message.new_chat_members[0].username == f"{CASER}":
            try:
                chat_id = message.chat.id
                user_id = message.new_chat_members[0].id
                await client.promote_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    privileges=ChatPrivileges(
                        can_promote_members=True,
                        can_manage_video_chats=True,
                        can_pin_messages=True,
                        can_invite_users=True,
                        can_restrict_members=True,
                        can_delete_messages=True,
                        can_change_info=True
                    )
                )
                await client.set_administrator_title(chat_id, user_id, "مطور البوت")
                await client.send_message(message.chat.id, 
                    f"**انضم مطور البوت الى هنا الآن [مطور البوت](https://t.me/{CASER})⚡** يرجى من الأعضاء احترام وجوده 🥷🥷"
                )
            except Exception as e:
                await client.send_message(message.chat.id, f"**انضم مطور البوت الى هنا الآن [مطور البوت](https://t.me/{CASER})⚡** يرجى من الأعضاء احترام وجوده 🥷🥷")
    except Exception as e:
        print(e)
    #..........................................     مطور البوت انضم    ...............................................................
        #..........................................       كشف    ...............................................................
@Client.on_message(filters.command(["معلوماته","كشف"], ""))
async def kashf(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.reply_to_message:
       user_id = message.reply_to_message.from_user.id
       user = await client.get_chat_member(message.chat.id, user_id)  
       name = user.user.first_name
       CASER = await client.get_chat(user_id)
       bioo = CASER.bio
    elif message.text:
       username = message.text.split(" ", 1)[1]
       user = await client.get_chat_member(message.chat.id, username)
       name = user.user.first_name
       CASER = await client.get_chat(username)
       bioo = CASER.bio
    else:
       await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في رفعه")
       return
    await message.reply_text(f"❤ ¦ ɴᴀᴍᴇ : {user.user.mention}\n🥰 ¦ ᴜѕᴇ : @{user.user.username}\n🔥 ¦ ɪᴅ : {user.user.id}\n♥¦ ɪᴅ ᥇𝓲ꪮꪮ : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})\n?? ¦ ɪᴅ ᴄʜᴀᴛ : {message.chat.id}\n☠️ ¦ ᴄʜᴀᴛ : {message.chat.title}\n💕 ¦ ɢʀᴏᴜᴘ : @{message.chat.username}\n", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{user.user.username}")]]))
 #..........................................       كشف    ...............................................................
 #..........................................       المالك    ...............................................................
@Client.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""))
async def owner(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
        return 
    x = []
    async for m in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == enums.ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
        m = await client.get_users(int(x[0]))
        if m.photo:
            async for photo in client.get_chat_photos(x[0], limit=1):
                await message.reply_photo(
                    photo.file_id,
                    caption=(
                        f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 : {m.first_name}\n"
                        f"🎯 ¦𝚄𝚂𝙴𝚁 : @{m.username}\n"
                        f"🎃 ¦𝙸𝙳 : {m.id}\n"
                        f"✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n"
                        f"♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 : {message.chat.id}\n"
                        f"😎 ¦ [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")]]
                    )
                )
        else:
            await message.reply_text(
                f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 : {m.first_name}\n"
                f"🎯 ¦𝚄𝚂𝙴𝚁 : @{m.username}\n"
                f"🎃 ¦𝙸𝙳 : `{m.id}`\n"
                f"✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n"
                f"♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 : `{message.chat.id}`\n"
                f"😎 ¦ [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")]])
            )
    else:
        await message.reply_text("المالك غير موجود أو محذوف.")
 #..........................................       المالك    ...............................................................
  #..........................................       تاك    ............................................................
tak = []

@Client.on_message(filters.command(["قفل التاك", "تعطيل التاك","قفل تاك","تعطيل تاك"], ""), group=2173) 
async def takl5ock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if message.chat.id in tak:
         return await message.reply_text("تم معطل من قبل🔒")
       tak.append(message.chat.id)
       return await message.reply_text("تم تعطيل التاك بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح التاك", "تفعيل التاك","فتح تاك","تفعيل تاك"], ""), group=70643) 
async def tak24open(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if not message.chat.id in tak:
         return await message.reply_text("التاك مفعل من قبل ✅")
       tak.remove(message.chat.id)
       return await message.reply_text("تم فتح التاك بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
       
array = []

@Client.on_message(filters.command(["@all", "تاك","all","تكك"], "") & ~filters.private)
async def nummmm(client: client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in tak:
        return await message.reply_text(f"عزرا عزيزي [{message.from_user.mention}] \n التاك معطل اطلب من الادمنيه تفعيله ✨♥")           
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
     await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
     return
    await message.reply_text("**♪ جاري بدأ المنشن ، لايقاف الامر اضغط /cancel  💎 .**")
    i = 0
    txt = ""
    zz = message.text
    if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
    try:
     zz = zz.replace("@all","").replace("تاك","").replace("all","").replace("تكك","")
    except:
      pass
    array.append(message.chat.id)
    async for x in client.get_chat_members(message.chat.id):
       if message.chat.id not in array:
         return
       if not x.user.is_deleted:
        i += 1
        txt += f" {x.user.mention} ›"
        if i == 10:
         try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception:
              array.remove(message.chat.id)
    array.remove(message.chat.id)

@Client.on_message(filters.command(["/cancel", "بس منشن","ايقاف منشن","ايقاف تاك","ايقاف التاك","ايقاف تكك","بس تاك"], "")) 
async def stop(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.chat.id in tak:
        return await message.reply_text(f"عزرا عزيزي [{message.from_user.mention}] \n التاك معطل اطلب من الادمنيه تفعيله ✨♥")      
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in caes:
     await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
     return
    if message.chat.id not in array:
      await message.reply("**♪ المنشن متوقف بي الفعل  💎 .**")
      return 
    if message.chat.id in array:
     array.remove(message.chat.id)
     await message.reply("**♪ تم ايقاف المنشن عزيزي  💎 .**")
     return                    
  #..........................................       تاك    ...............................................................
    #..........................................       الايدي    ...............................................................
iddof = []
@Client.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=73) 
async def iddlock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if message.chat.id in iddof:
         return await message.reply_text("تم معطل من قبل🔒")
       iddof.append(message.chat.id)
       return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=703) 
async def iddopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in wenru or message.from_user.username in caes:
       if not message.chat.id in iddof:
         return await message.reply_text("الايدي مفعل من قبل ✅")
       iddof.remove(message.chat.id)
       return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
      
@Client.on_message(filters.command(["ايدي","الايدي","ا","ايدى","الايدى"], ""), group=713) 
async def iddd(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if await johned(client, message):
     return
    if message.chat.id in iddof:
        return await message.reply_text(f"عزرا عزيزي [{message.from_user.mention}] \n الايدي معطل اطلب من الادمنيه تفعيله ✨♥")  
    if message.from_user.photo:
        usr = await client.get_chat(message.from_user.id)
        user_id = usr.id
        CASER = usr.username
        name = usr.first_name
        if not id.get(message.from_user.id):
         id[user_id] = []
        idd = len(id[user_id])
        await message.reply_text(text=f"""**╭⎋¦ᚐ𝙽𝙰𝙼𝙴 : {message.from_user.mention}\n╰⊚ᚐᴜsᴇʀᚐ : @{message.from_user.username}\n╭⎋ɪᴅᚐ: `{message.from_user.id}`\n╰⊚ᚐʙɪᴏᚐ: [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})\n♥ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 : `{message.chat.id}`**""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ♥", callback_data=f"heart{user_id}")]]))
    else:
        usr = await client.get_chat(message.from_user.id)
        user_id = usr.id
        name = usr.first_name
        if not id.get(message.from_user.id):
         id[user_id] = []
        idd = len(id[user_id])
        await message.reply_text(text=f"""**╭⎋¦ᚐ𝙽𝙰𝙼𝙴 : {message.from_user.mention}\n╰⊚ᚐᴜsᴇʀᚐ : @{message.from_user.username}\n╭⎋ɪᴅᚐ: `{message.from_user.id}`\n╰⊚ᚐʙɪᴏᚐ: [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})\n♥ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 : `{message.chat.id}`**""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ♥", callback_data=f"heart{user_id}")]]))

id = {}

@Client.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    username = int(callback_request)
    usr = await client.get_chat(username)
    if usr.id not in id:
        id[usr.id] = [] 
    if query.from_user.mention not in id[usr.id]:
        id[usr.id].append(query.from_user.mention) 
    else:
        id[usr.id].remove(query.from_user.mention) 
    idd = len(id[usr.id])
    await query.edit_message_text(
        f"**╭⎋¦ᚐ𝙽𝙰𝙼𝙴 : {usr.first_name} \n╭⎋ɪᴅᚐ : `{usr.id}`\n╰⊚ᚐᴜsᴇʀᚐ: @{usr.username}\n╰⊚ᚐʙɪᴏᚐ : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})\n♥ ¦𝙲𝙷𝙰𝚃: {query.message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 : `{query.message.chat.id}`**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} ♥", callback_data=f"heart{usr.id}")]])
    )
    #..........................................       الايدي    ...............................................................
#............................................ اكس او ...........................................................................    
board = ["⬜️"] * 9
players = []
current_player = 0
fanish_game = None  

def create_board():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(board[0], callback_data="10"), InlineKeyboardButton(board[1], callback_data="11"), InlineKeyboardButton(board[2], callback_data="12")],
        [InlineKeyboardButton(board[3], callback_data="13"), InlineKeyboardButton(board[4], callback_data="14"), InlineKeyboardButton(board[5], callback_data="15")],
        [InlineKeyboardButton(board[6], callback_data="16"), InlineKeyboardButton(board[7], callback_data="17"), InlineKeyboardButton(board[8], callback_data="18")],
    ])

@Client.on_message(filters.command(["اكس او","اكس","xo","ox"], ""), group=76468513) 
async def sta54t_game(client, message):
    global players, board, fanish_game, current_player
    current_player = 0
    fanish_game = False
    players = [message.from_user.id]
    board = ["⬜️"] * 9
    await message.reply_text("""
انقر على الزر أدناه لبدء 👇🏻""", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("بدء اللعب 🎮", callback_data="join_game")]
    ]))

@Client.on_callback_query(filters.regex("join_game"))
async def join_game(client, call):
    global players, current_player
    current_player = 0
    if call.from_user.id not in players:
        players.append(call.from_user.id)
        await client.edit_message_text(
            call.message.chat.id, call.message.id,
            f"دور الاعب الاول : ❌",
            reply_markup=create_board())

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "⬜️":
            return board[combo[0]] 
    return None

def is_draw():
    return all(cell != "⬜️" for cell in board)

@Client.on_callback_query(
    filters.regex("10") | filters.regex("11") | filters.regex("12") |
    filters.regex("13") | filters.regex("14") | filters.regex("15") |
    filters.regex("16") | filters.regex("17") | filters.regex("18"))
async def handle_button(client, call):
    global current_player, players, fanish_game
    if fanish_game == True:
        await call.answer("اللعبة انتهت ⚡️", show_alert=True)
        return
    if call.from_user.id not in players:
        await call.answer("✋", show_alert=True)
        return
    if call.from_user.id != players[current_player]:
        await call.answer("ليس دورك", show_alert=True)
        return
    index = int(call.data) - 10
    if board[index] == "⬜️":
        board[index] = "❌" if current_player == 0 else "⭕️"
        current_player = 1 if current_player == 0 else 0
        user = await client.get_users(players[current_player])
        user_mention = user.mention()
        emo_xo = "❌" if current_player == 0 else "⭕️"
        await call.message.edit(
            f"دور الاعب : {emo_xo}\n{user_mention}",
            reply_markup=create_board())
        
        winner = check_winner()
        if winner:
            winner_mention =(await client.get_users(players[0 if winner == "❌" else 1])).mention
            await call.message.edit(
                f"الفائز 🎉: {winner_mention}")
            fanish_game = True 
            board[:] = ["⬜️"] * 9
        elif is_draw():
            await call.message.edit(
                "التعادل! 🤝")
            fanish_game = True
            board[:] = ["⬜️"] * 9
        if fanish_game==True:
            return
#............................................ اكس او ...........................................................................    
#............................................  لعبه البنك ...........................................................................    
def is_sudoer(_, __, message):
    return message.from_user.id == caserid
other_filters = filters.group &  ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private &  ~filters.via_bot & ~filters.forwarded
)

def load_bank_data():
    try:
        with open('bank_tom.json', 'r') as file:
            bank_data = json.load(file)
    except FileNotFoundError:
        bank_data = {}
    return bank_data
def save_bank_data(bank_data):
    with open('bank_tom.json', 'w') as file:
        json.dump(bank_data, file)

cooldown_time = 12 * 60 * 60  

def check_cooldown(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        time_passed = current_time - last_use_time
        remaining_time = cooldown_time - time_passed
        if time_passed < cooldown_time:
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            response = f"عذرًا، يجب الانتظار {hours} ساعة و {minutes} دقيقة قبل استخدام الكنز مرة أخرى"
            return False, response
    cooldown_data[str(user_id)] = current_time
    save_cooldown_data(cooldown_data)
    return True, None
def load_cooldown_data():
    try:
        with open('cooldown_data.json', 'r') as file:
            cooldown_data = json.load(file)
    except FileNotFoundError:
        cooldown_data = {}
    return cooldown_data
def save_cooldown_data(cooldown_data):
    with open('cooldown_data.json', 'w') as file:
        json.dump(cooldown_data, file)
def get_remaining_time(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        remaining_time = 20 * 60 - (current_time - last_use_time)
        if remaining_time < 0:
            remaining_time = 0
        return remaining_time
    return 0
##############££££££££££#############££££££££££#########££££#
LUCK_COOLDOWN = 1200  

last_luck_times = {}

def get_luck_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_luck_times:
        last_luck_time = last_luck_times[user_id]
        elapsed_time = current_time - last_luck_time
        remaining_time = LUCK_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_luck_time(user_id):
    last_luck_times[user_id] = int(time.time())
##############££££££££££#############££££££££££#########££££#
TRANSFER_COOLDOWN = 1200  


last_transfer_times = {}

def get_transfer_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_transfer_times:
        last_transfer_time = last_transfer_times[user_id]
        elapsed_time = current_time - last_transfer_time
        remaining_time = TRANSFER_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_transfer_time(user_id):
    last_transfer_times[user_id] = int(time.time())

@Client.on_message(filters.command(["تحويل"], ""), group=53)
async def transfer(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_transfer_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    await message.reply_text(f'تم تحويل {amount} دولار بنجاح')
                    update_transfer_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: تحويل + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["استثمار"], ""), group=53)
async def invest(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    # قم بتنفيذ الاستثمار وحساب العائد المحتمل
                    return_amount = amount * random.randint(50, 100) / 100
                    bank_data['accounts'][str(user_id)]['balance'] += return_amount
                    save_bank_data(bank_data)
                    cooldown_data = load_cooldown_data()
                    cooldown_data[str(user_id)] = int(time.time())
                    save_cooldown_data(cooldown_data)
                    await message.reply_text(f'تهانينا! لقد استثمرت {amount} دولار وحصلت على عائد بقيمة {return_amount} دولار')
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: استثمار + المبلغ')
        else:
            remaining_minutes = int(remaining_time / 60)
            remaining_seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {remaining_minutes} دقيقة و {remaining_seconds} ثانية بين كل عملية استثمار')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["حظ"], ""), group=53)
async def luck(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_luck_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    chance = random.randint(0, 1)
                    if chance == 1:
                        win_amount = amount * random.uniform(1, 3)
                        bank_data['accounts'][str(user_id)]['balance'] += win_amount
                        save_bank_data(bank_data)
                        await message.reply_text(f'تهانينا! لقد ربحت {win_amount} دولار')
                    else:
                        await message.reply_text('للأسف، لم تربح أي شيء')
                    update_luck_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: حظ + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["اضف"], "") & filters.create(is_sudoer), group=46468)
async def add_mhzboney(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        args = message.text.split(" ")
        if len(args) == 2 and args[1].isdigit():
            amount = int(args[1])
            bank_data = load_bank_data()
            if 'accounts' not in bank_data:
                bank_data['accounts'] = {}
            if str(user_id) in bank_data['accounts']:
                bank_data['accounts'][str(user_id)]['balance'] += amount
            else:
                bank_data['accounts'][str(user_id)] = {'balance': amount}
            save_bank_data(bank_data)
            await message.reply_text(f'تمت إضافة {amount} فلوس للمستخدم {user_id}')
        else:
            await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: اضف + المبلغ')
##############££££££££££#############££££££££££#########££££
@Client.on_message(filters.command(["حذف حسابه"], "") & filters.create(is_sudoer), group=5)
async def delete_account(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            del bank_data['accounts'][str(user_id)]
            save_bank_data(bank_data)
            await message.reply_text(f'تم حذف حساب المستخدم {user_id}')
        else:
            await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على شخص لحذف حسابه')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["حذف حسابي"], ""), group=6)
async def delete_my_account(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        del bank_data['accounts'][str(user_id)]
        save_bank_data(bank_data)
        await message.reply_text(f'تم حذف حسابك البنكي')
    else:
        await message.reply_text('لا تمتلك حسابًا بنكيًا')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["تصفير البنك"], "") & filters.create(is_sudoer), group=7)
async def reset_bank(client, message):
    bank_data = {'accounts': {}}
    save_bank_data(bank_data)
    await message.reply_text('تم مسح جميع حسابات البنك')  
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["فتح البنك"], "") & filters.create(is_sudoer), group=8)
async def enable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        await client.send_message(chat_id, 'لعبة البنك مفعلة بالفعل في المجموعة')
    else:
        bank_data['game_enabled'] = True
        save_bank_data(bank_data)
        await client.send_message(chat_id, 'تم تفعيل لعبة البنك في المجموعة')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["قفل البنك"], "") & filters.create(is_sudoer), group=9)
async def disable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        del bank_data['game_enabled']
        save_bank_data(bank_data)
        await client.send_message(chat_id, 'تم إيقاف لعبة البنك في المجموعة')
    else:
        await client.send_message(chat_id, 'لعبة البنك معطلة بالفعل في المجموعة')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["انشاء", "انشاء حساب بنكي"], ""), group=7536566)
async def create_account(client, message):
    user_id = message.from_user.id
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{photosource}"   
    username = message.from_user.username
    bank_data = load_bank_data()
    account_number = random.randint(100000000000000, 999999999999999)
    if 'accounts' not in bank_data:
        bank_data['accounts'] = {}
    if str(user_id) in bank_data['accounts']:
        await message.reply_text('لديك بالفعل حساب بنكي')
    else:
        bank_data['accounts'][str(user_id)] = {
            'username': username,
            'balance': 50,
            'account_number': account_number,
            'thief': 0
        }
        save_bank_data(bank_data)
        await message.reply_photo(
            photo=f"{ff}",
            caption=f"↤︎ تم إنشاء حساب بنكي بنجاح\n↤︎ اكتب بنكي لترى حسابك 😇\n↤︎ نوع البنك : بنك راضي\n↤︎ رقم حسابك {account_number}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ",
                            url=f"{soesh}"
                        ),
                    ],
                ]
            ),
        )
        
@Client.on_message(filters.command(["فلوسي"], ""), group=11)
async def check_balance(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    accounts = bank_data.get('accounts', {})
    if str(user_id) in accounts:
        balance = accounts[str(user_id)]['balance']
        await message.reply_text(f'رصيدك الحالي هو: {balance} دولار')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["فلوسه"], ""), group=12)
async def check_user_balance(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            balance = bank_data['accounts'][str(user_id)]['balance']
            await message.reply_text(f'رصيد {reply.from_user.username} هو: {balance} دولار')
        else:
            await message.reply_text(f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على رسالة المستخدم للحصول على معلومات الحساب')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["حسابي"], ""), group=13)
async def view_account(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        username = bank_data['accounts'][str(user_id)]['username']
        balance = bank_data['accounts'][str(user_id)]['balance']
        account_number = bank_data['accounts'][str(user_id)]['account_number']
        await message.reply_text(f'حسابك البنكي:\nالمستخدم: @{username}\nالرصيد: {balance} دولار\nرقم الحساب : {account_number}')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["بنكه"], ""), group=14)
async def view_user_account(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            username = bank_data['accounts'][str(user_id)]['username']
            balance = bank_data['accounts'][str(user_id)]['balance']
            account_number = bank_data['accounts'][str(user_id)]['account_number']
            await message.reply_text(f'حساب {reply.from_user.username} البنكي:\nالمستخدم: {username}\nالرصيد: {balance} دولار\nرقم حسابه : {account_number}')
        else:
            await message.reply_text(f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على رسالة المستخدم لعرض حسابه البنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_operation_times = {}

def get_operation_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_operation_times:
        last_operation_time = last_operation_times[user_id]
        elapsed_time = current_time - last_operation_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_operation_time(user_id):
    last_operation_times[user_id] = int(time.time())

@Client.on_message(filters.command(["مضاربه", "مضاربة"], ""), group=15) 
async def multiply(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_operation_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    multiplier = random.randint(2, 5)
                    result_amount = amount * multiplier
                    bank_data['accounts'][str(user_id)]['balance'] += result_amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تهانينا! لقد قمت بالمضاعفة وحصلت على {result_amount} دولار')
                    update_operation_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: مضاعفة + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_bribe_times = {}

def get_bribe_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_bribe_times:
        last_bribe_time = last_bribe_times[user_id]
        elapsed_time = current_time - last_bribe_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_bribe_time(user_id):
    last_bribe_times[user_id] = int(time.time())

@Client.on_message(filters.command(["رشوة", "رشوه"], ""), group=16)
async def bribe_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_bribe_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 1:
                amount = random.randint(300, 4000)
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('الرجاء الرد على رسالة لإرسال الرشوة')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('لا يمكنك إرسال رشوة لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تمت عملية الرشوة بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_bribe_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: رشوة')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200

last_wheel_times = {}

def get_wheel_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_wheel_times:
        last_wheel_time = last_wheel_times[user_id]
        elapsed_time = current_time - last_wheel_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_wheel_time(user_id):
    last_wheel_times[user_id] = int(time.time())

@Client.on_message(filters.command(["عجلة الحظ", "عجله الحظ"], ""), group=17)
async def wheel_of_fortune(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_wheel_remaining_time(user_id)
        if remaining_time <= 0:
            win_amount = random.randint(100, 5000)
            bank_data['accounts'][str(user_id)]['balance'] += win_amount
            save_bank_data(bank_data)
            if win_amount > 0:
                await message.reply_text(f'تهانينا! لقد فزت بمبلغ {win_amount} دولار في عجلة الحظ')
            else:
                await message.reply_text('عذرًا، لم تفز بأي مبلغ في عجلة الحظ هذه المرة')
            update_wheel_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_tip_times = {}

def get_custom_tip_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_tip_times:
        last_tip_time = last_tip_times[user_id]
        elapsed_time = current_time - last_tip_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
    
def update_custom_tip_time(user_id):
    last_tip_times[user_id] = int(time.time())

@Client.on_message(filters.command(["بقشيش"], ""), group=18)
async def custom_tip_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_custom_tip_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('الرجاء الرد على رسالة لإرسال البقشيش')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('لا يمكنك إرسال بقشيش لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تمت عملية البقشيش بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_custom_tip_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: بقشيش + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
SALARY_COOLDOWN = 1200  

last_salary_times = {}

def get_salary_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_salary_times:
        last_salary_time = last_salary_times[user_id]
        elapsed_time = current_time - last_salary_time
        remaining_time = SALARY_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_salary_time(user_id):
    last_salary_times[user_id] = int(time.time())

@Client.on_message(filters.command(["راتب"], ""), group=19)
async def salary(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_salary_remaining_time(user_id)
        if remaining_time <= 0:
            salary_amount = 3500
            bank_data['accounts'][str(user_id)]['balance'] += salary_amount
            save_bank_data(bank_data)
            await message.reply_text(f'تم صرف راتبك الشهري بمبلغ {salary_amount} دولار')
            update_salary_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
STEAL_COOLDOWN = 1200  
POLICE_COOLDOWN = 1200  

last_steal_times = {}
last_police_times = {}
last_protection_times = {}

def get_steal_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_steal_times:
        last_steal_time = last_steal_times[user_id]
        elapsed_time = current_time - last_steal_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def get_police_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_police_times:
        last_police_time = last_police_times[user_id]
        elapsed_time = current_time - last_police_time
        remaining_time = POLICE_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def get_protection_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_protection_times:
        last_protection_time = last_protection_times[user_id]
        elapsed_time = current_time - last_protection_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_steal_time(user_id):
    last_steal_times[user_id] = int(time.time())
def update_police_time(user_id):
    last_police_times[user_id] = int(time.time())
def update_protection_time(user_id):
    last_protection_times[user_id] = int(time.time())

@Client.on_message(filters.command(["سرقة", "سرقه"], ""), group=20640)
async def steal_mo55ney(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_steal_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('لا يمكنك سرقة نفسك!')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(target_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] += stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(user_id)]['thief'] += stolen_amount
                        save_bank_data(bank_data)
                        update_steal_time(user_id)
                        await message.reply_text(f'تمت عملية السرقة بنجاح! تم سرقة {stolen_amount} دولار من المستخدم')
                    else:
                        await message.reply_text('لا يمكنك سرقته لانه فقير')
            else:
                await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@Client.on_message(filters.command(["شرطة", "شرطه"], ""), group=21)
async def police_usehcr(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_police_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('لا يمكنك استخدام الأمر على نفسك!')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(user_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] += stolen_amount
                        save_bank_data(bank_data)
                        update_police_time(user_id)
                        await message.reply_text(f'تمت عملية القبض على المستخدم! تم خصم {stolen_amount} دولار من حسابك')
                    else:
                        await message.reply_text('رصيدك الحالي غير كافي للقبض على المستخدم')
            else:
                await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@Client.on_message(filters.command(["حماية", "حمايه"], ""), group=22)
async def protect_money(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_protection_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            protection_amount = random.randint(10, 50)
            if protection_amount <= bank_data['accounts'][str(user_id)]['balance']:
                bank_data['accounts'][str(user_id)]['balance'] -= protection_amount
                save_bank_data(bank_data)
                update_protection_time(user_id)
                await message.reply_text(f'تم تنفيذ عملية حماية الأموال بنجاح! تم خصم {protection_amount} دولار من حسابك')
            else:
                await message.reply_text('رصيدك الحالي غير كافي لحماية الأموال')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@Client.on_message(filters.command(["توب الحراميه", "توب سرقه", "توب السرقة", "توب السرقه", "توب سرقة"], ""), group=22)
async def top_thieves(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['thief'], reverse=True)
    top_thieves = sorted_accounts[:5]  
    response = "أعلى الحرامية في البنك:\n\n"    
    for thief_id in top_thieves:
        thief_username = await client.get_chat(int(thief_id)).username
        thief_balance = bank_data['accounts'][thief_id]['thief']
        response += f"@{thief_username}: {thief_balance} دولار\n"
    await message.reply_text(response)
##############££££££££££#############££££££££££#########££££#
@Client.on_message(filters.command(["توب فلوس","توب الفلوس"], ""), group=20543)
async def top_m659oney(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['balance'], reverse=True)
    top_accounts = sorted_accounts[:5]  
    response = "أعلى الأموال في البنك:\n\n"
    for account_id in top_accounts:
        account_username = await client.get_chat(account_id).username
        account_balance = bank_data['accounts'][account_id]['balance']
        response += f"@{account_username}: {account_balance} دولار\n"
    
    await message.reply_text(response)
    
@Client.on_message(filters.command(["البنك","بنك راضي","❤️‍🔥بنك راضي", "بنك"], ""), group=73)
async def mmmezat(client, message):
        bot_username = client.me.username
        soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم لعبة بنك راضي\n
[⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺]({soesh})\n

🏦 اوامر لعبه البنك ⇊

👮‍♂️ « المطور » ⇊
⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺\n
➕╖ `اضف فلوس` + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ `حذف حسابه` «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ `حذف حساب` + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ `تصفير البنك` «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺\n
📑╖ `انشاء` «» فتح حساب بنكي
🤑╢ `فلوسي` «» اموالي
💸╢ `فلوسه` «» امواله ❬ بالرد علي الشخص ❭
🏦╢ `بنكي` «» حسابي
💰╢ `بنكه` «» حسابه ❬ بالرد علي الشخص ❭
♻️╢ `تحويل` + المبلغ
☠️╢ `كنز`
🤖╢ `استثمار` + المبلغ
🍃╢ `حظ` + المبلغ
⏫╢ `مضاعفه` «» `مضاربه` + المبلغ
🎯╢ `عجله الحظ`
🤞╢ `رشوه`
🥺╢ `بقشيش`
⏳╢ `راتب`
📎╢ `سرقه` «» `اسرق` ❬ بالرد علي الشخص ❭
🚔╢ `شرطه` «» `شرطة` ❬ بالرد علي الشخص ❭
⭐️╢ `حمايه اموالي` «» ❬ لحمايه اموالك من السرقه ❭
👮╢ شرطه + اليوزر
💂‍♀️╢ `توب الحراميه` «» `توب السرقه`
⤴️╜ `توب الفلوس` «» `توب فلوس`


[⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺]({soesh})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ ⌝⚡", url=f"{soesh}"),                        
                 ],[
                    InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
           ]
        ),
    )   
#............................................ البنك ...........................................................................    
#............................................ الساعه ...........................................................................    
@Client.on_message(filters.command(["الساعه","الوقت","ساعه", "التاريخ"], ""), group=76763)
async def hossam(client, message):
    cairo_tz = pytz.timezone("Africa/Cairo")
    now = datetime.now(cairo_tz) 
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d") 
    await message.reply_text(f"الساعة الحالية: {current_time}\nتاريخ اليوم: {current_date}")
#............................................ الساعه ...........................................................................        
#............................................ حجرة........................................................................... 
game_state = {}

options = ["حجرة", "ورقة", "مقص"]

def get_winner(chat_id):
    player1_choice = game_state[chat_id]["player1"]["choice"]
    player2_choice = game_state[chat_id]["player2"]["choice"]
    player1_name = game_state[chat_id]["player1"]["name"]
    player2_name = game_state[chat_id]["player2"]["name"]
    
    if player1_choice == player2_choice:
        return "تعادل"
    elif (player1_choice == "حجرة" and player2_choice == "مقص") or (player1_choice == "ورقة" and player2_choice == "حجرة") or (player1_choice == "مقص" and player2_choice == "ورقة"):
        game_state[chat_id]["player1"]["score"] += 1
        return f"{player1_name}"
    else:
        game_state[chat_id]["player2"]["score"] += 1
        return f"{player2_name}"

@Client.on_message(filters.command(["حجرة"], ""), group=589)
async def stahxrt(client, message):
    if message.chat.id not in game_state:
        bot_username = client.me.username
        soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
        game_state[message.chat.id] = {
            "player1": {
                "name": message.from_user.first_name,
                "choice": None,
                "score": 0
            },
            "player2": {
                "name": None,
                "choice": None,
                "score": 0
            }
        }
        await message.reply(
            f"{game_state[message.chat.id]['player1']['name']} بدأ لعبة حجرة ورقة مقص.\n\nانتظر اللاعب الثاني...",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اضغط للعب", callback_data="join")],
                    [InlineKeyboardButton("⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺", url=f"{soesh}")]
                ]
            )
        )
    else:
        await message.reply_text("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")
        
@Client.on_callback_query(filters.regex("join"), group=58957)
async def joinhf(client, callback_query):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if callback_query.message.chat.id in game_state:
        if callback_query.from_user.first_name != game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player2"]["name"] = callback_query.from_user.first_name
            await callback_query.message.edit(
                f"{game_state[callback_query.message.chat.id]['player1']['name']} و {game_state[callback_query.message.chat.id]['player2']['name']} يلعبان حجرة ورقة مقص.\n\n👨‍💼 دور اللاعب: {game_state[callback_query.message.chat.id]['player1']['name']}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],[
                         InlineKeyboardButton("⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺", url=f"{soesh}")
                         ]
                    ]
                )
            )
        else:
            await callback_query.answer("انت منضم للعبه بالفعل", show_alert=True)
    else:
        await callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)

@Client.on_callback_query(filters.regex("^(حجرة|ورقة|مقص)$"), group=58965)
async def choovcse(client, callback_query):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if callback_query.message.chat.id in game_state:
        user_choice = callback_query.data
        bot_choice = choice(options)
        user_name = callback_query.from_user.first_name
        bot_name = client.me.first_name

        if user_name == game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player1"]["choice"] = user_choice
            await callback_query.message.edit(
                f"👨‍💼 اللاعب الأول: {game_state[callback_query.message.chat.id]['player1']['name']} لقد لعب \n\n👨‍💼 اللاعب الثاني: {game_state[callback_query.message.chat.id]['player2']['name']} اختر الآن...",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("⩹━★⊷⌯ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ⌯⊶★━⩺", url=f"{soesh}")]
                    ]
                )
            )
        elif user_name == game_state[callback_query.message.chat.id]["player2"]["name"]:
            if game_state[callback_query.message.chat.id]["player1"]["choice"] is None:
                await callback_query.answer("لا يمكنك اللعب حتى يلعب اللاعب الأول.", show_alert=True)
            else:
                game_state[callback_query.message.chat.id]["player2"]["choice"] = user_choice
                winner = get_winner(callback_query.message.chat.id)
                name_player1 = game_state[callback_query.message.chat.id]['player1']['name']
                name_player2 = game_state[callback_query.message.chat.id]['player2']['name']
                choice_player1 = game_state[callback_query.message.chat.id]['player1']['choice']
                choice_player2 = game_state[callback_query.message.chat.id]['player2']['choice']
                player1_score = game_state[callback_query.message.chat.id]['player1']['score']
                player2_score = game_state[callback_query.message.chat.id]['player2']['score']
                await callback_query.message.edit(
                    f"⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player1}\n\n❓ الإختيار : {choice_player1}\n\n🛒 النقاط : {player1_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player2}\n\n❓ الإختيار : {choice_player2}\n\n🛒 النقاط : {player2_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n🕺 اللاعب الفائز هو ⤵️ \n\n{winner}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯"
                )
                del game_state[callback_query.message.chat.id]
        else:
            await callback_query.answer("أنت لست جزء من هذه اللعبة.", show_alert=True)
    else:
        await callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)          
#............................................ حجرة...........................................................................         
#............................................ الردود ........................................................................... 
HOSSAm = {}

@Client.on_message(filters.regex("حذف رد"), group=55552)
async def delete_reply(client, message):
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
      chat_id = message.chat.id
      await message.reply_text("ادخل احذف الرد في البوت")
      try:
        ask = await client.ask(message.from_user.id, "أرسل اسم الرد الذي تريد حذفه", timeout=500)
        reply_name = ask.text
        if group_id not in HOSSAm:
            HOSSAm[group_id] = {}
        if reply_name in HOSSAm[group_id]:
            del HOSSAm[group_id][reply_name]
            await message.reply_text("تم حذف الرد بنجاح ✅♥")
        else:
            await message.reply_text("الرد غير موجود ✅♥")
      except Exception as e:
         await message.reply_text("ادخل البوت دوس /start وارجع اكتب اضف رد")            
    else:
        return await message.reply_text("عذرًا، هذا الأمر يُخص المشرفين")
        
@Client.on_message(filters.regex("اضف رد"), group=55552)
async def areply(client, message):
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in devmk:
      chat_id = message.chat.id
      await message.reply_text("ادخل ضيف الرد في البوت")
      try: 
        ask = await client.ask(message.from_user.id, "أرسل اسم الرد الجديد", timeout=500)
        reply_name = ask.text
        ask = await client.ask(message.from_user.id, "تم حفظ اسم الرد، الآن أرسل الرد", timeout=200)
        if ask.text:
          vvvv = ask.text
        elif ask.video:
          video = await client.download_media(ask.video)
          vvvv = video
        if group_id not in HOSSAm:
            HOSSAm[group_id] = {}
        HOSSAm[group_id][reply_name] = vvvv
        await message.reply_text("تم حفظ الرد بنجاح ✅♥")
      except Exception as e:
        await message.reply_text("ادخل البوت دوس /start وارجع اكتب اضف رد")
    else:
        await message.reply_text("عذرًا، هذا الأمر يُخص المالك والمشرفين فقط ✅♥")

@Client.on_message(filters.text & filters.group, group=57854)
async def ry_user(client, message):
    group_id = message.chat.id
    reply_name = None
    if group_id in HOSSAm:
        for user_reply_name in HOSSAm[group_id]:
            if user_reply_name in message.text:
                reply_name = user_reply_name
                break
    if reply_name:
        vvvv = HOSSAm[group_id][reply_name]
        try:
            await message.reply_video(vvvv)   
        except Exception as e:
            await message.reply_text(vvvv)
#............................................ الردود ........................................................................... 
#............................................ الترحيب ........................................................................... 
trhib = []

@Client.on_chat_member_updated(filters.group, group=57815550)
async def tr1hib(client, chat_member_updated):
    if chat_member_updated.new_chat_member and chat_member_updated.new_chat_member.status == ChatMemberStatus.MEMBER:
        group_id = chat_member_updated.chat.id
        user = chat_member_updated.new_chat_member.user
        user_mention = user.mention()
        if chat_member_updated.old_chat_member is None or chat_member_updated.old_chat_member.status == ChatMemberStatus.LEFT:
            if group_id in trhib:
                return  # لا ترسل رسالة الترحيب إذا كانت الردود مغلقة
            await client.send_message(chat_id=group_id, text=f"• نورتنا يا {user_mention}\n ❬ ممنوع الألفاظ والبرايفت واللينكات ❭ ⚠️\n❬ غير كدة كلنا أخوات وأصحاب ❭ ❤️ √")

@Client.on_message(filters.command(["قفل الترحيب", "تعطيل الترحيب"], "") & filters.group, group=763731243) 
async def tr2hib(client, message):
    bot_username = client.me.username    
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
        return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if message.chat.id in trhib:
            return await message.reply_text("تم معطل من قبل🔒")
        trhib.append(message.chat.id)
        return await message.reply_text("تم تعطيل الترحيب بنجاح ✅🔒")
    else:
        return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@Client.on_message(filters.command(["فتح الترحيب", "تفعيل الترحيب"], "") & filters.group, group=70612833) 
async def tr3hib(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
        return
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in caes:
        if not message.chat.id in trhib:
            return await message.reply_text("الترحيب مفعل من قبل ✅")
        trhib.remove(message.chat.id)
        return await message.reply_text("تم فتح الترحيب بنجاح ✅🔓")
    else:
        return await message.reply_text(f"عزرا عزيزي {message.from_user.mention}\n هذا الامر لا يخصك✨♥")
#............................................ الترحيب ...........................................................................         