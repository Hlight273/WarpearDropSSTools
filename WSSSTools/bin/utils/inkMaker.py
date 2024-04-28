import win32com.client
import os

#用于生成快捷方式

def create_shortcut(target_path, shortcut_path, start_in):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = start_in  # 设置工作目录为WSSSTools
    shortcut.Save()

root = os.path.dirname(os.path.dirname(os.getcwd()))
# 使用示例
target_path = root+r"\dist-version\WarpearDropSSTools\WSSSTools\main.exe"
shortcut_path = root+r"\dist-version\WarpearDropSSTools\WarpearDropSSTools.lnk"
start_in = root + r"\dist-version\WarpearDropSSTools\WSSSTools"

print(root,target_path,shortcut_path,sep="\n")
create_shortcut(target_path, shortcut_path,start_in)