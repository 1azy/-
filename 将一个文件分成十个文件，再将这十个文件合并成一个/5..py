# encoding = utf-8#
import os
import shutil
import math
import re
import sys
import glob

'''
提供两个功能：
1.把一个大文件分割成10个小文件
2.把这10个合并成一个大文件，要保证文件是正常的
3.用户输入路径，用户自定义是要按照每个文件的大小或是平均分成几份
4.输入一个分割前的文件名，就可以把那些分割后的文件名给找出来然后合并回去
-------------
'''


def split_file(filename,number,size):

    # 分解路径和文件名
    # [dirname,filename]=os.path.split(filepath)

    with open(filename, 'rb+') as fp:
        fsize = os.path.getsize(filename)
        avg = fragment_size(fsize, number, size)
        saved = 0
        lists = []
        i = 0
        while saved < fsize:
            if saved + avg <= fsize:
                save_file(fp, filename + str('%.4d ' % i), avg)
                saved = saved + avg
            else:
                save_file(fp, filename + str('%.4d ' % i), fsize - saved)
                saved = saved + (fsize - saved)

            lists.append(filename + str('%.4d ' % i))
            i = i + 1

    return lists


def fragment_size(fsize, number, size):
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

    mainpath = open(os.path.join(tofile, filename), 'wb')
    print(lists)
    for x in lists:
        # print(x)
        x1 = ''.join(x)
        # print(x1)
        filepath = os.path.join(x1)
        infile = open(filepath, 'rb')
        data = infile.read()
        mainpath.write(data)
        infile.close()

    mainpath.close()

def find_file(basepath,keyword):
    file_list = []
    filenames = os.listdir(basepath)
    print(filenames)
    for x in filenames:
        pattern = re.compile(keyword+'\d*')
        match = pattern.findall(x)
        if match:
            for i in match:
                if i != keyword:
                    i = basepath + '\\' + i
                    file_list.append(i)
    # print(sorted(file_list))


    return sorted(file_list)






def spilt_main():

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

def merge_main():
    filepath = input('输入被分割文件的完整路径：')
    [basepath, keyword] = os.path.split(filepath)
    # 查找文件路路径包含有该关键字的文件名
    file_list = find_file(basepath, keyword)

    topath = input('输入要合并后的文件路径：')
    rename = input('输入要合并后的文件名：')
    merge_file(file_list, topath, rename)






    # filename = 'F:\lazy2\huitouche\Huitouche.zip'



spilt_main()
merge_main()

