import pyrogram
import asyncio
import requests
from pyrogram import Client as client
from pyrogram import Client, idle
from pyrogram import filters, Client
import random
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned

points = {}  
c0aesar = {}              
u0sers = {}        

ph0otos = [
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"},
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@Client.on_message(filters.command(["ممثل", "ممثلين","• ممثلين •"], ""), group=1024682131)
async def dhjfyuh(client, message):
    actor = random.choice(ph0otos)
    bot_username = client.me.username
    user_id = message.from_user.id
    c0aesar[user_id] = actor['name']
    u0sers[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الممثل...؟ ")

@Client.on_message(filters.text, group=10790430)
async def yfugry(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in u0sers:
        correct_actor = c0aesar.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del c0aesar[user_id]
            del u0sers[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del c0aesar[user_id]
                del u0sers[user_id]

caesar1 = {}              
users1 = {}        

potss = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}
]

@Client.on_message(filters.command(["مغنين", "مغاني","• مغنين •"], ""), group=107082131)
async def moganen(client, message):
    actor = random.choice(potss)
    bot_username = client.me.username
    user_id = message.from_user.id
    caesar1[user_id] = actor['name']
    users1[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المغني...؟ ")

@Client.on_message(filters.text, group=10126430)
async def mogany(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in users1:
        correct_actor = caesar1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar1[user_id]
            del users1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caesar1[user_id]
                del users1[user_id]

cpaesr2 = {}              
upsrs2 = {}        

patos = [
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "الصين", "photo": "https://envs.sh/wfs.jpg"},
    {"name": "النيجر", "photo": "https://envs.sh/wf9.jpg"},
    {"name": "مصر", "photo": "https://envs.sh/wfN.jpg"},
    {"name": "سويسرا", "photo": "https://envs.sh/wfM.jpg"},
    {"name": "جزر الباهاما", "photo": "https://envs.sh/wfX.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "استونيا", "photo": "https://envs.sh/wfx.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "انجلترا", "photo": "https://envs.sh/waE.jpg"},
    {"name": "البرازيل", "photo": "https://envs.sh/wah.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "مالي", "photo": "https://envs.sh/waw.jpg"},
    {"name": "الكونغو", "photo": "https://envs.sh/wa0.jpg"},
    {"name": "العراق", "photo": "https://envs.sh/waS.jpg"},
    {"name": "ارمينيا", "photo": "https://envs.sh/waI.jpg"},
    {"name": "اسبانيا", "photo": "https://envs.sh/waA.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "فلسطين", "photo": "https://envs.sh/wa5.jpg"},
    {"name": "كينيا", "photo": "https://envs.sh/waK.jpg"},
    {"name": "سان مارينو", "photo": "https://envs.sh/waz.jpg"},
    {"name": "الفلبين", "photo": "https://envs.sh/wa-.jpg"},
    {"name": "المكسيك", "photo": "https://envs.sh/wOE.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "باكستان", "photo": "https://envs.sh/wOh.jpg"},
    {"name": "الجبل الاسود", "photo": "https://envs.sh/wO2.jpg"},
    {"name": "موزمبيق", "photo": "https://envs.sh/wOi.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "افغانستان", "photo": "https://envs.sh/wap.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "اندونيسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "الرأس الاخضر", "photo": "https://envs.sh/wOS.jpg"},
    {"name": "هولندا", "photo": "https://envs.sh/wOI.jpg"},
    {"name": "اندونسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "فنلندا", "photo": "https://envs.sh/wmu.jpg"},
    {"name": "الكونغو الديموقراطية", "photo": "https://envs.sh/wmt.jpg"},
    {"name": "النمسا", "photo": "https://envs.sh/wmP.jpg"},
    {"name": "ايطاليا", "photo": "https://envs.sh/wmq.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "السعوديه", "photo": "https://envs.sh/wmS.jpg"},
    {"name": "كولومبيا", "photo": "https://envs.sh/wmW.jpg"},
    {"name": "نيجريا", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "نيبال", "photo": "https://envs.sh/wmI.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "السويد", "photo": "https://envs.sh/wmA.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "انغولا", "photo": "https://envs.sh/wmc.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "المجر", "photo": "https://envs.sh/wfv.jpg"},
    {"name": "سوريا", "photo": "https://envs.sh/wmL.jpg"},
    {"name": "ايرلندا", "photo": "https://envs.sh/wm5.jpg"},
    {"name": "كازاخستان", "photo": "https://envs.sh/wmz.jpg"},
    {"name": "بنين", "photo": "https://envs.sh/wan.jpg"},
    {"name": "بنغلاديش", "photo": "https://envs.sh/wOt.jpg"},
    {"name": "قبرص", "photo": "https://envs.sh/wmk.jpg"},
    {"name": "تنزانيا", "photo": "https://envs.sh/wm8.jpg"},
    {"name": "افريقيا الوسطى", "photo": "https://envs.sh/wm7.jpg"},
    {"name": "مقدونيا", "photo": "https://envs.sh/PgC.jpg"},
    {"name": "موريتانيا", "photo": "https://envs.sh/wmr.jpg"},
    {"name": "غنيا الاستوائية", "photo": "https://envs.sh/wms.jpg"},
    {"name": "فرنسا", "photo": "https://envs.sh/wMF.jpg"},
    {"name": "اليابان", "photo": "https://envs.sh/wMt.jpg"},
    {"name": "فيتنام", "photo": "https://envs.sh/wMi.jpg"},
    {"name": "مالطا", "photo": "https://envs.sh/wMP.jpg"},
    {"name": "تايوان", "photo": "https://envs.sh/wM0.jpg"},
    {"name": "بوروندي", "photo": "https://envs.sh/wMB.jpg"},
    {"name": "مالاوي", "photo": "https://envs.sh/wMT.jpg"},
    {"name": "اثيوبيا", "photo": "https://envs.sh/wMp.jpg"},
    {"name": "لبنان", "photo": "https://envs.sh/wM_.jpg"},
    {"name": "البانيا", "photo": "https://envs.sh/wMj.jpg"},
    {"name": "تايلاند", "photo": "https://envs.sh/wMc.jpg"},
    {"name": "جنوب افريقيا", "photo": "https://envs.sh/wMZ.jpg"},
    {"name": "طاجيكستان", "photo": "https://envs.sh/wfk.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "استراليا", "photo": "https://envs.sh/wMK.jpg"},
    {"name": "السودان", "photo": "https://envs.sh/wM3.jpg"},
    {"name": "غانا", "photo": "https://envs.sh/wMC.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "قطر", "photo": "https://envs.sh/wM4.jpg"},
    {"name": "الجزائر", "photo": "https://envs.sh/wMU.jpg"},
    {"name": "جزر القمر", "photo": "https://envs.sh/wMk.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "الدنمارك", "photo": "https://envs.sh/wfm.jpg"},
    {"name": "صربيا", "photo": "https://envs.sh/wM8.jpg"},
    {"name": "البحرين", "photo": "https://envs.sh/wOu.jpg"},
    {"name": "سنغافورة", "photo": "https://envs.sh/wMo.jpg"},
    {"name": "ايران", "photo": "https://envs.sh/wMr.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "أذربيجاني", "photo": "https://envs.sh/wMN.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "اوغندا", "photo": "https://envs.sh/wfo.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "بلجيكا", "photo": "https://envs.sh/wMa.jpg"},
    {"name": "ايسلندا", "photo": "https://envs.sh/wMO.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "اريتريا", "photo": "https://envs.sh/wMy.jpg"},
    {"name": "سيشل", "photo": "https://envs.sh/wMx.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "الامارات", "photo": "https://envs.sh/wXD.jpg"},
    {"name": "النرويج", "photo": "https://envs.sh/wXE.jpg"},
    {"name": "زامبيا", "photo": "https://envs.sh/wXh.jpg"},
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "المانيا", "photo": "https://envs.sh/wXd.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "اوكرانيا", "photo": "https://envs.sh/wXu.jpg"},
    {"name": "الصومال", "photo": "https://envs.sh/wXt.jpg"},
    {"name": "بوركينافاسو", "photo": "https://envs.sh/wXb.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "سلوفينيا", "photo": "https://envs.sh/wVY.jpg"},
    {"name": "ليبيا", "photo": "https://envs.sh/wVJ.jpg"},
    {"name": "جزر المالديف", "photo": "https://envs.sh/wVo.jpg"},
    {"name": "كندا", "photo": "https://envs.sh/wVs.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "اليونان", "photo": "https://envs.sh/wVH.jpg"}
]

@Client.on_message(filters.command(["اعلام", "علم","• اعلام •"], ""), group=101237782131)
async def aalame(client, message):
    actor = random.choice(patos)
    bot_username = client.me.username
    user_id = message.from_user.id
    cpaesr2[user_id] = actor['name']
    upsrs2[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا العلم...؟ ")

@Client.on_message(filters.text, group=11026439870)
async def alamy(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in upsrs2:
        correct_actor = cpaesr2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cpaesr2[user_id]
            del upsrs2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cpaesr2[user_id]
                del upsrs2[user_id]
                
caesar3 = {}              
users3 = {}        

photn = [
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}
]

@Client.on_message(filters.command(["لاعبين", "لاعب","• لاعبين •"], ""), group=9827065)
async def laaban(client, message):
    actor = random.choice(photn)
    bot_username = client.me.username
    user_id = message.from_user.id
    caesar3[user_id] = actor['name']
    users3[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الاعب..؟ ")

@Client.on_message(filters.text, group=458678)
async def alaeb(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in users3:
        correct_actor = caesar3.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar3[user_id]
            del users3[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caesar3[user_id]
                del users3[user_id]

cesar4 = {}              
urers4 = {}        

soraa = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}, 
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}, 
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"},
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@Client.on_message(filters.command(["مشاهير", "مشهور","• مشاهير •"], ""), group=700953)
async def masher(client, message):
    actor = random.choice(soraa)
    bot_username = client.me.username
    user_id = message.from_user.id
    cesar4[user_id] = actor['name']
    urers4[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المشهور...؟ ")

@Client.on_message(filters.text, group=75205)
async def mashor(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in urers4:
        correct_actor = cesar4.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cesar4[user_id]
            del urers4[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cesar4[user_id]
                del urers4[user_id]

ces5ar5 = {}              
ur5ers5 = {}        

so5raa5 = [
    {"name": "البدله", "photo": "https://envs.sh/Wsv.jpg"},
    {"name": "الحفله", "photo": "https://envs.sh/WsN.jpg"},
    {"name": "الارهابي", "photo": "https://envs.sh/Wsa.jpg"},
    {"name": "اكس لارج", "photo": "https://envs.sh/WsO.jpg"},
    {"name": "الرهينه", "photo": "https://envs.sh/Wsm.jpg"},
    {"name": "افواه وارانب", "photo": "https://envs.sh/WsX.jpg"},
    {"name": "ارض الخوف", "photo": "https://envs.sh/Wsy.jpg"},
    {"name": "الكيت كات", "photo": "https://envs.sh/Ws6.jpg"},
    {"name": "الفيل الازرق", "photo": "https://envs.sh/Wsx.jpg"},
    {"name": "باب الشمس", "photo": "https://envs.sh/W9E.jpg"},
    {"name": "السلم والثعبان", "photo": "https://envs.sh/Ws-.jpg"},
    {"name": "بطل من ورق", "photo": "https://envs.sh/Wve.jpg"},
    {"name": "الجوع", "photo": "https://envs.sh/Wvb.jpg"},
    {"name": "البيضه والحجر", "photo": "https://envs.sh/Ws9.jpg"},
    {"name": "المركب", "photo": "https://envs.sh/WvZ.jpg"},
    {"name": "جواب اعتقال ", "photo": "https://envs.sh/WvK.jpg"},
    {"name": "الرساله", "photo": "https://envs.sh/Wv4.jpg"},
    {"name": "السقا مات", "photo": "https://envs.sh/Wvk.jpg"},
    {"name": "الفرح", "photo": "https://envs.sh/Wvo.jpg"},
    {"name": "النمر الاسود", "photo": "https://envs.sh/WvN.jpg"},
    {"name": "الشبح", "photo": "https://envs.sh/Wvf.jpg"},
    {"name": "العصفور", "photo": "https://envs.sh/Wvm.jpg"},
    {"name": "بحب السيما", "photo": "https://envs.sh/Wvy.jpg"},
    {"name": "النمر والانثي", "photo": "https://envs.sh/Wv6.jpg"},
    {"name": "الكنز", "photo": "https://envs.sh/WND.jpg"},
    {"name": "جحيم في الماء", "photo": "https://envs.sh/WNd.jpg"},
    {"name": "الهروب", "photo": "https://envs.sh/WH1.jpg"},
    {"name": "اين العقل", "photo": "https://envs.sh/WHN.jpg"},
    {"name": "حب في الزنزانه", "photo": "https://envs.sh/Wge.jpg"},
    {"name": "بنتين من مصر", "photo": "https://envs.sh/Wg3.jpg"},
    {"name": "تراب الماس", "photo": "https://envs.sh/WgC.jpg"},
    {"name": "ساعه ونص", "photo": "https://envs.sh/Wg1.jpg"},
    {"name": "سواق الاتوبيس", "photo": "https://envs.sh/WgU.jpg"},
    {"name": "رسايل بحر", "photo": "https://envs.sh/Wgl.jpg"},
    {"name": "زاير الفجر", "photo": "https://envs.sh/Wgk.jpg"},
    {"name": "ضربه شمس", "photo": "https://envs.sh/Wg8.jpg"},
    {"name": "طيور الظلام", "photo": "https://envs.sh/Wgr.jpg"},
    {"name": "قلب امه", "photo": "https://envs.sh/Wgs.jpg"},
    {"name": "عسل اسود", "photo": "https://envs.sh/Wg9.jpg"},
    {"name": "ظرف طارق", "photo": "https://envs.sh/Wgv.jpg"},
    {"name": "في محطه مصر", "photo": "https://envs.sh/WgN.jpg"},
    {"name": "فتاه المصنع", "photo": "https://envs.sh/WgH.jpg"},
    {"name": "ميكرفون", "photo": "https://envs.sh/Wgg.jpg"},
    {"name": "يارب ولد", "photo": "https://envs.sh/Wgf.jpg"},
    {"name": "يارب ولد", "photo": "https://envs.sh/Wgf.jpg"},
    {"name": "ليل وقضبان", "photo": "https://envs.sh/WgM.jpg"},
    {"name": "نهر الخوف", "photo": "https://envs.sh/Wgy.jpg"},
    {"name": "مطب صناعي", "photo": "https://envs.sh/WgX.jpg"},
    {"name": "مافيا", "photo": "https://envs.sh/Wgx.jpg"},
    {"name": "جزيره الشيطان", "photo": "https://envs.sh/Wg-.jpg"},
    {"name": "زهايمر", "photo": "https://envs.sh/WfD.jpg"},
    {"name": "اذاعه حب", "photo": "https://envs.sh/WfQ.jpg"},
    {"name": "صرخه نمله", "photo": "https://envs.sh/Wfh.jpg"},
    {"name": "كف القمر", "photo": "https://envs.sh/Wfd.jpg"},
    {"name": "الخليه", "photo": "https://envs.sh/Wf2.jpg"},
    {"name": "قبضه الهلالي", "photo": "https://envs.sh/Wft.jpg"},
    {"name": "عيون الصقر", "photo": "https://envs.sh/Wfb.jpg"},
    {"name": "الارجواز", "photo": "https://envs.sh/WfP.jpg"},
    {"name": "الانس والجن", "photo": "https://envs.sh/Wfq.jpg"},
    {"name": "خمسه باب", "photo": "https://envs.sh/Wf0.jpg"},
    {"name": "ديل سمكه", "photo": "https://envs.sh/Wfc.jpg"},
    {"name": "المومياء", "photo": "https://envs.sh/WfL.jpg"},
    {"name": "الكيف", "photo": "https://envs.sh/WfG.jpg"},
    {"name": "كتكوت", "photo": "https://envs.sh/Wfz.jpg"},
    {"name": "الباشا تلميذ", "photo": "https://envs.sh/WfU.jpg"},
    {"name": "فيلم هندي", "photo": "https://envs.sh/Wfl.jpg"},
    {"name": "السفاح", "photo": "https://envs.sh/Wfr.jpg"}, 
    {"name": "السفاح", "photo": "https://envs.sh/Wfr.jpg"}, 
    {"name": "الحفيد", "photo": "https://envs.sh/WaW.jpg"}, 
    {"name": "الكرنك", "photo": "https://envs.sh/WaT.jpg"}, 
    {"name": "كباريه", "photo": "https://envs.sh/WaA.jpg"}, 
    {"name": "حبيبي نائما", "photo": "https://envs.sh/Wac.jpg"}, 
    {"name": "المجرم", "photo": "https://envs.sh/Wa3.jpg"}, 
    {"name": "ضغط عالي", "photo": "https://envs.sh/WaC.jpg"}, 
    {"name": "القرد بيتكلم", "photo": "https://envs.sh/Wa1.jpg"}, 
    {"name": "مولانا", "photo": "https://envs.sh/Wa4.jpg"}, 
    {"name": "الشموع السوداء", "photo": "https://envs.sh/Wal.jpg"}, 
    {"name": "اخر ديك في مصر", "photo": "https://envs.sh/Wa7.jpg"}, 
    {"name": "عصافير النيل", "photo": "https://envs.sh/WOk.jpg"}, 
    {"name": "كلاشنكوف", "photo": "https://envs.sh/WO8.jpg"}, 
    {"name": "الشياطين", "photo": "https://envs.sh/WO7.jpg"}, 
    {"name": "حبك نار", "photo": "https://envs.sh/WOJ.jpg"}, 
    {"name": "هروب مومياء", "photo": "https://envs.sh/WOo.jpg"}, 
    {"name": "معالي الوزير", "photo": "https://envs.sh/WOr.jpg"}, 
    {"name": "شجيع السيما", "photo": "https://envs.sh/WOs.jpg"}, 
    {"name": "عبود علي الحدود", "photo": "https://envs.sh/WO9.jpg"}, 
    {"name": "عيش الغرام", "photo": "https://envs.sh/WOv.jpg"}, 
    {"name": "المولد", "photo": "https://envs.sh/WON.jpg"}, 
    {"name": "العقرب", "photo": "https://envs.sh/WOH.jpg"}, 
    {"name": "أعدام الحب", "photo": "https://envs.sh/WOg.jpg"}, 
    {"name": "الوردة الحمراء", "photo": "https://envs.sh/WOM.jpg"}, 
    {"name": "الوردة الحمراء", "photo": "https://envs.sh/WOM.jpg"}, 
    {"name": "الساحر", "photo": "https://envs.sh/WOX.jpg"}, 
    {"name": "سحر العيون", "photo": "https://envs.sh/WOV.jpg"}, 
    {"name": "بركان الغضب", "photo": "https://envs.sh/WO-.jpg"}, 
    {"name": "أمير الظلام", "photo": "https://envs.sh/WmD.jpg"}, 
    {"name": "قلب الاسد", "photo": "https://envs.sh/WmE.jpg"}, 
    {"name": "الغسالة", "photo": "https://envs.sh/Wmh.jpg"}, 
    {"name": "عفريت مراتي", "photo": "https://envs.sh/Wmd.jpg"}, 
    {"name": "دم الغزال", "photo": "https://envs.sh/Wmi.jpg"}, 
    {"name": "البلياتشو", "photo": "https://envs.sh/WmW.jpg"}, 
    {"name": "الغواص", "photo": "https://envs.sh/WmT.jpg"}, 
    {"name": "أمير البحار", "photo": "https://envs.sh/Wmp.jpg"}, 
    {"name": "كابوريا", "photo": "https://envs.sh/WOt.jpg"}, 
    {"name": "غرام الأفاعي", "photo": "https://envs.sh/WOe.jpg"}, 
    {"name": "لص بغداد", "photo": "https://envs.sh/WOi.jpg"}, 
    {"name": "الناظر", "photo": "https://envs.sh/WOb.jpg"}, 
    {"name": "حرب أطاليا", "photo": "https://envs.sh/WOP.jpg"}, 
    {"name": "بشتري راجل", "photo": "https://envs.sh/WOw.jpg"}, 
    {"name": "عيون لا تنام", "photo": "https://envs.sh/WO0.jpg"}, 
    {"name": "الفندق", "photo": "https://envs.sh/WOW.jpg"}, 
    {"name": "اللص و الكلاب", "photo": "https://envs.sh/WOB.jpg"}, 
    {"name": "النظارة السوداء", "photo": "https://envs.sh/WOn.jpg"}, 
    {"name": "زوجتي و الكلب", "photo": "https://envs.sh/WOT.jpg"}, 
    {"name": "الزوجه الثانيه", "photo": "https://envs.sh/WOp.jpg"}, 
    {"name": "ابي فوق الشجره", "photo": "https://envs.sh/WOA.jpg"}, 
    {"name": "عروسه النيل", "photo": "https://envs.sh/WOj.jpg"}, 
    {"name": "غرام في الكرنك", "photo": "https://envs.sh/WOc.jpg"}, 
    {"name": "الفلوس", "photo": "https://envs.sh/WOZ.jpg"}, 
    {"name": "الوتر", "photo": "https://envs.sh/WOL.jpg"}, 
    {"name": "كلمني شكرا", "photo": "https://envs.sh/WO5.jpg"}, 
    {"name": "مجنون اميره", "photo": "https://envs.sh/WOG.jpg"}, 
    {"name": "عائله ميكي", "photo": "https://envs.sh/WOK.jpg"}, 
    {"name": "ياباني اصلي", "photo": "https://envs.sh/WOz.jpg"}, 
    {"name": "ابو شنب", "photo": "https://envs.sh/WO3.jpg"}, 
    {"name": "الهرم الرابع", "photo": "https://envs.sh/WOY.jpg"}, 
    {"name": "كنغر حبنا", "photo": "https://envs.sh/WOC.jpg"}, 
    {"name": "بنطلون جوليت", "photo": "https://envs.sh/WOR.jpg"}, 
    {"name": "جحيم تحت الماء", "photo": "https://envs.sh/WOy.jpg"}, 
    {"name": "سلام يا صاحبي", "photo": "https://envs.sh/WOS.jpg"}
]

@Client.on_message(filters.command(["افلام", "فيلم","• افلام •"], ""), group=76006953)
async def afalmme(client, message):
    actor = random.choice(so5raa5)
    bot_username = client.me.username
    user_id = message.from_user.id
    ces5ar5[user_id] = actor['name']
    ur5ers5[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الفيلم....؟ ")

@Client.on_message(filters.text, group=7562065)
async def afa2lm6me(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in ur5ers5:
        correct_actor = ces5ar5.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del ces5ar5[user_id]
            del ur5ers5[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del ces5ar5[user_id]
                del ur5ers5[user_id]

uses1 = {}        
caear1 = {}        

questions = [
    {"photo": "ما هو عدد الكواكب في النظام الشمسي؟", "name": "8"},
    {"photo": "ما هو لون الشمس؟", "name": "أبيض"},
    {"photo": "اسمه من خمسة حروف اذا حذفت اوله بقا ثمان؟", "name": "عثمان"},
    {"photo": "ما الشئ الذي يمتلك أسنان ولا يمكنه العض؟", "name": "المشط"},
    {"photo": "شيء يتجمد إذا تم تسخينه؟", "name": "البيض"},
    {"photo": "يحملك إلى اي مكان اذا حذفت اوله اصبح عظيم الشأن واذا حذفت اخره اصبح غالي الأثمان واذا عكسته تقشعر منه الأبدان؟", "name": "درب"},
    {"photo": "نوع من أنواع الحيوانات يقوم بحك أذنه من خلال أنفه فما هو؟", "name": "الفيل"},
    {"photo": "من هو خال ابن عمتك؟", "name": "ابوك"},
    {"photo": "ما هو الشي الذي يعتبر غير نظيف اذا ابيض لونه؟", "name": "اللسان"},
    {"photo": "ماهو الشيء الذي تراه ولا يراك؟", "name": "الظل"},
    {"photo": "يطير مثل الطيور ولكنه لا يغادر مكانه؟", "name": "العلم"},
    {"photo": "ماهو الشيء الذي لايقطع إلا اذا ادخلت اصابعك في عينيه؟", "name": "المقص"},
    {"photo": "ما هو الشيء الذي يمر خلال الباب ولا يدخل؟", "name": "المفتاح"},
    {"photo": "بيت لا يوجد له أبواب ولا نوافذ فما هو؟", "name": "بيت الشعر"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "الببغاء"},
    {"photo": "اين يوجد البحر الذي بدون ماء؟", "name": "الخريطه"},
    {"photo": "لي رقبة وليس لدي رأس ولي ذراعين وليس لدي يدين ما هذا؟", "name": "القميص"},
    {"photo": "ما الشخص الي يبدو بسيط لكن يحني له الملك رأسه؟", "name": "الحلاق"},
    {"photo": "شيء اذا رايناه لا نركبه واذا ركبناه فلا نره فما هو؟", "name": "النعش"},
    {"photo": "اوله ثالث تفاحة واخر التفاح ثانيه ورابع العمر له ثالث واخر الورد باقيه؟", "name": "احمد"},
    {"photo": "من هو النبي الذي مات ولم يولد؟", "name": "ادم"},
    {"photo": "شيء من الممكن ان يكون له خيال من الامام او الخلف ومن الممكن يكون بداخله؟", "name": "الحفرة"},
    {"photo": "شيء يستطيع التحدث بكل لغات العالم؟", "name": "صدى الصوت"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "حيوان يمشي ويقف بالرغم من أنه ليس لديه أقدام؟", "name": "الثعبان"},
    {"photo": "نوع من انواع الطيور يتكون من حرفين واذا قلبت الكلمة صارت اسم مهنة؟", "name": "بط"},
    {"photo": "مدينة لا يطحن فيها الدقيق ولا يموت فيها الميت؟", "name": "كل المدن"},
    {"photo": "ما هو الشيء الذي يعبر البحر دون أن يتبلل غير العجل في بطن أمه؟", "name": "الطائره"},
    {"photo": "ماهو الشيء الذي يبكي اذا لففت راسه؟", "name": "الحنفيه"},
    {"photo": "انا لا املك حياة ولكنني اموت فما اكون؟", "name": "البطاريه"},
    {"photo": "ما هو الشيء الذي يطلبه الناس دائمًا وإذا جاء هربوا منه؟", "name": "المطر"},
    {"photo": "فاكهة اسمها على اسم طائر؟", "name": "الكيوي"},
    {"photo": "ما هو الجرح الذي لا ينزف دم في جسم الإنسان؟", "name": "جرح المشاعر"},
    {"photo": "يطلع من بطن امه ويحك ظهر ابوه ويموت فما هو؟", "name": "عود الكبريت"},
    {"photo": "ماهو الشيء الذي تأكل منه مع إنه لا يؤكل؟", "name": "الصحن"},
    {"photo": "ماهو الشيء الذي نرميه بعد العصر؟", "name": "البرتقال"},
    {"photo": "ما الاسم الذي إذا حذفت اوله صار اسمين؟", "name": "ياسمين"},
    {"photo": "ماهو الشيء الذي يقرصك ولا تراه؟", "name": "الجوع"},
    {"photo": "شيء موجود في الليل ثلاث مرات وفي النهار مرة واحدة؟", "name": "حرف اللام"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "حرف اللام"},
    {"photo": "كلما كان هناك المزيد قل ما تراه ما هذا؟", "name": "الضباب"},
    {"photo": "ماهو الشيء الذي يسير ولا يمتلك أقدام؟", "name": "الساعه"},
    {"photo": "يتم أخذها منك قبل أن تأخذها؟", "name": "الصوره"},
    {"photo": "ماهو الشيء الذي يوجد وسط باريس؟", "name": "حرف الراء"},
    {"photo": "هو اليف ولكن اذا صار بالأبيض والاسود صار متوحش فما يكون؟", "name": "الحمار"},
    {"photo": "شيء تسمعه ولكن لا يسمعك تراه ولكن لا يراك؟", "name": "التلفاز"},
    {"photo": "شئ قلبه ابيض ويرتدي قبعة خضراء لكن لونه اسود؟", "name": "الباذنجان"},
    {"photo": "ماهو الشيء الذي له اعين ثلاث بينما له قدم واحدة؟", "name": "اشارة المرور"},
    {"photo": "ما هو الحيوان الأبكم الذي لا يتكلم ولا نسمع له صوت؟", "name": "الزرافه"},
    {"photo": "شيء اذا لمسته يصرخ؟", "name": "الجرس"},
    {"photo": "انا املك كل المعلومات التي تعرفها وانا اصغر من قبضة يدك من اكون؟", "name": "العقل"},
    {"photo": "ما هو الشيء الذي درجة حرارته ثابته سواء وضعته في الثلاجه أو على النار؟", "name": "الفلفل"},
    {"photo": "ماهي الفاكهة الصلبة التي يوجد بداخلها حليب؟", "name": "جوز الهند"},
    {"photo": "تاجر من التجار إذا اقتلعنا عينه طار فمن هو؟", "name": "عطار"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "بلد إسلامي اوله عبادة واخره نقود فما هو؟", "name": "الصومال"},
    {"photo": "ما هي الفاكهة التي تُجفف لتصبح زبيب؟", "name": "العنب"},
    {"photo": "شيء يغلبك دون ان يؤذيك؟", "name": "النوم"},
    {"photo": "ماهو الشيء الذي تشتريه لونه أسود ولكنك لاتستفيد منه إلا بعد أن يصبح لونه أحمر؟", "name": "الفحم"},
    {"photo": "طوله حوالي شبر ويحمل أطول من متر ماهو؟", "name": "الحذاء"},
    {"photo": "صغير الحجم لا تلقى له بال ولكن بوجهه تفتح الأبواب؟", "name": "المفتاح"},
    {"photo": "ماهما الميتتان التي يجوز اكلهما بدون اثم؟", "name": "السمك والجراد"},
    {"photo": "سيد وسيدة لديهما ست بنات وكل ابنة لها أخ واحد كم عدد أفراد العائلة؟", "name": "تسعه"},
    {"photo": "إذا كان سعيد على يمين سمير وجابر على يمين سعيد فمن يكون في الوسط؟", "name": "سعيد"},
    {"photo": "احمر وليس احمر اسود وليس اسود وابيض وليس ابيض ماهو؟", "name": "البحر"},
    {"photo": "ان ابتسمت لها ابتسمت لك ماهي؟", "name": "المراه"},
    {"photo": "ما هو أهون موجود و أعز مفقود؟", "name": "الماء"},
    {"photo": "الشيء الذي إذا ذبح بكى عليه الجميع؟", "name": "البصل"},
    {"photo": "من هو الشخص الذي يمشي على الأرض ولكنه يطول النجوم أيضًا؟", "name": "الظابط"},
    {"photo": "إنسان وزوجته لا هو من بني آدم ولا هي من بنات حواء من هما؟", "name": "ادم وحواء"},
    {"photo": "ما هو الشيء الذي يحمل طعامه فوق رأسه فإذا مشى أكل منه وإذا سكن غطى رأسه ونام؟", "name": "قلم الحبر"},
    {"photo": "ما هو الشيء الذي يحيا في أول الشهر ويموت في آخر الشهر؟", "name": "القمر"},
    {"photo": "ما الذي يمكنه أن يملأ الغرفة دون أن يشغل حيزا؟", "name": "النور"},
    {"photo": "طائر إذا قمت بقلب حروف اسمه رأيت عجب؟", "name": "بجع"},
    {"photo": "ينام بالحذاء ولا يخلعه؟", "name": "الحصان"},
    {"photo": "ما هي الكلمة الوحيدة التي تلفظ غلط دائمًا؟", "name": "غلط"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "اسم حيوان اذا قمت بتغيير اول حرف منه اصبح اهم عضو في جسم الإنسان؟", "name": "قلب"},
    {"photo": "ماهو الشئ الموجود في كل شيء؟", "name": "الاسم"},
    {"photo": "امرأة عقيم هل تنجب ابنتها أطفال؟", "name": "العقيم لا تلد"},
    {"photo": "ما هو الشئ الذي يمكن كسره دون ان نلمسه؟", "name": "الوعد"},
    {"photo": "قلعة خضراء وأرضها حمراء وسكانها لونهم أسود فما هي؟", "name": "البطيخه"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "ماهي الدولة التي حارب اهلها الذباب والعصافير لخطورتها؟", "name": "الصين"},
    {"photo": "ما هي اسم الفاكهة التي سُميت بإحدى سور القرآن الكريم باسمها؟", "name": "التين"},
    {"photo": "شيء كلما كان موجود كلما قل ماتراه؟", "name": "الظلام"},
    {"photo": "عقرب لا يلدغ ولا يسبب الذعر لأي أحد حتى الأطفال؟", "name": "عقرب الساعه"},
    {"photo": "فاكهة بها حبات اللؤلؤ؟", "name": "الرمان"},
    {"photo": "شيء موجود في الدقيقة مرتين ولا يوجد في الساعة؟", "name": "حرف القاف"},
    {"photo": "مدينة سعودية اسمها على اسم نبات فما هي؟", "name": "عرعر"},
    {"photo": "ماهو الشيء الذي كلما عرضته للشمس ازداد بللا؟", "name": "الثلج"},
    {"photo": "ما هو الشيء الذى كلما خطا خطوه فقد شيئًا من ذيله؟", "name": "ابره الخياطه"},
    {"photo": "ماهو الشيء الذي يتحرك بدون أرجل ويبكي بدون عيون؟", "name": "السحاب"},
    {"photo": "ما هو الشيء الذي بإمكانك تحقيقه دون بذل عناء؟", "name": "الفشل"},
    {"photo": "شيء اذا اطعمناه لا يشبع واذا سقيناه يموت؟", "name": "النار"},
    {"photo": "شيء ليس له بداية ولا نهاية ما هو هذا الشيء؟", "name": "الدائره"},
    {"photo": "طائر يلد ولايبيض فما هو؟", "name": "الخفاش"},
    {"photo": "شيء في السماء وليس في الماء فما هو؟", "name": "حرف السين"},
    {"photo": "شيء تملكه انت ولكن يستخدمه الآخرون اكثر منك؟", "name": "الاسم"},
    {"photo": "جزء من الجنة يعيش معنا في الأرض ما هو؟", "name": "الحجر الاسود"},
    {"photo": "يمتلك بحيرات بلا ماء وأراضي بلا زرع وجبال بلا أحجار؟", "name": "الخريطه"},
    {"photo": "اي كلمة تصبح اقصر اذا اضفت لها حرف؟", "name": "قصر"},
    {"photo": "ما هي درجة القرابة طفل من والده الحقيقي لكن هذا الطفل ليس ابنه؟", "name": "ابنته"},
    {"photo": "ماهو الشجر الذي يسميه الناس قاتل ابيه؟", "name": "الموز"},
    {"photo": "شيء يمكن قياسه لكن لايمكن رؤيته؟", "name": "الوقت"},
    {"photo": "ماهو الشيء الذي ينام ولا يقوم؟", "name": "الرماد"},
    {"photo": "شيء يمشي أمامك ولا تستطيع رؤيته؟", "name": "المستقبل"},
    {"photo": "شهر هجري اذا حذفت وسطه يتحول الي فاكهة؟", "name": "رمضان"}, 
    {"photo": "هو شيء يكون لونه أخضر في الأرض وأسود في الأسواق وأحمر في الأكواب، فما هو؟", "name": "الشاي"},
    {"photo": "يمكنه رفع الأثقال، لكنه لا يستطيع أن يمسك مسمار", "name": "البحر"},
    {"photo": "يقول الحقيقة ويكذب عندما يكون جائعا", "name": "الساعه"} 
]

@Client.on_message(filters.command(["لغز", "فزوره","• لغز •"], ""), group=6456565)
async def fazoraa(client, message):
    actor = random.choice(questions)
    bot_username = client.me.username
    user_id = message.from_user.id
    caear1[user_id] = actor['name']
    uses1[user_id] = user_id
    await message.reply_text(actor['photo'])

@Client.on_message(filters.text, group=5013245)
async def logzee(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in uses1:
        correct_actor = caear1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del caear1[user_id]
            del uses1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del caear1[user_id]
                del uses1[user_id]
                
uss2 = {}        
cear2 = {}        

qustions = [
    {"photo": "🏨🏨🏨🏨🏨🏣🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨", "name": "🏣"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "↗️↗️↗️↗️↗️↗️↗️↗️↗️⬆️↗️↗️↗️↗️↗️↗️↗️↗️↗️↗️", "name": "⬆️"},
    {"photo": "🍅🍅🍅🍅🍅🍅🍎🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅", "name": "🍎"},
    {"photo": "📫📫📫📫📫📫📫📪📫📫📫📫📫📫📫📫📫📫📫📫", "name": "📪"},
    {"photo": "🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇬🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫", "name": "🇳🇬"},
    {"photo": "💗💗💗💗💗💗💗💗💗🩷💗💗💗💗💗💗💗", "name": "🩷"},
    {"photo": "🔂🔂🔂🔂🔂🔂🔂🔁🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂", "name": "🔁"},
    {"photo": "😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰??😰😰😰😰😰😰😰😰😰😰", "name": "😨"},
    {"photo": "📥📥📥📤📥📥📥📥📥📥📥📥📥📥📥📥", "name": "📤"},
    {"photo": "🦡🦡🦡🦡🦝🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡", "name": "🦝"},
    {"photo": "👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂", "name": "👮"},
    {"photo": "🔼🔼🔼🔼🔼🔼🔽🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼", "name": "🔽"},
    {"photo": "👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕🧑‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕", "name": "🧑‍⚕"},
    {"photo": "💓💓💓💓💓💓💗💓💓💓💓💓💓💓💓💓💓💓💓", "name": "💗"},
    {"photo": "🚞🚞🚞🚞🚞🚃🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞", "name": "🚃"},
    {"photo": "😫😫😫😫😫😫😩😫😫😫😫😫😫😫😫😫😫😫😫😫😫", "name": "😩"},
    {"photo": "🧚‍♂🧚🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂", "name": "🧚"},
    {"photo": "😥😥😥😥😥😥😥😢😥😥😥😥😥😥😥😥😥😥😥😥😥", "name": "😢"},
    {"photo": "⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⏳⌛️⌛️⌛️", "name": "⏳"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "🌇🌇🌇🌇🌇🌆🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇", "name": "🌆"},
    {"photo": "🌗🌗🌗🌗🌗🌗🌓🌗🌗🌗🌗🌗🌗🌗🌗🌗", "name": "🌓"},
    {"photo": "🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🫢🤭🤭🤭🤭🤭🤭", "name": "🫢"},
    {"photo": "◼️◼️◼️🔳◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️", "name": "🔳"},
    {"photo": "🐓🐓🐓🐓🐓🪿🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓", "name": "🪿"},
    {"photo": "🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂", "name": "🧖"},
    {"photo": "🛠🛠🛠🛠🛠⚒🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠", "name": "⚒"},
    {"photo": "🕖🕖🕖🕖🕖🕖🕦🕖🕖🕖🕖🕖🕖🕖🕖🕖🕖", "name": "🕦"},
    {"photo": "😏😏😏😏😏😏😒😏😏😏😏😏😏😏😏😏😏😏", "name": "😒"},
    {"photo": "😮😮😮😮😮😮😮😦😮😮😮😮😮😮😮😮😮😮😮😮😮😮😮", "name": "😦"},
    {"photo": "🛬🛬🛬🛬🛫🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬", "name": "🛫"},
    {"photo": "🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂😶🙂🙂", "name": "😶"},
    {"photo": "🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙊🙉🙉", "name": "🙊"},
    {"photo": "🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇸🇩🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸", "name": "🇸🇩"},
    {"photo": "🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇹🇩🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪", "name": "🇹🇩"},
    {"photo": "🎥🎥🎥🎥🎥🎥🎥🎥🎥📹🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥", "name": "📹"},
    {"photo": "🖊🖊🖊🖊🖊🖋🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊", "name": "🖋"},
    {"photo": "🛌🛌🛌🛏🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌", "name": "🛌"},
    {"photo": "🔒🔒🔒🔒🔒🔒🔒🔓🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒", "name": "🔓"},
    {"photo": "👨‍💻👨‍💻👨‍💻👨‍💻🧑‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻", "name": "👨‍💻"},
    {"photo": "📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📄📑📑📑📑📑📑📑📑", "name": "📄"},
    {"photo": "🦻🦻🦻🦻🦻🦻👂🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻", "name": "👂"},
    {"photo": "⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈🌨⛈⛈⛈⛈", "name": "🌨"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🦏🦏🦏🦏🦏🦏🦏🦏🦏🐘🦏🦏🦏🦏🦏🦏🦏🦏🦏🦏", "name": "🐘"},
    {"photo": "💿💿💿💿💿💿💿💿📀💿💿💿💿💿💿💿", "name": "📀"},
    {"photo": "😐😐😐😐😐😐😑😐😐😐😐😐😐😐😐😐😐😐😐😐😐", "name": "😑"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "🩶🩶🩶🩶🩶🩶🩶🩶🤍🩶🩶🩶🩶🩶🩶🩶🩶", "name": "🤍"},
    {"photo": "🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♀🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂", "name": "🏋‍♀"},
    {"photo": "🇪🇬🇪🇬🇪🇬🇪🇬🇾🇪🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬", "name": "🇾🇪"},
    {"photo": "📸📸📸📸📸📸📸📷📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸", "name": "📷"},
    {"photo": "📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📱📲📲📲📲📲📲📲📲📲", "name": "📱"},
    {"photo": "🔆🔆🔆🔆🔆🔅🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆", "name": "🔅"},
    {"photo": "🏬🏬🏬🏬🏬🏬🏬🏬🏢🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬", "name": "🏢"},
    {"photo": "🥋🥋🥋🥋🥋🥋🥋🥼🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋", "name": "🥼"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "😧😧😧😧😧😧😧😧😧😧😯😧😧😧😧😧😧😧😧😧😧😧", "name": "😯"},
    {"photo": "🍽🍽🍽🍽??🍽🍽🍽🍽🍴🍽🍽🍽🍽🍽🍽🍽🍽🍽🍽", "name": "🍴"},
    {"photo": "📆📆📆📆📆📅📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆", "name": "📅"},
    {"photo": "🍀🍀🍀🍀🍀🍀🍀🍀☘🍀🍀🍀🍀🍀🍀🍀", "name": "☘"},
    {"photo": "🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚅🚄🚄🚄🚄🚄🚄🚄", "name": "🚅"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🌍🌍🌍🌍🌍🌏🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍", "name": "🌏"},
    {"photo": "🤹‍♀🤹‍♀🤹‍♀🤹🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀", "name": "🤹"},
    {"photo": "🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔉🔈🔈🔈🔈🔈", "name": "🔉"},
    {"photo": "⛰⛰⛰⛰⛰⛰🏔⛰⛰⛰⛰⛰⛰⛰⛰⛰", "name": "🏔"},
    {"photo": "😸😸😸😺😸😸😸😸😸😸😸😸😸😸😸😸😸", "name": "😺"},
    {"photo": "👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯🚶‍♀👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯", "name": "🚶‍♀"},
    {"photo": "❓❓❓❓❔❓❓❓❓❓❓❓❓❓❓❓❓", "name": "❔"},
    {"photo": "🔕🔕🔕🔕🔕🔕🔕🔕🔕🔔🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕", "name": "🔔"},
    {"photo": "🖐🖐🖐🖖🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐", "name": "🖖"},
    {"photo": "☃️☃️☃️☃️☃️☃️☃️⛄️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️", "name": "⛄️"},
    {"photo": "😌😌😌😌😌😌😌😌😌😌☺️😌😌😌😌😌", "name": "☺️"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍??👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🥼🧥🧥🧥🧥🧥🧥🧥🧥", "name": "🥼"},
    {"photo": "⏯⏯⏯⏯⏯⏸⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯", "name": "⏸"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🔨🔨🔨🔨⛏🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨", "name": "⛏"},
    {"photo": "📂📂📂📂📂📂📁📂📂📂📂📂📂📂📂📂", "name": "📁"},
    {"photo": "🦀🦀🦀🦀🦀🦀🦀🦞🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀", "name": "🦞"},
    {"photo": "👿👿👿👿👿😈👿👿👿👿👿👿👿👿👿👿👿👿👿👿👿", "name": "😈"},
    {"photo": "🔳🔳🔳🔳🔳🔳🔳🔳🔳◼️🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳", "name": "◼️"},
    {"photo": "🐼🐼🐼🐼🐼🐼🐼🐻‍❄️🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼", "name": "🐻‍❄️"},
    {"photo": "🔎🔎🔎🔎🔎🔎🔎🔎🔎🔍🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎", "name": "🔍"},
    {"photo": "🤼‍♂🤼🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂", "name": "🤼"},
    {"photo": "👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀🧑‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀", "name": "🧑‍🚀"}
]

@Client.on_message(filters.command(["مختلف", "اختلاف","الاختلاف","• مختلف •"], ""), group=6565065)
async def moktlf(client, message):
    actor = random.choice(qustions)
    bot_username = client.me.username
    user_id = message.from_user.id
    cear2[user_id] = actor['name']
    uss2[user_id] = user_id
    await message.reply_text(actor['photo'])

@Client.on_message(filters.text, group=5012465)
async def alatlaf(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    if user_id in uss2:
        correct_actor = cear2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text("احسنت، الإجابة صحيحة ✨♥")
            points[user_id]= points.get(user_id, 0) + 1
            del cear2[user_id]
            del uss2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"خطأ 😔💔 الإجابة هي: \n [{correct_actor}]({soesh})")
                del cear2[user_id]
                del uss2[user_id]
            
            
@Client.on_message(filters.command("نقاطي", ""), group=908070)
async def check_points(client, message):
    user_id = message.from_user.id
    if user_id in points:
        point = points.get(user_id)
        await message.reply_text(f"لديك {point} نقطة.")
    else:
        await message.reply_text("معكش نقاط اصلا")

@Client.on_message(filters.command("توب النقاط", ""), group=918171)
async def top_points(client, message):
    user_id = message.from_user.id	
    sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)   
    k = 0
    text = "اكثر الاشخاص الي معاها نقاط:\n\n"    
    for user_id, point in sorted_points:
        user = await client.get_users(user_id)
        k += 1
        text += f"{k}: {user.mention} : {point}\n"
        if k >= 5:
            break
    await message.reply_text(text)