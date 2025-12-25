FROM python:3.9-slim

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# تم إضافة httpx==0.24.1 في البداية لحل مشكلة البحث
RUN pip install --no-cache-dir \
    httpx==0.24.1 \
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
    lyricsgenius \
    flask

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

CMD redis-server --daemonize yes && python3 main.py
