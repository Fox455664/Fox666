async def start_zombiebot():
    global bot_id

    logger.info("جاري تشغيل البوت الأساسي...")
    await bot.start()

    me = await bot.get_me()
    bot_id = me.id
    logger.info(f"✅ تم تشغيل البوت: @{me.username} | ID: {bot_id}")

    logger.info("جاري تشغيل الحساب المساعد...")
    try:
        await lolo.start()
    except Exception as e:
        logger.warning(f"⚠️ فشل تشغيل الحساب المساعد: {e}")

    if casery:
        await bot.send_message(casery, "✅ تم تشغيل البوت بنجاح")

    logger.info("🚀 النظام يعمل الآن بالكامل")
    await idle()
