'''
给出一个句子，把首字母变成大写
'''

import string

def translate(s):

    ss = list(s)
    i = 0
    while i < len(ss):
        if i == 0:
           ss[i] = str.upper(ss[i])
        else:
            if ss[i-1] == ' ' or (ss[i-1].isalpha() == False and ss[i-1] != '\' '):
               ss[i] = str.upper(ss[i])

        i = i + 1

    return ''.join(ss)


s = input('输入一个句子：')
print(translate(s))


def cap_string(s):
    flag = True # 字符要不要转为大写
    rv = []

    for ch in list(s):
        if flag and ch.isalpha():
            rv.append(ch.upper())
            flag = False
        else:
            if not (ch.isalpha() or ch == '\''): # 遇到一个分隔符，标识下个字符又可以大写
                flag = True
            rv.append(ch)

    return ''.join(rv)


# print(cap_string('_Message _ Value - And Key Are Raw Bytes -- Decode If Necessary!'))