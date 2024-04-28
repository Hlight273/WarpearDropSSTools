#仅供测试
import WSScreenshot as wsshot
import os
from PIL import Image

def get_test_titlebox():
    datelist = ['2024.4.25','2024.4.26','2024.4.27','2024.4.28']
    for i in datelist:
        wsshot.get_imgae_title(i).save(os.path.join(os.path.dirname(os.getcwd()), "test", f"{i}.png"))

get_test_titlebox()