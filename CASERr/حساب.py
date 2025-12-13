from pyrogram import Client, types, filters, enums, raw
import pyromod
from pyrogram.errors import (PhoneNumberInvalid, PhoneCodeInvalid, SessionPasswordNeeded, PasswordHashInvalid, PhoneCodeExpired)
import asyncio
from pyromod import listen
from pyrogram import filters, Client
from pyrogram import Client, filters
from bs4 import BeautifulSoup
import asyncio
import requests
from requests import Session
import urllib.request as request
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
#from pyrolistener.exceptions import TimeOut
from os import remove

session = Session()
api = 'https://api.saidazim.uz/tiktok/'
turl = 'https://vm.tiktok.com/{id}'

caption = '''
- nickname : {nickname}
- username : {username}
- title : {title}
- views : {views}
- likes : {likes}
- commments : {comments}
- shares : {shares}
'''

def downloadTiktok(url):
    params = {
        'url': url
    }
    res = session.get(api, params= params).json()
    if res.get('id') is None : return {'error' : '- invalid url!!!'}
    _caption = caption.format(
        nickname = res['nickname'],
        username = res['username'],
        title = res['title'],
        views = res['view_count'],
        likes = res['like_count'],
        comments = res['comment_count'],
        shares = res['share_count']
    )
    return {
        'caption': _caption,
        'id': url.split('/')[3],
        'video': res['video']
    }

def downloadAudio(_id):
    url = turl.format(id=_id)
    params = {
        'url': url
    }
    res = session.get(api, params= params).json()
    audio = res['music']
    request.urlretrieve(audio, f'{_id}.mp3')


@Client.on_message(filters.command(["تيك توك"], "") & filters.private,group=75053)
async def reciveURL(app: Client, message: Message):
    ask = await app.ask(message.chat.id, "ارسل الان الرابط", timeout=200)
    response = downloadTiktok(ask.text)
    if response.get('error'): return await ask.reply(response['error'])
    request.urlretrieve(response['video'], f'{response["id"]}.mp4')
    markup = Markup([
        [Button('- Download Audio -',f'adownload {response["id"]}')],
        [Button('- Developer -', user_id = 5184436120)]
    ])
    await ask.reply_video(video = f'{response["id"]}.mp4', caption = response['caption'], reply_markup = markup, reply_to_message_id = message.id)  
    remove(f'{response["id"]}.mp4')

@Client.on_callback_query(filters.regex(r'^(adownload)'))
async def aDownload(_: Client, callback: CallbackQuery):
    _id = callback.data.split()[1]
    downloadAudio(_id)
    await callback.message.reply_audio(
        audio = f'{_id}.mp3',
        reply_to_message_id = callback.message.id
    )
    remove(f'{_id}.mp4')

class config:
    API_HASH = "b90c282e584222babde5f68b5b63ee3b"
    API_ID = 9157919


@Client.on_message(filters.command(["• حذف حساب •"], "") & filters.private, group=7053)
async def ON_START_BOT(app: Client, message: types.Message):
    await app.send_message(
        chat_id=message.chat.id,
        text="مرحبًا بك في حذف حسابات تليجرام.",
        reply_markup=types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='حذف بالرقم', callback_data="DELETACCO55UNT")
            ],
            [
                types.InlineKeyboardButton(text='حذف بالجلسه', callback_data="ADDITIONAL_ACTION")
            ]
        ])
    )

SESSSIONS = None
PASSWORD = None

@Client.on_callback_query(filters.regex('^ADDITIONAL_ACTION$'))
async def DELET_AC575COUNT(app: Client, query):
    global SESSSIONS
    data = await app.ask(query.message.chat.id, "ارسل الان الجلسه", timeout=200)
    SESSSIONS = data.text
    message_data = await app.send_message(chat_id=query.message.chat.id, text='جاري التحقق .')    
    await app.edit_message_text(chat_id=query.message.chat.id, message_id=message_data.id, text="هل أنت متأكد أنك تريد حذف الحساب؟", reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="نعم اريد", callback_data='OnDelete')]]))
    
