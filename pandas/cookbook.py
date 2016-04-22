#encoding=utf-8
import functools
import pandas as pd
df = pd.DataFrame(
    {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
df.ix[df.AAA >= 5,'BBB'] = -1;
df
df.ix[df.AAA >= 5,['BBB','CCC']] = 555;
df
df.ix[df.AAA < 5,['BBB','CCC']] = 2000;
df
df_mask = pd.DataFrame({'AAA' : [True] * 4, 'BBB' : [False] * 4,'CCC' : [True,False] * 2})
df_mask
df.where(df_mask,-1000)
df = pd.DataFrame(
    {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
import numpy as np
df['logic'] = np.where(df['AAA'] > 5,'high','low'); #三元运算符
df
df = pd.DataFrame(
   {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
dflow = df[df.AAA <= 5]
dfhigh = df[df.AAA > 5]
dflow
dfhigh
df = pd.DataFrame(
    {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA'];
newseries
newseries = df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA'];
newseries;
df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1;
df
df = pd.DataFrame(
    {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
aValue = 43.0
df.ix[(df.CCC-aValue).abs().argsort()]
#----------------------------------------------------------------------------
df = pd.DataFrame(
      {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
Crit1 = df.AAA <= 5.5
Crit2 = df.BBB == 10.0
Crit3 = df.CCC > -40.0
AllCrit = Crit1 & Crit2 & Crit3
CritList = [Crit1,Crit2,Crit3]
AllCrit =functools.reduce(lambda x,y: x & y, CritList)
df[AllCrit]
#------------------------------------------------------------------------
df = pd.DataFrame(
    {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
df
df[(df.AAA <= 6) & (df.index.isin([0,2,4]))]
data = {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}
df = pd.DataFrame(data=data,index=['foo','bar','boo','kar']);
df
df.loc['bar':'kar'] #Label
df.ix[0:3] #Same as .iloc[0:3]
df.ix['bar':'kar'] #Same as .loc['bar':'kar']
#---------------------------------------------------------------------------------
df2 = pd.DataFrame(data=data,index=[1,2,3,4]); #Note index starts at 1.
df2
df2.iloc[1:3] #Position-oriented
df2.loc[1:3] #Label-oriented
df2.ix[1:3] #General, will mimic loc (label-oriented)
df2.ix[0:3] #General, will mimic iloc (position-oriented), as loc[0:3] would raise a KeyError
#--------------------------------------------------------------------------------------
df = pd.DataFrame(
      {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40], 'CCC' : [100,50,-30,-50]});
df
df[~((df.AAA <= 6) & (df.index.isin([0,2,4])))]
#------------------------------------------------------------------------------
rng = pd.date_range('1/1/2013',periods=100,freq='D')
rng
data = np.random.randn(100, 4)#100*4的矩阵
data
cols = ['A','B','C','D']
df1, df2, df3 = pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols)
pf = pd.Panel({'df1':df1,'df2':df2,'df3':df3});
pf