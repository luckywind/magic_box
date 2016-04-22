#encoding=utf-8
'''
参考：http://www.jianshu.com/p/e2c7d692fe2c
数据的可视化(visualization)
scikit-learn自带有一些经典的数据集，比如用于分类的iris和digits数据集，还有用于回归分析的boston house prices数据集。
可以通过下面的方式载入数据：
'''
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
'''
该数据集是一种字典结构，数据存储在.data成员中，输出标签存储在.target成员中。

画出任意两维的数据散点图
可以用下面的方式画出任意两个维度的散点图，这里以第一维sepal length和第二维数据sepal width为例：
'''
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
irisFeatures = iris["data"]
irisFeaturesName = iris["feature_names"]
irisLabels = iris["target"]

def scatter_plot(dim1, dim2):
    for t,marker,color in zip(xrange(3),">ox","rgb"):
           # zip()接受任意多个序列参数，返回一个元组tuple列表
        # 用不同的标记和颜色画出每种品种iris花朵的前两维数据
        # We plot each class on its own to get different colored markers
        plt.scatter(irisFeatures[irisLabels == t,dim1],
                    irisFeatures[irisLabels == t,dim2],marker=marker,c=color)
    dim_meaning = {0:'setal length',1:'setal width',2:'petal length',3:'petal width'}
    plt.xlabel(dim_meaning.get(dim1))
    plt.ylabel(dim_meaning.get(dim2))

plt.subplot(231)
scatter_plot(0,1)
plt.subplot(232)
scatter_plot(0,2)
plt.subplot(233)
scatter_plot(0,3)
plt.subplot(234)
scatter_plot(1,2)
plt.subplot(235)
scatter_plot(1,3)
plt.subplot(236)
scatter_plot(2,3)

plt.show()
'''
构建分类模型
根据某一维度的阈值进行分类
如果我们的目标是区别这三种花朵，我们可以做一些假设。比如花瓣的长度(petal length)好像将Iris Setosa品种与其它两种花朵区分开来。
我们可以以此来写一段小代码看看这个属性的边界是什么：
'''
petalLength = irisFeatures[:,2] #select the third column,since the features is 150*4
isSetosa = (irisLabels == 0) #label 0 means iris Setosa
maxSetosaPlength = petalLength[isSetosa].max()
minNonSetosaPlength = petalLength[~isSetosa].min()

print ('Maximum of setosa:{0} '.format(maxSetosaPlength))
print ('Minimum of others:{0} '.format(minNonSetosaPlength))
