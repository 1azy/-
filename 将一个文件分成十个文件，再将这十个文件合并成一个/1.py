#encoding = utf-8#
import os
import shutil
import math
import re
import sys
'''
提供两个功能：
1.把一个大文件分割成10个小文件
-------------
'''


def split_file(filename):
    with open(filename,'rb+') as fp:
        fsize = os.path.getsize(filename)
        avg = fragment_size(fsize)
        saving = 0

        for i in range(10):
            if i < 9 :
               save_file(fp,filename+str(i),avg)
               saving = saving + avg
               a = fsize - saving
            else:
               save_file(fp, filename + str(i), fsize - saving)
               saving = saving + avg



def fragment_size(fsize):
    avg = math.ceil(fsize/10)
    print(avg)
    return avg



def save_file(fp,filename, fszie):
    limit = 4194304
    if fszie <= limit: # 文件大小小于4M
        with open(filename, 'wb') as f:
            f.write(fp.read(fszie))
    else:
        with open(filename, 'wb') as f:
            temp = 0  #已读字节
            while temp < fszie:
                if temp + limit > fszie:
                    reading = fszie - temp
                else:
                    reading = limit
                f.write(fp.read(reading))
                temp = temp + reading






filename = 'D:\\OrderSystem.zip'
split_file(filename)
