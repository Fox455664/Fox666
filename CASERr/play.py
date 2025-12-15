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
# تصحيح الاستيراد ليتوافق مع الإصدار 1.1.6
from pytgcalls.types import StreamAudioEnded, AudioPiped, AudioVideoPiped, HighQualityAudio, MediumQualityVideo

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

import glob
import os

async def download(client, bot_username, link, video: Union[bool, str] = None):
    loop = asyncio.get_running_loop()
    logger = await get_logger(bot_username)
    output_file = f"{bot_username}_{random.randint(1000, 9999)}.%(ext)s"

    cookies_path = "/root/cookies.txt"

    ydl_opts = {
        "format": "bestvideo+bestaudio/best" if video else "bestaudio/best",
        "outtmpl": output_file,
        "quiet": True,
        "nocheckcertificate": True,
        "cookiefile": cookies_path,
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if not video else []
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            await loop.run_in_executor(None, lambda: ydl.download([f"https://youtube.com{link}"]))
    except Exception as e:
        error_message = f"حدث خطأ أثناء التحميل: {e}"
        print(error_message)
        await client.send_message(logger, f"**فشل التحميل:**\n`{error_message}`")
        return None

    files = glob.glob(f"{bot_username}_*.mp3" if not video else f"{bot_username}_*.*")
    if not files:
        await client.send_message(logger, "**فشل تحميل الملف من يوتيوب. قد يكون الفيديو خاص أو به قيود.**")
        return None

    file_path = files[0]
    sent_msg = await client.send_audio(logger, file_path) if not video else await client.send_video(logger, file_path)
    downloaded_path = await sent_msg.download()

    try:
        os.remove(file_path)
    except Exception as e:
        print(f"خطأ أثناء حذف الملف: {e}")

    return downloaded_path

Music = {}

@Client.on_message(filters.command(["قفل الميوزك","ق ميوزك"], ""),group=18798)
async def abra245g(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    Music.setdefault(bot_username, []).append(bot_username)
    await message.reply_text(f"• تم قفل الميوزك بواسطه ↤︎「 {message.from_user.mention}")

@Client.on_message(filters.command(["فتح الميوزك","ف ميوزك"], ""),group=545177)
async def abr54ag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    Music[bot_username].remove(bot_username)
    await message.reply_text(f"• تم فتح الميوزك بواسطه ↤︎「 {message.from_user.mention}")

@Client.on_message(filters.command(["مين شغل","م شغل","مين مشغل"], ""), group=5880)
async def playingy(client, message):
        chat_id = message.chat.id
        bot_username = client.me.username
        if chat_id in playing and playing[chat_id]:
            for hos in playing[chat_id]:
                user = await client.get_users(hos)
                user_mention = user.mention()
                await message.reply_text(f"اخر واحد شغل اهو {user_mention}")
        else:
            await message.reply_text("لم يقم احد بتشغيل شيء بعد.")

playing = {}        

async def join_assistant(client, hoss_chat_user, user):
        join = None
        try:
            hos_info = await client.get_chat(hoss_chat_user)
            if hos_info.invite_link:
                hos_link = hos_info.invite_link
            else:
                await client.send_message(hoss_chat_user, "لا يمكن العثور على رابط الدعوة لهذه المجموعة/القناة\n قم برفعي مشرف في الجروب أولاً")
                return None
            await user.join_chat(str(hos_link))
            join = True
        except Exception as e:
            print(f"حدث خطأ أثناء الانضمام: {str(e)}")
        return join        
        
yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]

@Client.on_message(filters.command(["شغل", "تشغيل", "فيد", "فديو", "/vplay", "/play"], "") & filters.group, group=57655580)
async def msonhfbg(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
        return
    if await johned(client, message):
        return
    bot_username = client.me.username
    user = await get_userbot(bot_username) 
    hoss = await get_call(bot_username)
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    OWNER_ID = await get_dev(bot_username)
    logger = await get_logger(bot_username)
    usr = await client.get_chat(devus)
    CASER = usr.username
    name = usr.first_name
    group_id = message.chat.id
    try:
      playing.setdefault(group_id, []).clear()
    except Exception as e:
      print(f"حدث خطأ : {str(e)}")
    playing.setdefault(group_id, []).append(message.from_user.id)
    
    if message.reply_to_message:
        if "v" in message.command[0] or "ف" in message.command[0]:
            vid = True
        else:
            vid = None
        mhm = await message.reply_text("**جاري تحميل الريك او الفديو انتظر**")
        photo = photosource
        audio_file = await message.reply_to_message.download()
        thum = "ملف صوتي" if message.reply_to_message.audio else "ملف فيديو"
        namechat = f"{message.chat.title}"
        button = [[InlineKeyboardButton(text="◁", callback_data=f"resume"), InlineKeyboardButton(text="II", callback_data=f"pause"), InlineKeyboardButton(text="▢", callback_data=f"stop"), InlineKeyboardButton(text="▷▷", callback_data=f"skip")], [InlineKeyboardButton(text="𝗖𝗵𝗔𝗻𝗘𝗲𝗟", url=f"{soesh}"), InlineKeyboardButton(text="𝗚𝗿𝗢𝘂𝗣", url=f"{gr}")], [InlineKeyboardButton(text=f"{name}", url=f"https://t.me/{CASER}")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣", url=f"https://t.me/{bot_username}?startgroup=True")]]
        loggerlink = message.chat.username if message.chat.username else f"https://t.me/c/{str(message.chat.id).replace('-100', '')}"
        user_mention = f"{message.from_user.mention}" if message.from_user else f"{message.author_signature}"
        c = await join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, user_mention, photo, thum, namechat)
        await mhm.delete()
        os.remove(audio_file)
        if not c:
            return
        await client.send_photo(group_id, photo=photo, caption=f"**𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})**", reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.id)
        await client.send_message(logger, f"**╭── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╮\n\n⌁ |𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n⌁ |𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n⌁ |𝗕𝘆 : {user_mention}\n⌁ |𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})\n\n╰── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╯**", disable_web_page_preview=True)
        return

    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply_text("**الامر تشغيل + الاغنيه \n مثلا\nتشغيل بحبك وحشتيني**")  
    
    if text in yoro:
        return await message.reply_text("**لا يمكن تشغيل هذا**")  
    
    mm = await message.reply_text("**جاري التشغيل انتظر 🎵♥**")    
    try:
        results = VideosSearch(text, limit=1)
        res = (await results.next())["result"]
        if not res:
            await mm.delete()
            return await message.reply_text("**لم يتم العثور على نتائج.**")
        result = res[0]
        thum = result["title"]
        duration = result["duration"]
        videoid = result["id"]
        yturl = result["link"]
    except Exception as e:
        await mm.delete()
        return await message.reply_text(f"**حدث خطأ اثناء البحث: {e}**")
        
    if "v" in message.command[0] or "ف" in message.command[0]:
        vid = True
    else:
        vid = None
        
    try:
        search_results = YoutubeSearch(text, max_results=1).to_dict()
        if not search_results:
            await mm.delete()
            return await message.reply_text("**لم يتم العثور على نتائج.**")
        link = f"{search_results[0]['url_suffix']}"
    except Exception as e:
        await mm.delete()
        return await message.reply_text(f"**حدث خطأ اثناء البحث: {e}**")
        
    audio_file = await download(client, bot_username, link, vid)

    if not audio_file:
        await mm.delete()
        return await message.reply_text("**تعذر تحميل الأغنية. تأكد أن الرابط متاح أو جرّب اسم مختلف.**")

    photo = await gen_bot_caesar(client, bot_username, OWNER_ID, CASER, message, videoid)   
    namechat = f"{message.chat.title}"     
    button = [[
        InlineKeyboardButton(text="◁", callback_data=f"resume"),
        InlineKeyboardButton(text="II", callback_data=f"pause"),
        InlineKeyboardButton(text="▢", callback_data=f"stop"),
        InlineKeyboardButton(text="▷▷", callback_data=f"skip")
    ], [
        InlineKeyboardButton(text="𝗖𝗵𝗔𝗻𝗘𝗲𝗟", url=f"{soesh}"),
        InlineKeyboardButton(text="𝗚𝗿𝗢𝘂𝗣", url=f"{gr}")
    ], [
        InlineKeyboardButton(text=f"{name}", url=f"https://t.me/{CASER}")
    ], [
        InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣", url=f"https://t.me/{bot_username}?startgroup=True")
    ]]
    loggerlink = message.chat.username if message.chat.username else f"https://t.me/c/{str(message.chat.id).replace('-100', '')}"
    await mm.delete()
    user_mention = f"{message.from_user.mention}" if message.from_user else f"{message.author_signature}"

    c = await join_call(bot_username, OWNER_ID, client, message, audio_file, group_id, vid, user_mention, photo, thum, namechat)
    if not c:
        return

    await client.send_photo(group_id, photo=photo, caption=f"**𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})**", reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.id)
    await client.send_message(logger, f"**╭── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╮\n\n⌁ |𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n⌁ |𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : `{thum}`\n⌁ |𝗕𝘆 : {user_mention}\n⌁ |𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : [{namechat}]({loggerlink})\n\n╰── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╯**", disable_web_page_preview=True)
    
async def jaoin_call(bot_username, message, audio_file, group_id, vid, user_mention, thum, namechat):
    Done = None
    try:
     hoss = await get_call(bot_username)
    except:
     return Done
    file_path = audio_file
    audio_stream_quality = MediumQualityAudio()
    video_stream_quality = MediumQualityVideo()
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    try:
        await hoss.join_group_call(group_id, stream, stream_type=StreamType().pulse_stream)
        Done = True
    except NoActiveGroupCall:
        await client.send_message(message.chat.id, "**قم بتشغيل المكالمة أولاً..**")
    except AlreadyJoinedError:
        if group_id not in playlist:
         playlist[group_id] = [] 
         vidd[group_id] = [] 
         namecha[group_id] = [] 
         user_mentio[group_id] = [] 
         thu[group_id] = [] 
        if group_id not in playlist[group_id]:
         playlist[group_id].append(file_path)
         vidd[group_id].append(vid)
         namecha[group_id].append(namechat)
         user_mentio[group_id].append(user_mention)
         thu[group_id].append(thum)
        if group_id in playlist:
         count = len(playlist[group_id])
        await message.reply_text("تم الاضافه الي القائمه")         
    except Exception:
        await client.send_message(message.chat.id, "**حدث خطأ في الخادم...**")
    except Exception as e:
        print(e)    
    return Done
     
     
@Client.on_message(filters.command(["تشغيل","شغل"], "") & filters.private, group=227195)
async def emplhsmoyment(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    OWNER_ID = await get_dev(bot_username)
    if message.text:
            if "v" in message.command[0] or "g" in message.command[0]:
                vid = True
            else:
                vid = None
            nae = await client.ask(message.chat.id, "ارسل الان ايدي الجروب الذي ترغب في التشغيل إليه\n باستخدام كود الايدي-100 \nمثل \n-1001703621834")
            group = int(nae.text)    
            ask = await client.ask(message.chat.id, "ارسل الأغنية الآن")
            file_id = ask.audio
            try:
                audio_file = await client.download_media(file_id)
            except Exception as e:
                await client.send_message(group_id, f"حدث خطأ أثناء تحميل الملف: {e}") 
            thum = None
            namechat = f"{message.chat.title}"
            if message.from_user is not None:
                user_mention = f"{message.from_user.mention}"
            else: 
                user_mention = f"{message.author_signature}"
            c = await jaoin_call(bot_username, message, audio_file, group, vid, user_mention, thum, namechat)
            if not c:
                return
            await message.reply_text("تم التشغيل بنجاح")

@Client.on_message(filters.command(["فيديو","فيد"], "") & filters.private, group=262816)
async def emywgplvoyment(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    OWNER_ID = await get_dev(bot_username)
    if message.text:
            if "v" in message.command[0] or "ف" in message.command[0]:
                vid = True
            else:
                vid = None
            nae = await client.ask(message.chat.id, "ارسل الان ايدي الجروب الذي ترغب في التشغيل إليه\n باستخدام كود الايدي-100 \nمثل \n-1001703621834")
            group = int(nae.text)
            ask = await client.ask(message.chat.id, "ارسل الفيديو الآن")
            file_id = ask.video
            try:
                audio_file = await client.download_media(file_id)
            except Exception as e:
                await client.send_message(group_id, f"حدث خطأ أثناء تحميل الملف: {e}")
            thum = None
            namechat = f"{message.chat.title}"
            if message.from_user is not None:
                user_mention = f"{message.from_user.mention}"
            else: 
                user_mention = f"{message.author_signature}"
            c = await jaoin_call(bot_username, message, audio_file, group, vid, user_mention, thum, namechat)
            if not c:
                return
            await message.reply_text("تم التشغيل بنجاح")

@Client.on_message(filters.command(["تحكم","التحكم"], ""), group=9736055)
async def gers(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    bot_username = client.me.username 
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    global thu
    o = 1
    button = [[InlineKeyboardButton(text="◁", callback_data=f"resume"), InlineKeyboardButton(text="II", callback_data=f"pause"), InlineKeyboardButton(text="▢", callback_data=f"stop"), InlineKeyboardButton(text="▷▷", callback_data=f"skip")]]
    group_id = message.chat.id
    if group_id in thu:
        count = len(thu[group_id])
        user_mentions = [str(user) for user in thu[group_id]]
        response = f"**╭── : [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh}) : ──╮\n\n⌁|𝗧𝗵𝗘 𝗦𝗼𝗡𝗴𝗦 𝗢𝗻 𝗧𝗵𝗘 𝗟𝗶𝗦𝘁:\n\n⌁|𝗡𝘂𝗠𝗯𝗘𝗿 𝗦𝗼𝗡𝗴𝗦: {count}\n\n**"
        if count == 0:
            return await message.reply_text("**مفيش اغاني في القائمه**")
        else:
            for user_mention in user_mentions:
                response += f"**{o}- {user_mention}\n**"
                o += 1
        await message.reply_text(response, reply_markup=InlineKeyboardMarkup(button), reply_to_message_id=message.id, disable_web_page_preview=True)
    else:
        await message.reply_text("**مفيش اغاني في القائمه**")
        
@Client.on_callback_query(filters.regex(pattern=r"^(pause|skip|stop|resume)$"))
async def admin_risghts(client: Client, CallbackQuery):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "pause":
        try:
         await hoss.pause_stream(chat_id)
         await CallbackQuery.answer("تم ايقاف التشغيل موقتا .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم ايقاف التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "resume":
        try:
         await hoss.resume_stream(chat_id)
         await CallbackQuery.answer("تم استكمال التشغيل .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم إستكمال التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "stop":
       try:    	
        playlist[chat_id].clear()
        thu[chat_id].clear()
        hossamm.clear()
       except Exception as e:
        print(f"{e}")
       try:    	
        await hoss.leave_group_call(chat_id)
       except Exception as e:
        print(f"{e}")
       await CallbackQuery.answer("تم انهاء التشغيل بنجاح .", show_alert=True)
       await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم انهاء التشغيل بواسطه**")
    if command == "skip":
       await change_stream(bot_username, chat_id, client)
       await CallbackQuery.answer("تم تخطي التشغيل .", show_alert=True)
       
@Client.on_message(filters.command(["اسكت", "ايقاف", "/stop", "انهاء"], "") & filters.group, group=55646568548)
async def ghuser(client, message):
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
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري ايقاف التشغيل**") 
     try:    	
      playlist[chat_id].clear()
      thu[chat_id].clear()
      hossamm.clear()
     except Exception as e:
      print(f"{e}")
     try:    	
      await hoss.leave_group_call(message.chat.id)
      await ho.edit_text("**حاضر سكت اهو 🥺**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")    
    else:
      return await message.reply_text(f"**عذرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥**")

@Client.on_message(filters.command(["اسكت", "ايقاف", "/stop", "انهاء","stop"], "") & filters.channel, group=5564656568548)
async def gh24user(client, message):
     hhs = client.me.username
     if hhs in Music.get(hhs, []):
      return
     bot_username = client.me.username
     user = await get_userbot(bot_username)  
     hoss = await get_call(bot_username)
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري ايقاف التشغيل**") 
     try:    	
      playlist[chat_id].clear()
      thu[chat_id].clear()
      hossamm.clear()
     except Exception as e:
      print(f"{e}")
     try:    	
      await hoss.leave_group_call(message.chat.id)
      await ho.edit_text("**حاضر سكت اهو 🥺**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")    

@Client.on_message(filters.command(["اسكت", "ايقاف", "/stop", "انهاء"], "") & filters.private, group=29)
async def stbop(client, message):
    group_id = message.chat.id
    chat_id = message.chat.id
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        nae = await client.ask(message.chat.id, "هات ايدي الجروب")
        group = int(nae.text)    
        ho = await message.reply_text("**جاري ايقاف التشغيل**") 
        try:
            await hoss.leave_group_call(group)
            await ho.edit_text("**تم ايقاف التشغيل بنجاح**")
        except Exception as e:
            await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
        await message.reply_text("هذا الامر للمطورين فقط")
 
@Client.on_message(filters.command(["تخطي", "/skip","تخطى"], "") & filters.group, group=5864548)
async def skip2(client, message):
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
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري تخطي التشغيل**") 
     await ho.delete()
     await change_stream(bot_username, chat_id, client)
    else:
     return await message.reply_text(f"**عذرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥**")

@Client.on_message(filters.command(["تخطي", "/skip","تخطى"], "") & filters.channel, group=5869864548)
async def ski25p2(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري تخطي التشغيل**") 
    await ho.delete()
    await change_stream(bot_username, chat_id, client)

@Client.on_message(filters.command(["تخطي", "/skip", "تخطى"], "") & filters.private, group=32)
async def skbip2(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        nae = await client.ask(message.chat.id, "هات ايدي الجروب")
        group = int(nae.text)    
        ho = await message.reply_text("**جاري تخطي التشغيل**") 
        await ho.delete()
        await change_stream(bot_username, group, client)
    else:
        await message.reply_text("هذا الامر للمطورين فقط")
    
@Client.on_message(filters.command(["توقف", "وقف","ايقاف مؤقت","ايقاف موقت"], "") & filters.group, group=58655654548)
async def sp2(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    if await johned(client, message):
     return
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in caes:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري توقف التشغيل**") 
     try:    	
      await hoss.pause_stream(chat_id)
      await ho.edit_text("**تم توقف التشغيل بنجاح**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
     return await message.reply_text(f"**عذرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥**")

@Client.on_message(filters.command(["توقف", "وقف","ايقاف مؤقت","ايقاف موقت"], "") & filters.channel, group=5866555654548)
async def s356p2(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري توقف التشغيل**") 
    try:    	
     await hoss.pause_stream(chat_id)
     await ho.edit_text("**تم توقف التشغيل بنجاح**")
    except Exception as e:
     await ho.edit_text("**مفيش حاجه شغاله اصلا**")
     
@Client.on_message(filters.command(["توقف", "وقف", "ايقاف مؤقت", "ايقاف موقت"], "") & filters.private, group=34)
async def hablt(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        nae = await client.ask(message.chat.id, "هات ايدي الجروب")
        group = int(nae.text)
        ho = await message.reply_text("**جاري توقف التشغيل**")
        try:
            await hoss.pause_stream(group)
            await ho.edit_text("**تم توقف التشغيل بنجاح**")
        except Exception as e:
            await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
        await message.reply_text("هذا الامر للمطورين فقط")
     
@Client.on_message(filters.command(["كمل","استكمال"], "") & filters.group, group=5866564548)
async def s12p2(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    if await johned(client, message):
     return
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in caes:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري استكمال التشغيل**") 
     try:    	
      await hoss.resume_stream(chat_id)
      await ho.edit_text("**تم استكمال التشغيل بنجاح**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
     return await message.reply_text(f"**عذرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥**")

@Client.on_message(filters.command(["كمل","استكمال"], "") & filters.channel, group=645866564548)
async def s12p582(client, message):
    hhs = client.me.username
    if hhs in Music.get(hhs, []):
     return
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري استكمال التشغيل**") 
    try:    	
     await hoss.resume_stream(chat_id)
     await ho.edit_text("**تم استكمال التشغيل بنجاح**")
    except Exception as e:
     await ho.edit_text("**مفيش حاجه شغاله اصلا**")
     
@Client.on_message(filters.command(["كمل", "استكمال"], "") & filters.private, group=36)
async def contbinue(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    OWNER_ID = await get_dev(bot_username)
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        nae = await client.ask(message.chat.id, "هات ايدي الجروب")
        group = int(nae.text)
        ho = await message.reply_text("**جاري استكمال التشغيل**")
        try:
            await hoss.resume_stream(group)
            await ho.edit_text("**تم استكمال التشغيل بنجاح**")
        except Exception as e:
            await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
        await message.reply_text("هذا الامر للمطورين فقط")
        
@Client.on_message(filters.command(["انضم"], ""), group=575580)
async def mson5454hfbg(client, message):
        hoss_chat_user = message.chat.id
        bot_username = client.me.username
        user = await get_userbot(bot_username) 
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          await message.reply("لا يمكن العثور على رابط الدعوة لهذه المجموعة/القناة\n قم برفعي مشرف في الجروب أولاً")
          return
        try:
          await user.join_chat(str(hos_link))
        except Exception as e:
          print(f"حدث خطأ أثناء الانضمام: {str(e)}")

@Client.on_message(filters.command(["/reboot"], ""), group=57557580)
async def mson5674hfbg(client, message):
        hoss_chat_user = message.chat.id
        bot_username = client.me.username
        h = await message.reply_text("جاري التحديث انتظر ♻️")
        await asyncio.sleep(5)
        try: 
          user = await del_userbot(bot_username) 
          call = await del_call(bot_username) 
          await Call(bot_username)
          await h.edit_text("تم التحديث بنجاح ♻️✅")
        except Exception as e:
          await message.reply_text("حدث خطا اثناء التحديث")
          
@Client.on_message(filters.command(["غادر"], ""), group=2257580)
async def mso2645fbg(client, message):
        hoss_chat_user = message.chat.id
        hoss_username = message.chat.username
        bot_username = client.me.username
        user = await get_userbot(bot_username) 
        chek = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.username in caes:                 
         try:
           await user.leave_chat(hoss_chat_user)
         except Exception as e:
           print(e)
         
@Client.on_callback_query(filters.regex(pattern=r"^(reboott)$"))
async def rebootthd(client: Client, CallbackQuery):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    await CallbackQuery.message.delete()
    if command == "reboott":
        try:
         h = await client.send_message(chat_id, "**جاري التحديث انتظر ♻️**")
         await asyncio.sleep(5)
         user = await del_userbot(bot_username) 
         call = await del_call(bot_username) 
         await Call(bot_username)
         await h.edit_text("**تم التحديث بنجاح ♻️✅**")
        except Exception as e:
         await client.send_message(chat_id, f"**حدث خطا اثناء التحديث**")
                  
@Client.on_message(filters.text & filters.group) 
async def leave_group(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user and (message.from_user.id == OWNER_ID or message.from_user.username in caes):
     if message.text == "اخروج": 
        await message.reply_text("سأغادر الآن 👋")

        await client.leave_chat(message.chat.id)
