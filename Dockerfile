FROM python:3.10-slim

# 1️⃣ تثبيت المتطلبات الأساسية
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ تحديث pip
RUN pip install --no-cache-dir --upgrade pip

# 3️⃣ تثبيت مكتبات البايثون (إصدار صحيح من py-tgcalls)
RUN pip install --no-cache-dir \
    pyrogram \
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
    python-dotenv

# 4️⃣ نسخ ملفات المشروع
WORKDIR /app
COPY . .

# 5️⃣ أمر التشغيل
CMD redis-server --daemonize yes && python3 main.py
