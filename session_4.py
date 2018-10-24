# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:26:45 2018

@author: s106179
"""

## Plotly is a package specialising in interative visulisations. It is available
## in R, Python and other programming languages and platforms.


## Example 1, Scatter Plot
import plotly as py
py.__version__
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np


N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)


# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.offline.plot(data, 
                filename = 'plot_eg1.html',
                auto_open = False)

## Simple line and scatter plots can be shown within the console using matplotlib
## It is tedious to create more complex plots with matplotlib but may be useful for simple data investigation

import matplotlib.pyplot as plt

# matplotlib example 1
plt.scatter(random_x, random_y)
plt.show()


## Example 2, Scatter Plot with more than 1 class
random_x2 = np.random.randn(N)
random_y2 = np.random.randn(N)

# Create a trace
trace2 = go.Scatter(
    x = random_x2,
    y = random_y2,
    mode = 'markers'
)

data = [trace, trace2]
py.offline.plot(data, 
                filename = 'plot_eg2.html',
                auto_open = False)

# matplotlib example 2
plt.scatter(random_x, random_y)
plt.scatter(random_x2, random_y2)
plt.show()


## Example 3, More than 1 type of charts plotted together
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace1, trace2]
py.offline.plot(data, 
                filename = 'plot_eg3.html',
                auto_open = False)

# matplotlib example 3
plt.scatter(random_x, random_y0)
plt.plot(random_x, random_y1, marker = 'o')
plt.plot(random_x, random_y2)
plt.show()

## Example 4, Customised styling of the chart
N = 500

trace0 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Above',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'red',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)-2,
    name = 'Below',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Styled Scatter',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

fig = dict(data=data, layout=layout)
py.offline.plot(fig, 
                filename = 'plot_eg4.html',
                auto_open = False)

## Example 5, Grouped bar charts
trace1 = go.Bar(
    x=['A', 'B', 'C'],
    y=[20, 14, 23],
    name='Group 1'
)
trace2 = go.Bar(
    x=['A', 'B', 'C'],
    y=[12, 18, 29],
    name='Group 2'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, 
                filename = 'plot_eg5.html',
                auto_open = True)

## Example 6, Stacked bar charts
data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, 
                filename = 'plot_eg6.html',
                auto_open = True)

## Example 7, Pie charts
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)
py.offline.plot([trace], 
                filename = 'plot_eg7.html',
                auto_open = False)

## Example 8, Styled pie charts
colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']        
trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors, 
                           line=dict(color='#000000', width=2)))

py.offline.plot([trace], 
                filename = 'plot_eg8.html',
                auto_open = True)

