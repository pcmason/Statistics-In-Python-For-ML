#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:41:54 2022

@author: paulmason
"""
#Nonparametric statistcial signficance tests
#Example using Nonparametric Hypothesis Tests to 2 if 2 data samples are drawn from same dists or not

#Import numpy to create data and get basic summary statistics
import numpy as np
#Imoprt nonparametric hypothesis tests from scipy
from scipy.stats import mannwhitneyu, wilcoxon, kruskal, friedmanchisquare

#Seed the RNG
np.random.seed(1)

#Generate 2 sets of univariate observations, identical except one has a mean of 50 while the other's is 51
data1 = 5 * np.random.randn(100) + 50
data2 = 5 * np.random.randn(100) + 51


#Output mean and std for data
print('data1: mean = %.3f, stdv = %.3f' % (np.mean(data1), np.std(data1)))
print('data2: mean = %.3f, stdv = %.3f' % (np.mean(data2), np.std(data2)))

#Compare 2 data samples with Mann-Whitney U Test, and output results of the test
stat, p = mannwhitneyu(data1, data2)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results with significance level at 5%
alpha = 0.05
if p > alpha:
    print('2 data samples are drawn from the same distribution. (fail to reject H0)')
else:
    print('2 data samples are drawn from different distributions. (reject H0)')

#Compare 2 data samples with Wilcoxon Signed-Rank Test and output the results
stat, p = wilcoxon(data1, data2)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results
if p > alpha:
    print('2 data samples are drawn from the same distribution. (fail to reject H0)')
else:
    print('2 data samples are drawn from different distributions. (reject H0)')
    
    
#Next 2 nonparametric tests are for 2+ datasets, so set data2 = data1 and create and new third dataset
data2 = data1
data3 = 5 * np.random.randn(100) + 52

#Compare 3 samples using the Kruskal-Wallis H Test and output what it returns
stat, p = kruskal(data1, data2, data3)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results
if p > alpha:
    print('All data samples are drawn from the same distribution. (fail to reject H0)')
else:
    print('1+ data sample(s) drawn from different distributions. (reject H0)')
    
    
#Compare 3 samples using the Friedman Test and output results. 
stat, p = friedmanchisquare(data1, data2, data3)
print('Statistics = %.3f, p = %.3f' % (stat, p))

#Interpret the results
if p > alpha:
    print('All data samples are drawn from the same distribution. (fail to reject H0)')
else:
    print('1+ data sample(s) drawn from different distributions. (reject H0)')


