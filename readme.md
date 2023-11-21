## linux
在 Linux 中使用 cron:

打開終端。
使用 crontab -e 編輯 cron 表。
添加一個定時任務，例如每天晚上 9 點：
```
0 21 * * * /path/to/python /path/to/your/script.py
```

## windows
在 Windows 中使用 Task Scheduler:

打開 Task Scheduler。
在右側選擇 "Create Basic Task..."。
按照嚮導的指示指定觸發器和動作。在 "Action" 步驟中，選擇 "Start a program"，然後指定你的 Python 解釋器的路徑和你的 Python 腳本的路徑。
確保你的腳本和 Git 被添加到系統的 PATH 變數中，以便腳本能夠執行 Git 命令。