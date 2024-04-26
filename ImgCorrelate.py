import os
import cv2
import numpy as np
from PIL import Image

def GetPosition(path1,path2):
    """
    cv2库，寻找子图的坐标,1为图像，2为子图,返回一个point
    """
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        return max_loc
    else:
        return
    
def GetPosition2(image,path2):
    """
    cv2库，寻找子图的坐标,1为图像，2为子图,返回一个point
    """
    img1 = ImageToCV2Img(image)
    img2 = cv2.imread(path2)
    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        return max_loc
    else:
        return

#把Imgae对象转为cv2的img
def ImageToCV2Img(image):
    image_array = np.array(image)
    # 将图像从RGB格式转换为BGR格式（OpenCV默认格式）
    return cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    


# # 读取 1.png 和 2.png
# img1 = cv2.imread('res/test.png')
# img2 = cv2.imread('res/bag.png')

# # 在 1.png 中寻找 2.png
# result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)

# # 找到最大匹配值的位置
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# # 返回最大匹配位置的坐标
# if max_val > 0.8:
#     x, y = max_loc
#     print("Found at:", x, y)
# else:
#     print("Not found")