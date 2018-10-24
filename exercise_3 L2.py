# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:15:23 2018

@author: Chaowu Song
"""

import pandas as pd
import numpy as np

## Define a data frame df as below
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

### 3.1 Group average of Grade and Grade_2 by Gender and ExamYear

### 3.2 Generate a pivot table which summarise maximum of Grade by Class (as row) and Passed (as column) with margin 
