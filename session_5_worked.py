# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:02:43 2018

@author: s99931
"""

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


def d_tanh(x):
    return 1 - mt.pow(mt.tanh(x), 2)    

# define a neuron (create a neuron class)
    # initialise
    # allow for forward propagation
    # allow for back propagation
class Neuron:
    def __init__(self, num_inputs, activation = "tanh"):
        self.num_inputs = num_inputs
        self.activation = activation
        self.weights = np.random.randn(num_inputs)
        self.bias = 0
        
        self.inputs = np.zeros(num_inputs)
        self.output = 0

    def forward_propagate(self, inputs):
        self.inputs = np.array(inputs)
        self.weighted_sum = np.sum(inputs * self.weights) + self.bias
        if self.activation == "tanh":
            self.output = mt.tanh(self.weighted_sum)
        else:
            self.output = self.weighted_sum
        return self.output
            
    def back_propagate(self, back_propagated_error_derivative, learning_rate):
        if self.activation == "tanh":
            self.weights_error_derivative = back_propagated_error_derivative * d_tanh(self.weighted_sum) * self.inputs
            self.bias_error_derivative = back_propagated_error_derivative * d_tanh(self.weighted_sum)
        else:
            self.weights_error_derivative = back_propagated_error_derivative * self.inputs
            self.bias_error_derivative = back_propagated_error_derivative
        self.weights -= learning_rate * self.weights_error_derivative
        self.bias -= learning_rate * self.bias_error_derivative
        return self.weights_error_derivative


#define a network
    # initialise given an input structure
    # allow for forward propagation
    # allow for back propagation
class SingleLayerNetwork:
    def __init__(self, num_inputs, num_hidden_neurons):
        self.hidden_neurons = []
        self.num_hidden_neurons = num_hidden_neurons
        for n in range(0, num_hidden_neurons):
            self.hidden_neurons.append(Neuron(num_inputs))
        self.output_neuron = Neuron(num_hidden_neurons, activation = "none")
        self.output = 0
        
    def forward_propagate(self, inputs):
        hidden_outputs = []
        for n in range(0, self.num_hidden_neurons):
            hidden_outputs.append(self.hidden_neurons[n].forward_propagate(inputs))
        self.output = self.output_neuron.forward_propagate(hidden_outputs)
        return self.output
        
    def back_propagate(self, actual, learning_rate):
        error_derivative = self.output - actual
        output_layer_derivative = self.output_neuron.back_propagate(error_derivative, learning_rate)
        for n in range(self.num_hidden_neurons):
            self.hidden_neurons[n].back_propagate(output_layer_derivative[n], learning_rate)
       

# initalise a network
my_network = SingleLayerNetwork(2, 8)
my_network.hidden_neurons[0].weights
my_network.hidden_neurons[0].bias

my_network.forward_propagate(train_x[0])
train_y[0]
# train and evaluate the network

train_errors = []
test_errors = []

learning_rate = 0.01

num_epochs = 10

for epoch in range(0, num_epochs):
    squared_error = 0
    for i in range(0, len(train_x)):
        output = my_network.forward_propagate(train_x[i])
        squared_error += mt.pow(output - train_y[i], 2)
        my_network.back_propagate(train_y[i], learning_rate)
        
    train_error = squared_error/len(train_x)
    train_errors.append(train_error)
    print(my_network.hidden_neurons[0].weights)
    
    squared_error = 0
    test_scores = []
    for i in range(0, len(test_x)):
        output = my_network.forward_propagate(test_x[i])
        test_scores.append(output)
        squared_error += mt.pow(output - test_y[i], 2)
    test_error = squared_error/len(test_x)
    test_errors.append(test_error)
            
plt.plot(train_errors)
plt.plot(test_errors)
plt.legend(['train_errors', 'test_errors'])
plt.show()
            
py.offline.plot([go.Histogram(x = test_scores), go.Histogram(x = test_y)])

