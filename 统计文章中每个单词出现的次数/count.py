#coding=utf-8

import re
import os
# 打开文件
# 读内容
# 对内容进行分词
# 统计每个词用了多少次
# 输出结果



def read_file(filename):

    with open(filename) as file1:
        str1 = file1.read()
        return str1

def spilt_text(text):

    result = re.split(r'[;,.() \r\n\*/]', text)
    words = []
    for x in result:
        if x != "":
            words.append(x)
    return words

def count_word(words):
    # {key:value}
    d = {}
    for word in words:
        a = d.get(word)
        if a is None:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    return d

s = read_file('How To Cover Your Tracks On The Internet.txt')
words = spilt_text(s)
a = count_word(words)
for k,v in a.items():
    print(k, ':', v)



