import asyncio
import os
import random
import requests
import pytz
from datetime import datetime
from typing import Union
from requests import Session, Response

# مكتبات بايروجرام
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant

# مكتبات تشغيل الصوت
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import AudioPiped
from pytgcalls.exceptions import NoActiveGroupCall, AlreadyJoinedError

# تحويل النص لصوت
from gtts import gTTS

# استيراد ملفات الإعدادات (تم ترتيبها لحل مشاكل الاستيراد)
try:
    from config import *
    from config import user, dev, call, logger, logger_mode, botname, appp
    from CASERr.daty import get_call, get_userbot, get_dev, get_logger
    # تأكد أن هذه المتغيرات موجودة في ملف CASERr.py وإلا سيظهر الخطأ مرة أخرى
    from CASERr.CASERr import devchannel, source, caes, devgroup, devuser, group, casery, johned, photosource, caserid
except ImportError as e:
    print(f"تحذير: هناك مشكلة في استيراد بعض المتغيرات: {e}")

# ================= متغيرات عامة =================
cairo_timezone = pytz.timezone('Africa/Cairo')
zone = pytz.timezone("Africa/Cairo")
s = Session()

# قوائم التفعيل
azan_enabled_chats = []
azkar_ses = []     # أذكار صوتية
azkar_chat = []    # أذكار كتابة
nday_chattm = []   # نداء (منشن)

# ================= أوامر تحويل النص لصوت (TTS) =================
@Client.on_message(filters.command("قول", ""), group=730550)
async def speak(client, message: Message):
    chat_id = message.chat.id
    data = message.text.split(maxsplit=1)
    if len(data) < 2:
        return await message.reply_text("اقول اي؟")
    
    wait = await message.reply_text('استنى بقرأ اللي انت كاتبه..')
    
    text_to_speak = data[1]
    # تحديد اللغة
    if text_to_speak.isascii():
        language = 'en'
    else:
        language = 'ar'
        
    # استخدام ID المستخدم بدلاً من اليوزرنيم لتجنب الأخطاء
    filename = f"{message.from_user.id}_{random.randint(1000, 9999)}.mp3"
    
    try:
        audio = gTTS(text=text_to_speak, lang=language)
        audio.save(filename)
        
        with open(filename, "rb") as audio_file:
            await message.reply_voice(voice=audio_file)
        
        await wait.delete()
    except Exception as e:
        await message.reply_text(f"حصل خطأ: {e}")
    finally:
        # حذف الملف في كل الأحوال
        if os.path.exists(filename):
            os.remove(filename)

# ================= أوامر الطقس =================
@Client.on_message(filters.command(["طقس"], ""), group=5305)
async def weather_handler(_: Client, message: Message):
    data = message.text.split(maxsplit=1)
    if len(data) < 2:
        return await message.reply_text("- خطأ في البيانات.\n- طقس + المدينة")
    try:
        return await message.reply_text(_weather(data[1]))
    except KeyError:
        await message.reply_text("- المدينة غير موجودة.")
    except Exception as e:
        await message.reply_text("حدث خطأ في جلب المعلومات.")

def _weather(query):
    params = {
        "q": query, 
        "APPID": "eedbc05ba060c787ab0614cad1f2e12b", 
        "units": "metric" 
    }
    response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params).json()
    if str(response.get("cod")) != "200":
        raise KeyError("City not found")
        
    name = f"- الاسم: {response['name']}\n╰───○ ● الدولة: {response['sys']['country']}\n\n"
    weather = f"- الطقس: {response['weather'][0]['main']}\n╰───○ ● الوصف: {response['weather'][0]['description']}\n\n"
    temp = f"- درجة الحرارة: {response['main']['temp']}\n╰───○ ● الشعور: {response['main']['feels_like']}\n\n"
    wind = f"- سرعة الرياح: {response['wind']['speed']}\n╰───○ ● الزاوية: {response['wind']['deg']}\n\n"
    humidity = f"- الرطوبة: {response['main']['humidity']}"
    caption = f"{name}{weather}{temp}{wind}{humidity}"
    return caption

