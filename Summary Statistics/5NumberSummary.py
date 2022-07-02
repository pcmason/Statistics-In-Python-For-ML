#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:14:43 2022

@author: paulmason
"""
#Generate sample data from a uniform dist between 0 and 1 and summarize it using the 5-number summary

from numpy import percentile
#Import rand to generate the dataset
from numpy.random import rand

#Generate the data sample
data = rand(1000)

#Calculate quartiles
quartiles = percentile(data, [25, 50, 75])

#Calculate min and max
data_min, data_max = data.min(), data.max()

#Print the 5 number summary
print('Min: %.3f' % data_min)
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3: %.3f'  % quartiles[2])
print('Max: %.3f' % data_max)

