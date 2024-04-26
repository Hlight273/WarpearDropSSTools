#pip install pyautogui,pynput,opencv-python

import os
import pygetwindow as gw
import shutil
import threading

import WSScreenshot

from pyautogui import hotkey, screenshot
from pynput import keyboard
from PIL import Image

#检测战矛窗口，并截图
def start():
    active_window = gw.getActiveWindow()
    if active_window and active_window.title == 'Warspear Online':
        windows = gw.getWindowsWithTitle('Warspear Online')
        if windows:
            win = windows[0]
            WSScreenshot.ss(win)

def on_press(key):
    #按下f3的事件
    if key == keyboard.Key.f3:
        try :
            screenshot_thread = threading.Thread(target=start)
            screenshot_thread.start()
            #start()
        except Exception as e :
            print(e)
  


print('战矛出货截图记录工具——v1.0')
print('请在出货界面按F3以截图，非出货界面则不会统计')
print('每日的出货，被分成不同的文件放在output文件夹中')

#初始化清除snip目录
if os.path.exists('snip'):
    shutil.rmtree('snip')

# 启动键盘监听
listener = keyboard.Listener(on_press=on_press)
listener.start()

# 运行监听循环
listener.join()