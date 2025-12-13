FROM python:3.10

# تحديث وتسطيب ffmpeg الضروري
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# تسطيب المكاتب يدوي عشان نضمن وجودها
RUN pip3 install -U pip
RUN pip3 install pyrogram tgcrypto py-tgcalls yt-dlp youtube-search-python aiohttp Pillow numpy unidecode aiofiles pyromod requests redis gTTS pytz kvsqlite beautifulsoup4 telegraph wget python-dotenv

# تجهيز الملفات
COPY . /app/
WORKDIR /app/

# أمر التشغيل
CMD ["python3", "main.py"]
