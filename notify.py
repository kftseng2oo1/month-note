import os
import json
import requests
from datetime import datetime

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_message(text):
    # 診斷資訊：檢查變數是否讀取成功
    if not TOKEN or not CHAT_ID:
        print("❌ 錯誤：找不到 TOKEN 或 CHAT_ID，請檢查 GitHub Secrets 設定！")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if response.status_code == 200:
            print("✅ 訊息發送成功！")
        else:
            print(f"❌ 發送失敗，錯誤碼：{response.status_code}")
            print(f"❌ 錯誤原因：{result.get('description')}")
    except Exception as e:
        print(f"❌ 發生異常：{str(e)}")

if __name__ == "__main__":
    today = datetime.now().strftime('%Y-%m-%d %H:%M')
    msg = f"🔔 任務系統測試\n時間：{today}\n恭喜你！自動化通知連線成功！"
    send_message(msg)
