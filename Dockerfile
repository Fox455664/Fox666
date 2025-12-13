FROM python:3.10

# تحديث وتسطيب ffmpeg عشان الميوزك يشتغل
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# تجهيز ملفات البوت
COPY . /app/
WORKDIR /app/

# تسطيب المكاتب
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# أمر التشغيل
CMD ["python3", "main.py"]