@Client.on_callback_query(filters.regex('^DELETACCO55UNT$'))
async def DELET_ACCOUNT(app: Client, query: types.CallbackQuery):
    global SESSSIONS
    ask = await app.ask(query.message.chat.id, "ارسل لي الآن الرقم بكود الدوله مثل \n +201058741514", timeout=300)
    hossahm = ask.text
    message_data = await app.send_message(chat_id=query.message.chat.id, text="انتظر، جاري إرسال الكود")
    session_client = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await session_client.connect()
    try:
        code = await session_client.send_code(hossahm)
    except PhoneNumberInvalid:
        await app.send_message(chat_id=query.message.chat.id, text="رقم الهاتف غير صحيح. ارسل /start وارسل الرقم بشكل صحيح")
        return
    ask = await app.ask(query.message.chat.id, "تم إرسال الكود إلى حسابك\nقم بإرسال الكود بين كل رقم مسافه \n بهذه الطريقة: 1 2 3 4 5", timeout=300)
    hoam = ask.text
    try:
        await session_client.sign_in(hossahm, code.phone_code_hash, hoam)
    except (PhoneCodeInvalid, PhoneCodeExpired):
        await app.send_message(chat_id=query.message.chat.id, text="الكود غير صحيح أو انتهت صلاحية الكود ارسل /start وحاول مره اخره")
        return
    except SessionPasswordNeeded:
        try:
            ask = await app.ask(query.message.chat.id, "الحساب محمي بكلمة سر، ارسل كلمة السر الآن (التحقوق) ", timeout=300)
            hm = ask.text
        except asyncio.exceptions.TimeoutError:
            await app.send_message(chat_id=query.message.chat.id, text="انتهى الوقت، يرجى المحاولة مرة أخرى.\n ارسل /start")
            return
        try:
            await session_client.check_password(password=hm)
            session_String = await session_client.export_session_string()
        except Exception:
            await app.send_message(chat_id=query.message.chat.id, text="كلمة السر غير صحيحة يرجى ارسال /start وحاول مره اخرى")
            await session_client.disconnect()
            return
    session_String = await session_client.export_session_string()
    SESSSIONS = session_String
    await session_client.disconnect()
    await app.send_message(chat_id=query.message.chat.id, text="يجب التاكيد ثم ارسال التوكن", reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="اضغط للتاكيد", callback_data='OnDelete')]]))
    
@Client.on_callback_query(filters.regex('^OnDelete$'))
async def DELET_ACCOUNT(app: Client, query):
    async with Client(':memory:', api_hash="", api_id="",  session_string=SESSSIONS) as session_client:
        await session_client.invoke(raw.functions.account.DeleteAccount(
            reason="not"))
    await app.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text="تم حذف الحساب بنجاح")

@Client.on_message(filters.command(["• استخراج api •"], "") & filters.private, group=7053)
async def start(app: Client, message):
    bot = await app.ask(message.chat.id, "اهلا بك \n أرسل رقم هاتفك مع رمز البلد للحصول على API ID و API HASH\n مثال : \n +201015978315", timeout=200)
    phone_number = bot.text
    with requests.Session() as req:
        login0 = req.post('https://my.telegram.org/auth/send_password', data={'phone': phone_number})
        if 'Sorry, too many tries. Please try again later.' in login0.text:
            await message.reply('تم حظر حسابك! يرجى المحاولة مرة أخرى بعد 8 ساعات.')
            return
        login_data = login0.json()
        random_hash = login_data['random_hash']
        await message.reply('أرسل الرمز الذي تم إرساله إلى حساب Telegram الخاص بك:')
        code = await app.listen(message.chat.id)
        login_data = {
            'phone': phone_number,
            'random_hash': random_hash,
            'password': code.text
        }        
        login = req.post('https://my.telegram.org/auth/login', data=login_data)        
        apps_page = req.get('https://my.telegram.org/apps')
        soup = BeautifulSoup(apps_page.text, 'html.parser')
        try:
            api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
            api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()
            await message.reply(f"API ID: {api_id}\nAPI HASH: {api_hash}")
        except:
            await message.reply('لا يمكن الحصول على APIs! سيتم إصلاح هذا الخطأ في التحديث القادم.')
            
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)

API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"

@Client.on_message(filters.command(["استخرج جلسه","• استخرج جلسه •"], "") & filters.private, group=827363666)
async def add_assistant_account(client, message):
        ask = await client.ask(message.chat.id, "ارسل لي الآن الرقم", timeout=300)
        hossahm = ask.text
        await message.reply_text("انتظر، جاري إرسال الكود")
        cliehnt = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
        await cliehnt.connect()
        try:
            code = await cliehnt.send_code(hossahm)
        except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
            return
        ask = await client.ask(message.chat.id, "تم إرسال الكود إلى حسابك، قم بإرسال الكود بهذه الطريقة: 1 2 3 4 5", timeout=300)
        hoam = ask.text
        try:
            await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await message.reply_text("الكود غير صحيح أو انتهت صلاحية الكود")
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await message.reply_text("الكود غير صحيح أو انتهت صلاحية الكود")
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                ask = await client.ask(message.chat.id, "الحساب محمي بكلمة سر، ارسل كلمة السر الآن", timeout=300)
                hm = ask.text
            except TimeoutError:
                return
            try:
                await cliehnt.check_password(password=hm)
                session = await cliehnt.export_session_string()
            except:
                await message.reply_text("كلمة السر غير صحيحة")
                return
        else:
            session = await cliehnt.export_session_string()
        await cliehnt.disconnect()
        SESSION = session
        await client.send_message(message.chat.id, f"`{SESSION}`")   