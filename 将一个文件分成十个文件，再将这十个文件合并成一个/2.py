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
        saved = 0
        for i in range(9):
            while saved < fsize:
                if saved + avg < fsize:
                    save_file(fp, filename + str(i), avg)
                else:
                    save_file(fp, filename + str(i), fsize - saved)

                saved = saved + avg
                i = i + 1





def fragment_size(fsize):
    avg = math.ceil(fsize/10)
    print(avg)
    return avg



def save_file(fp,filename, fszie):
    limit = 4194304
    if fszie <= limit: # 总文件大小小于4M，直接读取
        with open(filename, 'wb') as f:
            f.write(fp.read(fszie))
    else:
        with open(filename, 'wb') as f:
            temp = 0  #已读字节
            while temp < fszie:   # 若已读<总字节
                if temp + limit > fszie: #已读+限制大于总字节
                    reading = fszie - temp   # 读的部分=总字节-已读
                else:
                    reading = limit
                f.write(fp.read(reading))
                temp = temp + reading



filename = 'D:\\OrderSystem.zip'
split_file(filename)
