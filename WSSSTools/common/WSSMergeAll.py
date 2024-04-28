import sys
import os
import math

try:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)
    from conf import settings as WSSpath
except Exception as e:
    1+1==2
import glob
from PIL import Image

#获取合法图像的路径和图像字典
def __getValidImgDict():
    imgDict={}
    # 指定路径
    path = WSSpath.root_path() + "\\output"
    # 指定文件名格式
    filename_pattern = "out_*.png"
    # 指定目标图片宽度和高度
    target_width = 88 * 4
    target_height = 88

    # 使用glob模块获取所有符合条件的文件路径
    file_paths = glob.glob(path + "/" + filename_pattern)

    # 遍历文件路径
    for file_path in file_paths:
        
        # 打开图片
        image = Image.open(file_path)
        # 检查图片宽度和高度是否符合要求
        if image.width == target_width and image.height % target_height == 0:
            # 图片宽度符合要求且高度是88的倍数
            print("Found image:", file_path)
            # 在这里可以对满足条件的图片进行进一步处理或操作
            imgDict[file_path]=image
        else:
            # 图片宽度或高度不符合要求
            print("Invalid image:", file_path)
    return imgDict

def __printValidImg():
    print('>'*20)
    for i in __getValidImgDict().items():
        print('> '+i[0])
    print('>'*20)

#把大图列表分成小图的列表
def __split_images_by_height(imageList):
    sLen = 88
    imageList2 = []
    for image in imageList:
        width, height = image.size
        num_splits = height // sLen  # 计算需要分割成多少个图像元素
        for i in range(num_splits):
            top = i * sLen
            bottom = (i + 1) * sLen
            cropped_image = image.crop((0, top, width, bottom))
            imageList2.append(cropped_image)
    return imageList2

#拼贴小图
def __concatenate_images(imageList, length):
    sLen = 88
    w,h = 4*sLen, sLen
    result_image = Image.new('RGBA', (length, length))

    y_offset,x_offset = 0,0  #偏移量

    for image in imageList:
        image_width, image_height = image.size

        # 如果当前图像的高度超过剩余空间，需要在新的一列开始拼接
        if y_offset + image_height > length:
            y_offset = 0
            x_offset += w

        # 将当前图像拼接到大图中
        result_image.paste(image, (x_offset, y_offset))
        y_offset += image_height

    return result_image

#裁切，去掉多余的透明部分
def __crop_image(image):
    bbox = image.getbbox()
    cropped_image = image.crop(bbox)
    return cropped_image

def merge():
    sLen = 88
    w,h = 4*sLen, sLen
    imageList = list(__getValidImgDict().values())
    if len(imageList)==0:
        print('当前还没有符合条件的图片！')
        return
    
    imageList_split = __split_images_by_height(imageList)
    cnt = len(imageList_split)
    length = w * math.ceil((cnt/4)**0.5)#尽量总体拼接成一个方形
    #print(cnt,length) 

    out_image = __crop_image(__concatenate_images(imageList_split,length))
    out_path = os.path.join(WSSpath.root_path(), "output", f"out_merge.png")
    out_image.save(out_path)

    print('已合并图像！')

if __name__ == "__main__":
    merge()