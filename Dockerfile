FROM python:3.9-slim

# تحديث النظام وتثبيت الأدوات اللازمة
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    redis-server \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ترقية pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# نسخ ملف المتطلبات وتثبيت المكتبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# إعداد متغيرات البيئة ومجلد العمل
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .

# أمر التشغيل
CMD redis-server --daemonize yes && python3 main.py
