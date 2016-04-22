#encoding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
参考：http://pandas.pydata.org/pandas-docs/stable/10min.html
'''

#传一个列表来创建Series
s = pd.Series([1,3,5,np.nan,6,8])
s
#传一个numpy数组来创建数据框，datetime脚标，列标签
dates = pd.date_range('20130101',periods=6)
dates
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df
df.head()
df.tail()
df.index
df.columns
df.values
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
df['A']  #A列
df[0:3]  #前三行
df['20130102':'20130104']
df.loc[dates[0]]   #Selection by Label
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]
df.loc[dates[0],'A']
df.at[dates[0],'A']
'''
Selection by Position
'''
df
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]
df.iloc[1,1]
df.iat[1,1]
df[df.A > 0]
df[df > 0]
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]
'''
Setting
'''
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
s1
df['F'] = s1
df.at[dates[0],'A'] = 0
df
df.iat[0,1] = 0
df.loc[:,'D'] = np.array([5] * len(df))
df2 = df.copy()
df2[df2 > 0] = -df2
df2
'''
缺失值
'''
#Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1
df1.loc[dates[0]:dates[1],'E'] = 1
df1
'''
去掉所有含有缺失值的行
'''
df1.dropna(how='any')#返回了一个新的DataFrame!!!
df1            #原数据框并没有改变
df1.fillna(value=5)#填补缺失值
pd.isnull(df1)
'''
统计
'''
df.mean()
df.mean(1)#
df.var()
df.var(1)
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
s
df.sub(s, axis='index')
'''
Histgramming
'''
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()
'''
字符串方法
'''
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()
'''
Merge
'''
##   Concatenating pandas objects together with concat():
df = pd.DataFrame(np.random.randn(10, 4))
df
# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
'''
Join
'''
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
left
right
pd.merge(left, right, on='key')
'''
Append   Append rows to a dataframe
'''
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
s = df.iloc[3]
df.append(s, ignore_index=True)
df.append(s,ignore_index=False)
'''
Grouping
By “group by” we are referring to a process involving one or more of the following steps

Splitting the data into groups based on some criteria
Applying a function to each group independently
Combining the results into a data structure
'''
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                            'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
df
df.groupby('A').sum()
df.groupby(['A','B']).sum()
'''
Reshaping
'''
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                        'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                       'one', 'two', 'one', 'two']]))
tuples
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
df2
#    The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()
stacked
'''
With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(),
 which by default unstacks the last level:
'''
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)
'''
Pivot Tables
'''
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                       'B' : ['A', 'B', 'C'] * 4,
                      'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                      'D' : np.random.randn(12),
                      'E' : np.random.randn(12)})
df
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
'''
Out[48]:
C             bar       foo
A     B
one   A -0.542095  0.304671
      B -0.111869  0.098314
      C -0.407332 -1.565738
three A -0.163545       NaN
      B       NaN -1.780763
      C -1.052274       NaN
two   A       NaN  2.078835
      B -0.520428       NaN
      C       NaN -0.881369
'''

'''
时间序列
pandas has simple, powerful, and efficient functionality for performing resampling operations during
frequency conversion (e.g., converting secondly data into 5-minutely data).
This is extremely common in, but not limited to, financial applications.
'''
rng = pd.date_range('1/1/2012', periods=100, freq='S')
rng
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts
ts.resample('5Min', how='sum')
#Time zone representation
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
rng
ts = pd.Series(np.random.randn(len(rng)), rng)
ts
ts_utc = ts.tz_localize('UTC')
ts_utc
ts_utc.tz_convert('US/Eastern')#转换为另一个时区
#Converting between time span representations...
rng = pd.date_range('1/1/2012', periods=5, freq='M')
rng
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ps = ts.to_period()
ps
ps.to_timestamp()


df2 = pd.DataFrame({ 'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                       'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                       'D' : np.array([3] * 4,dtype='int32'),
                       'E' : pd.Categorical(["test","train","test","train"]),
                       'F' : 'foo' })
df2
df2.dtypes