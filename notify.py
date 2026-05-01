import os
import json
import requests
from datetime import datetime

# 取得環境變數
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_message(text):
    # 這裡是最容易出錯的地方，確保 TOKEN 前面有加 "bot" 字樣
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("✅ 發送成功！")
    else:
        print(f"❌ 發送失敗，錯誤碼：{response.status_code}")
        print(f"❌ 錯誤原因：{response.text}")
        # 這裡會印出詳細原因，如果是 Token 錯了，Telegram 會回傳 "Unauthorized" 或 "Not Found"

def check_tasks():
    today = datetime.now()
    message = f"<b>🔔 每月任務提醒</b>\n今天是 {today.strftime('%Y-%m-%d')}\n系統測試正常！"
    send_message(message)

if __name__ == "__main__":
    # 先檢查變數有沒有讀取到
    if not TOKEN or not CHAT_ID:
        print("❌ 錯誤：找不到環境變數 TELEGRAM_BOT_TOKEN 或 TELEGRAM_CHAT_ID")
    else:
        check_tasks()
