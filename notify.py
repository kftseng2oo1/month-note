import os
import requests
from datetime import datetime

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_tg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

def check_and_notify():
    today = datetime.now()
    day = today.day
    
    # 建立提醒訊息
    msg = f"<b>🔔 任務提醒 ({today.strftime('%Y-%m-%d')})</b>\n"
    msg += f"今天是 {day} 號，別忘了查看您的家務清單！\n"
    # 這裡可以換成你的 GitHub Pages 網址
    msg += f"\n👉 <a href='https://{os.environ.get('GITHUB_REPOSITORY_OWNER')}.github.io/{os.environ.get('GITHUB_REPOSITORY').split('/')[-1]}/'>開啟任務 App</a>"
    
    send_tg(msg)

if __name__ == "__main__":
    check_and_notify()
