import requests
import urllib
from urllib.request import urlretrieve
'''

上传图片
获得服务器给的url
拿到url后，下载url对应的图片

'''

def getphotourl():
    headers = { 'Accept': 'application/binary',
                'Host': 'img.huitouche.io',
                'Accept-Encoding': 'gzip'}

    url = 'http://img.huitouche.io/uploadImage?watermark=0'
    files = {'file': open('1.jpg', 'rb')}
    response = requests.post(url, files=files,headers=headers)

    a = response.json()

    return a['data'][0]['original']


def download(img_url):
    img_src = img_url
    urlretrieve(img_src, r'D:\\lazy\\1.jpg')



a = getphotourl()
download(a)
