#encoding = utf-8#
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
1.读取文件
2.统计文件的字符数
3.分割字符串
4.创建文件保存字符串
'''



def read_file(filename):
    with open(filename) as file1:
        s = file1.read()
        return s

def count_words(s):
    count = len(s)
    # print(count)
    avg = math.ceil(count/10)
    return avg


def save(savefile, str_x):
    fh = open(savefile, 'w', encoding='utf-8')
    fh.write(str_x)
    fh.close()

# 参数：字符串，平均数, 文件名
def split_document(avg,s,filename):
    '''
    循环十次，创建文件并把每次分割出来的字符串放到文件里面去
    '''
    file_type = os.path.splitext(filename)[1]
    # print(file_type)
    i = 0
    lists = []
    for i in range(0,10):
        #创建文件
        name = str(i) + file_type
        lists.append(name)
        fp = open(name, 'w')
        fp.close()
        # 分割字符串
        str_x = s[int(avg * i):int(avg*(i+1))]
        save(name,str_x)
        i = i+1

    return lists, file_type


def merge_file(lists,file_type):
    text = []
    for x in lists:
        s = read_file(x)
        text.append(s)

    all = ''.join(text)
    name = 'ALLTEXT' + file_type
    fp = open(name, 'w')
    fp.close()

    save(name, all)








filename = 'How To Cover Your Tracks On The Internet.txt'
s = read_file(filename)
avg = count_words(s)
split_document(avg,s,filename)
# print(os.path.dirname(filename) )
# print(split_document(avg,s,filename))
merge_file(split_document(avg,s,filename)[0],split_document(avg,s,filename)[1])