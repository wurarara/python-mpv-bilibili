# python-mpv-bilibili
***用python脚本一键调用mpv播放bilibili视频***

更具体的内容可以前往我的GitHub page查看 [**使用Python调用MPV播放B站视频（一）**](https://wurarara.github.io/)

## 以下做一些简单的讲解

### 目的
```
1. 解决每一次调用mpv播放器的时候都需要进行的繁琐步骤。
2. you-get命令行教程居多，py文件的写法反而相对较少，所以写出来方便有需要的人查阅。
```
### 步骤

首先是获取cookies，我用的是谷歌的扩展程序EditThisCookie，登录bilibili后进入视频播放页面，右键空白处然后选择EditThisCookie，选择扳手（设置），选择 options，找到 Choose the preferred export format for cookies，选择 Netscape HTTP Cookies File，然后回到刚才的页面导出cookies，新建cookies.txt文件，粘贴进去。

下面的步骤不再多言，注释写的很清楚，更具体的可以查看上方给出的文章。

### 两个问题
```
1. 会自动下载bilibili视频弹幕，本人无法解决。
2. 不是打开即可运行，本人设置了打开方式为IDLE，然后F5运行，速度相对快一些，其他例如vscode，prcharm的话相对慢。
```
<br>有解决办法的话欢迎提出~
