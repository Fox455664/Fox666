FROM python:3.10

# تحديث وتسطيب ffmpeg الضروري
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# تسطيب المكاتب (تم إضافة youtube-search)
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir pyrogram tgcrypto py-tgcalls yt-dlp youtube-search-python youtube-search aiohttp Pillow numpy unidecode aiofiles pyromod requests redis gTTS pytz kvsqlite beautifulsoup4 telegraph wget python-dotenv

# تجهيز الملفات
COPY . /app/
WORKDIR /app/

# أمر التشغيل
CMD ["python3", "main.py"]
