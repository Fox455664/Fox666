# --- START OF FILE main.py ---
import asyncio
from pyrogram import Client
import os
import sys
import random
from bot import start_zombiebot
from pyromod import listen

async def main():
    await start_zombiebot()
    print("Bot is running...")
    await asyncio.Event().wait()  # يخلي البوت شغال دايمًا

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
# --- END OF FILE main.py ---