# ================= أوامر مواقيت الصلاة (كتابة) =================
pnames: dict = {
    'Fajr': "الفجر", 'Sunrise': "الشروق", 'Dhuhr': "الظهر", 'Asr': "العصر",
    'Maghrib': "المغرب", 'Isha': "العشاء", 'Imsak': "الامساك",
    'Midnight': "منتصف الليل", 'Firstthird': "الثلث الأول من الليل", 'Lastthird': "الثلث الأخير من الليل"
}

@Client.on_message(filters.command(["مواقيت الصلاه", "مواقيت الصلاة"], ""), group=71198535)
async def sendAdhan(_: Client, message: Message) -> None:
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text("- اكتب اسم المنطقه بجانب الأمر،")
    
    address = parts[1]
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: 
        return await message.reply_text("- حدث خطأ أثناء جلب مواقيت الصلاة.")
    await message.reply_text(adhan)    

def getAdhan(address: str) -> Union[str, bool]:
    params = {"address": address, "method": 1, "school": 0}
    try:
        res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
        data: dict = res.json()
        if data["code"] != 200: return False
        
        data = data["data"]
        timings = data["timings"]
        date_h = data["date"]["hijri"]
        date_g = data["date"]["gregorian"]
        
        if 'Sunset' in timings: del timings['Sunset']
        
        next_p: str = getNext(timings)
        caption = f"- {next_p}\n- مواقيت الصلاة:"
        for prayer, time in timings.items():
            if prayer in pnames:
                caption += f"\n    - {pnames[prayer]}: {time}"
        
        caption += f"\n\n- التاريخ: {date_h['date']} (هـ) | {date_g['date']} (م)"
        return caption
    except Exception:
        return False
    
def getNext(timings: dict) -> str:
    current_time = datetime.now(zone).strftime("%H:%M")
    next_prayer = None
    for prayer, time in timings.items():
        if current_time < time:
            next_prayer = prayer
            break
    if next_prayer is None: return "انتهت صلوات اليوم."
    
    next_prayer_time = datetime.strptime(timings[next_prayer], "%H:%M")
    current_time_dt = datetime.strptime(current_time, "%H:%M")
    time_difference = next_prayer_time - current_time_dt
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"متبقى على صلاة {pnames.get(next_prayer, next_prayer)} {hours} ساعه و {minutes} دقيقه."

# ================= نظام الأذان الصوتي التلقائي =================

prayer_stickers = {
    "الفجر": {"channel_username": "WORLED_CAESAR", "message_id": 349},
    "الظهر": {"channel_username": "WORLED_CAESAR", "message_id": 350},
    "العصر": {"channel_username": "WORLED_CAESAR", "message_id": 351},
    "المغرب": {"channel_username": "WORLED_CAESAR", "message_id": 352},
    "العشاء": {"channel_username": "WORLED_CAESAR", "message_id": 353},
}

