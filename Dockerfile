FROM python:3.10-slim

# 1️⃣ متطلبات النظام
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ تحديث pip
RUN pip install --no-cache-dir --upgrade pip

# 3️⃣ تثبيت المكتبات (نسخة مؤكدة شغالة)
RUN pip install --no-cache-dir \
    pyrogram==2.0.106 \
    tgcrypto \
    pytgcalls==1.0.0 \
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

# 4️⃣ نسخ المشروع
WORKDIR /app
COPY . .

# 5️⃣ التشغيل
CMD redis-server --daemonize yes && python3 main.py
