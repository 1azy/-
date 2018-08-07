
import re
from re import split
'''
打印某个文件的倒数十行
'''

def read_file():
    with open('How To Cover Your Tracks On The Internet.txt') as file_object:
        content = file_object.read()
    return content


def spilt_text(text):
    result = split(r'[\n]',text)
    list = []
    for x in result:
        if x :
            list.append(x)

    return list[-10:]




a =spilt_text(read_file())
for x in a:
    print(x)


print(''.join(open('How To Cover Your Tracks On The Internet.txt').readlines()[-10:]))





#
# a = ['a','b','c']
#
# print(''.join(a))
# print(a)
# print(',p;'.join(a))