# WarpearDropSSTools
WarpearDropScreenshotTools，战矛掉落截图工具。
Windows系统可用
程序入口是WSDropSniPaste.py。
如果没有python环境，也可以在release找到[打包后的版本](https://github.com/Hlight273/WarpearDropSSTools/releases/tag/v1.0 "发布 release")，解压到一个文件夹后点击exe运行

------------

#### 更新日志

------------

#### v1.0

由于春季掉落过于构式，本人决定统计一下掉落究竟是个什么情况，以便日后岁月史书..

##### 使用方法：

运行WSDropSniPaste.py后，打开战矛在线客户端。
游戏窗口在前台时，按下f3完成截图。如果有掉落物界面，就会把掉落物截图切片拼接到
/项目目录/output 的一张长图下... 到时候去这里找就行了

------------
#### 打包
```bash
pyinstaller -i icon.ico -F WSDropSniPaste.py
```
然后把res文件夹手动放过去