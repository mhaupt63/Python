# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:23:35 2018

@author: s99931
"""

import numpy as np
import pandas as pd
import math as mt
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# import sample data: actual location will depend on where you have it saved.
titanic_data = pd.read_csv("D:/Titanic data/train.csv")
titanic_data_test = pd.read_csv("D:/Titanic data/test.csv")
titanic_data_test_target = pd.read_csv("D:/Titanic data/gender_submission.csv")
titanic_data_test = pd.merge(titanic_data_test, titanic_data_test_target, on = 'PassengerId')

# standardise predictive variables
train_x = titanic_data[['Age', 'Fare']].copy()
age_mean = train_x['Age'].mean()
age_std = train_x['Age'].std()
fare_mean = train_x['Fare'].mean()
fare_std = train_x['Fare'].std()

train_x['Age'] = (train_x['Age'] - age_mean)/age_std
train_x['Fare'] = (train_x['Fare'] - fare_mean)/fare_std
train_x = np.nan_to_num(train_x.values)

test_x = titanic_data_test[['Age', 'Fare']].copy()
test_x['Age'] = (test_x['Age'] - age_mean)/age_std
test_x['Fare'] = (test_x['Fare'] - fare_mean)/fare_std
test_x = np.nan_to_num(test_x.values)

# define target variable
train_y = np.nan_to_num(titanic_data['Survived'].values).astype(float)
test_y = np.nan_to_num(titanic_data_test['Survived'].values).astype(float)

# define a neuron (create a neuron class)
    # initialise
    # allow for forward propagation
    # allow for back propagation
class Neuron:
    # def __init__(self):

    # def forward_propagate(self):

    # def back_propagate(self):


#define a network
    # initialise given an input structure
    # allow for forward propagation
    # allow for back propagation
class SingleLayerNetwork:
    # def __init__(self):
        
    # def forward_propagate(self, inputs):
        
    # def back_propagate(self, actual, learning_rate):
       

# initalise a network

# train and evaluate the network


        
            
