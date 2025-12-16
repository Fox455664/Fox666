import asyncio
from pyrogram import Client
import os
import sys
import logging
from bot import start_zombiebot

# ================= Flask =================
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

# =========================================

# إعداد السجلات
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Main")

async def main():
    logger.info("Initializing system...")

    # تشغيل Flask في Thread منفصل
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    try:
        await start_zombiebot()
    except Exception as e:
        logger.error(f"CRITICAL ERROR in main loop: {e}", exc_info=True)

    logger.info("Service is running. Press Ctrl+C to stop.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.critical(f"Fatal startup error: {e}", exc_info=True)
