import cv2
import numpy as np
from PIL import Image

def GetPosition(path1,path2):
    """
    cv2库，寻找子图的坐标,1为图像，2为子图,返回一个point
    """
    img1 = __cv_imread(path1)
    img2 = __cv_imread(path2)
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
    img1 = __ImageToCV2Img(image)
    img2 = __cv_imread(path2)
    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        return max_loc
    else:
        return

#传入cv2.img如果是绝对路径带中文，就会报错，很麻烦，我们用另一种方式间接读取
#防止中文路径报错，原文见https://blog.csdn.net/weixin_49716548/article/details/129304642
def __cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    # cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

#把Imgae对象转为cv2的img
def __ImageToCV2Img(image):
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