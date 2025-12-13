# --- START OF FILE casery.py ---
import os

# -- IMPORTANT --
# هنجيب البيانات من إعدادات Koyeb عشان نضمن إنها الجديدة
# ومتتكتبش هنا عشان لو الحساب اتحظر منعدلش في الكود

caes = ["@f_o_x_351", "zozooryy", "@cyv0we"]
casery = os.getenv("OWNER_USERNAME", "f_o_x_351")
caserid = int(os.getenv("OWNER_ID", "7669264153"))
OWNER = os.getenv("BOT_NAME_AR", "النسور")
muusiic = os.getenv("MUSIC_TEXT", "SOURCE Titanx")
suorce = os.getenv("SOURCE_NAME_IMG", "SOURCE Titanx")
source = os.getenv("SOURCE_CHANNEL_LINK", "https://t.me/fox68899")
ch = os.getenv("SOURCE_CHANNEL_USER", "fox68899")
group = os.getenv("SOURCE_GROUP_LINK", "https://t.me/fox68899")
photosource = os.getenv("SOURCE_PHOTO_URL", "https://envs.sh/ws4.webp")

# هنا التغيير المهم: مسحنا القيم القديمة عشان يجبرها تيجي من Koyeb
bot_token = os.getenv("BOT_TOKEN")
bot_token2 = os.getenv("SESSION_STRING")

# لو القيم مش موجودة نطلع خطأ عشان نعرف
if not bot_token:
    print("Error: BOT_TOKEN is missing in Environment Variables!")
if not bot_token2:
    print("Error: SESSION_STRING is missing in Environment Variables!")
# --- END OF FILE casery.py ---
