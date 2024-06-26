import common.WSScreenshot as WSScreenshot
import common.WSSMergeAll as WSSMergeAll

def __init():
    print('战矛出货截图记录工具——v1.1.1')
    print('-请在出货界面按F3以截图，非出货界面则不会统计')
    print('-如果需要撤回上一次的拼贴，请在控制台输入revoke；如果想输出合并的大图，输入merge')
    print('-每日的出货，被分成不同的文件放在output文件夹中，可以使用merge命令在该目录输出一张合并的大图')

def __printHelp():
    print("未知命令，现有命令：revoke —— 撤回上次拼贴, merge —— 输出一张合并的大图片")

def __run():
    while True:
        s = input()
        try:
            __readCommand(s)
        except IndexError as e :
            1+1==2
        except Exception as e :
            print(e)
        
def __readCommand(s):
    input_parts = s.split()
    command = input_parts[0]
    arguments = input_parts[1:]
    if command == "revoke":
        WSScreenshot.ctrlv()
        # if len(arguments) > 0:
        #     n = int(arguments[0])
        #     if n > 1:
        #         # 执行带参数的功能
        #         print(f"执行带参数的功能，参数值为 {n}")
        #     else:
        #         print("参数必须大于1")
        # else:
        #     # 执行不带参数的功能
        #     print("执行不带参数的功能")
    elif command == "merge":
        WSSMergeAll.merge()
    else:
        __printHelp()

def start():
    __init()
    __run()
    