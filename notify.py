import os
import requests
import sys

# 強制讀取環境變數
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_test():
    if not TOKEN or not CHAT_ID:
        print("錯誤：找不到 TOKEN 或 CHAT_ID 環境變數")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": "🚨 來自 GitHub Actions 的測試訊息！如果你看到這個，代表連線成功了。",
        "parse_mode": "HTML"
    }
    
    try:
        r = requests.post(url, json=payload)
        print(f"狀態碼: {r.status_code}")
        print(f"回傳內容: {r.text}")
    except Exception as e:
        print(f"發生異常: {e}")

# 這裡不加 if 判斷，確保執行時一定跑
print("腳本啟動中...")
send_test()
