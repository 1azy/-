# encoding = utf-8#
import os
import shutil
import math
import re
import sys

'''
提供两个功能：
1.把一个大文件分割成10个小文件
2.把这10个合并成一个大文件，要保证文件是正常的
-------------
'''


def split_file(filename):

    with open(filename, 'rb+') as fp:
        fsize = os.path.getsize(filename)
        avg = fragment_size(fsize)
        saved = 0
        lists = []
        i = 0
        while saved < fsize:
            if saved + avg <= fsize:
                save_file(fp, filename + str(i), avg)
                saved = saved + avg
            else:
                save_file(fp, filename + str(i), fsize - saved)
                saved = saved + (fsize - saved)

            lists.append(filename + str(i))
            i =i+1

    return lists


def fragment_size(fsize):
    avg = math.ceil(fsize / 10)
    print(avg)
    return avg


def save_file(fp, filename, fszie):
    limit = 4194304
    if fszie <= limit:  # 总文件大小小于4M，直接读取
        with open(filename, 'wb') as f:
            f.write(fp.read(fszie))
    else:
        with open(filename, 'wb') as f:
            temp = 0  # 已读字节
            while temp < fszie:  # 若已读<总字节
                if temp + limit > fszie:  # 已读+限制大于总字节
                    reading = fszie - temp  # 读的部分=总字节-已读
                else:
                    reading = limit
                f.write(fp.read(reading))
                temp = temp + reading

def merge_file(lists,tofile,filename): # 合并文件

    if not os.path.exists(tofile):
        os.mkdir(tofile)

    mainpath = open(os.path.join(tofile,filename),'wb')
    # other = lists[1:]

    for x in lists:

        filepath = os.path.join(x)
        infile = open(filepath,'rb')
        data = infile.read()
        mainpath.write(data)
        infile.close()

    mainpath.close()






filename = 'D:\\OrderSystem.zip'
split_file(filename)
merge_file(split_file(filename),'x','zzzzzzzz')
