import threading
from flask import Flask
import os
import sys

app = Flask(__name__)
@app.route('/')
def health_check():
    return "OK", 200

def run_flask():
    app.run(host='0.0.0.0', port=8000)

threading.Thread(target=run_flask, daemon=True).start()

# كود تشغيل البوت الخاص بك يكمل هنا...
