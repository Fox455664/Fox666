import os
import sys
import subprocess
import threading
from flask import Flask

# --- سيرفر وهمي لإرضاء Koyeb ---
app = Flask(__name__)
@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    # سيعمل على المنفذ 8000 الذي يطلبه Koyeb
    app.run(host='0.0.0.0', port=8000)

# تشغيل السيرفر في خيط (Thread) منفصل
threading.Thread(target=run_flask, daemon=True).start()
# --------------------------------

# --- كود التثبيت التلقائي للمكتبات ---
def install_missing_libraries():
    required_packages = ["telethon", "oldpyro", "pytube", "flask"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_missing_libraries()
# -----------------------------------

import asyncio
from pytgcalls import idle
from bot import *
from pyromod import listen

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_zombiebot())
    except Exception as e:
        print(f"Error: {e}")
