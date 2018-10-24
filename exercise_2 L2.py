# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:44:46 2018

@author: Chaowu Song
"""

## Exercise 2

## There are 3 data frames defined as below.
import pandas as pd
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
    
### 2.1 Row bind them together and set the key to be "df1", "df2", "df3".

### 2.2 Column bind them together and set the column names to be "df1", "df2", "df3".


## There are 2 data frames defined as below
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C1': ['C0', 'C1', 'C2', 'C3'],
                        'D1': ['D0', 'D1', 'D2', 'D3']},
                        index= [1, 3, 5, 7])
    
df2 = pd.DataFrame({'A': ['A2', 'A3', 'A6', 'A7'],
                        'B': ['B2', 'B3', 'B4', 'B7'],
                        'C2': ['C4', 'C5', 'C6', 'C7'],
                        'D2': ['D4', 'D5', 'D6', 'D7']},
                        index= [1, 2, 3, 4])
   
### 2.3 Column bind them together while inner join in the rows by the key of each data frame

### 2.4 Perform left, right, inner and outer join of these two data frames by column A and B
