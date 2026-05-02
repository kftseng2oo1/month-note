import os
import requests
from datetime import datetime

# 從 GitHub Secrets 讀取設定
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_tg_message(text):
    """發送 Telegram 訊息的函式"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": text, 
        "parse_mode": "HTML",
        "disable_web_page_preview": False  # 允許顯示網頁預覽
    }
    r = requests.post(url, json=payload)
    return r.json()

def check_and_notify():
    """執行檢查與通知"""
    today = datetime.now()
    day = today.day
    
    # 建立精美的提醒訊息
    # 這裡已經加入你的專屬網址
    message = f"<b>🔔 任務提醒 ({today.strftime('%Y-%m-%d')})</b>\n\n"
    message += f"今天是本月的第 <b>{day}</b> 號。\n"
    message += "別忘了檢查並完成您在 App 中的家務清單喔！\n\n"
    message += f"👉 <a href='https://kftseng2oo1.github.io/month-note/'>點此開啟任務 App</a>"

    # 執行發送
    result = send_tg_message(message)
    
    # 在 GitHub Actions 日誌中印出結果以便追蹤
    if result.get("ok"):
        print("✅ 通知已成功送達 Telegram！")
    else:
        print(f"❌ 發送失敗，錯誤代碼：{result.get('error_code')}")
        print(f"錯誤描述：{result.get('description')}")

if __name__ == "__main__":
    check_and_notify()