@Client.on_message(filters.text & ~filters.private & filters.regex(r"^(تفعيل الاذان|تعطيل الاذان)$"), group=20)
async def handle_azan_command(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذان":
        if chat_id in azan_enabled_chats:
            await msg.reply_text("الأذان مفعل بالفعل في هذه المجموعة")
        else:
            azan_enabled_chats.append(chat_id)
            await msg.reply_text("تم تفعيل الاذان بنجاح ✨♥")
    elif msg.text == "تعطيل الاذان":
        if chat_id in azan_enabled_chats:
            azan_enabled_chats.remove(chat_id)
            await msg.reply_text("تم تعطيل الاذان بنجاح✨♥")
        else:
            await msg.reply_text("الأذان معطل بالفعل في هذه المجموعة")

async def stop_azan(bot_username):
    hoss = await get_call(bot_username)
    for chat_id in azan_enabled_chats:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception:
            pass

async def play_azan(chat_id, bot_username, client):
    hoss = await get_call(bot_username)    
    azan_audio_path = "./Hossam/azan.mp3"
    
    if not os.path.exists(azan_audio_path):
        # محاولة لإعلام المجموعة إذا كان الملف مفقوداً
        try: await client.send_message(chat_id, "ملف الأذان الصوتي غير موجود.")
        except: pass
        return

    stream = AudioPiped(azan_audio_path)
    try:
        await hoss.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        try:
            await hoss.join_assistant(chat_id, chat_id)
            await asyncio.sleep(1) # انتظار قليل
            await hoss.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except Exception as e:
            await client.send_message(chat_id, f"مشكلة في الاتصال بالكول: {e}")
    except AlreadyJoinedError:
        try:
            await hoss.leave_group_call(chat_id)
            await asyncio.sleep(2)
            await hoss.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except Exception:
             pass
    except Exception as e:
        print(f"Azan Play Error: {e}")

def get_prayer_time():
    try:
        response = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0").json()
        timings = response['data']['timings']
        
        # تحويل الوقت لـ 12 ساعة للتوافق مع التنسيق المطلوب أو مقارنة 24 ساعة
        # هنا سنعتمد على التنسيق المباشر (غالبا API يرجع 24 ساعة مثل 16:30)
        current_time = datetime.now(cairo_timezone).strftime('%H:%M')
        
        # خريطة الصلوات
        prayers_map = {
            'Fajr': "الفجر",
            'Dhuhr': "الظهر",
            'Asr': "العصر",
            'Maghrib': "المغرب",
            'Isha': "العشاء"
        }

        for p_key, p_name in prayers_map.items():
            if timings[p_key] == current_time:
                return p_name
        return None
    except Exception as e:
        print(f"Error checking prayer time: {e}")
        return None

async def send_prayer_message(app, chat_id, prayer_name):
    try:
        await app.send_message(chat_id, f"حان الآن موعد أذان {prayer_name} 🕊❤")
        
        if prayer_name in prayer_stickers:
            sticker_info = prayer_stickers[prayer_name]
            try:
                msg = await app.get_messages(sticker_info["channel_username"], sticker_info["message_id"])
                if msg.sticker:
                    await app.send_sticker(chat_id, msg.sticker.file_id)
            except Exception:
                pass
    except Exception:
        pass

async def azan_loop(bot_username):
    app = appp[bot_username]
    print(f"Start Azan Loop for {bot_username}")
    while True:
        try:
            prayer_name = get_prayer_time()
            if prayer_name:
                await stop_azan(bot_username)
                for chat_id in azan_enabled_chats:
                    await send_prayer_message(app, chat_id, prayer_name)
                    await play_azan(chat_id, bot_username, app)
                # الانتظار 3 دقائق حتى لا يكرر الأذان في نفس الدقيقة
                await asyncio.sleep(180)
            else:
                await asyncio.sleep(40)
        except Exception as e:
            print(f"Error in azan loop: {e}")
            await asyncio.sleep(60)

# ================= الأذكار الصوتية =================

@Client.on_message(filters.text & ~filters.private & filters.regex(r"^(تفعيل الاذكار الصوتيه|تعطيل الاذكار الصوتيه)$"), group=220)
async def azkar_sound_command(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذكار الصوتيه":
        if chat_id in azkar_ses:
            await msg.reply_text("الاذكار مفعل بالفعل في هذه المجموعة")
        else:
            azkar_ses.append(chat_id)
            await msg.reply_text("تم تفعيل الاذكار الصوتيه بنجاح ✨♥")
    elif msg.text == "تعطيل الاذكار الصوتيه":
        if chat_id in azkar_ses:
            azkar_ses.remove(chat_id)
            await msg.reply_text("تم تعطيل الاذكار الصوتيه بنجاح✨♥")
        else:
            await msg.reply_text("الاذكار الصوتيه معطله بالفعل في هذه المجموعة")

async def stop_azkar(bot_username):
    hoss = await get_call(bot_username)
    for chat_id in azkar_ses:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception:
            pass

async def play_azkar(chat_id, bot_username, client):
    hoss = await get_call(bot_username)    
    azkar_path = "./Hossam/saly.mp3"
    
    if not os.path.exists(azkar_path): return

    stream = AudioPiped(azkar_path)
    try:
        await hoss.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        try:
            await hoss.join_assistant(chat_id, chat_id)
            await asyncio.sleep(1)
            await hoss.join_group_call(chat_id, stream, stream_type=StreamType().pulse_stream)
        except Exception: pass
    except AlreadyJoinedError:
        try:
            await hoss.leave_group_call(chat_id)
            await asyncio.sleep(1)
            await hoss.join_group_call(chat_id, stream, stream_type=StreamType().pulse_stream)
        except Exception: pass
    except Exception: pass

async def azkar_sound_loop(bot_username):
    app = appp[bot_username]
    print(f"Start Azkar Sound Loop for {bot_username}")
    while True:
        try:
            # هنا يمكنك إضافة منطق لوقف الصوت القديم إذا أردت
            # await stop_azkar(bot_username) 
            for chat_id in azkar_ses:
                await play_azkar(chat_id, bot_username, app)
            
            await asyncio.sleep(600) # كل 10 دقائق
        except Exception as e:
            print(f"Error in azkar sound loop: {e}")
            await asyncio.sleep(60)

# ================= الأذكار النصية =================

@Client.on_message(filters.text & filters.group & filters.regex(r"^(تفعيل الاذكار|تعطيل الاذكار)$"), group=2220)
async def azkar_text_command(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذكار":
        if chat_id in azkar_chat:
            await msg.reply_text("الاذكار مفعل بالفعل في هذه المجموعة")
        else:
            azkar_chat.append(chat_id)
            await msg.reply_text("تم تفعيل الاذكار بنجاح ✨♥")
    elif msg.text == "تعطيل الاذكار":
        if chat_id in azkar_chat:
            azkar_chat.remove(chat_id)
            await msg.reply_text("تم تعطيل الاذكار بنجاح✨♥")
        else:
            await msg.reply_text("الاذكار معطله بالفعل في هذه المجموعة")

xt = [
    "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
    "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
    "استغفر الله العظيم وأتوبُ إليه 🌹",
    "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم",
    "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
    "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
    "سبحان الله وبحمده سبحان الله العظيم🌸",
    "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
    "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
    "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
    "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
    "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
    "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
    "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
    "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
    "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
    "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
    "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
    "استغفر الله العظيم وأتوبُ إليه.",
    "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
    " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
    "ماتستغفر ربنا كده🥺❤️",
    "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
    "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
    "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
    "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
    "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
    "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
    "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
    "أصبحنا وأصبح الملك لله ولا اله الا الله.",
    "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
    "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
    "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
    "- اللهم القبول الذي لا يزول ❤️🍀.",
    "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
    "سبحان الله وبحمده ،سبحان الله العظيم.",
    "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه، عودوا السنتكم على الذكر.",
    "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
    "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
    "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
    "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
    "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
    "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
    "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
    "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
    "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت ??💜.",
    "- وبك أصبحنا يا عظيم الشأن ??❤️.",
    "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
    "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
    "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
    "صلي على النبي بنيه الفرج❤️",
    "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
    "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
    "لا اله الا الله سيدنا محمد رسول الله🌿💜",
    "قول معايا - استغفر الله استفر الله استغفر الله -",
    "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
    "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
    "صلي على محمد❤️",
    "ماتيجو نقرء الفاتحه سوا🥺"
]

async def azkar_text_loop(bot_username):
    app = appp[bot_username]
    print(f"Start Azkar Text Loop for {bot_username}")
    while True:
        try:
            if azkar_chat:
                zekr = random.choice(xt)
                for chat_id in azkar_chat:
                    try:
                        await app.send_message(chat_id, zekr)
                    except Exception:
                        pass
            await asyncio.sleep(600)
        except Exception as e:
            print(f"Error in azkar text loop: {e}")
            await asyncio.sleep(60)

# ================= نداء الأعضاء (المنشن) =================

@Client.on_message(filters.text & filters.group & filters.regex(r"^(تفعيل|فتح|تعطيل|قفل) (النداء|الندائ|المنشن التلقائي)$"), group=207380)
async def nday_command(c, msg):
    chat_id = msg.chat.id
    text = msg.text
    if any(x in text for x in ["تفعيل", "فتح"]):
        if chat_id in nday_chattm:
            await msg.reply_text("النداء مفعل بالفعل في هذه المجموعة")
        else:
            nday_chattm.append(chat_id)
            await msg.reply_text("تم تفعيل النداء بنجاح ✨♥")
    elif any(x in text for x in ["تعطيل", "قفل"]):
        if chat_id in nday_chattm:
            nday_chattm.remove(chat_id)
            await msg.reply_text("تم تعطيل النداء بنجاح✨♥")
        else:
            await msg.reply_text("النداء معطل بالفعل في هذه المجموعة")
                     
async def nday_loop(bot_username):
    app = appp[bot_username]
    print(f"Start Nday Loop for {bot_username}")
    while True:
        try:
            for chat_id in nday_chattm:
                members = []
                # جلب عينة من الأعضاء (50 عضو) لتخفيف الحمل
                async for member in app.get_chat_members(chat_id, limit=50):
                    if not member.user.is_bot and not member.user.is_deleted:
                        members.append(member)
                
                if members:
                    random_member = random.choice(members)
                    mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
                    
                    msgs = [
                        f"بقلنا ساعه مستنينك فينك 😾 {mention}",
                        f"• يـا قمـري ❤️‍🔥 {mention}",
                        f"حبيبي لي م بتتكلم معنا 🤔 {mention}",
                        f"• يـا تفاحه 🍏 فينك {mention}",
                        f"• هو انت لي قمر كده 🌚♥ {mention}",
                        f"• ويــن طامــس يحـلــو : {mention}",
                        f"• الأشياء معك لها طعم آخر بنكهة الحب 🤍 {mention}",
                        f"• مشتاقيـن حــب وينڪ : {mention}",
                        f"• أجمل وجهات النظر هي النظر لوجهك ♥️. {mention}",
                        f"• أنـتِ مسائي وأجمـل مسـاء, وأنا مع كـل مسـاء أحـبـك . 💕 {mention}",
                        f"مشتهين عسل؟ {mention}",
                        f"حياة المشاهير صعبه بس وحشتنى : {mention}",
                        f"وش الشي الي تفكر فيه الحين ؟ {mention}",
                        f"هل تفضلين الزواج عن حب أم زواج الصالونات؟ {mention}",
                        f"ستبقي أنت أهم وأول أمنياتي في هذه الحياة مهما زادت طموحاتي 💜 {mention}",
                        f"عرفناا عنك؟ {mention}",
                        f"لست أمام عيوني لكن كل يوم أراك  🍂 {mention}",
                        f"أحبتتك لدرجة كبيرة جداً ، فلا تغيب عني أبداً ، فعند غيابك تغيب كل الأشياء معك. 💐! {mention}",
                        f"الثلج يكون بمثابة الهدية للشتاء، والشمس تكون كالهدية للصيف، والزهور هدية الربيع ، وأنت هديتي طوال العمر. 🧡 {mention}",
                        f"وكأن حديثك موسيّقى هادئة ينصت لها قلبي 💜 {mention}"
                    ]
                    try:
                        await app.send_message(chat_id, random.choice(msgs))
                    except Exception:
                        pass
            
            await asyncio.sleep(600)
        except Exception as e:
            print(f"Error in nday loop: {e}")
            await asyncio.sleep(60)

# ================= تشغيل المهام =================
# هذا الأمر مهم جداً لتشغيل الحلقات الخلفية
# ارسل /تشغيل_النظام في المجموعة أو الخاص لتفعيل المهام

@Client.on_message(filters.command(["تشغيل_النظام", "start_tasks"]), group=999)
async def start_all_systems(client, message):
    # التأكد من أن الشخص هو المطور (يمكنك تفعيل هذا الشرط)
    # if message.from_user.id != devuser: return
    
    bot_username = client.me.username
    await message.reply_text("جاري تشغيل مهام الخلفية (الأذان، الأذكار، النداء)...")
    
    # تشغيل الحلقات
    asyncio.create_task(azan_loop(bot_username))
    asyncio.create_task(azkar_sound_loop(bot_username))
    asyncio.create_task(azkar_text_loop(bot_username))
    asyncio.create_task(nday_loop(bot_username))
    
    await message.reply_text("✅ تم تشغيل جميع الأنظمة بنجاح.")
