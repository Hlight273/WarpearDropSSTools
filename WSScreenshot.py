import os
import datetime
import winsound
import pyautogui
import pygetwindow as gw

import ImgCorrelate

from PIL import Image

sLen = 88 #ws出货框宽=高

def today():
    return datetime.date.today().strftime("%Y-%m-%d")
def timestamp():
    return datetime.datetime.now().timestamp()

#需要保证每次截图，文件目录都在
def mkdirTree():
    os.makedirs('output', exist_ok=True)
    os.makedirs(f'snip/{today()}', exist_ok=True)

#根据当前年月日时分秒生成文件名
def getSsFileName():
    path = os.path.join(os.getcwd(), "snip", today())
    file_name = os.path.join(path, f"ss_{timestamp()}.png")
    return file_name

#返回背包ui左上角在完整截图内的坐标，如果没有就返回None
def get_Position_DropUI(ss):
    return ImgCorrelate.GetPosition2(ss,'res/bag.png') 

#返回裁剪成掉落框后的image对象
def get_SS_Cropped(ss,oriPos):
    x,y=oriPos
    offsetX,offsetY = 14,14
    x-=offsetX
    y-=offsetY
    region = (x,y,x+4*sLen,y+sLen)
    cropped_ss = ss.crop(region)
    return cropped_ss

#返回完整截图
def get_SS_Full(wsWin):
    left,top,width,height = wsWin.left+9, wsWin.top+38, wsWin.width-9-9, wsWin.height-9-38
    return pyautogui.screenshot(region=(left,top,width,height))

#传入待拼接的切片图，完成拼接操作
def ssJoint(cropped_ss):
    os.makedirs('output', exist_ok=True)
    w,h = 4*sLen, sLen
    image_path = os.path.join(os.getcwd(), "output", f"out_{datetime.date.today().strftime('%Y%m%d')}.png")
    pImage, count = None, 0 #count切片数量
    if os.path.exists(image_path):
        pImage = Image.open(image_path)
        count = int(pImage.height/sLen) #图像总高度除以切片高度=切片数量
        newpImage = Image.new("RGBA", (w, (count+1)*h))
        newpImage.paste(pImage, (0, 0))
        newpImage.paste(cropped_ss, (0*w, count*h))
        newpImage.save(image_path)
    else:
        pImage = Image.new("RGBA", (w, h))
        pImage.paste(cropped_ss, (0*w, count*h))
        pImage.save(image_path)
    if count == 0:
        count+=1
    print(f'已记录{datetime.date.today().strftime('%Y年%m月%d日')}的第{count}次掉落')

#截图功能主入口，在主进程中调用它，需要参数ws窗口的句柄
def ss(wsWin):
    try :
        #先创建当前截图所有的所需目录
        mkdirTree()
        #保存完整截图，一变等下在完整截图中寻找小背包ui
        screenshot = get_SS_Full(wsWin)
        #传入本次截图，尝试在完整截图中查找背包子图像的左上角坐标
        oriPos = get_Position_DropUI(screenshot)

        #如果没找到
        if oriPos == None: 
            print('未找到掉落物')
        #如果找到
        else:
            winsound.PlaySound("res/ss.wav", winsound.SND_FILENAME)
            #获得剪切后的截图
            cropped_ss = get_SS_Cropped(screenshot,oriPos)
            cropped_ss.save(getSsFileName())
            #拼接到一起
            ssJoint(cropped_ss)
    except PermissionError as e:
            print('截图失败：截图频率过高！')
    except Exception as e :
        print(f'截图失败：{e}')
    