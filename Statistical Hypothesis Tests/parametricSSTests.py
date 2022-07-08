#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:49:50 2022

@author: paulmason
"""
#Example program using parametric hypothesis tests

#Import numpy to create 2 Gaussian datasets
import numpy as np
#Import parametric equations from scipy.stats
from scipy.stats import ttest_ind, ttest_rel, f_oneway

#Set constant significance level of 5%
ALPHA = 0.05

#Seed the RNG
np.random.seed(1)

#Create 2 Gaussian datasets that both have std of 5 and differing means. (drawn from diff pops)
data1 = 5 * np.random.randn(100) + 50
data2 = 5 * np.random.randn(100) + 51

#Output mean and std for data
print('Data1: Mean = %.3f, Stdv = %.3f' % (np.mean(data1), np.std(data1)))
print('Data2: Mean = %.3f, Stdv = %.3f' % (np.mean(data2), np.std(data2)))

#Compare 2 data samples with Student's T-Test and print output
stat, p = ttest_ind(data1, data2)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results
if p > ALPHA:
    print('Fail to reject H0, same distributions.')
else:
    print('Reject H0, different distributions.')
    
    
#Compare 2 data samples with Paired Student's T-Test and print results
stat, p = ttest_rel(data1, data2)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results
if p > ALPHA:
    print('Fail to reject H0, same distributions')
else:
    print('Reject H0, different distributions')
    
#Create a third dataset for rest of the parametric tests
data3 = 5 * np.random.randn(100) + 52

#Compare 3 data samples with Analysis of Variance Test (ANOVA)
stat, p = f_oneway(data1, data2, data3)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#interpret the results
if p > ALPHA:
    print('Fail to reject H0, all distributions are equal')
else:
    print('Reject H0, 1+ distribution(s) are unequal')
    
    



