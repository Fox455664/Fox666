import os
import re
import asyncio
import random
from typing import Union
import aiohttp
import aiofiles
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from unidecode import unidecode
import yt_dlp
from youtube_search import YoutubeSearch
from youtubesearchpython.__future__ import VideosSearch

from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import StreamAudioEnded
from pytgcalls.types.stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream.quality import HighQualityAudio, MediumQualityVideo

# --- Local Imports ---
from config import user, dev, call, logger, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger, del_userbot, del_call
from CASERr.CASERr import devchannel, source, caes, devgroup, devuser, group, casery, johned, photosource, muusiic, suorce


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""
    for i in list:
        if len(text1) + len(i) < 30:
            text1 += " " + i
        elif len(text2) + len(i) < 30:
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()
    return [text1, text2]


async def gen_bot_caesar(client, bot_username, OWNER_ID, CASER, message, videoid):
    if os.path.isfile(f"photos/{videoid}_{bot_username}.jpg"):
        return f"photos/{videoid}_{bot_username}.jpg"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub(r"\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()                    
        youtube = Image.open(f"thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        image2 = background   
        wxyz = await client.get_chat(OWNER_ID)
        CAR = wxyz.username
        vvv = wxyz.photo.big_file_id
        wxy = await client.download_media(vvv)
        yoube = Image.open(wxy)
        imge1 = changeImageSize(1280, 720, yoube)
        imge2 = imge1.convert("RGBA")
        imge3 = imge1.crop((280, 0, 1000, 720))
        lum_img = Image.new("L", [720, 720], 0)
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
        img_arr = np.array(imge3)
        lum_img_arr = np.array(lum_img)
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        imge3 = Image.fromarray(final_img_arr)
        imge3 = imge3.resize((450, 450))
        image2.paste(imge3, (50, 150), imge3)
        
        wxz = await client.get_chat(bot_username)
        CA1R = wxz.username
        bot_id = wxz.id
        vvv5 = wxz.photo.big_file_id
        wx6y = await client.download_media(vvv5)
        yo5ube = Image.open(wx6y)
        im2ge1 = changeImageSize(1280, 720, yo5ube)
        im2ge2 = im2ge1.convert("RGBA")
        im2ge3 = im2ge1.crop((280, 0, 1000, 720))
        lum_i2mg = Image.new("L", [720, 720], 0)
        draw = ImageDraw.Draw(lum_i2mg)
        draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
        img2_arr = np.array(im2ge3)
        lum2_img_arr = np.array(lum_i2mg)
        final2_img_arr = np.dstack((img2_arr, lum2_img_arr))
        im2ge3 = Image.fromarray(final2_img_arr)
        im2ge3 = im2ge3.resize((270, 270))
        image2.paste(im2ge3, (515, 250), im2ge3)
        
        image3 = image1.crop((280, 0, 1000, 720))
        lumimg = Image.new("L", [720, 720], 0)
        draw = ImageDraw.Draw(lumimg)
        draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
        img_arr = np.array(image3)
        lum_img_arr = np.array(lumimg)
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        image3 = Image.fromarray(final_img_arr)
        image3 = image3.resize((450, 450))
        image2.paste(image3, (800, 150), mask=image3)
        font1 = ImageFont.truetype("font.ttf", 30)
        font2 = ImageFont.truetype("font.ttf", 70)
        font3 = ImageFont.truetype("font.ttf", 35)
        font4 = ImageFont.truetype("font.ttf", 50)
        image4 = ImageDraw.Draw(image2)
        image4.text((350, 10), f"{suorce}", fill="white", font=font2, stroke_width=2, stroke_fill="white", align="left")
        image4.text((470, 645), f"{muusiic}", fill="white", font=font4, stroke_width=2, stroke_fill="white", align="left")
        title1 = truncate(title)
        image4.text((130, 610), f"UsEr: @{CAR}", (255, 255, 255), font=font3)
        image4.text((130, 650), f"ID: {OWNER_ID}", (255, 255, 255), font=font3)
        image4.text((920, 610), f"ViEwS: {views}", (255, 255, 255), font=font3)
        image4.text((400, 100), text=title1[0], fill="white", stroke_width=1, stroke_fill="white", font=font3, align="left")
        image2 = ImageOps.expand(image2, border=20, fill=make_col())
        image2 = image2.convert("RGB")
        image2.save(f"photos/{videoid}_{bot_username}.jpg")
        os.remove(f"thumb{videoid}.png")
        file = f"photos/{videoid}_{bot_username}.jpg"
        return file
    except Exception as e:
        print(e)

        
playlist = {}
hossamm = []
vidd = {}
namecha = {}
user_mentio = {}
thu = {}
phot = {}

@Client.on_message(filters.command(["مرر"], ""), group=545148)
async def sp1853552(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
        return
    if await johned(client, message):
        return
    bot_username = client.me.username
    user = await get_userbot(bot_username) 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in caes:
        try:
            query = message.text.split(None, 1)[1].strip()
            duration_to_skip = int(query)
            if not hossamm:
                await message.reply_text("قائمة التشغيل فارغة.")
                return
            next_song = hossamm[0]
            chat_id = message.chat.id        
            ho = await message.reply_text("جاري تمرير التشغيل") 
            stream = (
                AudioPiped( 
                    next_song,
                    audio_parameters=HighQualityAudio(),
                    additional_ffmpeg_parameters=f"-ss {duration_to_skip}",
                )
            )
            await hoss.change_stream(chat_id, stream)
            await ho.edit_text(f"تم بنجاح تمرير {duration_to_skip} ثواني")
        except IndexError:
            await message.reply_text("يرجى تحديد المدة الصحيحة للتمرير.")
        except ValueError:
            await message.reply_text("يرجى إدخال رقم صحيح للمدة.")
        except Exception as e:
            print(e)
            await ho.edit_text("حدث خطأ أثناء تمرير التشغيل.")

@Client.on_message(filters.command(["مرر"], ""), group=54548)
async def sp853552(client, message):
    try:
        query = message.text.split(None, 1)[1].strip()
        duration_to_skip = int(query)
        if not hossamm:
            await message.reply_text("قائمة التشغيل فارغة.")
            return
        next_song = hossamm[0]
        bot_username = client.me.username
        hoss = await get_call(bot_username)
        userbot = await get_userbot(bot_username)
        chat_id = message.chat.id        
        ho = await message.reply_text("جاري تمرير التشغيل") 
        stream = (
            AudioVideoPiped(
                next_song,
                audio_parameters=HighQualityAudio(),
                video_parameters=MediumQualityVideo(),
                additional_ffmpeg_parameters=f"-ss {duration_to_skip}",
            )
        )
        await hoss.change_stream(chat_id, stream)
        await ho.edit_text(f"تم بنجاح تمرير {duration_to_skip} ثواني")
    except IndexError:
        await message.reply_text("يرجى تحديد المدة الصحيحة للتمرير.")
    except ValueError:
        await message.reply_text("يرجى إدخال رقم صحيح للمدة.")
    except Exception as e:
        print(e)
        await ho.edit_text("حدث خطأ أثناء تمرير التشغيل.")
       
async def join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, user_mention, photo, thum, namechat): 
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)    
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    usr = await client.get_chat(devus)
    user_id = usr.id
    CASER = usr.username
    name = usr.first_name
    Done = None
    file_path = audio_file
    audio_stream_quality = MediumQualityAudio()
    video_stream_quality = MediumQualityVideo()
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
        hossamm.append(file_path)
        Done = True
    except NoActiveGroupCall:
        h = await join_assistant(client, group_id, userbot)
        if h:
         try:
           await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
           hossamm.append(file_path)
           Done = True
         except Exception:
           buttoon = [[InlineKeyboardButton(text="تحديث ♻️", callback_data=f"reboott")]]
           await client.send_message(message.chat.id, "**حدث خطا اثناء التشغيل\nاضغط علي الزر بالاسفل لتحديث ♻️\nاو تاكد من تشغيل المكالمه الصوتيه**", reply_markup=InlineKeyboardMarkup(buttoon))
    except AlreadyJoinedError:
        if group_id not in playlist:
         playlist[group_id] = [] 
         vidd[group_id] = [] 
         namecha[group_id] = [] 
         user_mentio[group_id] = [] 
         thu[group_id] = [] 
         phot[group_id] = [] 
        if group_id not in playlist[group_id]:
         playlist[group_id].append(file_path)
         hossamm.append(file_path)
         vidd[group_id].append(vid)
         namecha[group_id].append(namechat)
         user_mentio[group_id].append(user_mention)
         thu[group_id].append(thum)
         phot[group_id].append(photo)
        if group_id in playlist:
         count = len(playlist[group_id])
        loggerlink = message.chat.username if message.chat.username else message.chat.title
        button = [[InlineKeyboardButton(text="◁", callback_data=f"resume"), InlineKeyboardButton(text="II", callback_data=f"pause"), InlineKeyboardButton(text="▢", callback_data=f"stop"), InlineKeyboardButton(text="▷▷", callback_data=f"skip")], [InlineKeyboardButton(text="𝗖𝗵𝗔𝗻𝗘𝗲𝗟", url=f"{soesh}"), InlineKeyboardButton(text="𝗚𝗿𝗢𝘂𝗣", url=f"{gr}")], [InlineKeyboardButton(text=f"{name}", url=f"https://t.me/{CASER}")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣", url=f"https://t.me/{bot_username}?startgroup=True")]]
        await client.send_photo(group_id, photo=photo, caption=f"**𝗔𝗱𝗗 𝗦𝗼𝗡𝗴 𝗧𝗼 𝗣𝗹𝗔𝘆 : {count}\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})**", reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.id)
    except Exception:
        await client.send_message(message.chat.id, "**حدث خطأ في الخادم...**")
    except Exception as e:
        print(e)    
    return Done
    
async def Call(bot_username):
    hoss = await get_call(bot_username)
    @hoss.on_stream_end()
    async def stream_end_handler1(client, update: Update):
        if not isinstance(update, StreamAudioEnded):
            return        
        await change_stream(bot_username, update.chat_id, client)

async def change_stream(bot_username, chat_id, client): 
    hoss = await get_call(bot_username)    
    OWNER_ID = await get_dev(bot_username)
    logger = await get_logger(bot_username)
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    apppp = appp[bot_username]
    usr = await apppp.get_chat(devus)
    user_id = usr.id
    CASER = usr.username
    name = usr.first_name

    if chat_id in playlist and playlist[chat_id] and vidd[chat_id] and namecha[chat_id] and user_mentio[chat_id] and thu[chat_id] and phot[chat_id]:
        next_song = playlist[chat_id].pop(0)
        vid = vidd[chat_id].pop(0)
        namechat = namecha[chat_id].pop(0)
        user_mention = user_mentio[chat_id].pop(0)
        thum = thu[chat_id].pop(0)
        photo = phot[chat_id].pop(0)

        try:
            chat_info = await apppp.get_chat(chat_id)
            loggerlink = chat_info.username if chat_info.username else chat_info.title

            audio_stream_quality = MediumQualityAudio()
            video_stream_quality = MediumQualityVideo()
            hossamm.clear()
            stream = AudioVideoPiped(next_song, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(next_song, audio_parameters=audio_stream_quality)
            await hoss.change_stream(chat_id, stream)
            hossamm.append(next_song)

            button = [[
                InlineKeyboardButton(text="◁", callback_data="resume"),
                InlineKeyboardButton(text="II", callback_data="pause"),
                InlineKeyboardButton(text="▢", callback_data="stop"),
                InlineKeyboardButton(text="▷▷", callback_data="skip")
            ], [
                InlineKeyboardButton(text="𝗖𝗵𝗔𝗻𝗘𝗲𝗟", url=soesh),
                InlineKeyboardButton(text="𝗚𝗿𝗢𝘂𝗣", url=gr)
            ], [
                InlineKeyboardButton(text=f"{name}", url=f"https://t.me/{CASER}")
            ], [
                InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣", url=f"https://t.me/{bot_username}?startgroup=True")
            ]]

            await apppp.send_photo(chat_id, photo=photo,
                caption=f"**𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})**",
                reply_markup=InlineKeyboardMarkup(button)
            )

            await apppp.send_message(logger,
                f"**╭── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╮\n\n"
                f"⌁ |𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n"
                f"⌁ |𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n"
                f"⌁ |𝗕𝘆 : {user_mention}\n"
                f"⌁ |𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})\n\n"
                f"╰── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╯**",
                disable_web_page_preview=True
            )
        except Exception as e:
            print(f"خطأ في change_stream: {e}")
    else:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception:
            print("مفيش حاجه شغاله اصلا")
