FROM python:3.9-slim

# 1️⃣ تثبيت أدوات النظام الأساسية
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ تحديث أدوات بايثون
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3️⃣ تثبيت المكتبات (التصحيح النهائي لإصلاح خطأ InputMode)
# النسخة 1.1.6 هي الأكثر استقراراً وتوافقاً مع بوتات الميوزك
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
    tgcrypto \
    py-tgcalls==1.1.6 \
    yt-dlp \
    youtube-search-python \
    youtube-search \
    aiohttp \
    Pillow \
    numpy \
    unidecode \
    aiofiles \
    pyromod \
    requests \
    redis \
    gTTS \
    pytz \
    kvsqlite \
    beautifulsoup4 \
    telegraph \
    wget \
    python-dotenv \
    lyricsgenius

# 4️⃣ نسخ ملفات البوت
WORKDIR /app
COPY . .

# 5️⃣ أمر التشغيل
CMD redis-server --daemonize yes && python3 main.py
