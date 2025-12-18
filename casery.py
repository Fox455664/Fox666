import os

# المطورين الاحتياطيين للسورس
caes = ["f_o_x_351", "zozooryy", "cyv0we"]

# جلب البيانات من Koyeb
casery = os.getenv("OWNER_USERNAME", "f_o_x_351").replace("@", "")
caserid = int(os.getenv("OWNER_ID", "7669264153")) # تأكد من وضع ID الخاص بك في Koyeb
OWNER = os.getenv("BOT_NAME_AR", "النسور")
muusiic = os.getenv("MUSIC_TEXT", "SOURCE Titanx")
suorce = os.getenv("SOURCE_NAME_IMG", "SOURCE Titanx")
source = os.getenv("SOURCE_CHANNEL_LINK", "https://t.me/fox68899")
ch = os.getenv("SOURCE_CHANNEL_USER", "fox68899").replace("@", "")
group = os.getenv("SOURCE_GROUP_LINK", "https://t.me/fox68899")
photosource = os.getenv("SOURCE_PHOTO_URL", "https://envs.sh/ws4.webp")

bot_token = os.getenv("BOT_TOKEN")
bot_token2 = os.getenv("SESSION_STRING")

# Redis Configuration (يفضل استخدام رابط خارجي من Upstash أو Redislabs)
REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")
