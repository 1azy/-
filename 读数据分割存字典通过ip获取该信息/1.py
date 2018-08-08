
a = ['a','b','c']
b = ['1','2','3']
#
x = zip(a,b)
# print(dict(x))



print([('a', 1), ('b',2)])
# dict
print(dict([('a', 1), ('b',2)]))

for temp in x:
    print(temp)


c = {}
c['a'] = 2
print(c)
print(c.get('a'))
print(c['a'])
print(c.get('x','abc'))



try:
    print(c['x'])
except KeyError as e :
    print(e)
