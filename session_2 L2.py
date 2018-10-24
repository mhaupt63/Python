# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:35:25 2018

@author: Chaowu Song

Python Training Series 2 Pandas
"""

## Pandas is a software library written for the Python programming language
## for data manipulation and analysis.
## In particular, it offers data structures and operations for manipulating
## numerical tables and time series.
## It is very similar to data.table in R.

## Import pandas and other packages
import numpy as np
import pandas as pd
import os

## Change working directory
os.chdir("C:/Users/s106179/Desktop/")

## Create a dataframe from importing a csv file
sample_data = pd.read_csv("sample_data.csv")
help(pd.read_csv)
type(sample_data)
sample_data.head(3)
sample_data.shape
type(sample_data['model'])
type(sample_data['mpg'])


## Subsetting
## Question: how to subset a Data Frame by certain logic(s)
# Create a data frame using dictionaries:
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); df

# Select columns using a list of column names
df['AAA']
df[['AAA', 'CCC']]
# Subset by (row, column): use "loc" method
# Use a list of indexes or boolean values for row subsetting, 
# and a list of column names for comlumn subsetting.
# this is similar to data.frame indexing in R
df.loc[[1,2], ] # no columns selected defaults to all columns
df.loc[:, ['AAA', 'BBB']] # to select all rows, need to use ':', this is impying start:end
df.loc[(df.AAA <= 5) & ~(df.BBB >= 20), ['AAA', 'BBB']]
# To subset just by index values: use "iloc" method
# can either use a list of indexes or
# from(inclusive):to(exclusive):by
df.iloc[[1,3]]
df.iloc[1 : 4 : 2] # from index 1 to 3, by 2 (excluded '4'), remember indexes start from 0!
# cannot do conditional subsetting with "iloc" method
df.iloc[(df.AAA <= 5) & ~(df.BBB >= 20)] # will return error: cant use boolean indexing with iloc


## Conditional overwriting
df = pd.DataFrame(
         {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
df
###  One column overwriting
df.loc[df.AAA >= 5, 'BBB'] = 100
df
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 100
df
###  More than column overwriting many to many
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = [100, 200]
df
###  Column to column
df.loc[df.AAA >= 5, 'BBB'] = df.loc[df.AAA >= 5, 'CCC']
df
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = df.loc[df.AAA >=5, ['CCC', 'BBB']]
df

# Return the values of a dataframe as a numpy array/matrix:
# Use "values" method
# This will later be important for input to Neural Network models
df.values
df['AAA'].values


## Sorting
### sort accoring to one column
aValue = 43.0
df.loc[(df.CCC - aValue).abs().argsort()]
df.loc[df.AAA.argsort()]
### Sorting by hierachical indice
import itertools
index = list(itertools.product(['Ada','Quinn','Violet'],['Comp','Math','Sci']))
headr = list(itertools.product(['Exams','Labs'],['I','II']))
indx = pd.MultiIndex.from_tuples(index,names=['Student','Course'])
cols = pd.MultiIndex.from_tuples(headr) #Notice these are un-named
data = [[70+x+y+(x*y)%3 for x in range(4)] for y in range(9)]
df = pd.DataFrame(data,indx,cols); df
df.sort_values(by=('Labs', 'II'), ascending=False)
df.sort_values(by=[('Labs', 'II'), ('Exams', 'I')], ascending=False)


## Merge, join, and concatenate
###  Concatenating objects (row binding), it is using a list object, so 
###  it works more like rbindlist

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
    
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
    
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
    
frames = [df1, df2, df3]
### row bind, it always takes a list object
result = pd.concat(frames)
result
### this will help specify which part belongs to which data frame input
pd.concat(frames, keys=['x', 'y', 'z'])


### by default "concat" will keep the indexes from the orriginal data frames
### this can be confusing if you haven't deliberately set the indexes for the orriginal dataframes
### to reset the indexes when concatenating, use "ignore_index=True"
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
    
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']})
    
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']})
    
frames = [df2, df1, df3]
### row bind, it always takes a list object
pd.concat(frames, ignore_index=True)

### You can also achieve similar result with "append" method
df1.append(df2, ignore_index=True)

### Using Concatenate for the second axis (axis=1) will allow inner join (intersection),
### outter join (union), or Use a specific index (in the case of DataFrame) or
### indexes (in the case of Panel or future higher dimensional objects),
### i.e. the join_axes argument
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                     'D': ['D2', 'D3', 'D6', 'D7'],
                     'F': ['F2', 'F3', 'F6', 'F7']},
                    index=[2, 3, 6, 7])
###  the default is an "outer" join: keep everything (similar to column bind in R)
pd.concat([df1, df4], axis=1)
### column bind and only include rows with matching indices
pd.concat([df1, df4], axis=1, join='inner') 
### join and specify indexies to include
pd.concat([df1, df4], axis=1, join_axes=[df1.index])
###  duplicate column names are allowed in the merged table  
###  key is important in concatenating, which tends to be ignored in R

### Database-style DataFrame joining/merging
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                         'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
    

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                          'key2': ['K0', 'K0', 'K0', 'K0'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})  

pd.merge(left, right, on=['key1', 'key2'])
## Exercise why this returns 5 rows where there are ony 4 rows in left?
pd.merge(left, right, on=['key1', 'key2'], how = 'left')
pd.merge(left, right, on=['key1', 'key2'], how = 'right')
pd.merge(left, right, on=['key1', 'key2'], how = 'outer')

### Join on index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                         index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                          'D': ['D0', 'D2', 'D3']},
                          index=['K0', 'K2', 'K3'])
### will use key to join and then the keys will appear in the data as
### new columns
left.join(right)
left.join(right, how='outer')
### alternatively
pd.merge(left, right, left_index=True, right_index=True, how='outer')


##  Group by operations
df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
                      'size': list('SSMMMLL'),
                      'weight': [8, 10, 11, 1, 20, 12, 12],
                      'adult' : [False] * 5 + [True] * 2}); df
### group by multiple columns
df[['animal', 'adult', 'weight']].groupby(['animal', 'adult']).mean()
### group by with user defined functions
grades = [48,99,75,80,42,80,72,68,36,78]
df = pd.DataFrame( {'ID': ["x%d" % r for r in range(10)],
                        'Gender' : ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M'],
                        'ExamYear': ['2007','2007','2007','2008','2008','2008','2008','2009','2009','2009'],
                        'Class': ['algebra', 'stats', 'bio', 'algebra', 'algebra', 'stats', 'stats', 'algebra', 'bio', 'bio'],
                        'Participated': ['yes','yes','yes','yes','no','yes','yes','yes','yes','yes'],
                        'Passed': ['yes' if x > 50 else 'no' for x in grades],
                        'Employed': [True,True,True,False,False,False,False,True,True,False],
                        'Grade': grades})
df['Grade_2'] = np.random.rand(10)
df.groupby(['Class', 'Gender']).apply(lambda x: x['Grade'] * x['Grade_2'])
###  The first input is the dataframe being grouped by
df.groupby(['Class', 'Gender']).apply(lambda x, a, b: x[a] * x[b], 'Grade', 'Grade_2')


##  Pivot Table
df = pd.DataFrame(data={'Province' : ['ON','QC','BC','AL','AL','MN','ON'],
    'City' : ['Toronto','Montreal','Vancouver','Calgary','Edmonton','Winnipeg','Windsor'],
    'Types' : ['A', 'B', 'A', 'A', 'B', 'B', 'A'],
    'Sales' : [13,6,16,8,4,3,1],
    'Population' : np.random.randn(7)}); df
### Herachical row names    
pd.pivot_table(df,
                       values=['Sales', 'Population'],
                       index=['Province', 'Types'],
                       columns=['City'],
                       aggfunc=np.sum,
                       margins=True)
### Herachical column names
pd.pivot_table(df,
                       values=['Sales', 'Population'],
                       index=['Province'],
                       columns=['City', 'Types'],
                       aggfunc=np.sum,
                       margins=True)
### More than one operation
table = pd.pivot_table(df,
                       values=['Sales', 'Population'],
                       index=['Province'],
                       columns=['City', 'Types'],
                       aggfunc=[np.sum, np.min],
                       margins=True)
table

## Output data
table.to_csv("sample_output.csv")
