#coding= utf-8
#创建字典
info = {'name':'lilei','age':20}
print info
info = dict(name='lilei',age=20)
print info
#添加内容
info.update({'city':'beijing','phone':'nokia'})
print info
print info.items()#返回一个元组

a = {'k1':'v1','k2':'v2','k1':'v3'}  #被重复的键对应的值将被覆盖
print a

for x,y in a.items():
    print x,y

#########对字典排序,用到从键得值
a = {'a':'haha','b':'hehe','d':'heihei','c':'hiahia'}
key_list = a.keys()
key_list.sort()
for x in key_list:
    print x,a[x]

#####从字典的值得到字典的键？？？？？？
"""
1，字典索引的是键，而不是值 -> 迭代，穷举
2，值不唯一
3，一个值可能对应多个键
"""
a = {'a':'haha','b':'hehe','d':'haha','c':'hiahia'}
search_value = 'haha'
key_list = []
for x,y in a.items():
    if y==search_value:
        key_list.append(x)

print key_list

a = "dagewageASLJGQIGHdjgow52q23634"
print sorted(a)
print sorted(a,reverse=True)

import string
a = ''.join([x for x in a if not x.isdigit()])
#print sorted(a,key=string.upper())
"""
可以理解为：
1，用string.upper这个方法，去执行列表里的每一个数据
2，
"""
##翻译表,以一个字符为单位替换
g = string.maketrans('123','abc')
a = '1434537290'
print a.translate(g)
a.translate(g,'1')##以g为翻译表，并删除所有的1
print a.translate(g,'1')

#####  with
with open('d:\\a.txt','a') as g:
    g.write('xixixixixxi')