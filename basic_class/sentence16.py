# #coding=utf-8
# python语句讲解
#
#
# 1.print语句
#
# 	1.1 基本输出
# 	1.2 print的逗号
# 	1.2 输出到文件 >>为重定向
# print "2",
# print "3"
f=open('E:/pyprint.txt','w')
print >> f,"第一行"
print >> f,"第二行"
f.close
#
#
# 2.控制流语句（control flow）
#
# 	2.1 由条件和执行代码块组成。
# 		2.1.1 条件可分为决策、循环和分支
# 	2.2 格式（冒号与4个空格永不忘）
# 	2.3 if while for 函数，皆为contorl flow
#
#
# 3.布尔值
#
# 	3.1 控制流与真假值息息相关
# 		3.1.1 不要误解了真假与布尔值
#
# 	3.2 布尔值的几个最基本运算符
# 		3.2.1 and
# 		3.2.2 or
# 		3.2.3 is 检查共享
# 		3.2.4 == 检查值 1==True
# 		3.2.5 not
# 		3.2.6 其他若干比较符号
#
#
# 4. if语句 （控制流语句）
#
#
# 	4.1 if的组成 if else elif pass
# 		4.1.1 if与elif替代了switch
# 		4.1.2 pass
#
# 	4.2 奇技淫巧 三元表达式
# 		4.2.1 x if  else
# 		4.2.2 活用list
# 		4.2.3 三元表达式玩玩就好
#
# 习题一：
#
# 1 用while语句的2种方法输出数字：1到10
i=0
while i in xrange(10):
    i+=1
    print i,
#
# 2 用for语句和continue 输出结果：1 3 5 7 9
i=0
for i in xrange(10):
    i+=1
    if(i%2==0):
        continue
    else: print i,

# 习题二：假设有列表
#
# a = [1,2,3,4,5,6]
#
# 1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，
#
# 输出字符串'not find'
a = [1,2,3,4,5,6]

for i in range(a.__len__()):
    print i

# 2 用while语句操作上面的列表a，输出下面结果：
#
# [2,3,4,5,6,7]
#

