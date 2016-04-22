#coding=utf-8
def test():
    "这里写文档注释"
    return "文档注释测试"
print test.__doc__##打印文档注释

def weizhicanshu(a,b,c,d,e):
    "返回一个元组"
    return a,b,c,d,e
print weizhicanshu(1,2,3,4,5)

##方法里修改全局变量global声明
b = 3
def test2():
    global b
    b=4
    return b
print test2()




