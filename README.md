# 任務管理中心（month-note）

最簡版的每月家務清單，加上 GitHub Actions 每天用 Telegram 提醒。

**線上使用**：https://kftseng2oo1.github.io/month-note/

## 主要功能
- 兩種任務：每月固定（每月幾號或月底）、臨時任務（指定日期）
- 分類：財務、生活、數位、其他
- 完成／復原，每項可寫備忘（帳號、細節），完成時自動加上時間戳記
- 資料存在 localStorage：`monthlyTasks`

## 每日提醒（GitHub Actions）
- `.github/workflows/main.yml`：每天 UTC 01:00（台灣 09:00）執行，也可手動觸發
- `notify.py`：透過 Telegram Bot 發送「今天是本月第 N 號，記得檢查清單」並附 App 連結
- 需在 repo 的 Settings → Secrets 設定 `TELEGRAM_BOT_TOKEN`、`TELEGRAM_CHAT_ID`

## 備註
- 目前沒有 `manifest.json`，`sw.js` 存在但無法安裝成 App。
- 功能較完整的後續版本是 [house](https://github.com/kftseng2oo1/house)（LINE／Email 通知、雲端同步）。
