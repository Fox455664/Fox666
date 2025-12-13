FROM python:3.10

# 1. تحديث وتسطيب ffmpeg و git و redis-server
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg git redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. تحديث pip
RUN pip3 install -U pip

# 3. تسطيب المكاتب (بالإصدار الصحيح 1.1.0 + redis)
RUN pip3 install --no-cache-dir pyrogram tgcrypto py-tgcalls==1.1.0 yt-dlp youtube-search-python youtube-search aiohttp Pillow numpy unidecode aiofiles pyromod requests redis gTTS pytz kvsqlite beautifulsoup4 telegraph wget python-dotenv

# 4. تجهيز الملفات
COPY . /app/
WORKDIR /app/

# 5. أمر التشغيل (بيشغل الـ Redis في الخلفية وبعدين يشغل البوت)
CMD redis-server --daemonize yes && python3 main.py
