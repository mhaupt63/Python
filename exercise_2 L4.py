# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:09:03 2018

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

## 2.2 Generate a pie chart out of x and y1, save it as 'pie_chart.html'.