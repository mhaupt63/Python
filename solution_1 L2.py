# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 17:28:26 2018

@author: Chaowu Song
"""

## Exercise 1

## 1.1 Create a data frame which has 3 columns, column A, B and C.
##     Column A is 4,5,6,7,8,9
##     Column B is 10,20,30,40,50,60
##     Column C is 'a','b','a','a','b','a'

import pandas as pd
df = pd.DataFrame(
         {'A':[4,5,6,7,8,9], 'B':[10,20,30,40,50,60], 'C':['a','b','a','a','b','a']}) 

## 1.2 Subset the dataframe df by the following conditions and return new data frames
##       return df_1 which is all columns of df when column A is greater than 5
##       return df_2 which is all columns of df when column A is less than 6 and column C is equal to 'a'
##       return df_3 which is column A and column B of df when column C is 'a' or column B is less than 30
 
df_1 = df.loc[df.A > 5]
df_2 = df.loc[(df.A < 6) & (df.C == 'a')]
df_3 = df.loc[(df.B < 30) | (df.C == 'a'), ['A', 'B']]

## 1.3 Overwrite certain columns based on certain conditions
##       overwrite column C to be 'e' when column A is less than 6
##       overwrite column B to be the same as column A when column B is great than 40
df.loc[df.A < 6, 'C'] = 'e'
df.loc[df.B > 40, 'B'] = df.loc[df.B > 40, 'A']
