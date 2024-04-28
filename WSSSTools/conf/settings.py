import os
import datetime
from pathlib import Path

# 获取WSSSTools目录
def work_path():
    return os.getcwd()
# 获取WSSSTools的上一级目录，也就是根目录
def root_path():
    return os.path.dirname(work_path())

#获取资源目录
def res_path(filename):
    return os.path.join(work_path(),  'res', filename)

#资源目录
path_img_bag = res_path('bag.png')
path_img_title = res_path('title.png')
path_sound_ss = res_path('ss.wav')
path_font_timesBold = res_path('Times New Roman Bold.ttf')
path_font_BookAntiqua = res_path('Book Antiqua.ttf')
path_font_BookAntiqua_bold = res_path('Book Antiqua Bold.ttf')

#返回今日的截图path
def path_sspasted_today():
    return os.path.join(root_path(), "output", f"out_{datetime.date.today().strftime('%Y%m%d')}.png")

if __name__ == "__main__":
    print(' --'+str(work_path()),
          root_path(),
      path_img_bag,
      path_sound_ss,
      sep='\n --')
    print(os.getcwd())