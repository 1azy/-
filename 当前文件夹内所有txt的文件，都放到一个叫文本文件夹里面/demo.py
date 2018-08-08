#encoding = utf-8#
'''
1.在当前文件夹新建一个文件名为"文本文件夹"
2.获取到该文件下所有的txt
3.放到新建的文件夹中
'''

import os
import shutil

def mkdir(path):

    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def move_files(from_path,to_path):
    # path = "d:\\data"  # 设置路径
    dirs = os.listdir(path)  # 获取指定路径下的文件
    for i in dirs:  # 循环读取路径下的文件并筛选输出
        # if os.path.splitext(i)[1] == ".txt":  # 筛选txt文件
        #     print(i)
        # elif os.path.splitext(i)[1] == ".pdf":
        #     print(i)
        # elif os.path.splitext(i)[1] == ".png":
        #     print(i)
        # print(os.path.splitext(i)[1])
        # print(os.path.splitext(i)[1][1:])
        foldername = os.path.splitext(i)[1][1:]
        if foldername:
            save_path = os.path.join(to_path,foldername)
            mkdir(save_path)

            filename = os.path.join(from_path,i)
            shutil.move(filename, save_path)

        # print(os.path.join(to_path,foldername))
            # # 合成完整的目录名
        # old = path +'\\'+ x
        # new = file + '\\' + x
        # shutil.move(old, new)



#file 新建文件夹路径， path 被查找txt文件的文件夹路径

file = "F:\\lazy2\\test"
mkdir(file)
path = 'F:\\lazy2'
move_files(path,file)



# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['lazy'] = 60   # 往字典中添加值对
# print(d['Michael']) # 输出Michael的分数
# d['Michael'] = 75 # 修改Michael的分数
# # 判断字典的key存不存在
# # print(d['Thomas'])  # 直接报错
# print('Thomas' in d)  #返回False
# print(d.get('Thomas', -1)) # -1为找不到的返回默认值，若没有设置，返回None
# d.pop('Tracy')  # 在字典中删除值对
# print(d)  # {'lazy': 60, 'Bob': 75, 'Michael': 75}

# print(os.path.splitext(r'F:/lazy/2018.2.22/练手/当前文件夹内所有txt的文件，都放到一个叫文本文件夹里面/demo.py'))
#
# def fool(x):
#     print(x+3)
#     return  x+3
#
# a=fool(3)+54
# b=fool(3)
# print(fool(10))
# # print(a)
# # print(b)
# # fool(20)
