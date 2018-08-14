'''
s='abcdefg'，输出'gfedcba'
'''


s='abcdefg'
ss = ''
index = len(s) - 1
while index >= 0:
    ss = ss + s[index]
    index = index - 1

print(ss)


list = [1,2,3,4,5]

print(list[3:])   #从下标为3的元素开始，到最后一位 输出[4, 5]
print(list[1:3])  #从下标为1的元素开始，到下标为3的停止，不包括3 输出[2, 3]