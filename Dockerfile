FROM python:3.9-slim

# 1️⃣ تثبيت أدوات النظام
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ تحديث أدوات بايثون
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3️⃣ تثبيت المكتبات (إصدارات متوافقة لمنع التعارض)
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
    tgcrypto \
    ntgcalls==1.1.3 \
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

# 4️⃣ إعداد متغيرات البيئة لإظهار السجلات فوراً
ENV PYTHONUNBUFFERED=1

# 5️⃣ نسخ الملفات
WORKDIR /app
COPY . .

# 6️⃣ التشغيل مع التأكد من عمل Redis
CMD redis-server --daemonize yes && python3 main.py
