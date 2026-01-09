import threading
import asyncio
from flask import Flask
from bot import bot, lolo, start_zombiebot # استدعاء البوت والمساعد ودالة التشغيل

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    app.run(host='0.0.0.0', port=8000, use_reloader=False)

if __name__ == "__main__":
    # 1. تشغيل Flask في الخلفية عشان السيرفر ميفصلش
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("✅ Flask Server Started on port 8000")

    # 2. تشغيل البوت (نظام القيصر)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_zombiebot())
    except KeyboardInterrupt:
        print("❌ Stopped")
