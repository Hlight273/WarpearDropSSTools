import os
import datetime
import winsound
import pyautogui
import pygetwindow as gw

import sys
import traceback

from PIL import Image,ImageDraw,ImageFont

try:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    from conf import settings as WSSpath
    import common.ImgCorrelate as ImgCorrelate
except Exception as e:
    1+1==2

sLen = 88 #ws出货框宽=高

def __today():
    return datetime.date.today().strftime("%Y-%m-%d")
def __timestamp():
    return datetime.datetime.now().timestamp()

#需要保证每次截图，文件目录都在
def __mkdirTree():
    os.makedirs(f'{WSSpath.root_path()}/output', exist_ok=True)
    os.makedirs(f'{WSSpath.work_path()}/snip/{__today()}', exist_ok=True)

#根据当前年月日时分秒生成文件名
def __newSsFileName():
    path = os.path.join(WSSpath.work_path(), "snip", __today())
    file_name = os.path.join(path, f"ss_{__timestamp()}.png")
    return file_name

#返回带文字的标题ui 的Imgae
def get_imgae_title(text):
    #字体信息
    font = WSSpath.path_font_BookAntiqua_bold
    font_size = 40
    text_color = (255, 255, 0)  #黄色
    #描边信息
    outline_width = 2
    outline_color = (0, 0, 0)
    #背景图片
    titleImage = Image.open(WSSpath.path_img_title)
    draw = ImageDraw.Draw(titleImage)
    font = ImageFont.truetype(font, font_size)  # 选择字体和字号
    #居中
    box = font.getbbox(text)
    text_width, text_height = box[2]-box[0], box[3]-box[1]
    text_position = ((titleImage.width - text_width) // 2, (titleImage.height - text_height) // 2 - 5)  # 计算文本的位置使其居中
    # 描边
    draw.text(text_position, text, font=font, fill=outline_color, stroke_width=outline_width, stroke_fill=outline_color)
    # 绘制文本
    draw.text(text_position, text, font=font, fill=text_color)
    return titleImage

#返回背包ui左上角在完整截图内的坐标，如果没有就返回None
def __get_Position_DropUI(ss):
    return ImgCorrelate.GetPosition2(ss,WSSpath.path_img_bag) 

#返回裁剪成掉落框后的image对象
def __get_SS_Cropped(ss,oriPos):
    x,y=oriPos
    offsetX,offsetY = 14,14
    x-=offsetX
    y-=offsetY
    region = (x,y,x+4*sLen,y+sLen)
    cropped_ss = ss.crop(region)
    return cropped_ss

#返回完整截图
def __get_SS_Full(wsWin):
    left,top,width,height = wsWin.left+9, wsWin.top+38, wsWin.width-9-9, wsWin.height-9-38
    return pyautogui.screenshot(region=(left,top,width,height))

#传入待拼接的切片图，完成拼接操作
def __ssJoint(cropped_ss):
    w,h = 4*sLen, sLen
    image_path = os.path.join(WSSpath.root_path(), "output", f"out_{datetime.date.today().strftime('%Y%m%d')}.png")
    titleImage = get_imgae_title(datetime.date.today().strftime("%Y.%m.%d"))
    pImage, count = None, 0 #count切片数量
    if os.path.exists(image_path):
        pImage = Image.open(image_path)
        count = int(pImage.height/sLen) #图像总高度除以切片高度=切片数量
        newpImage = Image.new("RGBA", (w, (count+1)*h))
        newpImage.paste(pImage, (0, 0))
        newpImage.paste(cropped_ss, (0*w, (count)*h))
        newpImage.save(image_path)
    else:
        pImage = Image.new("RGBA", (w, 2*h))
        pImage.paste(titleImage, (0, 0))
        pImage.paste(cropped_ss, (0, h))
        pImage.save(image_path)
    if count==0:
        count+=1
    print(f'已记录{datetime.date.today().strftime('%Y年%m月%d日')}的第{count}次掉落')

#截图功能主入口，在主进程中调用它，需要参数ws窗口的句柄
def ss(wsWin):
    try :
        #先创建当前截图所有的所需目录
        __mkdirTree()
        #保存完整截图，一变等下在完整截图中寻找小背包ui
        screenshot = __get_SS_Full(wsWin)
        #传入本次截图，尝试在完整截图中查找背包子图像的左上角坐标
        oriPos = __get_Position_DropUI(screenshot)

        #如果没找到
        if oriPos == None: 
            print('未找到掉落物')
        #如果找到
        else:
            winsound.PlaySound(WSSpath.path_sound_ss, winsound.SND_FILENAME)
            #获得剪切后的截图
            cropped_ss = __get_SS_Cropped(screenshot,oriPos)
            cropped_ss.save(__newSsFileName())
            #拼接到一起
            __ssJoint(cropped_ss)
    except PermissionError as e:
        print('截图失败：截图频率过高！')
    except Exception as e :
        print(e) # 输出：division by zero
        print(sys.exc_info()) # 输出：(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001A1A7B03380>)
        
        # 以下两步都是输出错误的具体位置，报错行号位置在第几行
        print('\n','>>>' * 20)
        print(traceback.print_exc())
        print('\n','>>>' * 20)
        print(traceback.format_exc())
        print(f'截图失败：{e}')


#撤回上次贴图
def ctrlv():
    try :
        w,h = 4*sLen, sLen
        path = WSSpath.path_sspasted_today()
        if os.path.exists(path):
            image = Image.open(path)
            count = int(image.height/sLen)#已截图数量
            if count<=1:#最后一张不干
                print('今日还没有截图！')
            else:
                region = (0,0,w,h*(count-1))
                image2 = image.crop(region)
                image2.save(path)
            print('已撤销今日上一次截图！')
        else:
            print('今日还没有截图！')
    except Exception as e :
        print(f'撤回失败：{e}')