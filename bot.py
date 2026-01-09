async def start_zombiebot():
    logger.info("جاري تشغيل البوت...")
    await bot.start()
    
    # --- كود إرسال رسالة التشغيل المصلح ---
    try:
        from casery import caserid
        # الحصول على معلومات المطور والبوت
        me = await bot.get_me()
        bot_username = me.username
        
        msg = f"""
✅ **تم تشغيل البوت بنجاح**

🤖 **يوزر البوت:** @{bot_username}
🆔 **أيدي المطور:** `{caserid}`
🕒 **الوقت:** {os.popen('date').read()} (Server Time)

🚀 النظام يعمل الآن بالكامل!
"""
        await bot.send_message(caserid, msg)
        logger.info(f"✅ Startup message sent to {caserid}")
    except Exception as e:
        logger.warning(f"⚠️ فشل إرسال رسالة التشغيل للمطور: {e}")
    # --------------------------------------

    if bot_token2:
        logger.info("جاري تشغيل المساعد...")
        try:
            await lolo.start()
        except Exception as e:
            logger.warning(f"⚠️ فشل تشغيل المساعد: {e}")
            
    logger.info("🚀 النظام يعمل الآن بالكامل!")
    await idle()
