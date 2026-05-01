import os
import json
import requests
from datetime import datetime

# 從 GitHub Secrets 取得金鑰
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def check_tasks():
    # 這裡模擬檢查 index.html 中的任務邏輯 (實務上建議將任務清單存為 tasks.json 方便讀取)
    # 範例：檢查今天是否為 1 號
    today = datetime.now()
    day_str = str(today.day)
    
    # 這裡你可以手動維護一個清單，或讀取檔案
    message = f"🔔 早安！今天是 {today.strftime('%Y-%m-%d')}\n提醒你今日任務：\n"
    
    # 這裡先寫死一個測試，確保運作正常
    send_message(message + "檢查 GitHub Actions 自動化通知測試成功！")

if __name__ == "__main__":
    check_tasks()