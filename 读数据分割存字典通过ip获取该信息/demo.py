import csv
from re import split

"""
1、按行分割csv文件，放在lists[]
2、按列分割lists中的数据，放在
3、创建一个keys[],存放表头
4、创建一个字典，遍历lists 如果list是lists中的行，往字典中添加，k=head[i],v=list[i]

"""
def read_file(filename):
    with open(filename,encoding='utf-8') as file_object:
         return file_object.read()

def parse_text(text):
    '''
    返回结构 数组
    [[]] 返回一个数组里面嵌套数组
    '''
    # result 返回一个按行切割的数组
    result = split(r'[\n]', text)
    # print(result[0])
    # 创建一个results存放 逗号切割的数组
    results = []
    #  遍历result数组，将里面所有内容按逗号分隔
    for x in result:
        temp = split(r'[,]', x)
        # print(temp)
        results.append(temp)
    # for i in range(len(result)):
    #     temp = split(r'[,]', result[i])
    #     results.append(temp)


    keys = results[0]
    a = {}

    '''
    遍历results[1：]中所有数据
    将keys和x
    '''
    for x in results[1:]:
        #把key和value关联起来，转化为字典
        d = dict(zip(keys,x))
        # a[key] = value
        # 取出d里面的ip的值作为a的key，d本身作为a的value
        a[d.get('ip')] = d
        # print(a)
        # if len(x) != len(keys):
        #     continue
        # d={}
        # for i in  range(len(keys)):
        #     d[keys[i]] = x[i]
        #
        # a[d.get('ip')] = d

    return a




text = read_file('ustc.csv')
d = parse_text(text)
print(d['60.168.178.218'])


