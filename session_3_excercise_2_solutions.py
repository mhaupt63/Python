# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:11:16 2018

@author: s99931
"""

import re

from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import Flatten


# Read in the data set of film reviews and scores.
file = open("G:/Pricing/Python and Deep Learning Group/Projects/Word Embedding NN/imdb_labelled.txt","r")
data_text_lines = file.readlines()
len(data_text_lines)

# Use regex to "parse" text data. 
# Data is tab separated with sentence on left and score {0,1} on the right.
split_line_regex = re.compile(r'(.*)\t(\d+)\n') 

sentences = []
scores = []

# loop through and append parsed data to relevant list
for i in range(0, len(data_text_lines)):
    sentence = split_line_regex.search(data_text_lines[i]).group(1)
    sentences.append(sentence)
    
    score = split_line_regex.search(data_text_lines[i]).group(2)
    scores.append(score)

# convert number strings to integers
scores = list(map(int, scores)) 

sentences
scores

# 1. Create a list of sentences with the non-word characters removed and all lower case characters
sentences_modified = []

for i in range(0, len(sentences)):
    # remove non-word characters
    sentence = re.sub(r'[^\w\s]', "", sentences[i])
    # convert all to lower case
    sentence = sentence.lower()
    sentences_modified.append(sentence)
    
sentences_modified
    
# 2. Create a list of sentences split into component words
    
sentences_split = []

word_regex = re.compile(r'\s*([\w]+)\s*')

for i in range(0, len(sentences_modified)):
    words = word_regex.findall(sentences_modified[i])
    sentences_split.append(words)

sentences_split

# 3. Create a list of words and their assosciacted scores

words = []
word_scores = []

for i in range(0, len(sentences_split)):
    for j in range(0, len(sentences_split[i])):
        word = sentences_split[i][j]
        words.append(word)
        # assosciate word with score for sentence
        word_scores.append(scores[i])

words

# 4. count the number of words and unique number of words in the list
number_of_words = len(words)
unique_number_of_words = len(set(words))

number_of_words
unique_number_of_words

# 5. "one-hot" encode the words
# this step assigns each unique word a unique integer value
integer_encoder = LabelEncoder()
one_hot_encoded_words = integer_encoder.fit_transform(words)
one_hot_encoded_words

# Use a Neural Network to "learn" the word embedding
# Embedding is the process of assigning a value to a word
# in this case we are learning the assosciation of words to good or bad reviews.
# we are only embedding 1 dimension of meaning, but in practice we can do more.
model = Sequential()
model.add(Embedding(unique_number_of_words, 1, input_length = 1))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(one_hot_encoded_words, word_scores, validation_split = 0.25, batch_size = 1, epochs = 3)

# test the embedding
print(words[948])
model.predict(one_hot_encoded_words[948:949])

print(words[1770])
model.predict(one_hot_encoded_words[1770:1771])



