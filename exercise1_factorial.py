# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(n):
    if  type(n) is not int:
        print("n should be integer")
        fact=0
    elif n==0:
        fact=1
    else:
        fact=n * factorial(n-1)
    return fact

n=7
c=factorial(n)

print("factorial of %s is %s"  %(n,c))


### Recusion, set factorial0=1