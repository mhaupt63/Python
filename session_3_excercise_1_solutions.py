# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:43:22 2018

@author: s99931
"""

import re

film_review = "The film's sole bright spot was Jonah Hill (who will look almost unrecognizable to fans of the recent Superbad due to the amount of weight he lost in the interim)."

# 1. Count the number of captial letters in the film review
# hint: the len() function returns the length of a list
# hint: [A-Z] is the capital letter set.

# Soultion:
capital_letter_regex = re.compile(r'[A-Z]')
len(capital_letter_regex.findall(film_review))

# 2. create a new string which is the same as the film review 
# but removes any non word characters (other than spaces)
# hint: "\w" matches word characters
# hint: can use the re.sub finction

# Solution
film_review_punctuation_removed = re.sub(r'[^\w\s]', "", film_review)
film_review_punctuation_removed

# 3. split the film review into a list of words.
# hint: use the string created in part 2.

# Solution
word_regex = re.compile(r'\s*([\w]+)\s*')
words = word_regex.findall(film_review_punctuation_removed)
words

# 4. count the unique number of words in the film review
# hint "set" function removes duplicates from a list

len(set(words))
