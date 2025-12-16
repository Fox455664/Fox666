import asyncio
import logging
import threading
from flask import Flask

from bot import start_zombiebot

# ======================
# Flask Health Check
# ======================
app = Flask(__name__)

@app.route("/")
def health():
    return "OK", 200


def run_flask():
    app.run(host="0.0.0.0", port=8000)


# ======================
# Logging
# ======================
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)
logger = logging.getLogger("Main")


# ======================
# Main
# ======================
async def main():
    logger.info("Initializing system...")
    await start_zombiebot()


if __name__ == "__main__":
    # تشغيل Flask في Thread
    threading.Thread(target=run_flask, daemon=True).start()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
    except Exception as e:
        logger.critical(f"Fatal startup error: {e}", exc_info=True)
