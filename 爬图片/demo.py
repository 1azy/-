
"""
1.下载网页源码
2.提取网页源码里的图片地址
3.根据地址下载图片
"""

import urllib
import os
import requests
import re
from urllib.request import urlretrieve

def mkdir(path):

    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def get_photo_url(keyword,page):

    r = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}&pn={1}&ct=&ic=0&lm=-1&width=0&height=0'
        .format(keyword,page*20))

    pattern = re.compile(r'\"objURL\":\"(.*?)\"', re.S)

    urls = pattern.findall(r.text)

    return urls


def download(urls):

    mkdir('downloads') # 当前目录新建一个download文件夹
    for x in urls:

        a = x.split("/")[-1]  #文件名
        print(a)
        try :
             urlretrieve(x,'downloads\\'+a)  #以这个文件路径'downloads\\'+a ，作为x的文件路径
        except urllib.error.HTTPError as e:
             print(e)
        except OSError as e:
             print(e)
        except Exception as e:
            print(e)



page = 0
keyword = input('输入想要搜索的关键词：')
# download(get_photo_url(keyword,page))
# Q = input('是否需要继续打印下一页[Y/N]：')
# while Q == 'Y' or Q == 'y':
#     page = page + 1
#     download(get_photo_url(keyword,page))
#     print('目前已下载',page,"页")
#     Q = input('是否需要继续打印下一页,目前为第[Y/N]：')

while True:
    page = page + 1
    download(get_photo_url(keyword,page))