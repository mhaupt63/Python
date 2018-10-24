# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:36:17 2018

@author: s106179
"""



'''
#Get basic help
'''
#Basic Help; Following command provide quick help on print
#print?

#You can also do following for help;
help(print)

'''
===============================================================================
Python Base Types 

   Numerical Types:
       integer, float, boolean, complex
       
   String Type
      string, bytes.
===============================================================================
'''
# Define objects which will appear in the environment
x = 1
y = 2
x + y

# Delete objects, pay attention to two ways of providing inputs to the function
del(x)
del y

'''
#Define Float and checks;
'''
x_f=10.5
x_f           #Only Name the vars prints the var;
print(x_f)    #print() var using print function;
type(x_f)     #type() function to check the type;

'''
#Define String Type; There is no character type in python;
'''

x_char="C"
x_char
type(x_char)


# Check type of a variable
type('This is a string')
type(None)


'''
===============================================================================
Python Container Types;
===============================================================================
'''

'''
#Tuples;
'''
# Tuples are an immutable data structure (cannot be altered), it is different from vecotr in R
# as there can be more than 1 type of elements stored in Tuples
x = (1, 'a', 2, 'b')
type(x)


'''
#List;
'''
# Lists are a mutable data structure.
x = [1, 'a', 2, 'b']
type(x)


'''
# Logical operators;
'''

# Logical operators
1 == 1 #equal
1 != 2 #not equal


#! #not
1 == 1 and 2 == 2 #and
1 == 1 or 2 == 3 #or

# Use the `in` operator to check if something is inside a list.
1 in [1, 2, 3]

# The operators below are widely used in R but in Python they are not used
# in connecting different conditions. They are bitwise operators which will
# operate for 0 and 1.
1 & 1
1 & 0
0 | 1
0 | 0
0 ^ 1
~ 0


# Subsetting and concatenating strings

# Use `+` to concatenate lists, don't mix this with vectorised arithmetic in R.
[1, 2] + [3, 4]

# Use `*` to repeat lists.
[1] * 3

# Now let's look at strings. Use bracket notation to slice a string.
x = 'This is a string'
print(x[0]) #first character
print(x[0 : 1]) #first character, but we have explicitly set the end character
print(x[0 : 2]) #first two characters
# This will return the last element of the string.
# Pay attention the logic of indexing using negative numbers
x[-1]
# This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
x[-4:-2]
# This is a slice from the beginning of the string and stopping before the 3rd element.
x[:3]
# And this is a slice starting from the 4th element of the string and going all the way to the end.
x[3:]


# tuple and list
x = (1, 2, 3)
type(x)
y = [1, 2, 3]
type(y)


'''
# Mutability;
'''

x[1] = 4   #Unmutable Tuple
y[1] = 4   #Mutable List


'''
# Dictionary;
'''
# Dictionaries associate keys with values.
x = {'ABC': 'abc@gmail.com', 'DEF': 'edfg@outlook.com'}
x['ABC'] # Retrieve a value by using the indexing operator

# Update a new observation in the dict
x['XYZ'] = None
x['XYZ']

# Iterate over all of the keys, using x will iterate over the keys
# for loop is closed by remove indenting
for item in x:
    print(x[item])
# Equivalently
for item in x.keys():
    print(item)
    

# Iterate over all of the values:
for email in x.values():
    print(email)

# Iterate over all of the items in the list:
# It is looping every row and then every column
for name, email in x.items():
    print(name)
    print(email)
# It is just looping every row
for name in x.items():
    print(name)


'''
# If, elif, else;
'''
# If, elif, else
var1 = 100
if (var1 == 100):
   print("1 - Got a true expression value")
   print(var1)
else:
   print("1 - Got a false expression value")
   print(var1)


var = 100
if (var == 200):
   print("1 - Got a true expression value")
   print(var)
elif (var == 150):
   print("2 - Got a true expression value")
   print(var)
elif (var == 100):
   print("3 - Got a true expression value")
   print(var)
else:
   print("4 - Got a false expression value")
   print(var)

'''
# Copy variable
'''

x = [1, 2, 3]
y = x
y[2] = 4
x

y = x.copy()
y[2] = 5
x
y  
   

# Define functions
# `add_numbers` is a function that takes two numbers and adds them together.
def add_numbers(x, y):
    return x + y 
add_numbers(1, 2)

# `add_numbers` updated to take an optional 3rd parameter. Using `print` allows printing of multiple expressions within a single cell.

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

# `add_numbers` updated to take an optional flag parameter.


def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))  
type(add_numbers)



'''
            #Create Numpy Array 1 Dimnensional;
'''

import numpy as np
dat1 = np.array(['a','b','c','d'])  #Create a numpy array
type(dat1)                         #find type of object
np.size(dat1)                      #Find size. Returns 4;
dat1.dtype                        #Numpy type has dtype prooperty which returns type of element

dat2 = np.array([1,2,3,4.0,5.0])   #Added last 2 values and floats
dat2                               #All values shown as float as array has 1 type;
type(dat2)   
dat2.dtype                        #Numpy type has dtype prooperty which returns type of element

dat3=np.array([0]*10)            #put first element as 0 and then do it 10 times
dat3
np.size(dat3)

dat4=np.array(range(10))          #Create np array from Range function;
dat4=np.arange(10)               #create array with 10 values
dat4=np.arange(1,10)             #Start from 1 finish at <10 i.e. 9.
dat4=np.arange(0,10,2)           #Start from 0 finish at <10 in increments of 2.
dat4

dat5=np.arange(0,10)
dat5
dat6=dat5*2                     #Each element get multiplied by 2;
dat6

dat7=dat5+dat6                 #Element wise addition of two arrays;
dat7

'''
            #Create Numpy Array 2 Dimnensional;
'''

dat1=np.array([[1,2,3],[4,5,6]])             #Define 2d array. Notice 2 square brackets;
dat1

dat2=np.arange(0,10).reshape(2,5)            #Row major order; Shapes a ten element array into 2*5;
dat2

np.size(dat2)
np.size(dat2,1)                             #1 represents column. output 5;


#### Lgical Operators on Arrays;

dat2>5                                    #Returns True false as boolean elemnt wise;

(dat2<2) | (dat2>5)                       #Multiple conditions. Retruns True false as boolean Aelemnt wise;


import math as mt                         #Importing math library so that i can use log function.
np.vectorize(mt.log)(dat1)                #Use Vectorise() to apply log function element wise;
dat1

k=dat2>5
k
dat2[k]                                       


'''
            #Slicing and combining Arrays;
            * General Syntax:   a1[<start>:<end>:<step>]
'''
#########Slicing Arrays;

dat1=np.arange(0,10)
dat1

dat1[3::]      #Pick everything starting and including 3;
dat1[:4:]      #Pick everything ending at 4. Note 4 being higher indiex not included;
dat1[::2]      #Pick everythingbut with increment of 2;
dat1[::-1]      #Reverse order.Pick everythingbut with increment of 1

dat2=np.arange(0,20)
dat3=dat2.reshape(4,5)     #Create 2D Array;

dat3

dat3[3::]

dat3[2:5,1]     #Pick all from to 2 to 5 and column 1;

#########Combining Arrays;

a=np.arange(9).reshape(3,3)
a

b=(a+1)*10           #Add 1 to each elemnt and then multiply by 10;
b

np.hstack((a,b))                 #Horizontal stack arrays. Looks like R cbind, SAS Set statement;

np.concatenate((a,b),axis=1)     #Same as above. Use concatenate axis=1;

np.concatenate((a,b),axis=0)     #Use concatenate axis=0; Vertical stack. like rbind, sas append;
np.vstack((a,b))                #Same as above. Use concatenate axis=1; Vertical stack. like rbind, sas append;