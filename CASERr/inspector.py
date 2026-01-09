import traceback
from pyrogram import Client, filters
from pyrogram.types import Message

# ==============================================================================
# 🧨 EARLY INSPECTOR
# يشتغل قبل أي Handler في السورس كله
# ==============================================================================

@Client.on_message(filters.all, group=-999999)
async def early_inspector(client, message: Message):
    try:
        user_id = message.from_user.id if message.from_user else None
        username = (
            f"@{message.from_user.username}"
            if message.from_user and message.from_user.username
            else "NoUser"
        )

        text = message.text or f"[{message.media}]"

        print(
            f"\n🧨 [EARLY] "
            f"user={username} ({user_id}) | "
            f"chat={message.chat.id} | "
            f"text={text}"
        )

        # لازم نكمّل عشان باقي الملفات تشتغل
        message.continue_propagation()

    except Exception as e:
        print("❌ ERROR in early_inspector")
        traceback.print_exc()
        message.continue_propagation()


# ==============================================================================
# 🧪 START PROBE
# يثبت هل /start بيوصل ولا بيتقتل
# ==============================================================================

@Client.on_message(filters.command("start"), group=-999998)
async def start_probe(client, message: Message):
    try:
        print("🧪 /start وصل للبوت")
        await message.reply_text("🧪 /start وصل للبوت (debug)")
        message.continue_propagation()

    except Exception:
        print("❌ ERROR in start_probe")
        traceback.print_exc()
        message.continue_propagation()
