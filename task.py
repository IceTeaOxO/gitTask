import os
import subprocess
from datetime import datetime

# 設置日誌文件的路徑
log_file_path = 'git_push_log.txt'

# 讀取目錄清單文件
with open('directory_list.txt', 'r') as file:
    directories = [line.strip() for line in file]

# GitHub 存儲庫 URL
repo_url = 'https://github.com/username/repo.git'

# 提交訊息
commit_message = f'Auto commit at {datetime.now()}'


# 開啟日誌文件，以附加模式（'a'）
with open(log_file_path, 'a') as log_file:
    for directory_path in directories:
        try:
            # 變換到資料夾目錄
            os.chdir(directory_path)

            # 執行 Git 命令
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', commit_message])
            # subprocess.run(['git', 'push', repo_url, 'master'])
            subprocess.run(['git', 'push', '--set-upstream', 'origin', 'main'])
            

            # 寫入成功信息到日誌文件
            log_file.write(f'Successfully pushed changes for {directory_path}\n')

        except Exception as e:
            # 寫入例外情況信息到日誌文件
            log_file.write(f'{datetime.now()} Error pushing changes for {directory_path}: {str(e)}\n')

# 提示腳本執行完成
print('Script execution completed.')
    
