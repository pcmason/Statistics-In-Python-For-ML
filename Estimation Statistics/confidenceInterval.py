#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:32:11 2022

@author: paulmason
"""
#Examples using confidence intervals

#Import the sqrt method for the CI equation
from math import sqrt

#Get a 95% CI of an imaginary error of .2 of an imaginary dataset of 50 values
interval = 1.96 * sqrt((0.2 * (1 - 0.2)) / 50)

#Output the confidence interval and an interpretation
print('Confidence Interval: %.3f' % interval)
print('Classification error of model is .2 +/- %.3f' % interval)

#Show impact of n on CI
interval = 1.96 * sqrt((0.2 * (1 - 0.2)) / 100)
print('Confidence Interval: %.3f' % interval)
print('Classification error of model is .2 +/- %.3f' % interval)

#Import the statsmodel method to calculate CI
from statsmodels.stats.proportion import proportion_confint

#Hypothetical model that had 88 correct observations out of 100 total with at CI of 95%
lower, upper = proportion_confint(88, 100, 0.05)
print('Classification Accuracy Lower Bound: %.3f, Classification Accuracy Upper Bound: %.3f' % (lower, upper))

#Import numpy for the bootstrap CI calculation
import numpy as np

#Seed the RNG
np.random.seed(1)

#Create uniform dataset of 1000 values between .5 and 1
data = 0.5 + np.random.rand(1000) * 0.5

#Perform bootstrap procedute 100 times
scores = list()
for _ in range(100):
    #Bootstrap sample
    indices = np.random.randint(0, 1000, 1000)
    sample = data[indices]
    #Calculate and store statistic
    statistic = np.mean(sample)
    scores.append(statistic)
    
#Print median of the bootstrap scores list
print('Median = %.3f' % np.median(scores))

#Calculate 95% CI
alpha = 5.0

#Calculate lower percentile (2.5)
lower_p = alpha / 2.0
#Retrieve the observation at the lower percentile
lower = max(0.0, np.percentile(scores, lower_p))
print('%.1fth percentile = %.3f' % (lower_p, lower))

#Calculate upper percentile (97.5)
upper_p = (100 - alpha) + (alpha / 2.0)
#Retrieve the observation at the upper percentile
upper = min(1.0, np.percentile(scores, upper_p))
print('%.1fth percentile = %.3f' % (upper_p, upper))

#Interpret the results
print('There is a 95 percent liklihood that the range %.3f - %.3f covers the true statistic mean' % (lower, upper))


    