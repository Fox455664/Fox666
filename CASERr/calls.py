from pytgcalls.types import Update, StreamAudioEnded
from CASERr.daty import get_call

async def Call(bot_username):
    hoss = await get_call(bot_username)

    @hoss.on_stream_end()
    async def stream_end_handler(client, update: Update):
        if not isinstance(update, StreamAudioEnded):
            return

        try:
            # استدعاء دالة التغيير من ملف التشغيل
            # الاستيراد هنا داخلي عشان نمنع أي مشاكل
            from CASERr.play import change_stream
            await change_stream(bot_username, update.chat_id, client)
        except Exception as e:
            print(f"Error in stream_end_handler: {e}")
