import sys
import os
from you_get import common as you_get                #导入you-get库

cookies_bl = "Enter the path of the cookies.txt exported from bilibili between the quotation marks"   #在引号之间输入从bilibili导出的cookies.txt的路径
sys.argv = ['you-get','-c',cookies_bl]
video_url = input("input URL: ")
url = video_url     #需要下载的视频地址
sys.argv = ['you-get', '-i', url,'--no-proxy']          #获取视频信息，且不使用代理
you_get.main()

format_msg = input("input format_msg: ")            #选择format，并输入
sys.argv = ['you-get','--format={}'.format(format_msg),'-u',url,'--no-proxy']        #获取你选择的视频格式的真实链接，且不使用代理
you_get.main()

video_url = input("Please enter the real video URL: ")
audio_url = input("Please enter the real audio URL: ")
cmd = 'mpv "' +  video_url + '" --audio-file="' + audio_url +  '" --referrer="https://www.bilibili.com" --no-ytdl'       #cmd命令，调用mpv播放你选择的视频
os.system(cmd)
