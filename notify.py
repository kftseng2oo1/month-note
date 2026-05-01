def check_and_notify():
    today = datetime.now()
    day = today.day
    
    # 針對你的專案網址進行優化
    project_url = "https://kftseng2oo1.github.io/month-note/"
    
    message = f"<b>🔔 任務提醒 ({today.strftime('%Y-%m-%d')})</b>\n"
    message += f"主人早安！今天是本月的第 {day} 號。\n"
    message += "別忘了進去 App 檢查當日需要完成的固定任務喔！\n"
    message += f"\n👉 <a href='{project_url}'>點此開啟 我的家務小幫手</a>"

    print(send_tg_message(message))
