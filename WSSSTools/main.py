#pip install pyautogui,pynput,opencv-python
import os 
import pygetwindow as gw
import shutil
import threading

import common.WSScreenshot as WSScreenshot
import common.WSSConsole as WSSConsole

from pynput import keyboard

def init():
    if os.path.exists('snip'):
        shutil.rmtree('snip')
    # 启动键盘监听
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    # # 运行监听循环
    # listener.join()

#检测战矛窗口，并截图
def start():
    active_window = gw.getActiveWindow()
    if active_window and active_window.title == 'Warspear Online':
        windows = gw.getWindowsWithTitle('Warspear Online')
        if windows:
            win = windows[0]
            WSScreenshot.ss(win)

def on_press(key):
    try :
        #按下f3的事件
        if key == keyboard.Key.f3:
            screenshot_thread = threading.Thread(target=start)
            screenshot_thread.start()
            #start()
    except Exception as e :
        print(e)

if __name__ == "__main__":
    init()
    WSSConsole.start()