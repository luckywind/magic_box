#encoding=utf-8
'''
列表方法
'''
ls = [1,2,3,2]
ls.append(4)
#向列表中插入元素，但每次只能插入一个
ls.count(2)
#统计列表中某元素的个数
ls.extend([2,3,5])
#向列表中插入元素，但每次可以插入多个元素
ls.index(2, 1, 5)
#返回列表中指定元素所在的索引位置，可以通过start和stop参数设置搜索范围
ls.insert(3, 3)
#向列表中的指定索引位置插入元素
ls.pop(5)
#删除指定索引位置的元素，返回被删除的元素
x = ls.remove(2)
#删除指定元素值
ls.reverse()
#将列表中元素进行逆排序
ls.sort(cmp=None, key=None, reverse=True)
#默认将列表中元素进行升序，可以通过reverse参数将升序设为降序

'''
元组方法
'''
t = (1,2,2,2,3,4,5,6,7)
t.count(2)
#统计元组中某元素的个数
t.index(2, 2, 6)
#返回元组中某元素所在是索引位置，可以通过start和stop参数设置搜索范围

'''
字典方法
'''
dic = {'k1':'v1','k2':2,'k3':'v3','k4':2}
dic.clear()
#删除字典中所有项
dic.copy()
#复制列表中所有项

# dic.fromkeys(S[,v])
# #新建字典，键为S，值为v，如果S为长字符串，返回的键为字符串中的每一个字符，值将重复
# dic.get(k[,d])
# #获取字典中指定键的值，如果k不属于字典中的键，则返回None
dic.has_key('k2')
#返回字典中是否包含键'k2'
dic.items()
#返回字典中的索引键值，每一对键值存放在元组中，所有键值对存放在列表中
dic.iteritems()
#键值迭代器，一般用于for循环
dic.iterkeys()
#键迭代器，一般用于for循环
dic.itervalues()
#值迭代器，一般用于for循环
dic.keys()
#返回字典所有键
dic.pop('k1')
#删除字典中指定键的值，并返回被删除键的对应值
dic.popitem()
#删除某个键值对，无需往方法中传入参数
#dic.setdefault(k[,d])
#类似于dit.get(k,d)方法，如果k属于字典中的键，则返回对于的值，否则，将往字典中重新插入键值
#dic.update([E, ]**F)
#将字典E中的键值对更新到dic中
dic.values()
#返回字典中所有值(values)，存放在列表中
dic.viewitems()
#返回字典中键值的视图，单个键值对存放在元组中，所有键值对存放在列表中
dic.viewkeys()
#返回字典中键的视图，所有键存放在列表中
dic.viewvalues()
#返回字典中值的视图，所有值存放在列表中

'''
字符串方法
'''
string = 'sdgewdlgidetEITG'
string.capitalize()
#返回元字符串，且将字符串第一个字母转为大写
# string.center(width[, fillchar])
# #将字符串中心化处理，两边用一个字符表示（切记非字符串）
# string.count(sub[, start[, end]])
# #计数字符串中某子集的数量，可以通过start和stop参数设置搜索范围
# string.endswith(suffix[, start[, end]])
# #返回字符串是否以某个字符串结束 可以通过start和stop参数设置搜索范围
# string.expandtabs(tabsize)
# #将字符串中(tab符号)\t转换空格，默认一个tabsize为8个字符
# 例：
# str = "this is\tstring example....wow!!!";
# print "Original string: " + str;
# print "Defualt exapanded tab: " + str.expandtabs();
# print "Double exapanded tab: " + str.expandtabs(16);
# string.find(sub [,start [,end]])
# #返回指定字符串的索引位置，，可以通过start和stop参数设置搜索范围，如果未找到sub时返回-1
# string.format(*args, **kwargs)
# #通过{}和:来代替%，可以接受无限个参数，位置可以不按顺序，可以不用或者用多次。应用非常广泛的字符串方法
# 例：
# '{name},{age}'.format(age=18,name='kzc')
# string.index(sub [,start [,end]])
# #类似于string.find()方法，但未找到sub时会报错
# string.join(iterable)
# #用于将序列中的元素以指定的字符连接生成一个新的字符串
# 例：
# str = "-";
# seq = ("a", "b", "c"); # 字符串序列
# print str.join( seq );
# string.ljust(width[, fillchar])
# #返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
# string.partition(sep)
# #用来根据指定的分隔符将字符串进行分割，分割点为首次出现sep的地方，且包含分隔符，结果存为元组
# string.replace(old, new[, count])
# #用新的字符替换老字符，还可以指定替换的个数
# string.rfind(sub [,start [,end]])
# #返回sub字符串最后一次出现的位置，如果没有匹配项则返回-1，可以通过start和stop参数设置搜索范围
# string.rindex(sub [,start [,end]])
# #返回子字符串sub在字符串中最后出现的位置，如果没有匹配的字符串会报异常，可以通过start和stop参数设置搜索范围
# string.rjust()
# #返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
# string.rpartiton()
# #用来根据指定的分隔符将字符串进行分割，分割点为最后一次出现sep的地方，且包含分隔符，结果存为元组
# string.split([sep [,maxsplit]])
# #用来根据指定的分隔符将字符串进行分割，不包含分隔符，结果存为列表，不指定sep时，默认将将空格作为分隔符
# string.startswith(prefix[, start[, end]])
# #返回字符是否以某字符开始，可以通过start和stop参数设置搜索范围
# string.swapcase()
# #用于对字符串的大小写字母进行转换，小写字符转为大写，大写字母转为小写
# string.translate(table [,deletechars])
# #根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到deletechars参数中
# string.zfill()
# #返回指定长度的字符串，原字符串右对齐，前面填充0
# string.upper()
# #将字符串全部转为大写
# string.lower()
# #将字符串全部转为小写
# string.isupper()
# #返回字符串中是否全为大写 --> True/False
# string.islower()
# #返回字符串中是否全为小写 --> True/False
# string.isdigit()
# #返回字符串中是否只包含数字 --> True/False
# string.isalpha()
# #返回字符串中是否只包含数字 --> True/False
# string.isalnum()
# #返回字符串中是否只包含字母或数字 --> True/False
# string.isspace()
# #返回字符串中是否只包含空格 --> True/False
# string.istitle()
# #返回字符串中首字母是否大写 --> True/False
# string.strip()
# #去除字符串中收尾空格
# string.lstrip()
# #去除字符串左边空格
# string.rstrip()
# #去除字符串右边空格
