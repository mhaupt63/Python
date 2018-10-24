# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:56:07 2018

@author: RAGHU
"""


tax_bracket={ 
             0:[30000  , 0.15],
             1:[80000  , 0.30],
             2:[150000, 0.45]
        }



def tax_table(income,tax_bracket):
    cnt=len(tax_bracket)
    print(cnt)
    total_tax=0
    while cnt >0 :
        tax=0
        if(income-tax_bracket[cnt-1][0]>0):
            tax=(income-tax_bracket[cnt-1][0])*tax_bracket[cnt-1][1]
            income=tax_bracket[cnt-1][0]
        else:
            tax=0
        total_tax+=tax
        cnt-=1
    return total_tax
    
 
x=tax_table(151000,tax_bracket)       
print(x)    
    