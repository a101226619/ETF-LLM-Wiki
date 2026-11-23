# ETF LLM Wiki + HTML 教學簡報

## 直接開啟
雙擊 `slides/index.html` 即可離線瀏覽 12 頁簡報。左右方向鍵可切換，測驗可點選。

## 檔案
- `AGENTS.md`：專案與 Graph/Loop 規則
- `raw/S01–S05.md`：五份來源摘要（非原文全文）
- `wiki/topics/`：五個教學知識頁
- `wiki/index.md`：知識索引
- `wiki/log.md`：分批 ingest 紀錄
- `slides/`：HTML/CSS/JS 教學簡報
- `scripts/check.py`：可執行的靜態驗證
- `reports/`：檢查結果與反思

## 檢查
在專案根目錄執行 `python scripts/check.py`。

## 部署
將整個資料夾上傳 GitHub repository，GitHub Pages 選 main/root；簡報網址為 `https://帳號.github.io/儲存庫名稱/slides/`。實際網址需完成部署才會產生。

本專案是摘要型 Wiki；尚未建立自動連網抓取/自動 LLM 審查 Agent。檢查程式不等同瀏覽器版面測試。
