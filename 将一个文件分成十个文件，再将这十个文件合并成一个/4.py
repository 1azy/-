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
3.用户输入路径，用户自定义是要按照每个文件的大小或是平均分成几份
'''


def split_file(filepath,number,size):

    # 分解路径和文件名
    [dirname,filename] = os.path.split(filepath)

    with open(filepath, 'rb+') as fp:
        fsize = os.path.getsize(filepath)
        avg = fragment_size(fsize, number, size)
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


def fragment_size(fsize,number,size):
    if size == 0:
        avg = math.ceil(fsize / int(number))
    if number == 0:
        avg = size
    print(avg)
    return int(avg)


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

    for x in lists:

        filepath = os.path.join(x)
        infile = open(filepath,'rb')
        data = infile.read()
        mainpath.write(data)
        infile.close()

    mainpath.close()



def spilt_main():

    # filename = 'D:\\OrderSystem.zip'
    filepath = input('输入文件位置：')
    choose = input('通过个数分割输入1，通过文件大小分割输入2：')
    if choose == '1':
        size = 0
        number = input('输入分割成多少个文件：')
        split_file(filepath,number,size)
    if choose == '2':
        number = 0
        size = input('输入每个文件的大小：')
        split_file(filepath, number, size)


    # filename = 'D:\\OrderSystem.zip'
    # topath= input('输入移动后的位置：')
    # split_file(filepath)
    # merge_file(split_file(filepath),topath,'zzzzzzzz')


spilt_main()