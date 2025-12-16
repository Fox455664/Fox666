import asyncio
from pyrogram import Client
from aiohttp import web
import sys
from bot import start_zombiebot

# --- وظيفة سيرفر الويب (عشان Koyeb) ---
async def web_server():
    async def handle(request):
        return web.Response(text="Bot is running correctly!")

    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Koyeb بيحتاج البورت 8000
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
    print("✅ Web Server started on port 8000")

# --- وظيفة التشغيل الرئيسية ---
async def main():
    # 1. نشغل السيرفر الأول عشان Koyeb ميفصلش البوت
    await web_server()
    
    # 2. نشغل البوت
    try:
        await start_zombiebot()
        print("✅ Bot started successfully")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        # لو البوت فشل، منقفلش السكريبت عشان السيرفر يفضل شغال ونشوف اللوج
        
    # 3. نفضل مشغلين البوت للأبد
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
