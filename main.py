import threading
import asyncio
from flask import Flask
from bot import start_zombiebot  # استدعاء دالة تشغيل البوت

# --- إعداد سيرفر Flask ---
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    # تشغيل Flask على بورت 8000
    app.run(host='0.0.0.0', port=8000, use_reloader=False)

# --- التشغيل الرئيسي ---
if __name__ == "__main__":
    # 1. تشغيل Flask في خيط منفصل (Background)
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("✅ Flask Server Started on port 8000")

    # 2. تشغيل البوت (هذا الأمر سيمنع الكود من الإغلاق)
    try:
        asyncio.run(start_zombiebot())
    except KeyboardInterrupt:
        print("❌ Bot Stopped")
