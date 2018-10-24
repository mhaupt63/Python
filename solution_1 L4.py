# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:28:48 2018

@author: s106179
"""

## Exercise 1

## 1.1 Define 2 vectors x_rand and y_rand, each contains 200 random
##     numbers from a uniform distribution, then generate a 
##     scatter plot out of x_rand and y_rand. Save this plot as 
##     'first_scatter_plot.html'.

import numpy as np
import plotly as py
import plotly.graph_objs as go

N = 200
x_rand = np.random.rand(N)
y_rand = np.random.rand(N)
trace = go.Scatter(
    x = x_rand,
    y = y_rand,
    mode = 'markers'
)
data = [trace]
py.offline.plot(data, 
                filename = 'first_scatter_plot.html',
                auto_open = False)

## 1.2 Define 4 vectors x1, x2, y1 and y2, each contains 500 random
##     numbers from a uniform distribution, then generate a
##     scatter plot out of (x1, y1), (x2, y2). (x1, y1) should be grouped as 
##     'group 1' and coloured as green. (x2, y2) should be grouped as 'group 2'
##     and coloured as RGB(193, 66, 66) with a transparency of 0.8.
##     Then save the plot as 'second_scatter_plot.html'.

N = 500
x1, x2, y1, y2 = \
np.random.rand(N), np.random.rand(N), \
np.random.rand(N), np.random.rand(N)
trace0 = go.Scatter(
    x = x1,
    y = y1,
    name = 'group 1',
    mode = 'markers',
    marker = dict(
        color = 'green'
    )
)
trace1 = go.Scatter(
    x = x2,
    y = y2,
    name = 'group 2',
    mode = 'markers',
    marker = dict(
        color = 'rgba(193, 66, 66, 0.8)'
    )
)
data = [trace0, trace1]
fig = dict(data=data)
py.offline.plot(data, 
                filename = 'second_scatter_plot.html',
                auto_open = False)

## 1.3 Define 3 vectors x, y_point and y_line. x has 200 elements which are
##     evenly distributed between 0 and 1 (i.e. the distance between 
##     consecutive elements in x is the same). y_point has 200 elements which 
##     are random numbers generated from a uniform distribution between 0 
##     and 1. y_line has 200 elements which are random numbers generated 
##     from a uniform distribution between -1 and -5. Generate a point chart
##     out of (x, y_point) (coloured in blue and labelled as 'dot'), 
##     and a line chart out of (x, y_line) (coloured in orange and labelled as
##     'line') together. Save the chart as 'third_scatter_plot.html'.

N = 200
x = np.linspace(0, 1, N)
y_point = np.random.rand(N)
y_line = np.random.rand(N) * (-4) -1

# Create traces
trace0 = go.Scatter(
    x = x,
    y = y_point,
    mode = 'markers',
    name = 'dot',
    marker = dict(
            color = 'blue')
)
trace1 = go.Scatter(
    x = x,
    y = y_line,
    mode = 'lines+markers',
    name = 'line',
    marker = dict(
            color = 'orange')
)

data = [trace0, trace1]
py.offline.plot(data, 
                filename = 'third_scatter_plot.html',
                auto_open = False)