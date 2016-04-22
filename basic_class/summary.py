#coding=utf-8
# 1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 1.1 请将a字符串的大写改为小写，小写改为大写。
a = "aAsmr3idd4bgs7Dlsf9eAF"
print a.swapcase()
# 1.2 请将a字符串的数字取出，并输出成一个新的字符串。
for i in a:
    if(i.isdigit()):
        print i,
print ''.join([s for s in a if s.isdigit()])
# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
a = a.lower()
print dict([(x,a.count(x)) for x in set(a)])
# 1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list=list(a)#转为list
set_list = list(set(a_list))##通过转换为set去重后再转回list
set_list.sort(key=a_list.index)#对去重以后的list进行原先的排序
print ''.join(set_list)##拼接成字符串

# 1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
a_list=list(a)

print a[::-1]
# 1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
l = sorted(a)#数字在前面排序、大写在中间排序、小写在后面排序
a_upper_list=[]
a_lower_list=[]
for x in l:
    if x.isupper():
        a_upper_list.append(x)
    elif x.islower():
        a_lower_list.append(x)


for y in a_upper_list:
    y_lower = y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)

print ''.join(a_lower_list)
# 1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
search = 'boy'
u=set(a)
u.update(list(search))
print len(set(a))==len(u)
# boy = 'boy'
# for x in boy:
#     if x in a:
#         print 'True'
#     else:print 'False'
#
# print [(x in a) for x in boy]
# 1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
search = ['boy','girl','bird','dirty']
b=set(a)
for i in search:
    b.update(list(i))

print len(b)==len(set(a))
# 1.9 输出a字符串出现频率最高的字母
l = [(x,a.count(x)) for x in set(a)]
l.sort(key = lambda k:k[1],reverse=True)
print l[0][0]
# 2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。
import os
m= os.popen('python -m this').read()
m = m.replace('\n','')
l=m.split(' ')
print [(x,l.count(x)) for x in ['be','is','than']]
# 3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
size = 102324123499123
print '%s kb'%(size >>10)
print '%s mb'%(size>>20)
# 4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
a =  [1,2,3,6,8,9,10,14,17]
print str(a)[1:-1].replace(', ','')##先去掉两边的[]，再去掉逗号