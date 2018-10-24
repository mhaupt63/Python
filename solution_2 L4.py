# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:28:48 2018

@author: s106179
"""

## Exercise 2

## 2.1 Generate a stacked bar and grouped bar chart out of the data below.
##     save them as 'bar_chart_stacked.html' and 'bar_chart_grouped.html'.

import plotly as py
import plotly.graph_objs as go

x = ['A', 'B', 'C', 'D', 'E']
y1 = [10, 15, 20, 25, 30]
y2 = [30, 25, 20, 15, 10]

trace1 = go.Bar(
    x = x,
    y = y1,
    name='Group 1'
)
trace2 = go.Bar(
    x = x,
    y = y2,
    name='Group 2'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, 
                filename = 'bar_chart_stacked.html',
                auto_open = False)

layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, 
                filename = 'bar_chart_grouped.html',
                auto_open = False)

## 2.2 Generate a pie chart out of x and y1, save it as 'pie_chart.html'.
trace = go.Pie(labels=x, values=y1)
py.offline.plot([trace], 
                filename = 'pie_chart.html',
                auto_open = False)

