# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:10:31 2018

@author: s99931
"""

import re

testString = "Tutu, the cuttlefish, catapultled a carrot 21 meters high!"

#Basic

regex = re.compile(r'cat')

print(testString)
print(regex.search(testString))






#Character sets

regex = re.compile(r'[qz]') #10-point Scrabble letters

print(testString)
print(regex.search(testString))

regex = re.compile(r'[aeiou]') #vowells

print(testString)
print(regex.search(testString))






#OR groups

regex = re.compile(r'dog|pig') 

print(testString)
print(regex.search(testString))


regex = re.compile(r'catfish|cuttlefish') 

print(testString)
print(regex.search(testString))





#Special characters: . ^ $ * + ? { } [ ] \ | ( )

regex = re.compile(r'c.t') #. any character

print(testString)
print(regex.search(testString))

regex = re.compile(r'^c.t') #^ start of string

print(testString)
print(regex.search(testString))

#escape characters, not must use "r" flag in python to correctly use backslashes

regex = re.compile(r'\d') # match a number

print(testString)
print(regex.search(testString))


regex = re.compile(r'\bcat\b') #match the word "cat"

print(testString)
print(regex.search(testString))





#Grouping

regex = re.compile(r'(c.t)') 

print(testString)
print(regex.search(testString).group(1))

regex = re.compile(r'(c.t)(apultled)') 
regex = re.compile(r'c.t|apultled') 


print(testString)
print(regex.findall(testString))


regex = re.compile(r'(c.t)')

print(testString)
print(regex.findall(testString)) #note: "findall", returns vector








#Repitition

#* 0 or any
regex = re.compile(r'(t\w*t)') 

print(testString)
print(regex.findall(testString))

#+ 1 or more
regex = re.compile(r'(t\w+t)') 

print(testString)
print(regex.findall(testString))

#{m,n} specific number of times, between m and n times. blank m = 0, blank n = infinity
regex = re.compile(r'([Tt]u){2,}')  

print(testString)
print(regex.search(testString))






#greedy vs non-greedy

#greedy
regex = re.compile(r'c.*t')  #greedy repitition matches everything between first and last possible match

print(testString)
print(regex.findall(testString))

#non-greedy
regex = re.compile(r'c.*?t') #non-greedy repitition matches everything between first and next possible match

print(testString)
print(regex.findall(testString))


#greedy
regex = re.compile(r'c\w*t')  

print(testString)
print(regex.findall(testString))

#non-greedy
regex = re.compile(r'c\w*?at')  

print(testString)
print(regex.findall(testString))






#example: exclamed words
regex = re.compile(r'(\w+!)')

print(testString)
print(regex.findall(testString))

#example: split text into array of words
regex = re.compile(r'\b(\w+)\b')

print(testString)
print(regex.findall(testString))


#Complex example

testString2 = "[\cost] for the claim on 21-December, the cost is $ 20,050."
testString3 = "[\description] car crash."

text_type_regex = re.compile(r'\[\\(.*)\]')
dollar_regex = re.compile(r'\$\s*([0-9,]+)\b')
claim_type_regex = re.compile(r'(crash|theft)')
comma_regex = re.compile(r',')


strings = [testString2,testString3]

for string in strings:
    print(string)
    text_type = text_type_regex.search(string).group(1)
    if text_type == 'description':
        claim_type = claim_type_regex.search(string).group(1)
        print(text_type + ": " + claim_type)
    if text_type == 'cost':
        cost = dollar_regex.search(string).group(1)
        cost = comma_regex.sub('',cost)
        print(text_type + ": " + cost)





