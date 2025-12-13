FROM python:3.9-slim

# 1️⃣ متطلبات النظام (تثبيت الحزم الضرورية)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ تحديث pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3️⃣ تثبيت المكتبات (التصحيح هنا)
# تم تغيير pytgcalls==0.0.24 إلى py-tgcalls==1.0.3 ليتوافق مع الكود
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
    tgcrypto \
    py-tgcalls==1.0.3 \
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

# 4️⃣ نسخ المشروع
WORKDIR /app
COPY . .

# 5️⃣ التشغيل
CMD redis-server --daemonize yes && python3 main.py
