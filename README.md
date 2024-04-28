# WarpearDropSSTools
WarpearDropScreenshotTools，战矛掉落截图工具。

这是一个为战矛在线WarspearOnline制作的一款掉落截图统计小工具

Windows系统可用
程序入口是WSDropSniPaste.py。
如果没有python环境，也可以在release找到[打包后的版本](https://github.com/Hlight273/WarpearDropSSTools/releases "发布 release")，解压到一个文件夹后点击exe运行

------------

#### 更新日志

------------

#### v1.1.1


###### 拼贴功能

新增命令 —— merge，输入后在 根目录/output 下会输出out_merge.png，整合前面所有的掉落成为一张大图

###### 优化打包

现在打包还会在根目录自动生成一个快捷方式

------------

#### v1.1.0


###### 撤销功能

由于有时候会不小心把其他遮挡的ui也截图进去，现在在命令行输入revoke可以撤销仅限今天的上一次掉落截图切片

###### 一键打包构建release

运行 根目录/WSSSTools/bin 中的 build.bat 可以在 根目录/dist-version/中找到打包的版本

###### 优化了项目结构

优化结构的时候还遇到了一些小问题，我程序的入口在WSSSTools下，但是ide打开的是更外面一层的目录。这时候以vscode为例需要配置工作目录(cwd)，然后再启动调试


------------

#### v1.0.0

由于春季掉落过于构式，本人决定统计一下掉落究竟是个什么情况，以便日后岁月史书..

###### 使用方法：

运行WSDropSniPaste.py后，打开战矛在线客户端。
游戏窗口在前台时，按下f3完成截图。如果有掉落物界面，就会把掉落物截图切片拼接到
/项目目录/output 的一张长图下... 到时候去这里找就行了

###### 打包 (请参照新版方法)
```bash
pyinstaller -i icon.ico -F WSDropSniPaste.py
```
然后把res文件夹手动放过去

------------


#### 项目地址
```bash
git clone https://github.com/Hlight273/WarpearDropSSTools.git
```