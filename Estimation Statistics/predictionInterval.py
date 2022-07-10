#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:54:18 2022

@author: paulmason
"""
#Worked example of using prediction intervals with a linear regression

#Import numpy for dataset creation & summary statistics and import pyplot for plotting
import numpy as np
import matplotlib.pyplot as plt
#Import linear regression method from scipy
from scipy.stats import linregress


#Seed the RNG
np.random.seed(1)

#Create dataset x that is has Gaussian dist with around mean = 100 & stdv = 20
x = 20 * np.random.randn(1000) + 100
#Create y as dependent to x
y = x + (10 * np.random.randn(1000) + 50)

#Print summary statistics for x and y
print('X: mean = %.3f, stdv = %.3f' % (np.mean(x), np.std(x)))
print('Y: mean = %.3f, stdv = %.3f' % (np.mean(y), np.std(y)))

#Fit a linear regression
b1, b0, r_value, p_value, std_err = linregress(x, y)
print('b0 = %.3f, b1 = %.3f' % (b1, b0))

#Make a prediction
yhat = b0 + b1 * x

#Define new input, expected value and prediction
x_in = x[0]
y_out = y[0]
yhat_out = yhat[0]

#Estimate std of yhat
sum_errs = np.sum((y - yhat)**2)
stdev = np.sqrt(1 / (len(y) - 2) * sum_errs)

#Calculate prediction interval with 95% confidence
interval = 1.96 * stdev
print('Prediction interval = %.3f' % interval)

#Calculate lower and upper bound of the prediction interval
lower, upper = yhat_out - interval, yhat_out + interval
print('95 percent liklihood that the true value is between %.3f and %.3f' % (lower, upper))
print('True value = %.3f' % y_out)

#Scatterplot of data and predictions and prediction interval for predicted value
plt.scatter(x, y)
plt.plot(x, yhat, color = 'r')
plt.errorbar(x_in, y_out, yerr = interval, color = 'black', fmt = 'o')
plt.show()
