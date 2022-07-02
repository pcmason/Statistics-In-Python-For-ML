#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 11:40:23 2022

@author: paulmason
"""
#Example using a normal distribution

#Import libs for Gaussian data creation and plotting
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#X-axis for the plot
x_axis = np.arange(-3, 3, 0.001)

#Y-axis for Gaussian dist
y_axis = norm.pdf(x_axis, 0, 1)

#Plot the data
plt.plot(x_axis, y_axis)
plt.show()

#Seed the RNG
np.random.seed(1)

#Create a Gaussian dist with a mean of 50 and std of 5
data = 5 * np.random.randn(10000) + 50

#Plot the histogram of the generated data
plt.hist(data)
plt.show()

#Created a histogram with 100 bins to show the Guassian dist better
plt.hist(data, bins = 100)
plt.show()

#Calculate and output mean of data
data_mean = np.mean(data)
print('Mean: %.3f' % data_mean)

#Calculate and output the median
data_med = np.median(data)
print('Median: %.3f' % data_med)

#Plot low vs high variance
plt.plot(x_axis, norm.pdf(x_axis, 0, 0.5)) #low
plt.plot(x_axis, norm.pdf(x_axis, 0, 1)) #high
plt.show()

#Calculate and output variance
data_var = np.var(data)
print('Variance: %.3f' % data_var)

#Calculate and output standard deviations
data_std = np.std(data)
print('Standard Deviation: %.3f' % data_std)