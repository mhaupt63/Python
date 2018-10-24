# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:29:26 2018

@author: s99931
"""

# import the regular expression package
import re

example_string = "933EBM was parked when the Tornado hit causing damages to the rear end and front bumper. Water has entered 933EBM as well causing water damage to the interior.”"

# regular expressions (AKA "regex") are used to parse and extract information from text by matching patterns
# in its simplest form a regex identifies a match of one string in another
# for example, just say we have the question: is the word "hit" in a given string?

# use the re.compile method to defeine the regex
example_regex = re.compile(r'hit')
# search a string for a match with the compiled regex
print(example_regex.search(example_string))

example_regex = re.compile(r'ball')
print(example_regex.search(example_string))

example_regex = re.compile(r'park')
print(example_regex.search(example_string))
# notice the above matches the word "parked"

## Character sets:
# use if we want to match at least one of multiple cahracter.
# example: does the string contain any 10 point scrabble letters?
# use the square brackets [] to define a set
ten_point_scrabble_letter_regex = re.compile(r'[qz]')
print(ten_point_scrabble_letter_regex.search(example_string))

vowels_regex = re.compile(r'[aeiouAEIOU]')
print(vowels_regex.search(example_string))

# use the ^ symbol at the start of a character set to match anything but the set:
# example :
not_vowells_regex = re.compile(r'[^aeiouAEIOU]')
print(not_vowells_regex.findall(example_string))

## Or statements
behind_regex = re.compile(r'behind|rear')
print(behind_regex.search(example_string))

### Special characters:  ( ) . ^ $ * + ? { } [ ] \ | 

## Grouping: using round brackets
# used in conjunction with "findall" method for string capture
parked_regex = re.compile(r'(park)ed')
print(parked_regex.search(example_string))
print(parked_regex.findall(example_string))

## match any character: .
example_regex = re.compile(r'(r.e)')
print(example_regex.findall(example_string))

## "escape" character: \
# used for matching any of the special characters
match_full_stop_regex = re.compile(r'\.')
print(match_full_stop_regex.search(example_string))
# or to reference a predefined group
# example "\w" is the character group for either leters or digits
example_regex = re.compile(r'(r\we)')
print(example_regex.findall(example_string))

## Reptition: 
# "+": 1 or more
# "*": 0 or more
# {N}: N times
# example: matching a word followed by a full stop.
word_followed_by_full_stop_regex = re.compile(r'(\w+)\s*\.')
print(word_followed_by_full_stop_regex.findall(example_string))

three_letter_words = re.compile(r'\s+(\w{3})\s+')
print(three_letter_words.findall(example_string))


## Start of end of string
# "^": start of string
# "$": end of string
digit_regex = re.compile(r'\d')
print(digit_regex.findall(example_string))
digit_at_start_regex = re.compile(r'^\d')
print(digit_at_start_regex.findall(example_string))
digit_at_end_regex = re.compile(r'\d$')
print(digit_at_end_regex.findall(example_string))

## Example:
# extract registration numbers from the text:
registration_regex = re.compile(r'(\d{3}[A-Z]{3})')
print(registration_regex.findall(example_string))

##Replacement
# use the re.sub() function to replace patterns in a string
# either
registration_regex.sub("car_registration", example_string)
# or
re.sub(r'(\d{3}[A-Z]{3})', "car_registration", example_string)
